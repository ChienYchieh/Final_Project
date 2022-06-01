#!/usr/bin/env python
# coding: utf-8

# In[31]:


import random
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
web = requests.get('https://www.google.com/search?q=%E6%AD%A3%E5%A6%B9&rlz=1C1VDKB_zh-TWTW968TW968&sxsrf=ALiCzsbpJ32YYwZzhP_-xhIp1A0rPCTIyg:1653983833798&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjXtYL3oYn4AhWXmFYBHRbOAJAQ_AUoAXoECAIQAw&biw=1500&bih=889&dpr=2.html', cookies={'over18':'1'})
web2=requests.get('https://www.google.com/search?q=%E7%BE%8E%E5%A5%B3&tbm=isch&ved=2ahUKEwjI-dSdlIv4AhVH-WEKHckNCAoQ2-cCegQIABAA&oq=%E7%BE%8E%E5%A5%B3&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyBQgAEIAEMgUIABCABDILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CAgAELEDEIMBOgQIABADOgcIIxDqAhAnOgQIIxAnOgQIABAeOgQIABAYOgYIABAeEAVQhq4CWJPjAmCp5QJoCHAAeACAAYgBiAGbCpIBBDExLjSYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCsABAQ&sclient=img&ei=bMiWYsiTDcfyhwPJm6BQ&bih=889&biw=1500&rlz=1C1VDKB_zh-TWTW968TW968&hl=zh-TW', cookies={'over18':'1'})
web3=requests.get('https://www.google.com/search?q=%E7%BE%8E%E5%A5%B3&tbm=isch&hl=zh-TW&chips=q:%E7%BE%8E%E5%A5%B3,g_1:%E5%8F%B0%E7%81%A3:A4x7Jp_Bh8k%3D&rlz=1C1VDKB_zh-TWTW968TW968&sa=X&ved=2ahUKEwi049PFlIv4AhWPS_UHHdS8DfEQ4lYoAnoECAEQIQ&biw=1483&bih=889',cookies={'over18':'1'})
soup = BeautifulSoup(web.text, "html.parser")
soup2= BeautifulSoup(web2.text, "html.parser")
soup3= BeautifulSoup(web3.text, "html.parser")
imgs = soup.find_all('img')
imgs2= soup2.find_all('img')
imgs3= soup3.find_all('img')
name = 0

img_urls = []# 根據爬取的資料，建立一個圖片名稱與網址的空串列
img_urls2 = []
img_urls3 = []
Girl_Array=[]

for i in imgs:                         # 修改 for 迴圈內容
    img_urls.append([i['src'], name])    # 將圖片網址與編號加入串列中
    name = name + 1                      # 編號增加 1
    
for i in imgs2:                         
    img_urls2.append([i['src'], name])   
    name = name + 1 

for i in imgs3:                         
    img_urls3.append([i['src'], name])   
    name = name + 1
# ran_num = random.randint(1, 20)
# result1 = img_urls[ran_num][0]
# result2=result1+".jpg"
for i in range(len(img_urls)):
    result1 = img_urls[int(i)][0]
    result2=result1+".jpg"
    Girl_Array.append(result2)
for i in range(len(img_urls2)):
    result1 = img_urls[int(i)][0]
    result2=result1+".jpg"
    Girl_Array.append(result2)
for i in range(len(img_urls3)):
    result1 = img_urls[int(i)][0]
    result2=result1+".jpg"
    Girl_Array.append(result2)

