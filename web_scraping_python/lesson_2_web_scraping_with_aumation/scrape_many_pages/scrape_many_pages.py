#import relevant libraries
import requests 
from bs4 import BeautifulSoup
from time import sleep #time library has function to do w/ time
#e.g sleep() function stops program for a specific amount of time.

#https://openlibrary.org/search?subject=Cats&page=1
#965 pages in total and 20 books/items per page.
#we have to iterate over the amount of pages we want to scrape.
#iterate to a page, changing the num in url, scrape then iterate.
#all code needs to be inside the for loop.




my_list = []
#step 1: create for loop to iterate over 4 pages.
for i in range(1, 5):
    #step 2: code for URL to change accordingly change based on range:
    url = "https://openlibrary.org/search?subject=Cats&page=" + str(i)
    #str(i) converts the int from range into a string &  concatenates it to url string

    #step 3: send a requeset to URL w/ page num:
    response = requests.get(url, headers = {"Accept": "text/html"})
    #url hold the url request. 
    #no need to know what "Accept" & "text" & "html" in headers attribute means. 

    #step 4: parse the response from html to python data:
    parsedResponse = BeautifulSoup(response.text, "html.parser")
    #parsedResponse hold the entire HTML document?

    #step 5: find/identify html elements
    titles = parsedResponse.find_all("a", class_="results")
    #find all a elements with a class attribute of "results"
    #titles does not have the actual text though. 
    #it stores a list with each a element found.  

    #step 6: print out:
    print("\nPage Number:", i)  
    for element in titles:
        print(element.text) #end nested for loop.
        my_list.append(element.text)#append all titles to a list.

    print("\n") 
#end outer for loop.


#CHALLENGE: Create a list
print(my_list)

#how do i save the list to a csv file?sss


