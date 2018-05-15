from bs4 import BeautifulSoup
import urllib.request as req
import re

site = req.Request('https://stackoverflow.com/questions/16970982/find-unique-rows-in-numpy-array')
page = req.urlopen(site)
soup = BeautifulSoup(page, 'html.parser') # from url
arr = []
arr2 = {}
answers = []

for table in soup.find_all('div',{'class':'post-text'}):

    arr.append(table.text)

size_of_arr = len(arr)
count = 0

while (count < size_of_arr):
    if (count == 0):
        arr2['questions'] = {"title": soup.title.text, "Body": arr[count]}
    else:
        answers.append(arr[count])
    count = count + 1
arr2['answers'] = answers
print(arr2)

################################################################################
