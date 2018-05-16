from bs4 import BeautifulSoup
import urllib.request as req
import re

site = req.Request('https://stackoverflow.com/questions/16970982/find-unique-rows-in-numpy-htmlpage_textay')
page = req.urlopen(site)
soup = BeautifulSoup(page, 'html.parser') # from url
htmlpage_text = [] #container for html page
ans_con = {} #container for answers
answers = []#container for answer
vote_container = []#container for votes
tags = []#final output for question and answers
tagsAD = [] #final output for Acc and Date
test2_con = []
test3_con = []
count = 0
anscount = 1

#getting the vote counts
for vote_count in soup.find_all('div',{'class':'vote'}):
	vote_container.append(vote_count.span.text)


#getting question and answers
for table in soup.find_all('div',{'class':'post-text'}):
    htmlpage_text.append(table.text)

#code for accepted answers
for test2 in soup.find_all('div',{'class':'user-details'}):
	if (test2.a is not None):
		test2_con.append(test2.a.text)
	else:
		test2_con.append("N/A")


#code for the dates
for test in soup.find_all('div',{'class':'user-action-time'}):
        if (test2 is not None):
                test3_con.append(test.text)
        else:
                test3_con.append("N/A")

#creating object for account and date
count = 0
while(count < len(test2_con)):
	mainAD = {} #for account and date
	mainAD['Account'] = test2_con[count]
	mainAD['Date'] = test3_con[count]
	tagsAD.append(mainAD)
	count = count + 1



size_of_htmlpage_text = len(htmlpage_text)

while (anscount < size_of_htmlpage_text):
	mainAnswer = {}
	mainAnswer['answer'] = htmlpage_text[anscount]
	mainAnswer['Upvote '] = vote_container[anscount]

	#for debugging
	if(anscount >= 2):
		myStr = tagsAD[anscount]['Date']
		myStr2 = tagsAD[anscount+1]['Date']
		if(myStr.find("edited") & myStr2.find("answered")):
			print("found edited")
			mainAnswer['edited by'] = tagsAD[anscount]
			mainAnswer['answered by'] = tagsAD[anscount+1]
		else:
			mainAnswer['edited by'] = "N/A"
			mainAnswer['answered by'] = tagsAD[anscount]
	######################################################
	tags.append(mainAnswer)
	anscount = anscount + 1

ans_con['questions'] = {"title": soup.title.text, "Body": htmlpage_text[0], "Upvote": vote_container[0], "Edited by": tagsAD[0], "Asked By":tagsAD[1]}
ans_con['answers'] = tags

print(ans_con)
