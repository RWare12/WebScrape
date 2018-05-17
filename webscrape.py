from bs4 import BeautifulSoup
import simplejson as json
import urllib.request as req
import re

URL = input('ENTER URL: ')
if "https://stackoverflow.com/questions/" in URL:
	site = URL
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
	anscount = 0
	ctr = 2

	#getting the vote counts
	for vote_count in soup.find_all('div',{'class':'vote'}):
		vote_container.append(vote_count.span.text)


	#getting question and answers
	for table in soup.find_all('div',{'class':'post-text'}):
	    htmlpage_text.append(table.text)

	#code for accepted answers users
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
		mainAD['Name'] = test2_con[count]
		mainAD['Date'] = test3_con[count]
		tagsAD.append(mainAD)
		count = count + 1

	size_of_htmlpage_text = len(htmlpage_text)

	while (anscount < size_of_htmlpage_text):

		mainAnswer = {}

		if(anscount != 0):
			mainAnswer['answer'] = htmlpage_text[anscount]
			mainAnswer['Upvote '] = vote_container[anscount])
		if(anscount >= 1):
			if(len(tagsAD) > 4):
			        try:
			                myStr = tagsAD[ctr]['Date']
			                if "edited" in myStr:
			                        mainAnswer['edited by'] = tagsAD[ctr]
			                        mainAnswer['answered by'] = tagsAD[ctr+1]
			                        ctr = ctr + 2
			                else:
			                        mainAnswer['edited by'] = "N/A"
			                        mainAnswer['answered by'] = tagsAD[ctr]
			                        ctr = ctr + 1
			        except IndexError:
			                myStr = 'null'
			else:
			                myStr = tagsAD[anscount]['Date']
			                if "edited" in myStr:
			                        mainAnswer['edited by'] = tagsAD[anscount]
			                        mainAnswer['answered by'] = tagsAD[anscount+1]
			                        anscount = anscount + 1
			                else:
			                        mainAnswer['edited by'] = "N/A"
			                        mainAnswer['answered by'] = tagsAD[anscount]
		if (anscount != 0):
			tags.append(mainAnswer)
		anscount = anscount + 1

	myStr = tagsAD[0]['Date']
	if "edited" in myStr:
	        ans_con['questions'] = {"title": soup.title.text, "Body": htmlpage_text[0], "Upvote": vote_container[0], "Edited by": tagsAD[0], "Asked By":tagsAD[1]}
	else:
	        ans_con['questions'] = {"title": soup.title.text, "Body": htmlpage_text[0], "Upvote": vote_container[0], "Edited by": "N/A", "Asked By":tagsAD[0]}
	ans_con['answers'] = tags

	with open("Nodejs.json","w") as newFile:
		json.dump(ans_con, newFile, indent = 4)
else:
	print("Can't handle URL")
