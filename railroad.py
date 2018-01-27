import requests,time
import mechanize, lxml
from bs4 import BeautifulSoup
import pandas as pd



br = mechanize.Browser()
url = 'http://safetydata.fra.dot.gov/officeofsafety/publicsite/summary.aspx'

def select_form(form):
	return form.attrs.get('action',None)== './summary.aspx'

##submit the right form
def submit_form(year):
	br.open(url)
	br.select_form(predicate=select_form)
	br.form['ctl00$ContentPlaceHolder1$DropDownYear']=[item.name]
	br.form['ctl00$ContentPlaceHolder1$ListBoxStats']=['r14'] # this does the states stuff 
	br.submit()

#form submited, now into DF
def results_to_df (item, results):
	chart = br.response().read()
	table = pd.read_html(chart)[1]
	fatal=table.iloc[:, 0:5]
	fatal.columns=header
	df=fatal.append
	return df.to_csv('fatal.csv', index=False)

#get right headers 
def headers(chart):
	soup = BeautifulSoup(chart,'lxml').findAll('table')
	item = soup[1]
	years = item.find_all('th',{'class':'c header','scope':'col'})
	year_header = [year.get_text() for year in years]
	header = ['State']+year_header
	return header

#Find years to submit
#Since each year has 3 previous years, item should be every 4 years 
def get_years():
	br.open(url)
	br.select_form(predicate=select_form)
	items = br.form.find_control('ctl00$ContentPlaceHolder1$DropDownYear')
	return items

#do all of the above 
def scrape():
	for item in items:
		df=submit_form(item)


scrape()




# # #Works once from here --

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






