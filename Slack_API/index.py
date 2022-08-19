import json 
import requests 
url = '輸入權杖' 
     
headers = {'Content-type':'application/json'} 
payload = { 
    'text':'串接成功' 
} 
json_payload = json.dumps(payload) 
r = requests.post(url,headers=headers,data=json_payload) 
print(r.text)