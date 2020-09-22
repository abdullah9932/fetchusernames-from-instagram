import os
import function as insta_public
from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.keys import Keys

def main():
        File1='hashtags.txt'
        noofhashtags=2
        noofusrnames=100
        browser='firefox'
        username=''
        password=''
        login='No'
        user=str(username)
        password=str(password)
        if browser=='chrome':
            driver = webdriver.Chrome() 
        elif browser=='firefox':
            driver=webdriver.Firefox()
        time.sleep(2)
        if login=='Yes':
            driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
            time.sleep(3)
            driver.find_element_by_name('username').send_keys(user)
            driver.find_element_by_name('password').send_keys(password)
            driver.find_element_by_name('password').send_keys(Keys.RETURN)
            time.sleep(8)
        else:
            for j in range(0,noofhashtags):
               with open(File1) as Links:
                   hashtag = Links.readlines()[j]
                   Link='https://www.instagram.com/explore/tags/'+hashtag
                   insta_public.download(Link,driver,j,noofusrnames)
                    
                    
           
if __name__ == "__main__":
    main()
