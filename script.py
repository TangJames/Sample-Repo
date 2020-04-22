import requests
# name = input('Your name? ')
# print("Hello,", name)


r = requests.get("http://www.tangjames.com/")
print(r.status_code)
print(r.ok)