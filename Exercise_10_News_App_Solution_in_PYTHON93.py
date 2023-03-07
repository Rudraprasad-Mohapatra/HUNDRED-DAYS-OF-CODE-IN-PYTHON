# Exercise 10
# Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application

import requests
import json #use it for parsing string get from the request
query  = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-02-07&sortBy=publishedAt&apiKey=efc9ef834b5c46aeb4705815ea22b20e"
r = requests.get(url)
# print(r.text) #now we have the string data
news = json.loads(r.text)
# print(news,type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print()
    print("--------------------------------------")
    print()
