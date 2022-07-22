import requests
"""
 Write a Python code to send a request to a web page, and print the JSON value of the response.
 Also print each key value of the response.
"""
r = requests.get("https://httpbin.org/get")
print(r.json())
print(r.json()['url'])
