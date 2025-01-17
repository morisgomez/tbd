#parsing json data to python data to work with:

#import necessary libraries
import requests
import json

#EXAMPLE 1: lemonade with raspberrz
print("\nPRODUCT EXAMPLE 1\n")
#define base URL
base_url = "https://api.upcitemdb.com/prod/trial/lookup"
#define parameters
parameters = {"upc": "025000044908"}
#make API request, passing in base URL and parameters
response = requests.get(base_url, params=parameters)
#parse the text from the API response using JSON schema
info = json.loads(response.text)#actual parsing of json here.

#print(info) #prints all json.
#print(info["items"]) #prints json stored in 'items'
item = info["items"][0]
#print(item) #gets first item of "items"

#get the products title:
title = item["title"] #have to know how to navigate json data to make this easier to get wanted info.

print(title) 
#title is string type.
#"Simply Lemonade w/ Raspberry Bottle, 52 fl oz"

#get brand name in string type:
brand = item["brand"]
print(brand)
print(item)
#learn json to navigate data more easily.s