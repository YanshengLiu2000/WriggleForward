import random
import socket

import requests
from bs4 import BeautifulSoup

URL='http://www.nationalgeographic.com.au/animals/'


def get_content(url, data=None):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    timeout = random.choice(range(80, 100))
    # dont know why there is a while True in this line!
    try:
        req = requests.get(url=url, headers=header, timeout=timeout)
        req.encoding = 'UTF-8'
        return req.text
    except socket.timeout as e:
        print("!!!error occurs in get_content()!")


html=get_content(URL)
# print(html)
soup=BeautifulSoup(html,'lxml')
all_img=soup.find_all('span',{'class':'LazyLoader'})
number=0
for span in all_img:
    img_url_pre=span.find('img',{'class':'LazyImage'})
    img_url=img_url_pre['data-src']
    r=requests.get(img_url,stream=True)
    image_name=str(number)+'image.jpg'
    number+=1
    with open('./%s' % image_name,'wb') as f:
        for chunk in r.iter_content(chunk_size=64):
            f.write(chunk)
    print('%s has been saved!' % image_name)

