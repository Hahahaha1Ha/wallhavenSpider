import os
from string import ascii_letters
import sys
import json
def write_save_path():
    path_lake_get=getattr(sys,"_MEIPASS",os.path.dirname(os.path.abspath(__file__)))+'\\bugLake.json'
    with open(path_lake_get,'r+') as path_lake:
        pathlakefinal=json.load(path_lake)
    final=choose_save(pathlakefinal)
    print("最后路径如下",final)
    return final

def choose_save(pathlake):
    outcheck=True
    while outcheck:
        print("保存路径如下,选择一个存储图片")
        for a1 in range(1,6):
            print(("{}号路径:".format(a1)),pathlake["datapath"][("path_{}".format(a1))])
        getpathindex=str(input("选择1-5号:"))
        if getpathindex not in ["1","2","3","4","5"]:
            getpathindex = 1

        if pathlake["datapath"][("path_{}".format(getpathindex))] == "None":
            write_save(pathlake,getpathindex)
        else:
            askcheck=str(input("需要重新设置路径吗? \n 1--->换 \n 0--->不换 \n"))
            if askcheck[0] not in ("1","0"):
                askcheck="0"
                if not (os.path.isdir(pathlake["datapath"][("path_1")])):
                    print("1号路径不存在,请重新设置")
                    write_save(pathlake,1)
                return pathlake["datapath"][("path_{}".format(getpathindex))]
            elif askcheck[0] is "1":
                write_save(pathlake,getpathindex)
                return pathlake["datapath"][("path_{}".format(getpathindex))]
            else:
                if not (os.path.isdir(pathlake["datapath"][("path_{}".format(getpathindex))])):
                    print("{}号路径不存在,请重新设置".format(getpathindex))
                    write_save(pathlake,getpathindex)
                    return pathlake["datapath"][("path_{}".format(getpathindex))]
                else:
                    return pathlake["datapath"][("path_{}".format(getpathindex))]
        outcheck=False


def write_save(path_read,write_path):
    path=getattr(sys,"_MEIPASS",os.path.dirname(os.path.abspath(__file__)))+'\\bugLake.json'
    outcheck=True
    while outcheck:
        try:
            setpath=(input("输入一个路径:"))
        except FileNotFoundError:
            print("啊哦,此路径似乎不存在")
        else:
            a1=""
            for _ in setpath:
                if _ != '"' :
                    a1 += _
            if os.path.isdir(a1) is False:
                print("此路径似乎无法使用,尝试使用绝对路径或者换一个")
            else:
                path_read["datapath"][("path_{}".format(write_path))] = a1
                with open(path,"w",encoding="utf-8") as pathlake_back:
                    json.dump(path_read,pathlake_back,indent=1,)
                outcheck=False
            


