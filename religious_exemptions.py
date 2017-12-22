import requests,time
from bs4 import BeautifulSoup


url = requests.get('https://www2.ed.gov/about/offices/list/ocr/docs/t9-rel-exempt/z-index-links-list-2009-2016.html')

# path = raw_input('Users/sohyunlee/Desktop/pdfs')

html = url.content

soup = BeautifulSoup(html,'html.parser')

table = soup.find_all('table')

resulttable = table[2]

link_list = []

lists = resulttable.find_all('td')

rows = lists[:-1]

for row in rows:
	link = row.find('a').text

	pdf_links = ['http://www2.ed.gov/about/offices/list/ocr/docs/t9-rel-exempt/'+link]
	
	new_links = [str(pdf_links[0])for links in pdf_links]
	# print new_links


	for link in new_links:
		file_name = link.split('/')[-1]
	
		print "Downloading file %s " % link

		r = requests.get(link)


		f =  open(file_name,'w') 
		f.write(r.content)
		
		f.close()

		time.sleep(10)	




			

	

# time.sleep(2)
