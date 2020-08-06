
import requests, json, os, time, random, webbrowser

from selenium import webdriver
from bs4 import BeautifulSoup	


path="./News.json" ##path of you JSON file
if os.path.exists(path):
	data=json.load(open("./News.json","r"))
	print(data)

else:


	Chromedriver=webdriver.Chrome('/home/kaushal/Downloads/chromedriver') ## main path of chrome driver


	### to check Covid or Coronavirus Data
	def check(href,title):
	    if (href.find("corona")!=-1) or (title.find("corona")!=-1):
	        news[href]=title
	    elif (href.find("covid")!=-1) or (title.find("covid")!=-1):
	        news[href]=title
	    elif (href.find("Covid")!=-1) or (title.find("Covid")!=-1):
	        news[href]=title
	    elif (href.find("Corona")!=-1) or (title.find("Corona")!=-1):
	        news[href]=title
	    elif (href.find("COVID")!=-1) or (title.find("COVID")!=-1):
	        news[href]=title
	    elif (href.find("CORONA")!=-1) or (title.find("CORONA")!=-1):
	        news[href]=title



	timesofindia="https://timesofindia.indiatimes.com/"


	maindiv={} # Main Data Dictionary
	news={} 


	driver = Chromedriver ## Chrome driver for Selenium
	driver.get(timesofindia)
	time.sleep(20)

	mainContent=driver.find_elements_by_xpath("//*[@id='content']/div")
	for i in mainContent:
		for j in i.find_elements_by_css_selector("a"):
			href=j.get_attribute('href')
			if href==None:
				pass
			else:
				title=j.get_attribute("title")
				if title=='' or title==None or title=='None':
					title=j.text
				check(href,title)

	maindiv['timesofindia']=news




	########################################################################################


	ndtv="https://www.ndtv.com/"


	news={}

	driver = Chromedriver ## Chrome driver for Selenium
	driver.get(ndtv)
	time.sleep(2)


	for a in driver.find_elements_by_css_selector("body > div:nth-child(8) a"):
		html=a.get_attribute('outerHTML')
		href=a.get_attribute('href')
		soup= BeautifulSoup(html,"html.parser")
		title=soup.text
		if title=='' or title==' ' or title=='  ' or title=='\n\n':
			pass
		else:
			check(href,title)



	for a in driver.find_elements_by_css_selector("body > div:nth-child(13) a"):
		html=a.get_attribute('outerHTML')
		href=a.get_attribute('href')
		soup= BeautifulSoup(html,"html.parser")
		title=soup.text
		if title=='' or title==' ' or title=='  ' or title=='\n\n':
			pass
		else:
			check(href,title)



	maindiv['ndtv']=news
	 



	########################################################################################


	hindustantimes="https://www.hindustantimes.com/"

	news={}

	driver = Chromedriver ## Chrome driver for Selenium
	driver.get(hindustantimes)
	time.sleep(2)


	section1= driver.find_element_by_xpath("/html/body/div[1]/section[1]")
	section2= driver.find_element_by_xpath("/html/body/div[1]/section[2]")
	section3= driver.find_element_by_xpath("/html/body/div[1]/section[3]")

	for a in section1.find_elements_by_css_selector("a"):
	    href=a.get_attribute('href')
	    title=a.get_attribute("title")
	    if title=='':
	        title=a.text
	    check(href,title)

	for b in section2.find_elements_by_css_selector("a"):
	    href=b.get_attribute('href')
	    title=b.get_attribute("title")
	    if title=='':
	        title=a.text
	    check(href,title)

	for c in section3.find_elements_by_css_selector("a"):
	    href=c.get_attribute('href')
	    title=c.get_attribute("title")
	    if title=='':
	        title=a.text
	    check(href,title)
		

	maindiv['hindustantimes']=news




	file=open("News.json","w")
	filedata=json.dump(maindiv,file,indent=4) ## Dumping the main data into JSON file
	file.close()