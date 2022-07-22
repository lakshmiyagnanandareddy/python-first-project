import requests
"""
Write a Python code to check the status code issued by a server in response to a client's request made to the server.
Print all of the methods and attributes available to objects on successful request
"""
print(requests.get("https://www.w3resource.com/python-exercises/requests/index.php").status_code)
print(requests.get("https://www.w3resource.com/python-exercises/requests/index.php").__dir__())