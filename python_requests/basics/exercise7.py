import requests
"""
Write a Python code to send some sort of data in the URL's query string.
"""
payload = {'key' : 'value', 'key1' : "value1"}
r = requests.get("https://www.w3resource.com/python-exercises/requests/index.php", params=payload)
print(r.url)
print()