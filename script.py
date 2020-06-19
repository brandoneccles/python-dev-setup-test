import requests


r = requests.get("https://www.jolt.com")
print(r.status_code)
