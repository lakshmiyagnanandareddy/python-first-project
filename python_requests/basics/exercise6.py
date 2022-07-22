import requests
"""
Write a Python code to send a request to a web page and stop waiting for a response after a given number of seconds.
In the event of times out of request, raise Timeout exception.
"""
try:
    print(requests.get("https://www.w3resource.com/python-exercises/requests/index.php", timeout=0))
except:
    requests.exceptions.Timeout
    print("time : 0")