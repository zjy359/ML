#!/user/
#-*- coding:utf-8 -*-
#!/user/
#-*- coding:utf-8 -*-
import json
import requests
# https请求方式:
# GET https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET


def get_access_token(app_id, app_secret):
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}'
    resq = requests.get(url).json()
    access_token = resq.get('access_token')
    return access_token
#http请求方式:
# POST https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=ACCESS_TOKEN
def send_wx_customer_msg(access_token, opend_id, msg="有人闯入了你的家"):
    url = f'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={access_token}'
    req_data={
        "touser":opend_id,
        "msgtype":"text",
        "text":
        {
             "content":msg
        }
    }
    requests.post(url, data=json.dumps(req_data, ensure_ascii=False).encode('utf-8'))


# req_str = json.dumps(req_data,ensure_ascii=False)
# req_data = req_str.encode('utf-8')
# requests.post(url,data= req_data)

if __name__ == '__main__':
    app_id = 'wx387ef2b7f6a63f64'
    app_secret = '6797262eef0955bdda085a71a052fd86'
    access_token = get_access_token(app_id, app_secret)
    send_wx_customer_msg(access_token, "oTE_f0X1yZeUStN8x5IsQLWHdYSs")
