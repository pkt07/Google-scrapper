from bs4 import BeautifulSoup
import re
from urllib.request import urlopen, Request
from openpyxl import Workbook
import os
from datetime import datetime
import pandas
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# import urllib.request
# import time
# from openpyxl import Workbook
# import os
# from datetime import datetime
email_list = []
phone_list = []

def function(page):
	save_excel =True
	scrape = BeautifulSoup(page, 'html.parser')
	scrape = scrape.get_text()

	phone_numbers = set(re.findall(r"\+\d{2}\s?0?\d{10}",scrape))
	emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",scrape))
	
	if len(emails) == 0:
        print("No email address(es) found.")
        print("-----------------------------\n")
    else:
        
        count = 1
        for item in emails:
		email_list.append(emails)
            print('Email address #' + str(count) + ': ' + item)
            count += 1

df = pandas.read_csv('url.csv')
for x in df['gg'][0:50]:
	print(x)
	try: 
		function(urlopen(x))
	except:
		pass
		hdr = {'User-Agent': 'Mozilla/5.0'}
		req = Request(x,headers=hdr)
		# page = urlopen(req)
		function(urlopen(req))


pandas.DataFrame(email_list).to_csv('ph_info.csv')
