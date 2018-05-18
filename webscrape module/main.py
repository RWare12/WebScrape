import stackParser
import saveJsonFile

URL = ''

while(URL is not 'q'):
    print('Enter \'q\' to exit!')
    URL = input('ENTER URL: ') #getting URL
    if "https://stackoverflow.com/questions/" in URL:
            result = stackParser.parse(URL)
            saveJsonFile.saveFile(result)
    else:
            print("Invalid URL!")

exit()
