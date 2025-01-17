#import necessary libraries
import requests

#define base URL
base_url = "http://api.openweathermap.org/data/2.5/forecast"
#api.openweathermap.org/data/2.5/forecast
#?q={city name}&appid={API key}
#define parameters
parameters = {"id": "524901", "mode": "json", "appid": "b2afa807e08862eb30b93a27fbaaf0c3"}
#b2afa807e08862eb30b93a27fbaaf0c3
#change the mode to "xml" if you want xml data.

#make API request, passing in base URL and parameters
response = requests.get(base_url, params = parameters)

# print out text from API response
print(response, "\n") #200.
print(response.text) #json data. 

# print out text from api response but in xml: