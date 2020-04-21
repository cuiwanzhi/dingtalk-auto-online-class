import pyautogui as auto
import time
import threading as thd
import datetime
def indx():
    while 1:
        print("indx")
        poss = auto.locateCenterOnScreen("qiandaotixing.jpg")
        print(poss)
        if poss !=None:
            auto.moveTo(poss)
            auto.click()
        
        time.sleep(1)
        poss = auto.locateCenterOnScreen("qiandaoanniu.jpg")
        print(poss)
        if poss !=None:
            auto.moveTo(poss)
            auto.click()
            
        poss = auto.locateCenterOnScreen("zhibo.jpg")
        print(poss)
        if poss !=None:
            auto.moveTo(poss)
            auto.click()
            zhiboing()
            
        time.sleep(10)

def qiandaochenggong():
    while 1:
        print("qingdaochengong")
        poss = auto.locateCenterOnScreen("zhibo.jpg")
        print(poss)
        if poss !=None:
            auto.moveTo(poss)
            auto.click()
            zhiboing()
        time.sleep(60)

def zhiboing():
    while 1:
        print("zhibo")
        poss = auto.locateCenterOnScreen("fanhui.jpg")
        print(poss)
        if poss !=None:
            auto.moveTo(poss)
            auto.click()
            s = TimeNow()
            if s == "ok":
                indx()
            else:
                ready()
        time.sleep(120)

def TimeNow():
    for i in range (2):
        # 范围时间
        d_time = datetime.datetime.strptime(str(datetime.datetime.now().date())+x[i], '%Y-%m-%d%H:%M')
        d_time1 =  datetime.datetime.strptime(str(datetime.datetime.now().date())+y[i], '%Y-%m-%d%H:%M')
         
        # 当前时间
        n_time = datetime.datetime.now()
         
        # 判断当前时间是否在范围时间内
        if n_time > d_time and n_time<d_time1:
            auto.keyDown('win')  # hold down the shift key
            auto.press('d')     # press the left arrow key
            auto.keyUp('win')    # release the shift key
            print("isTime")
            return "ok"
    print("notTime")
    return "no"
def StartDD():
    while 1:
        print("qidong")
        poss = auto.locateCenterOnScreen("qidong.jpg")
        poss2 = auto.locateCenterOnScreen("qidong2.jpg")
        print(poss)
        print(poss2)
        if poss !=None:
            auto.moveTo(poss)
            auto.click()
            auto.click()
            print("StartDD")
            indx()
        else:
            if poss2 != None:
                auto.moveTo(poss2)
                auto.click()
                auto.click()
                print("StartDD")
                indx()
def ready():
    while 1:
        s = TimeNow()
        if s=="ok":
            StartDD()
        time.sleep(600)

x=["7:30","14:20"]#上课时间
y=["12:00","17:00"]#下课时间
ready()
