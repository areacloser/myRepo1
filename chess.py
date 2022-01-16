from tkinter import *
import tkinter.messagebox

win = Tk()
win.title("井字棋 -- By lanlan2_")
win.iconbitmap("chess.ico")
win.configure(background="lightblue")
win.resizable(0,0)

counter = 1
e1 = 1
e2 = 1
e3 = 1
e4 = 1
e5 = 1
e6 = 1
e7 = 1
e8 = 1
e9 = 1
li = [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]

B1 = Button(text=li[0][0], font="consolas 40 bold")
B1.grid(row=1, column=1)
B2 = Button(text=li[0][1], font="consolas 40 bold")
B2.grid(row=1, column=2)
B3 = Button(text=li[0][2], font="consolas 40 bold")
B3.grid(row=1, column=3)
B4 = Button(text=li[1][0], font="consolas 40 bold")
B4.grid(row=2, column=1)
B5 = Button(text=li[1][1], font="consolas 40 bold")
B5.grid(row=2, column=2)
B6 = Button(text=li[1][2], font="consolas 40 bold")
B6.grid(row=2, column=3)
B7 = Button(text=li[2][0], font="consolas 40 bold")
B7.grid(row=3, column=1)
B8 = Button(text=li[2][1], font="consolas 40 bold")
B8.grid(row=3, column=2)
B9 = Button(text=li[2][2], font="consolas 40 bold")
B9.grid(row=3, column=3)
Lb = Label(text="版本：2021.10.1", font="黑体 10 italic", bg="lightblue")
Lb.grid(row=4, column=2)

tkinter.messagebox.showinfo("特别鸣谢", "东华初级中学生态园校区T251班2025108号钟细节")

def judge():
    global win
    
    if (li[0][0] == li[0][1] and li[0][1] == li[0][2] != "   ") or (li[1][0] == li[1][1] and li[1][1] == li[1][2] != "   ") or (li[2][0] == li[2][1] and li[2][1] == li[2][2] != "   ") or (li[0][0] == li[1][0] and li[1][0] == li[2][0] != "   ") or (li[0][1] == li[1][1] and li[1][1] == li[2][1] != "   ") or (li[0][2] == li[1][2] and li[1][2] == li[2][2] != "   ") or (li[0][0] == li[1][1] and li[1][1] == li[2][2] !="   ") or (li[0][2] == li[1][1] and li[1][1] == li[2][0] !="   "):
        if counter % 2 == 0:
            tkinter.messagebox.showinfo("提示", "先手者获胜！")

        else:
            tkinter.messagebox.showinfo("提示", "后手者获胜！")

        win.destroy()

    else:
        if counter == 10:
            tkinter.messagebox.showinfo("提示", "双方打平！")

            win.destroy()
    
def chessd1(event):
    global B1, e1, counter

    if e1 == 1:
        if counter % 2 == 1:
            li[0][0] = " x "
        
        else:
            li[0][0] = " o "
        
        B1.configure(text=li[0][0])
        e1 = 0
        counter += 1
        judge()
        
def chessd2(event):
    global B2, e2, counter

    if e2 == 1:
        if counter % 2 == 1:
            li[0][1] = " x "
        
        else:
            li[0][1] = " o "
        
        B2.configure(text=li[0][1])
        e2 = 0
        counter += 1
        judge()

def chessd3(event):
    global B3, e3, counter

    if e3 == 1:
        if counter % 2 == 1:
            li[0][2] = " x "
        
        else:
            li[0][2] = " o "
        
        B3.configure(text=li[0][2])
        e3 = 0
        counter += 1
        judge()

def chessd4(event):
    global B4, e4, counter

    if e4 == 1:
        if counter % 2 == 1:
            li[1][0] = " x "
        
        else:
            li[1][0] = " o "
        
        B4.configure(text=li[1][0])
        e4 = 0
        counter += 1
        judge()
        
def chessd5(event):
    global B5, e5, counter

    if e5 == 1:
        if counter % 2 == 1:
            li[1][1] = " x "
        
        else:
            li[1][1] = " o "
        
        B5.configure(text=li[1][1])
        e5 = 0
        counter += 1
        judge()

def chessd6(event):
    global B6, e6, counter

    if e6 == 1:
        if counter % 2 == 1:
            li[1][2] = " x "
        
        else:
            li[1][2] = " o "
        
        B6.configure(text=li[1][2])
        e6 = 0
        counter += 1
        judge()


def chessd7(event):
    global B7, e7, counter

    if e7 == 1:
        if counter % 2 == 1:
            li[2][0] = " x "
        
        else:
            li[2][0] = " o "
        
        B7.configure(text=li[2][0])
        e7 = 0
        counter += 1
        judge()
        
def chessd8(event):
    global B8, e8, counter

    if e8 == 1:
        if counter % 2 == 1:
            li[2][1] = " x "
        
        else:
            li[2][1] = " o "
        
        B8.configure(text=li[2][1])
        e8 = 0
        counter += 1
        judge()

def chessd9(event):
    global B9, e9, counter

    if e9 == 1:
        if counter % 2 == 1:
            li[2][2] = " x "
        
        else:
            li[2][2] = " o "
        
        B9.configure(text=li[2][2])
        e9 = 0
        counter += 1
        judge()
    
B1.bind("<Button-1>", chessd1)
B2.bind("<Button-1>", chessd2)
B3.bind("<Button-1>", chessd3)
B4.bind("<Button-1>", chessd4)
B5.bind("<Button-1>", chessd5)
B6.bind("<Button-1>", chessd6)
B7.bind("<Button-1>", chessd7)
B8.bind("<Button-1>", chessd8)
B9.bind("<Button-1>", chessd9)

win.mainloop()
