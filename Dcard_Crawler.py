import urllib.request as req
import requests
import json
import os
import time

def getimg(url):
    global index
    request=req.Request(url,headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        #print(data)

    data=json.loads(data)
    for key in range(len(data)):
        post=data[key]["media"]
        title=data[key]["title"]
        for i in range(len(filterSign)):
            title=title.replace(filterSign[i],"_")
        print(title)
        index=0
        for keys in range(len(post)):
            imgurl=post[keys]["url"]
            # print(imgurl)
            # img=requests.get(imgurl)
            req.urlretrieve( imgurl , 'C:\ImageSave\%s_%s.jpg' %(title,index) )
            index= index+1
            time.sleep(5) #保持禮貌
    #print(data[99]["id"])        
    return data[99]["id"]

path="C:\ImageSave"
if not os.path.isdir(path):
    os.mkdir(path)

filterSign=["\n","\\","/","*","?","\"",":","<",">","|"]

print("感情 relationship , 有趣 funny , 心情 mood , 美食 food , 女孩 girl , 美妝 makeup , 穿搭 dressup , 工作 job , 西斯 sex")
Kanban=input("輸入你想要的看板(英文):")
number=input("輸入你要抓取得文章數量(一百為一個單位):")
print("努力下載中...")

url="https://www.dcard.tw/service/api/v2/forums/"+ Kanban +"/posts?popular=false&limit=100"
count=0
while count<int(number):
    url="https://www.dcard.tw/service/api/v2/forums/"+ Kanban +"/posts?popular=false&limit=100&before="+str(getimg(url))
    count+=1        