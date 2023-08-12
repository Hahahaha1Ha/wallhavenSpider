import time
from bs4 import BeautifulSoup
import requests
import re
import os
from tqdm import tqdm

def mainControl():
    target_1=str(input("键入你需要爬的主题"))
    page=input("选择你需要的页数")
    GetHtmlPack(page,target_1)

def GetHtmlPack(Pages,target):
    Catch=re.compile(r'https://wallhaven.cc/w/[0-9a-z\D]{6}')
    http1='https://wallhaven.cc/search?q={}&search_image=&page={}'.format(str(target),str(Pages))
    RequestBack=requests.get(http1,headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'}).content
    HtmlBack=BeautifulSoup(RequestBack,'html.parser')
    LiFound=HtmlBack.find_all("a",attrs={"class":"preview","target":"_blank"})
    for i in range(0,len(LiFound)):
        time.sleep(1.2)
        downLoad(Catch.findall(str(LiFound[i])))
    
    print("已下载",len(LiFound),"张图片")

def downLoad(Https):
    DataPath=""
    StrValue=Https[0]
    FinalHttp="https://w.wallhaven.cc/full/{}/wallhaven-{}.jpg".format(StrValue[-6:-4],StrValue[-6::])
    ImageData=requests.get(FinalHttp,"html.parser",stream=True)
    ImageData1=BeautifulSoup(ImageData.content,"html.parser")
    total1=int(ImageData.headers.get('content-length',0))
    if checkHttps(ImageData1):
        Name1=StrValue[-6::]+'.jpg'
        o=open(DataPath+Name1,'wb')
        a1=tqdm(desc=(StrValue[-6::]),total=total1,unit='iB',unit_scale=True,unit_divisor=1024)
        for BackData in ImageData.iter_content(chunk_size=1):
                size=o.write(BackData)
                a1.update(size)
        print("已成功下载",(StrValue[-6::]))
    else:
        FinalHttp="https://w.wallhaven.cc/full/{}/wallhaven-{}.png".format(StrValue[-6:-4],StrValue[-6::])
        ImageData=requests.get(FinalHttp,"html.parser",stream=True)
        Name1=StrValue[-6::]+'.png'
        o=open(DataPath+Name1,'wb')
        a1=tqdm(desc=(StrValue[-6::]),total=total1,unit='iB',unit_scale=True,unit_divisor=1024)
        for BackData in ImageData.iter_content(chunk_size=1):
                size=o.write(BackData)
                a1.update(size)
        print("已成功下载",(StrValue[-6::]))

def checkHttps(https):
    Check=re.compile(r'[0-9a-z]{3}\s[a-zA-Z\D]{3}\s[a-zA-Z\D]{5}')
    Found=https.find_all("title")
    FinalAnswer=True
    if Found == []:
        pass
    else:
        Find=Found[0]
        Get=Check.findall(str(Find))
        if '404' in Get[0]:
            FinalAnswer=False
    return FinalAnswer

mainControl()

