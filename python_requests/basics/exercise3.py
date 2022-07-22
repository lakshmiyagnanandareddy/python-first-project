import requests
"""
Write a Python code to send a request to a web page, and print the response text and content.
Also get the raw socket response from the server.
"""
print(requests.get("https://www.w3resource.com/python-exercises/requests/index.php").text)
print(requests.get("https://www.w3resource.com/python-exercises/requests/index.php").content)
print(requests.get('https://api.github.com/events', stream = True).raw)
