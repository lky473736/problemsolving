from tkinter import *
window = Tk()

def plus() :
    k = float(e1.get())
    j = float(e2.get())
    print (k + j)

def minus() :
    k = float(e1.get())
    j = float(e2.get())
    print (k - j)
    
def multi() :
    k = float(e1.get())
    j = float(e2.get())
    print (k * j)

def divide() :
    k = float(e1.get())
    j = float(e2.get())
    print (k / j)
    
e1 = Entry (window, bg = "lightgray")
e2 = Entry (window, bg = "lightgray")

e1.pack()
e2.pack()

bt1 = Button (window, text = "덧셈", command = plus)
bt2 = Button (window, text = "뺄셈", command = minus)
bt3 = Button (window, text = "곱셈", command = multi)
bt4 = Button (window, text = "나눗셈", command = divide)

bt1.pack()
bt2.pack()
bt3.pack()
bt4.pack()

window.mainloop()