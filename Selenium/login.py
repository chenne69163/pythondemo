import requests
import json

url = "http://192.168.129.30:6060/overview?cid=compass-stack"

headers = {
    'Content-Type':'application/json',
    'Authorization':'Basic YWRtaW46UHdkMTIzNDU2'
}

body = {
	"username" : "admin",
	"password" : "Pwd123456"
}

r = requests.get(url, headers = headers)

print(r.status_code)
#print(r.headers)
print(r.raise_for_status())
print(r.headers.get('content-type'))
print(r.cookies)

#print(r.text)

print(r.elapsed.total_seconds())