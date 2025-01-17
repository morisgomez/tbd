#https://www.upcitemdb.com/ has thousands of items tracked via barcodes.
#we want to make requests to that website's api to get info on items.

#import necessary libraries
import requests

#define base URL
base_url = "https://api.upcitemdb.com/prod/trial/lookup"
#url to make a request to api.

#sdefine parameters
parameters = {"upc": "025000044908"}
#parameters make up part of the get request. 
#upc means universal product code. 
#025000044908 is the upc of a lemonade item. 

#make API request, passing in base URL and parameters
response = requests.get(base_url, params=parameters)
#the request type is a get and we store the response in variable.
#request url can also look like this: https://api.upcitemdb.com/prod/trial/lookup?upc=0885909950805
#and this for another item https://api.upcitemdb.com/prod/trial/lookup?upc=025000044908
#?upc=0885909950805 we are query-ing a upc hence the '?'

#print out the response URL 
print(response.url)
#https://api.upcitemdb.com/prod/trial/lookup?upc=025000044908
#if paste above url in browser, you get to a page w/ info on item but in json format.


#request url samples:
#https://api.upcitemdb.com/prod/trial/lookup?upc=0885909950805
#https://api.upcitemdb.com/prod/trial/lookup?upc=025000044908