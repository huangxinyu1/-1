# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:08:46 2019

@author: Python
"""

import requests
import time
from hashlib import md5
import random,json

key = input("要输入的单词:")
s = md5()
s.update("5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36".encode())
bv = s.hexdigest()
ts = int(time.time()*1000)
salt = str(ts)+str(random.randint(0,10))

string = "fanyideskweb" + key + str(salt) + "p09@Bn{h02_BIEe]$P^nG"
s = md5()

s.update(string.encode())
sign = s.hexdigest()

# F12或抓包工具抓到的POST的地址
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
#Accept-Encoding: gzip, deflate
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Content-Length': '253',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'OUTFOX_SEARCH_USER_ID=-1544471975@124.207.192.18; OUTFOX_SEARCH_USER_ID_NCOO=967949253.351933; td_cookie=18446744070977862614; JSESSIONID=aaaZJbgXzCunPga8_5YKw; ___rl__test__cookies=1551339488918',
'Host': 'fanyi.youdao.com',
'Origin': 'http://fanyi.youdao.com',
'Referer': 'http://fanyi.youdao.com/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',
        }
# 处理Form表单数据
data = {
        "i":key,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":salt,
        "sign":sign,
        "ts":str(ts),
        "bv":bv,
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult":"false",
    }



res = requests.post(url,data=data,headers=headers)

res.encoding="utf-8"
html =res.text

rDict = json.loads(html)
print("翻译:",rDict["translateResult"][0][0]["tgt"])
try:
    rlist = rDict["smartResult"]["entries"]
    print("解释:","".join(rlist))
except:
    print("出错")














































