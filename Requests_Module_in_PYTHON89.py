import requests
# # get request
# response = requests.get("https://www.codewithharry.com")
# print(response.text)

# # post request
# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": 'harry',
#     "body": 'bhai',
#     "userId": 110,
# } 
# # just a dictionary
# headers = {
#     'Content-type': 'application/json; charset=UTF-8',
# }
# response = requests.post(url,headers = headers,json = data)
# print(response.text)


# web scrapping
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
print(r.text)

# use bs4 module for scrapping
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

for heading in soup.find_all("h2"):
    print(heading.text)
"""
NOTES:
Requests module in python
The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python. This module enables you to send HTTP requests using Python code and makes it possible to interact with APIs and web services.

Installation
pip install requests
Get Request
Once you have installed the Requests module, you can start using it to send HTTP requests. Here is a simple example that sends a GET request to the Google homepage:

import requests
response = requests.get("https://www.google.com")
print(response.text)
Post Request
Here is another example that sends a POST request to a web service and includes a custom header:

import requests

url = "https://api.example.com/login"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Content-Type": "application/json"
}
data = {
    "username": "myusername",
    "password": "mypassword"
}

response = requests.post(url, headers=headers, json=data)

print(response.text)
In this example, we send a POST request to a web service to authenticate a user. We include a custom User-Agent header and a JSON payload with the user's credentials.

bs4 Module
There is another module called BeautifulSoup which is used for web scraping in Python. I have personally used bs4 module to finish a lot of freelancing task.
"""