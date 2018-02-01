import requests,time
import mechanize, lxml, re
from bs4 import BeautifulSoup
import pandas as pd

open ('fatal.csv','w')


br = mechanize.Browser()
url = 'http://safetydata.fra.dot.gov/officeofsafety/publicsite/summary.aspx'

def select_form(form):
	return form.attrs.get('action',None)== './summary.aspx'

fatals=[]	

#submit the right form and into df
def submit_form(item):
	final = pd.DataFrame([])
	br.open(url)
	br.select_form(predicate=select_form)
	br.form['ctl00$ContentPlaceHolder1$DropDownYear']=[item]
	br.form['ctl00$ContentPlaceHolder1$ListBoxStats']=['r14'] # this does the states stuff 
	br.submit()
	return br.response().read()

def add_to_df(page,fatals):
	table = pd.read_html(page)[1]
	results=table.iloc[:, 0:5]
	soup = BeautifulSoup(page,'lxml').findAll('table')
	table = soup[1]
	years = table.find_all('th',{'class':re.compile('c [Hh]eader'),'scope':'col'})
	year_header = [year.get_text() for year in years][:4]
	header = ['State']+year_header
	print header
	results.columns=header
	fatals.append(results)
	return fatals 
	
	# fatal=pd.concat(fatal,axis=1)
	# print fatal
	# return fatal.to_csv('fatal.csv', index=False)
	
#Find years to submit
def get_years():
	br.open(url)
	br.select_form(predicate=select_form)
	items = br.form.find_control('ctl00$ContentPlaceHolder1$DropDownYear').get_items()
	return items

#each put those years into submit form 
def scrape():
	items=get_years()
	for item in items:
		page = submit_form(item.name) 
		add_to_df(page,fatals)

scrape()

#merge collected dfs on key column "state"
final = reduce(lambda left,right: pd.merge(left,right,on=['State'],how='outer'),fatals).fillna('nodata')
final.to_csv('fatal.csv', index=False)













## works for one year

# br = mechanize.Browser()
# br.open('http://safetydata.fra.dot.gov/officeofsafety/publicsite/summary.aspx')



# def select_form(form):
# 	return form.attrs.get('action',None)== './summary.aspx'
# br.select_form(predicate=select_form)

# br.form['ctl00$ContentPlaceHolder1$DropDownYear']=['2017']
# br.form['ctl00$ContentPlaceHolder1$ListBoxStats']=['r14']
# br.submit()

# #start parsing
# chart = br.response().read()
# #puts the chart on sheet but need better headers, also only collecting FATAL
# table = pd.read_html(chart)[1]
# #only collects first 5 columns with all rows hence FATAL
# fatal=table.iloc[:, 0:5]

# #Creating headers to surface years
# soup = BeautifulSoup(chart,'lxml').findAll('table')
# item = soup[1]
# years = item.find_all('th',{'class':'c header','scope':'col'})
# year_header = [year.get_text() for year in years]

# #new header here
# header = ['State']+year_header

# #setting new header to the fatal df 
# fatal.columns=header

# fatal.to_csv('fatal.csv',index=False)






