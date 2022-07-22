import requests
r = requests.get("https://files.realpython.com/media/The-Python-Print-Function_Watermarked.26066d64ad82.jpg")
print(r)    # if "response [200]- is in the request ,output: is ok!"
# print(r.text)   # it shows the web content in the html code.
print(dir(r))
r1 = requests.get("https://files.realpython.com/media/The-Python-Print-Function_Watermarked.26066d64ad82.jpg")

with open("requestdemopic.jpg", "wb") as z:
    z.write(r1.content)

print(r.status_code)    # status_code- it shows the status of the link.
print(r.ok)
payload = {'page': 2, 'count': 25}
r = requests.get("https://files.realpython.com/media/The-Python-Print-Function_Watermarked.26066d64ad82.jpg",  params=payload)
print(r.headers)
print(r.text)
print(r.url)
payload = {'username': 'nandu', 'password': 'testing'}
r = requests.post("https://files.realpython.com/media/The-Python-Print-Function_Watermarked.26066d64ad82.jpg", data=payload)
print(r.text)
print(r.json)
r = requests.get("https://httpbin.org/basic-auth/nandu/testing", auth=('nand', 'testing'))  # it use's for authentication.
print(r)
r = requests.get("https://httpbin.org/delay/2", timeout=5)  # it is used for time maintaining.
print(r)
