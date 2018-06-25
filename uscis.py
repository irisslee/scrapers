import requests,re, os, time
import pandas as pd
from bs4 import BeautifulSoup

input_dir = os.path.join(os.getcwd(),'uscis','input')
os.path.exists(input_dir) or os.mkdir(input_dir)


def get_links():
	url = requests.get('https://www.uscis.gov/tools/reports-studies/immigration-forms-data/data-set-form-i-485-application-adjustment-status')
	html = url.content
	soup = BeautifulSoup(html,'html.parser')
	atags = soup.find_all('a',{'type':re.compile('^text.*')})
	link_list=[]

	for a in atags:
		prefix = 'https://uscis.gov'
		link = prefix+a.get('href')
		link_list.append(link)
	print len(link_list)
	return link_list


def download_links():
	link_list = get_links()
	for link in link_list:
		time.sleep(5)
		try:
			name = re.search(r'(?<=[Pp]erformancedata.)(.*$)',link).group()
		except AttributeError:
			name = re.search(r'.{14}$',link).group()

		loc = os.path.join(input_dir, name)
		response = requests.get(link)
		with open(loc,'wb') as f:
			f.write(response.content)

		print ('downloading {}'.format(link))

download_links()

