from bs4 import BeautifulSoup
import urllib.request as req

def parse(URL):
        page = req.urlopen(URL)
        soup = BeautifulSoup(page, 'html.parser') # from url
        htmlpage_text = [] #container for html page
        finalMainAnswer = {} #container for answers
        vote_container = []#container for votes
        initialOutput = []#final output for question and answers
        initialOutputAD = [] #final output for Acc and Date
        userDetails_Container = []
        dateContainer = []
        count = 0
        anscount = 1
        ctr = 2

        #getting the vote counts
        for vote_count in soup.find_all('div',{'class':'vote'}):
            vote_container.append(vote_count.span.text)


        #getting question and answers
        for table in soup.find_all('div',{'class':'post-text'}):
            htmlpage_text.append(table.text.strip())

        #code for accepted answers users
        for test2 in soup.find_all('div',{'class':'user-details'}):
            if (test2.a is not None):
                userDetails_Container.append(test2.a.text)
            else:
                userDetails_Container.append("N/A")


        #code for the dates
        for test in soup.find_all('div',{'class':'user-action-time'}):
                if (test2 is not None):
                        dateContainer.append(test.text.strip())
                else:
                        dateContainer.append("N/A")

        #creating object for account and date
        count = 0
        while(count < len(userDetails_Container)):
            mainAD = {} #for account and date
            mainAD['Name'] = userDetails_Container[count]
            mainAD['Date'] = dateContainer[count]
            initialOutputAD.append(mainAD)
            count = count + 1



        size_of_htmlpage_text = len(htmlpage_text)

        while (anscount < size_of_htmlpage_text):

            mainAnswer = {}
            mainAnswer['answer'] = htmlpage_text[anscount]
            mainAnswer['Upvote '] = vote_container[anscount]

            if(len(initialOutputAD) > 4):
                    try:
                            myStr = initialOutputAD[ctr]['Date']
                            if "edited" in myStr:
                                    mainAnswer['edited by'] = initialOutputAD[ctr]
                                    mainAnswer['answered by'] = initialOutputAD[ctr+1]
                                    ctr = ctr + 2
                            else:
                                    mainAnswer['edited by'] = "N/A"
                                    mainAnswer['answered by'] = initialOutputAD[ctr]
                                    ctr = ctr + 1
                    except IndexError:
                            myStr = 'null'
            else:
                            myStr = initialOutputAD[anscount]['Date']
                            if "edited" in myStr:
                                    mainAnswer['edited by'] = initialOutputAD[anscount]
                                    mainAnswer['answered by'] = initialOutputAD[anscount+1]
                                    anscount = anscount + 1
                            else:
                                    mainAnswer['edited by'] = "N/A"
                                    mainAnswer['answered by'] = initialOutputAD[anscount]
            initialOutput.append(mainAnswer)
            anscount = anscount + 1


        myStr = initialOutputAD[0]['Date']
        if "edited" in myStr:
                finalMainAnswer['questions'] = {"title": soup.title.text, "Body": htmlpage_text[0], "Upvote": vote_container[0], "Edited by": initialOutputAD[0], "Asked By":initialOutputAD[1]}
        else:
                finalMainAnswer['questions'] = {"title": soup.title.text, "Body": htmlpage_text[0], "Upvote": vote_container[0], "Edited by": "N/A", "Asked By":initialOutputAD[0]}
        finalMainAnswer['answers'] = initialOutput
        return finalMainAnswer
