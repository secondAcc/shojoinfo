from selenium import webdriver
import zipfile
import requests
import time
import shutil
import os
from bs4 import BeautifulSoup as bs

print("initializing...")
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome("../programs/chromedriver.exe")  # ,chrome_options=options)


class address:
    def init(self):
        self.name = ""
        self.addr = ""

    def name(self, a):
        self.name = a

    def addr(self, a):
        self.addr = a


def login():
    global checklog
    url = "https://github.com/login"
    driver.get(url)
    driver.find_element_by_name('login').send_keys('hello111353@gmail.com')
    driver.find_element_by_name('password').send_keys('dlgusdn0019')
    driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[7]').click()
    checklog = True


def download():
    global checklog
    global code
    login()
    url = "https://github.com/shojoinfo/shojoinfo"
    driver.get(url)
    driver.find_element_by_css_selector(
        '#js-repo-pjax-container > div.container-lg.clearfix.new-discussion-timeline.experiment-repo-nav.px-3 > div.repository-content > div.file-navigation.in-mid-page.d-flex.flex-items-start > details.get-repo-select-menu.js-get-repo-select-menu.position-relative.details-overlay.details-reset > summary').click()
    driver.find_element_by_css_selector(
        '#js-repo-pjax-container > div.container-lg.clearfix.new-discussion-timeline.experiment-repo-nav.px-3 > div.repository-content > div.file-navigation.in-mid-page.d-flex.flex-items-start > details.get-repo-select-menu.js-get-repo-select-menu.position-relative.details-overlay.details-reset > div > div > div.get-repo-modal-options > div.mt-2 > a:nth-child(2)').click()
    zip = zipfile.ZipFile('C:\\Users\\dolph\\Downloads\\shojoinfo-master.zip')
    zip.extractall('C:\\Users\\dolph\\Desktaop\\web\\resources')
    file = ('./shojoinfo-master/sourcefile.txt')
    shutil.move(file, ('./resources/sourcefile.txt'))
    shutil.rmtree('./resources/shojoinfo-master')


def extr():
    zip = zipfile.ZipFile('C:\\Users\\dolph\\Downloads\\shojoinfo-master.zip')
    zip.extractall('C:\\Users\\dolph\\Desktop\\web\\resources')
    file = ('./shojoinfo-master/sourcefile.txt')
    shutil.move(file, ('./resources/sourcefile.txt'))
    shutil.rmtree('./resources/shojoinfo-master')


def clear():
    file = './resources/sourcefile.txt'
    f = open(file, 'r', encoding='UTF8')
    line = f.readlines()
    f.close()
    code = []
    index = 0
    print("check")
    while index < len(line):
        if index % 3 == 0:
            a = address()
            a.name(str(line[index]))
            print(line[index])
        elif index % 3 == 1:
            a.addr(str(line[index]))
            print(line[index])
        elif index % 3 == 2:
            code.append(a)
        index += 1
    index = 0
    f = open(file, 'w', encoding='UTF8')
    while index < len(code):
        i = str(code[index].name)
        if not ("소녀전선 일반" in i or "소녀전선 0-" in i or "소녀전선 긴급" in i or "소녀전선 야간" in i):
            code[index].name = str(0)
        index += 1
    for i in code:
        if (str(i.name) == str(0)):
            continue
        f.write(str(i.name))
        f.write(str(i.addr))
        print(i.addr)
    f.close()


class newfile_info():
    def __init__(self, l):
        self.name = ""
        self.addr = ""
        self.text = l
        self.stage=""
    def init(self,num):
        self.stage=str(num)
        self.text = self.text[:self.text.find('<th>')]
        self.text = self.text[self.text.find('MIDNIGHT'):]
    def clear(self):
        self.text = self.text[self.text.find('href'):]

        self.addr = self.text[self.text.find('"'):self.text.find('" target')+1]
        self.addr = self.addr[self.addr.find('"')+1:self.addr.find('" style')]
        self.text = self.text[self.text.find('217);">') + 7:]
        self.text=self.text[self.text.find(self.stage+"-"):]
        self.name = self.text[:self.text.find('</')]


def newfile():
    f=open("resource.txt",'w')
    url = "https://jabjang.tistory.com/478"
    driver.get(url)
    html = driver.page_source
    html = bs(html, 'html.parser')
    tablenum=11
    num=0
    while num<=11:
        select="div.article > div.tt_article_useless_p_margin > "
        if num==1:
            select+="div:nth-child(16) > table > tbody"
        else:
            select+="table:nth-child(%d) > tbody"%tablenum
        find = newfile_info(str(html.select(select)))
        find.init(num)
        while find.text.find('href') != -1:
            find.clear()
            f.write(find.name+"\n"+find.addr+"\n")
            print("name :"+find.name + find.addr)
        tablenum+=5
        if num==1:
            tablenum+=3
        if num==10:
            tablenum-=1
        num+=1
    f.write("1-4N\nhttps://jabjang.tistory.com/150")
    f.close()

def test():
    a=10
    print(str(a)+"-")

code=""
while code != 'exit':
    print(">>>", end='')
    code = input()
    if code == "login":
        login()
    elif code == 'extract':
        extr()
    elif code == 'download':
        download()
    elif code == 'clear':
        clear()
        print("test.txt created. if it's all, copy sourcefile.txt")
        print("please add 0-")
    elif code == 'newfile':
        newfile()
    elif code=='test':
        test()
    else:
        print("no operate")
