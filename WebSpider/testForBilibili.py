# coding : UTF-8
import random
import re
import socket
import requests
from bs4 import BeautifulSoup


class Detecting(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('class Detecting is running:%s' %self._func.__name__)
        # print('1111111',*args)
        # print('222222222',**kwargs)
        output = self._func(*args)
        print('class Detecting is ending:%s' %self._func.__name__)
        return output

def line_here():
    print("=======================================================================================================")
#不对,bilibili仍旧无法爬去视频信息

@Detecting
def get_content(url, data=None):
    header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Cookie':'finger=edc6ecda; LIVE_BUVID=AUTO4915313547991291; fts=1531354832; buvid3=28DCADD6-FA5C-452C-BFF7-C1A813A6950B6688infoc; DedeUserID=15215774; DedeUserID__ckMd5=0128c237b8633e09; SESSDATA=de1297b3%2C1533946858%2C2120a295; bili_jct=22f2da3a7f21022e520fcef44c6a37b8; sid=82fgiimu; rpdid=owimllkisldoskolxksxw; bp_t_offset_15215774=142127722026902305; _dfcaptcha=d351d76f54567e4e03b2060b817ed16e',
    }
    timeout = random.choice(range(80, 100))
    # dont know why there is a while True in this line!
    try:
        req = requests.get(url=url, headers=header, timeout=timeout)
        req.encoding = 'UTF-8'
        return req.text
    except socket.timeout as e:
        print("!!!error occurs in get_content()!")


# @Detecting
# def get_data(html_content):
#     final=[]
#     soup=BeautifulSoup(html_content, "html.parser")
#     body=soup.body
#     day=body.find_all('li',{'class':'skyid'})
#     for element in day:
#         print()
#         temp={}
#         date=element.find('h1').string
#         print("this is date",date)
#         temperature_max=element.find('span').string
#         temperature_min = element.find('i').string
#         # print("there are temperature:{} / {}".format(temperature_max,temperature_min))
#         weather=element.find('p',{'class':'wea'}).string
#         # print("The weather is ",weather)
#         wind=element.find('p',{'class':'win'})
#         wind_level=wind.find('i').string
#         # print(wind_level)
#         wind_dir=wind.find('em').find_all('span')
#         for wd in wind_dir:
#             print(str(wd))
#             print('test:::::::::',wd['title'])
#             """
#             可以用soup['class']获得class的名字 like class='zhazha' soup['class']== 'zhazha'
#             """
#             search_obj=re.search(r"title=\"(.*?)\"", str(wd))
#             # print(search_obj.group(1))
#     return 0

def get_video(html_content):
    soup=BeautifulSoup(html_content, "html.parser")
    body=soup.body
    video_div=body.find('div',{'id':'app'}).find('div',{'class':'bilibili-player-video'})
    print('test============================',video_div)
    return 0

if __name__ == '__main__':
    target = 'https://www.bilibili.com/'
    html_content = get_content(target)
    print(html_content)
    line_here()
    get_video(html_content)