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

#step 5: find/identify all book titles:
titles = parsedRepsonse.find_all("a", class_="results")
#find all a elements with a class attribute of "results"
#titles does not have the actual text though. 
#it stores a list with each a element found.


#step 6: iterate over the titles and print each text (extraction):
for element in titles:
    print(element.text)
#for each item/element in the list titles, we go in and tet the actual html text which is the title of each item.
#a class="results" href="/works/OL655908W?edition=key%3A/books/OL6549269M" itemprop="url">Twas the night before Christmas: a visit from St. Nicholas</a>
#above is the ex of one element in list in titles

