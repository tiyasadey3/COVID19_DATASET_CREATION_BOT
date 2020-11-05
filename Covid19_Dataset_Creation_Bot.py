from selenium import webdriver
import pandas as pd
import time
import os
cd='d:\\webdrivers\\chromedriver.exe'
browser = webdriver.Chrome(cd)
browser.get("https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?")
time.sleep(20)
df=pd.DataFrame(columns=['Rank','Country','Total Cases','New Cases','Deaths','New Deaths','Recovered','Active Cases','Critical'])



for i in browser.find_elements_by_xpath("//*[@id='main_table_countries_today']/tbody/tr"):
	td_list=i.find_elements_by_tag_name('td')
	row=[]
	for td in td_list:
		row.append(td.text)
	data={}
	for j in range(len(df.columns)):
		data[df.columns[j]]=row[j]
	df=df.append(data,ignore_index=True)
print(df)
df=df.iloc[1:]
print(df)
path='c:\\Users\\TIYASA\\Downloads'
path1=os.path.join(path,'coviddata.csv')
df.to_csv(path1,index=False)
Print("The data has been stored "+path1+".")
chrome_browser.quit()