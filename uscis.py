import requests,re, os
import pandas as pd
from bs4 import BeautifulSoup

input_dir = os.path.join(os.getcwd(),'uscis')
os.path.exists(input_dir) or os.mkdir(input_dir)

f = open('uscis/links.txt', 'w') 

url = requests.get('https://www.uscis.gov/tools/reports-studies/immigration-forms-data/data-set-form-i-485-application-adjustment-status')
html = url.content
soup = BeautifulSoup(html,'html.parser')

# body = soup.find_all('div', {'id':'main-body'})

atags = soup.find_all('a',{'type':re.compile('^text.*')})


for a in atags:
	prefix = 'https://uscis.gov'
	link = prefix+a.get('href')
	f.write(link +"\n")

f.close()