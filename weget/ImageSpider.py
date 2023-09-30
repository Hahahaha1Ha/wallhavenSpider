from time import sleep
from bs4 import BeautifulSoup
import requests
import re
from tqdm import tqdm
import json
import random
from get_sort import asksort

def mainControl():
    sort=asksort()
    target_1=str(input("键入你需要爬的主题"))
    page=input("选择你需要的页数")
    GetHtmlPack(page,target_1,sort)

def GetHtmlPack(Pages,target,sortget):
    connectfile='./DataSpider/bugLake.json'
    with open(connectfile,'r') as file:
        lake=json.load(file)
    randomint=random.randint(1,5)
    a7="a{}".format(randomint)
    Catch=re.compile(r'https://wallhaven.cc/w/[0-9a-z\D]{6}')
    http1='https://wallhaven.cc/search?q={}&categories={}&purity={}&sorting={}&page={}'.format(str(target),sortget[0],sortget[1],sortget[2],str(Pages))
    RequestBack=requests.get(http1,headers={"User-Agent":lake[a7]}).content
    HtmlBack=BeautifulSoup(RequestBack,'html.parser')
    LiFound=HtmlBack.find_all("a",attrs={"class":"preview","target":"_blank"})
    for i in range(0,len(LiFound)):
        sleep(1.2)
        downLoad(Catch.findall(str(LiFound[i])))
    
    print("已下载",len(LiFound),"张图片")

def downLoad(Https):
    DataPath="F:\python Collect\DataSpider\ImageDataGet\\"
    StrValue=Https[0]
    FinalHttp="https://w.wallhaven.cc/full/{}/wallhaven-{}.jpg".format(StrValue[-6:-4],StrValue[-6::])
    ImageData=requests.get(FinalHttp,"html.parser",stream=True)
    ImageData1=BeautifulSoup(ImageData.content,"html.parser",from_encoding="iso-8859-1")
    total1=int(ImageData.headers.get('content-length',0))
    if checkHttps(ImageData1):
        Name1=StrValue[-6::]+'.jpg'
        o=open(DataPath+Name1,'wb')
        a1=tqdm(desc=(StrValue[-6::]),total=total1,unit='iB',unit_scale=True,unit_divisor=1024,ncols=80)
        for BackData in ImageData.iter_content(chunk_size=1):
                size=o.write(BackData)
                a1.update(size)
    else:
        FinalHttp="https://w.wallhaven.cc/full/{}/wallhaven-{}.png".format(StrValue[-6:-4],StrValue[-6::])
        ImageData=requests.get(FinalHttp,"html.parser",stream=True)
        Name1=StrValue[-6::]+'.png'
        o=open(DataPath+Name1,'wb')
        a1=tqdm(desc=(StrValue[-6::]),total=total1,unit='iB',unit_scale=True,unit_divisor=1024,ncols=80)
        for BackData in ImageData.iter_content(chunk_size=10):
                size=o.write(BackData)
                a1.update(size)

def checkHttps(https):
    Check=re.compile(r'[0-9a-z]{3}\s[a-zA-Z\D]{3}\s[a-zA-Z\D]{5}')
    Found=https.find_all("title")
    FinalAnswer=True
    if not Found:
        pass
    else:
        Find=Found[0]
        Get=Check.findall(str(Find))
        for c in ['404','403','402','401']:
            if c in Get[0]:
                FinalAnswer=False
    return FinalAnswer


mainControl()
