import requests,time,os,re,json,urllib3
urllib3.disable_warnings()
xmly_cookie=os.getenv("COOKIE")
entcorpid=os.getenv("ENTWX_CORPID")
entcorpsecret=os.getenv("ENTWX_CORPSECRET")
zdm_cookie=os.getenv("ZDM_COOKIE")

def getWxToken():
    url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s"%(entcorpid,entcorpsecret)
    respon=requests.get(url)
    data=respon.json()
    # print(data)
    return data["access_token"]
def sendWxMsg(con):
    token=getWxToken()
    msg="%s"%con
    # print(msg)
    url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s"%token
    data={
   "touser" : "@all",
   "toparty" : "",
   "totag" : "",
   "msgtype" : "text",
   "agentid" : 1000002,
   "text" : {
       "content" : msg
   },
   "safe":0,
   "enable_id_trans": 0,
   "enable_duplicate_check": 0,
   "duplicate_check_interval": 1800
}
    respon=requests.post(url=url,json=data)
    print(respon.json())

def xmly_signin():

    url_sigin = "http://hybrid.ximalaya.com/web-activity/signIn/action?aid=8&ts={}}&_sonic=0&_sonic=0 h2"
    url_taskrecords = "http://hybrid.ximalaya.com/web-activity/task/taskRecords?ts=1604656300792&_sonic=0&_sonic=0 h2"

    url_get_coin="http://m.ximalaya.com/starwar/lottery/task/gold-coin"
    headers = {
        "cookie": xmly_cookie,
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36",
        "Content-Type": "application/json"
    }
    respon_getcoin=requests.get(url_get_coin,headers=headers)
    msg={}
    # print("totalGoldCoins",respon_getcoin.json()["totalGoldCoins"])
    msg["coins"]=respon_getcoin.json()["totalGoldCoins"]
    day=time.strftime("%Y%m%d", time.localtime())
    data={
        'aid': 9,
        "date": day,

    }
    respon_sigin=requests.post(url_sigin,headers=headers,)
    # print("msg",respon_sigin.json()["data"]["msg"])
    msg["msg"]=respon_sigin.json()["data"]["msg"]
    respon_taskrecords=requests.post(url_taskrecords,headers=headers,json=data)
    # print("countDownMills",respon_taskrecords.json()["data"]["countDownMills"])
    msg["countDownMills"]=respon_taskrecords.json()["data"]["countDownMills"]
    msg["alert"]="喜马拉雅签到通知20210225"
    sendWxMsg(msg)

def zdm_checkin():
    url="https://zhiyou.smzdm.com/user/checkin/jsonp_checkin?callback=jQuery112406736468018154295_1576225909494&_=1576225909497"
    headers={
            'Host': 'zhiyou.smzdm.com',
            'Referer': 'https://www.smzdm.com/',
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'Cookie': zdm_cookie
        }
    s = requests.Session()
    respon=s.get(url=url,headers=headers,params={},verify=False)
    content_list = re.findall(r'[(](.*?)[)]', respon.text)
    content_json = json.loads(content_list[0])
    msg=content_json["data"]
    msg["alert"]="什么值得买签到通知"
    sendWxMsg(msg)

if __name__ == '__main__':
    xmly_signin()
    zdm_checkin()