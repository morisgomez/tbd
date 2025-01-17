#step 1: import relevant libaries/modules
import requests #allows us to send HTTP requests to websites.
from bs4 import BeautifulSoup #helps parse the data the requests library retrieves across the internet.
#both bs4 and requests work together to web scrape. 
#note: when need to install new module, use 'pip install [name]'
#in the terminal.

#step 2: determine URL for the web-page needing scraping.
url =  "https://openlibrary.org/search?subject=Cats"

#step 3: send a request to URL:
response = requests.get(url, headers={"Accept": "text/html"}) #what does this code mean?
#video doesnt explain.
#do I need to know what each word means?

#print(response) #200 response = success. 

#step 4: parse the response from request into python:
parsedRepsonse = BeautifulSoup(response.text, "html.parser") #what does this code mean?
#video doesnt explain.
#do I need to know what each word means?

print(parsedRepsonse) #prints out all html document.
print(parsedRepsonse.prettify()) #prints out all html document. same as print(parsedResponse)