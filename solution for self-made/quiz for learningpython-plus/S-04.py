from tkinter import *
from tkinter import messagebox

window = Tk()

class registersys :
    def __init__(self) :
        self.idlist = []
        self.pwlist = []

    def register(self) :
        while True :
            newid = input("id를 입력하세요 : ")

            if newid in self.idlist :
                print ("다른 이름의 아이디를 사용해 주십시오.")
                
            else :
                self.idlist.append(newid)
                break

        while True :
            newpw = input("pw를 입력하세요 : ")

            if len(newpw) >= 8 :
                self.pwlist.append(newpw)
                print ("계정 생성이 완료되었습니다.")
                break
            
            else :
                print ("비밀번호는 8자 이상으로 구성하여 주십시요.")

    def printall(self) :
        print ("아이디 : ", self.idlist)
        print ("비밀번호 : ", self.pwlist)


def login() :
    id = e1.get()
    pw = e2.get()

    if id in s.idlist :
        k = s.idlist.index(id)

        if pw == s.pwlist[k] :
            print ("로그인에 성공하였습니다.")
            exit()
        else :
            label = messagebox.showinfo("About", "아이디 혹은 비밀번호가 일치하지 않습니다.")
    else :
        label = messagebox.showinfo("About", "아이디 혹은 비밀번호가 일치하지 않습니다.")


s = registersys()

l1 = Label(window, text="아이디")
l2 = Label(window, text="비밀번호")
e1 = Entry(window)
e2 = Entry(window)
btn1 = Button(window, text="로그인", command=login)
btn2 = Button(window, text="회원가입", command=s.register)

l1.grid (row=0, column=0)
e1.grid (row=0, column=1)
l2.grid (row=1, column=0)
e2.grid (row=1, column=1)
btn1.grid (row=2, column=1)
btn2.grid (row=2, column=0)

window.mainloop()
