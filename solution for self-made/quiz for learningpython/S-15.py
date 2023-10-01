# dictionary와 tkinter 이용하여 스타벅스 키오스크 시스템 구현

from tkinter import *

window = Tk()

directory = ("drink", "bread", "etc")

drinklist = ['americano', 'latte', 'cappuccino', 'mocha', 'chocolate', 'macchiato']
breadlist = ['flatbread', 'honeybread', 'bagel', 'croissant']
etclist = ['icecream', 'affogato', 'soup']

buy = []

directorydic = {directory[0] : drinklist, 
           directory[1] : breadlist, 
           directory[2] : etclist}

print ("안녕하세요! 여기는 스타벅스입니다.")

def drinksel() :
    print (directorydic[directory[0]])
    
    while True : 
        dsel = input("어떤 음료를 주문하시겠어요? (만약 메뉴 추가를 중지하고 싶으시면 0을 입력하세요) : ")
        
        if dsel == 'master' : 
            master()
        
        if dsel == '0' :
            print ("현재 선택하신 메뉴 리스트는 다음과 같습니다. : ", buy)
            break
        
        if dsel in drinklist :
            print ("정상적으로 추가되었습니다.")
            buy.append (dsel)
        
        else :
            print ("메뉴에 없는 제품입니다.")
            
def breadsel() :
    print (directorydic[directory[1]])
    
    while True : 
        dsel = input("어떤 빵을 주문하시겠어요? (만약 메뉴 추가를 중지하고 싶으시면 0을 입력하세요) : ")
        
        if dsel == '0' :
            print ("현재 선택하신 메뉴 리스트는 다음과 같습니다. : ", buy)
            break
        
        if dsel in breadlist :
            print ("정상적으로 추가되었습니다.")
            buy.append (dsel)
        
        else :
            print ("메뉴에 없는 제품입니다.")
        
def etcsel() :
    print (directorydic[directory[2]])
    
    while True : 
        dsel = input("어떤 메뉴를 주문하시겠어요? (만약 메뉴 추가를 중지하고 싶으시면 0을 입력하세요) : ")
        
        if dsel == '0' :
            print ("현재 선택하신 메뉴 리스트는 다음과 같습니다. : ", buy)
            break
    
        if dsel in etclist :
            print ("정상적으로 추가되었습니다.")
            buy.append (dsel)
        
        else :
            print ("메뉴에 없는 제품입니다.")
            
def drinkmaster() :
    while True : 
        print (directorydic[directory[0]])
        
        a = int(input("0 : 추가 / 1 : 삭제 / 2 : 종료 : "))
        
        if a == 0 :
            b = input("추가할 메뉴 : ")
            drinklist.append(b)
            
        elif a == 1 :
            c = input("삭제할 메뉴 : ")
            drinklist.remove(c)
        
        else :
            break
        
def breadmaster() :
    while True : 
        print (directorydic[directory[1]])
        
        a = int(input("0 : 추가 / 1 : 삭제 / 2 : 종료 : "))
        
        if a == 0 :
            b = input("추가할 메뉴 : ")
            breadlist.append(b)
            
        elif a == 1 :
            c = input("삭제할 메뉴 : ")
            breadlist.remove(c)
        
        else :
            break
        
def etcmaster() :
    while True : 
        print (directorydic[directory[2]])
        
        a = int(input("0 : 추가 / 1 : 삭제 / 2 : 종료 : "))
        
        if a == 0 :
            b = input("추가할 메뉴 : ")
            etclist.append(b)
            
        elif a == 1 :
            c = input("삭제할 메뉴 : ")
            etclist.remove(c)
        
        else :
            break
            
def master () :
    print ("관리자 모드에 접속하였습니다.")
    
    while True : 
        print (directorydic)
        mod = input("조정이 필요한 디렉토리 입력 (0 : 종료): ")
    
        match mod : 
            case '0' : 
                break
        
            case "drink" :
                drinkmaster()
        
            case "bread" :
                breadmaster()
            
            case "etc" :
                etcmaster()
                
            case _ :
                print ("디렉토리 입력이 잘못되었습니다. 프로그램을 종료합니다.")
                exit()
                
def bye() :
    print ("선택하신 메뉴는 ", buy, "입니다.")
    print ("감사합니다. 스타벅스였습니다!")
    exit()
                
bt1 = Button (window, text = "음료", command = drinksel)
bt2 = Button (window, text = "빵", command = breadsel)
bt3 = Button (window, text = "음료", command = etcsel)
bt4 = Button (window, text = "주문 완료", command = bye)

bt1.pack()
bt2.pack()
bt3.pack()
bt4.pack()

window.mainloop()