from selenium import webdriver
import zipfile
import requests
import time
import shutil
import os
from bs4 import BeautifulSoup as bs

checklog=False
print("initializing...")
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver=webdriver.Chrome("./programs/chromedriver.exe")#,chrome_options=options)
class address:
    def init(self):
        self.name=""
        self.addr=""
    def name(self,a):
        self.name=a
    def addr(self,a):
        self.addr=a
def login():  
    global checklog
    url="https://github.com/login"
    driver.get(url)
    driver.find_element_by_name('login').send_keys('hello111353@gmail.com')
    driver.find_element_by_name('password').send_keys('dlgusdn0019')
    driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[7]').click()
    checklog=True

def download():
    global checklog
    global code
    login()
    url="https://github.com/shojoinfo/shojoinfo"
    driver.get(url)
    driver.find_element_by_css_selector('#js-repo-pjax-container > div.container-lg.clearfix.new-discussion-timeline.experiment-repo-nav.px-3 > div.repository-content > div.file-navigation.in-mid-page.d-flex.flex-items-start > details.get-repo-select-menu.js-get-repo-select-menu.position-relative.details-overlay.details-reset > summary').click()
    driver.find_element_by_css_selector('#js-repo-pjax-container > div.container-lg.clearfix.new-discussion-timeline.experiment-repo-nav.px-3 > div.repository-content > div.file-navigation.in-mid-page.d-flex.flex-items-start > details.get-repo-select-menu.js-get-repo-select-menu.position-relative.details-overlay.details-reset > div > div > div.get-repo-modal-options > div.mt-2 > a:nth-child(2)').click()
    zip=zipfile.ZipFile('C:\\Users\\dolph\Downloads\\shojoinfo-master.zip')
    zip.extract('C:\\Users\\dolph\\Desktop\\web\\resources')

def extr():
    zip=zipfile.ZipFile('C:\\Users\\dolph\\Downloads\\shojoinfo-master.zip')
    zip.extractall('C:\\Users\\dolph\\Desktop\\web\\resources')
    file=('./shojoinfo-master/sourcefile.txt')
    shutil.move(file,('./resources/sourcefile.txt'))
    shutil.rmtree('./resources/shojoinfo-master')

def clear():
    file='./resources/sourcefile.txt'
    f=open(file,'r',encoding='UTF8')
    line=f.readlines()
    f.close()
    check=0
    code=[]
    index=0
    while index<len(line):
        if index%3==0:
            a=address()
            a.name(str(line[index]))
        elif index%3==1:
            a.addr(str(line[index]))
        elif index%3==2:
            code.append(a)
        index+=1
    print(code)
    index=0
    f=open(file,'w',encoding='UTF8')
    while index<len(code):
        i=code[index].name
        if not("소녀전선 일반" in i or "소녀전선 0-" in i or "소녀전선 긴급" in i or "소녀전선 야간" in i):
            code[index].name=0
        index+=1
    for i in code:
        f.write(i.name)
        f.write(i.addr)
        print(i.addr)
    f.close()

print("init end")
code=''
while code!='exit':
    print(">>>",end='')
    code=input()
    if code=="login":
        login()
    elif code=='extract':
        extr()
    elif code=='download':
        download()
    elif code=='clear':
        clear()
    else:
        print("no operate")
        continue