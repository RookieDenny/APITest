import requests 

# LINE Notify 權杖 
token = '輸入權杖' 
# 要發送的訊息 
message = '串接成功' 
# HTTP 標頭參數與資料 
headers = { "Authorization": "Bearer "+ token ,'Content-Type':'application/x-www-form-urlencoded'} 
data = { 'message': message } 
# 以 requests 發送 POST 請求 
requests.post("https://notify-api.line.me/api/notify", 
    headers=headers,params=data)