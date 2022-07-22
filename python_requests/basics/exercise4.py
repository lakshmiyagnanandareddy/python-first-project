import requests
"""
Write a Python code to send a request to a web page, and print the information of headers.
Also parse these values and print key-value pairs holding various information.
"""
print(requests.get("https://www.w3resource.com/python-exercises/requests/index.php").headers)
print(requests.get("https://www.w3resource.com/python-exercises/requests/index.php").headers["Date"])