# try:
import requests,time,os
#     import time
#     import os
# except:
#     import pip
#     pip.main(['install','requests','time','os'])
#http://m.ximalaya.com/starwar/task/listen/layout/center/home
#python 实现微信接口 https://cloud.tencent.com/developer/article/1562230
# url_home_get="http://m.ximalaya.com/starwar/task/listen/layout/center/home"
url_record_get="http://m.ximalaya.com/starwar/lottery/check-in/record"
# url_v1_post="https://mermaid.ximalaya.com/collector/web-pl/v1"
url_action_post="http://m.ximalaya.com/starwar/lottery/check-in/check/action"
url_sigin="http://hybrid.ximalaya.com/web-activity/signIn/action?aid=8&ts={}}&_sonic=0&_sonic=0 h2"
url_taskrecords="http://hybrid.ximalaya.com/web-activity/task/taskRecords?ts=1604656300792&_sonic=0&_sonic=0 h2"

cookie=os.getenv("cookie")
#https://cloud.tencent.com/developer/article/1476101
#Appium是移动端自动化测试工具，它可以模拟App内部的各种操作，本次用到就有「点击」和「下滑」。
#其实就跟selenium 一样，只不过一个是电脑端自动化，一个是手机端自动化。
#mitmproxy

def xmly_signin():
    url_record_get = "http://m.ximalaya.com/starwar/lottery/check-in/record"
    url_get_coin="http://m.ximalaya.com/starwar/lottery/task/gold-coin"
    url_action_post = "http://m.ximalaya.com/starwar/lottery/check-in/check/action"
    time13=int(round(time.time()*1000))
    drawtaskaward="https://hybrid.ximalaya.com/web-activity/task/drawTaskAward?ts=%s&_sonic=0&_sonic=0 h2"%(time13)
    headers = {
        "cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36",
        "Content-Type": "application/json"
    }
    respon_getcoin=requests.get(url_get_coin,headers=headers)
    print("totalGoldCoins",respon_getcoin.json()["totalGoldCoins"])
    day=time.strftime("%Y%m%d", time.localtime())
    data={
        'aid': 9,
        "date": day,
        # "listenTime": 5374,
    }
    respon_sigin=requests.post(url_sigin,headers=headers,)
    print("msg",respon_sigin.json()["data"]["msg"])
    respon_taskrecords=requests.post(url_taskrecords,headers=headers,json=data)
    print("countDownMills",respon_taskrecords.json()["data"]["countDownMills"])
    # respon_record = requests.get(url_record_get)
    # print("continuousDays",respon_record.json())
if __name__ == '__main__':
    xmly_signin()
