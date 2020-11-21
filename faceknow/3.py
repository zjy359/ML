#!/user/
#-*- coding:utf-8 -*-
import json
import requests
# https请求方式:
# GET https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
app_id = 'wx387ef2b7f6a63f64'
app_secret = '6797262eef0955bdda085a71a052fd86'

url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}'

resq = requests.get(url).json()
access_token = resq.get('access_token')

#http请求方式:
# POST https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=ACCESS_TOKEN
url = f'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={access_token}'
open_id = "oTE_f0UEIejQ5x4HEqGtU5RXKglQ"
req_data={
    "touser":open_id,
    "msgtype":"text",
    "text":
    {
         "content":"有人闯入你家"
    }
}

req_str = json.dumps(req_data,ensure_ascii=False)
req_data = req_str.encode('utf-8')
requests.post(url,data= req_data)