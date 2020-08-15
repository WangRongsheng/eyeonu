import requests
import json
import os
import webbrowser
from requests.packages import urllib3
urllib3.disable_warnings()

def get_yourname(qq):
    url ='https://cloud.qqshabi.cn/api/qqinfo.php?qq='+str(qq)
    r = requests.get(url, verify=False)
    json_response = r.content.decode()
    dict_json = json.loads(json_response)
    return dict_json['name']

def get_skey_and_pskey():
    mingling = eval(input("请问您想通过QQ账号密码登录还是二维码扫描登录以获取key，如果是QQ账号密码请输入1，二维码登录请输入2，如果您已经获取到key请随意输入数字："))
    if str(mingling) == '1':
        url = 'https://demo.sqdxwz.com/qq/index.html'
        webbrowser.open(url)
    if str(mingling) == '2':
        url = 'https://demo.sqdxwz.com/qq/index2.html'
        webbrowser.open(url)

def get_sweet():
    url ='https://api.oioweb.cn/api/saohua.php'
    r = requests.get(url)
    json_response = r.content.decode()
    dict_json = json.loads(json_response)
    return dict_json['msg']

def get_your_sweet(qq,skey,pskey):
    url ='https://cloud.qqshabi.cn/api/care.php?uin='+str(qq)+'&skey='+str(skey)+'&pskey='+str(pskey)
    r = requests.get(url, verify=False)
    json_response = r.content.decode()
    dict_json = json.loads(json_response)
    return dict_json['count']

def main():
    print("为了进行查询，将进行获取key的操作，这将会打开你的浏览器！\n")
    print("！！！提示：成功登录之后，您将会看到您的【QQ账号】、【SKER】、【P_skey】、【superkey】，请您复制保存【SKER】、【P_skey】即可！！！\n")
    get_skey_and_pskey()
    print("\n")
    qq = input("请再次输入您要查询的QQ号：")
    qq_name = get_yourname(qq)
    skey = input("请输入您刚才保存的【SKEY】：")
    pskey = input("请输入您刚才保存的【P_skey】：")
    sweet_count = get_your_sweet(qq,skey,pskey)
    print("亲爱的{}，您的QQ上有{}特别关心你的人哦，如果有一天你知道他们是谁，请你一定要告诉他们：{}".format(qq_name,sweet_count,get_sweet()))

main()
    
    

