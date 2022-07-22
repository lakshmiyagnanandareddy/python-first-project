import requests
"""
 Write a Python code to verify the SSL certificate for a website which is certified. 
"""
print(requests.get("https://www.w3resource.com/python-exercises/requests/python-request-exercise-9.php", verify=True))
print(requests.get('https://rigaux.org/', verify=True))