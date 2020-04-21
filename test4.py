import pyautogui as auto
import time
import threading as thd
import datetime
import xlrd
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
    ClassTimeStart = -1 #第几大节课
    HowWeek = 0 #第几周
    int_vule1 = 0 #课程第几周开始周
    int_vule2 = 0 #课程第几周结束
    HaveClass = 0 #是否有课标志

    n_time = datetime.datetime.now() # 当前时间
    today = datetime.date.today() #获取日期
    print("date="+str(n_time))
    print("week="+str(today.weekday()))
    
    data = xlrd.open_workbook("test.xlsx")
    table = data.sheet_by_index(0) # 通过索引顺序获取
    nrows = table.nrows #行
    ncols = table.ncols #列
    
    
    d = datetime.date(2020,4,13) #第八周开始的日期
    interval =str( today - d)
    HowWeek = int(int(int(interval[0]) / 7) +8) #计算当前是第几周
    
   
    
    for i in range (4):
        # 范围时间
        d_time = datetime.datetime.strptime(str(datetime.datetime.now().date())+x[i], '%Y-%m-%d%H:%M')
        d_time1 =  datetime.datetime.strptime(str(datetime.datetime.now().date())+y[i], '%Y-%m-%d%H:%M')
        
        # 判断当前时间是否在范围时间内
        if n_time > d_time and n_time<d_time1:
            ClassTimeStart = i ;#第几大节课
            print(i)
            for j in range (3): #判断本周本大节课是否有课
        
                s = table.cell( int((int(ClassTimeStart)*3)+j),today.weekday()).value
                #print(s)
                if s != '':
                    sub=s.split(',', 1 )
                    int_vule1 =int( sub[0])
                    int_vule2 =int( sub[1])
                if HowWeek >= int_vule1 and HowWeek <= int_vule2:
                    HaveClass = 1
                break
            break

    print("HowWeek="+str(HowWeek))
    print("ClassTimeStart="+str(ClassTimeStart))
    print("HaveClass="+str(HaveClass))
    
    if HaveClass == 1:
        #print(int((int(ClassTimeStart)*3)+i))
        #print(today.weekday())
        HaveClass=0
        StartDD()
    else:
        ready()

    

def StartDD():
    auto.keyDown('win')  # hold down the shift key
    auto.press('d')     # press the left arrow key
    auto.keyUp('win')    # release the shift key
        
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
        time.sleep(600)
        TimeNow()
        
        


x=["7:30","10:10","14:20","19:20"]#上课时间
y=["10:00","11:50","16:50","21:50"]#下课时间
TimeNow()

