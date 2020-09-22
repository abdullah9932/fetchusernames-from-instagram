from bs4 import BeautifulSoup as bs
import time
from time import sleep
import re
import requests
import os
import json 

def download(url,driver,dir,name):
    counter=1
    usernames=""
    username=""
    driver.get(url)
    time.sleep(3)
    SCROLL_PAUSE_TIME = 1
    driver.find_element_by_class_name("_9AhH0").click()
    time.sleep(4)
    html_to_parse=str(driver.page_source)
    html=bs(html_to_parse,'html5lib')
    usernames=html.findAll("div", {"class":"e1e1d" })
    username=usernames[0]
    usrname=re.findall('<[a][^>]*>(.+?)</[a]>', str(username))
    with open("username.txt","a+") as usr:
        usr.write(str(usrname[0])+'\n')
    time.sleep(4)
    while(counter!=name):
        driver.find_element_by_link_text("Next").click()
        time.sleep(4)
        counter+=1
        html_to_parse=str(driver.page_source)
        html=bs(html_to_parse,"html5lib")
        time.sleep(3)
        usernames=html.findAll("div", {"class":"e1e1d" })
        username=usernames[0]
        usrname=re.findall('<[a][^>]*>(.+?)</[a]>', str(username))
        with open("username.txt","a+") as usr:
          usr.write(str(usrname[0])+'\n')
        time.sleep(5)    
    return
