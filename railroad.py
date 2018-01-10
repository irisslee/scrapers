import requests,time
import mechanize
from bs4 import BeautifulSoup


br = mechanize.Browser()
br.open('http://safetydata.fra.dot.gov/officeofsafety/publicsite/summary.aspx')

response = br.response()


def select_form(form):
	return form.attrs.get('action',None)== './summary.aspx'

br.select_form(predicate=select_form)



br.form['ctl00$ContentPlaceHolder1$DropDownYear']=['2003']
br.form['ctl00$ContentPlaceHolder1$ListBoxStats']=['r14']


br.submit()


# br.select_form(name = 'ctl00$ContentPlaceHolder1$DropDownYear')
# br['value']='2003'

# br.select_form(name = 'ctl00$ContentPlaceHolder1$ListBoxStats')
# br['value']='r14'

# submit = br.sumbit(name='ctl00$ContentPlaceHolder1$ButtonSubmit',value='Generate Statistics')

# http://toddhayton.com/2014/12/08/form-handling-with-mechanize-and-beautifulsoup/












# url = requests.get('http://safetydata.fra.dot.gov/officeofsafety/publicsite/summary.aspx')

# # path = raw_input('Users/sohyunlee/Desktop/pdfs')

# html = url.content

# soup = BeautifulSoup(html,'html.parser')




# table = soup.find_all('table')

# resulttable = table[2]

# link_list = []

# lists = resulttable.find_all('td')

# rows = lists[:-1]

# for row in rows:
# 	link = row.find('a').text

# 	pdf_links = ['http://www2.ed.gov/about/offices/list/ocr/docs/t9-rel-exempt/'+link]
	
# 	new_links = [str(pdf_links[0])for links in pdf_links]
# 	# print new_links


# 	for link in new_links:
# 		file_name = link.split('/')[-1]
	
# 		print "Downloading file %s " % link

# 		r = requests.get(link)


# 		f =  open(file_name,'w') 
# 		f.write(r.content)
		
# 		f.close()

# 		time.sleep(10)	