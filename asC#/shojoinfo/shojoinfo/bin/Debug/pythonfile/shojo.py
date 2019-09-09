import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests
import webbrowser as wb

###폴더주소 구하기###
pwd=str(os.getcwd())
pwd=pwd.replace("\pythonfile",'')
pwd=pwd.replace('\\','/') 

###chromedriver setting###
def setupdriver():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver=webdriver.Chrome(executable_path=pwd+"/programs/chromedriver.exe",chrome_options=options)
###map site open###
def showmap():
    url=""
    index=0
    addrCatch=False
    while index<len(address):
        search=""
        if len(fightName)==fightName.find('-')+2:
                search+="일반 "
        elif fightName[fightName.find('-')+2]=='N':
            search+="야간 "
        elif fightName[fightName.find('-')+2]=='E':
            search+="긴급 "
        search+=fightName[0:fightName.find('-')+2]
        if search in str(address[index]):
            url=str(address[index+1])
            print("address catched")
            addrCatch=True
            break
        index+=2
    if addrCatch==False:
        return -1
        
    print(url)
    wb.open(url)
    self.fieldName.setText("    "+fightName)
    #self.conditionName
    self.layout.addWidget(self.fieldName)
    self.setLayout(self.contentLayout)

fi=pwd+"/resources/sourcefile.txt"
f=open(fi,'r',encoding='UTF8')
address=f.readlines()
f.close()
