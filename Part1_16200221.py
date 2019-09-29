from bs4 import BeautifulSoup
import urllib.request
import requests
import urllib.parse

import urllib.request
url = "http://mlg.ucd.ie/modules/COMP41680/news/index.html"  #main URL
response = urllib.request.urlopen(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(response, 'html.parser')
list_months = []
for a in soup.findAll('a', href=True): #get all hyperlinks
    list_months.append("http://mlg.ucd.ie/modules/COMP41680/news/"+a['href']) #get all links and concatinate to the main lonk and append to a list
    

del list_months[-3:] #del the last 3 links as they are useless

list_final = []
for i in list_months:
    response = urllib.request.urlopen(i)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response, 'html.parser')
    for a in soup.findAll('a', href=True):
        #print(a)
        if (a!="" or a != "index.html" ): #dont select empty or index.html links
            #print(a['href'])
            list_final.append("http://mlg.ucd.ie/modules/COMP41680/news/"+a['href'])
import re
count = 0
list_final_updated = []
for i in list_final:
    #if a link contains index.html or "http://mlg.ucd.ie/modules/COMP41680/news/" then go to next link
    search = re.search(r'\bindex.html\b',i)
    if (search):
        continue
    if (i == "http://mlg.ucd.ie/modules/COMP41680/news/"):
        continue
    else:
        list_final_updated.append(i) #final updated list of all links
     
    
for i in list_final_updated:
    f_name = (i.split("/")[-1]).split(".")[0]+".txt" #create a unique file name for each document
    #print(f_name)
    response = urllib.request.urlopen(i)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response, 'html.parser')
    p = soup.find_all('p')
    for j in p:
        with open(f_name,'a',encoding="utf-8") as csv_file: #open each link and get its text without tags and save ina  txt file
            csv_file.write(j.get_text())

