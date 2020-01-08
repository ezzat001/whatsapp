#!/usr/bin/python
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# ( -- LOGO * INFO -- ) #
bugs = '''
   ______        ___   _    _  _____ ____    _    ____  ____  
  / __ \ \      / / | | |  / \|_   _/ ___|  / \  |  _ \|  _ \ 
 / / _` \ \ /\ / /| |_| | / _ \ | | \___ \ / _ \ | |_) | |_) |
| | (_| |\ V  V / |  _  |/ ___ \| |  ___) / ___ \|  __/|  __/ 
 \ \__,_| \_/\_/  |_| |_/_/   \_\_| |____/_/   \_\_|   |_|    
  \____/                                                      
\n[$] BUGS WHATSAPP MESSAGES SENDER.
[$] URL = ('https://www.Brazzers.com/').
[$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''
#################################
# ( -- PROGRAMMED BY @BUGS -- ) #
#################################

# ( -- FULL SCRIPT -- ) #

print(bugs)
driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')
start = input('\n[X] PRESS ENTER TO START AFTER SKIPPING [QR] CODE.')
time.sleep(1)
print()
# -++++++++++++++++++++++++++++++++- ## -++++++++++++++++++++++++++++++++- ## -++++++++++++++++++++++++++++++++- #
nums_list = 'list'
nums_file = open(nums_list,'r')
file = open('msg','r')
message = file.read()
message_type = 'n'
if message_type == 'y' or 'Y':
	message = message.encode('utf-8')
	message = message.decode('unicode-escape')
elif message_type == 'n' or 'N':
	pass
else:
	print ('[X] THE SCRIPT STOPPED PLEASE ENTER A VALID CHOICE.')
	time.sleep(100000)
# -++++++++++++++++++++++++++++++++- ## -++++++++++++++++++++++++++++++++- ## -++++++++++++++++++++++++++++++++- #
sent = 0
for num in nums_file:
	sent+=1
	num = num.strip()
	url = 'https://web.whatsapp.com/send?phone='+num
	driver.get(url)
	if int(sent) == 1:
		pass
	else:
		alert = driver.switch_to_alert()
		alert.accept()
	time.sleep(1)
	inp_xpath = '//div[@class="_3u328 copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
	input_box = driver.find_element_by_class_name("_3u328")
	input_box.send_keys(message+Keys.ENTER)
	print ('[X] THE MESSAGE NUMBER HAS BEEN SENT TO [ '+num+' ].')
