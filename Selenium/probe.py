import requests
from Selenium import method

url = "http://192.168.129.30:6060/hodor/apis/admin.tenant.caicloud.io/v1alpha1/clusters/user-302c25-20200115133135-5g1/partitions"
token = method.get_token('admin', 'Pwd123456')
payload = "{\n    \"metadata\": {\n        \"name\": \"auth-smoketest\"\n    },\n    \"spec\": {\n        \"tenant\": \"auth\",\n        \"quota\": {\n            \"limits.cpu\": \"0.2\",\n            \"limits.memory\": \"0.2Gi\",\n            \"requests.cpu\": \"0.1\",\n            \"requests.memory\": \"0.1Gi\"\n        }\n    }\n}"
headers = {
  'X-Tenant': 'auth',
  'Content-Type': 'application/json',
  'Authorization': token
}

r = requests.request("POST", url, headers=headers, data = payload)

#print(r.text.encode('utf8'))
print(r.status_code)
print(r.raise_for_status())
print(r.headers.get('content-type'))
print(r.elapsed.total_seconds())