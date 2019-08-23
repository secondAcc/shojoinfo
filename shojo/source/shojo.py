import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests
import webbrowser as wb

###chromedriver setting###
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver=webdriver.Chrome("./programs/chromedriver.exe",chrome_options=options)

mainnum=0
subnum=0
tabmany=0
timename=""
fightName=""
popupui='./uifiles/popupui.ui'
   


class mypopup(QDialog):###새 탭###
    def __init__(self):
        super().__init__()
        self.layout=QVBoxLayout()
        self.setWindowTitle(fightName)
        print(fightName)
        uic.loadUi(popupui,self)
        self.init()

    def init(self):
        print("check")
        for i in range(0,100):
            btn=QPushButton("hi")
            self.contentLayout.addWidget(btn)
            self.contentLayout.addStretch(1)
        #self.name
        url=""
        index=0
        while index<len(address):
            if fightName in str(i):
                url=str(address[index+1])
                print("address catched")
                break
            index+=2
        print(url)
        wb.open(url)
        self.fieldName.setText("    "+fightName)
        #self.conditionName
        self.layout.addWidget(self.fieldName)
        self.setLayout(self.contentLayout)

class findFightTab(QWidget):###세부지역탭###
    def __init__(self):
        super().__init__()
        self.layout=QVBoxLayout()
        #self.status=self.statusBar()
        self.initUI()

    def initUI(self):
        but=[]
        self.w=[]
        for i in range(0,20):
            but.append(0)
            self.w.append(0)
        for i in range(0,6):
            self.name=(str(mainnum)+"-"+str(i+1)+timename)
            but[i]=QPushButton(self.name) ###버튼 제작###
            but[i].clicked.connect(self.newtab)
            self.layout.addWidget(but[i])
        self.layout.addStretch()
        self.setLayout(self.layout)

    def newtab(self):
        a=self.sender().text()
        print(a)
        global fightName
        global tabmany###버튼 눌렀을 때 탭 생성함수 호출###
        fightName=a
        self.w[tabmany]=mypopup()
        self.w[tabmany].show()
        tabmany+=1
class makeTab(QWidget):###난이도탭###
    def __init__(self):
        super().__init__()
        self.tabs=QTabWidget()
        self.layout=QVBoxLayout()        
        self.initUI()
        
    def initUI(self):
        global timename
        timename=""
        self.tabs.addTab(findFightTab(),"일반")
        timename="E"
        self.tabs.addTab(findFightTab(),"긴급(E)")
        timename="N"
        self.tabs.addTab(findFightTab(),"야간(N)")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

class makeOptionTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout=QVBoxLayout()

        self.initui()

    def initui(self):
        print("hi")

    def resourceDownload(self): ###주소 소스파일 제작###
        f=open("./resources/address.txt","w")
        addr = []    # 빈 리스트 생성
        index=0
        for i in range(2000):
            line = []          
            line.append("")
            addr.append(line)
    
            
class commonFightTab(QWidget):###지역탭###
    def __init__(self):
        super().__init__()
        self.tabs=QTabWidget()
        self.layout=QVBoxLayout()
        self.initUI()

    def initUI(self):
        global mainnum
        for i in range(0,13):
            mainnum=i
            self.tabs.addTab(makeTab(),str(i))
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
            

class MyApp(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
            ###전역탭###
        tabs = QTabWidget()
        tabs.addTab(commonFightTab(),'전역')
        tabs.addTab(makeOptionTab(),'option')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.resize(650,650)
        self.show()


f=open('./resources/sourcefile.txt','r',encoding='UTF8')
address=f.readlines()
f.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    