from bs4 import BeautifulSoup
import urllib.request as req
import re

site = req.Request('https://stackoverflow.com/questions/16970982/find-unique-rows-in-numpy-array')
page = req.urlopen(site)
soup = BeautifulSoup(page, 'html.parser') # from url


target = soup.find(id=re.compile('answers')).div.find_all('div', recursive=False)
print(target)
tags = []
arr = []
project = []


for table in soup.find_all('div',{'class':'post-text'}):
    #links=table.findAll('a')
    print(table.text)
    arr.append(table)
    #print("///////////////")
    #print('\n\n\n')



print("this is array: " , arr[0])
print("\n\n")
print("this is array: " , arr[1])





################################################################################
