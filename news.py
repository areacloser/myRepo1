import requests
import threading
import webbrowser
from tkinter import *
import tkinter.messagebox
from bs4 import BeautifulSoup

#东华初级中学生态园校区T151班7号兰忠源制作

win = Tk()
win.title("Today's News alpha V0.3.9 -- By lanlan2_")
win.geometry("+500+300")
win.iconbitmap("product.ico")
win.resizable(0,0)
win.configure(background="lightgreen")
win.overrideredirect(False)

tkinter.messagebox.showinfo("使用提示", "提示：\n1.数据自运行程序后将会自动刷新，若想手动刷新数据请单击‘更新处’文本\n2.双击窗口可以改变透明度，在窗体内滑动鼠标滚轮以恢复正常\n3.双击右键可以调节窗口大小，再次双击会重新锁定\n4.单击滚轮可再次唤醒提示")

counter = 1

try:
    requests.get("https://www.hao123.com")
    
except:
    tkinter.messagebox.showwarning("警告", "网络连接异常，请检查网络连接完好再重试。")
    
else:
    resp = requests.get("https://www.hao123.com")
    resp.encoding = "utf-8"
    res = resp.text
    soup = BeautifulSoup(res, "html.parser")

    d1 = soup.find(name="div", class_="index-page s-sbg1")
    d2 = d1.find(name="div", class_="index-page-inner ewc s-sbg2")
    d3 = d2.find(name="div", class_="header")
    d4 = d3.find(name="div", class_="hotsearchCon")
    d5 = d4.find(name="div", id="hotsearch-box")
    d6 = d5.find(name="div", class_="hotsearchtop")
    d7 = d6.find(name="div", class_="allhot-item")

    ul = d7.find_all(name = "ul", class_="boxhot")
    ul1 = ul[0]
    ul2 = ul[1]

    l1 = ul1.find_all(name="li")
    l2 = ul2.find_all(name="li")
    li1 = l1[0]
    li2 = l1[1]
    li3 = l1[2]
    li4 = l2[0]
    li5 = l2[1]
    li6 = l2[2]
    
    a1 = li1.find(name="a")
    a2 = li2.find(name="a")
    a3 = li3.find(name="a")
    a4 = li4.find(name="a")
    a5 = li5.find(name="a")
    a6 = li6.find(name="a")

    txt1 = "1." + a1.text
    txt2 = "2." + a2.text
    txt3 = "3." + a3.text
    txt4 = "4." + a4.text
    txt5 = "5." + a5.text
    txt6 = "6." + a6.text

    href1= a1["href"]
    href2= a2["href"]
    href3= a3["href"]
    href4= a4["href"]
    href5= a5["href"]
    href6= a6["href"]

    L1 = Label(win, text=txt1, fg="red", bg="lightgrey", font="宋体 16")
    L1.pack()
    B1 = Button(win, text="卖油翁直通车", bg="red")
    B1.pack()

    L2 = Label(win, text=txt2, fg="orange", bg="lightgrey", font="宋体 16")
    L2.pack()
    B2 = Button(win, text="卖油翁直通车", bg="orange")
    B2.pack()

    L3 = Label(win, text=txt3, fg="yellow", bg="lightgrey", font="宋体 16")
    L3.pack()
    B3 = Button(win, text="卖油翁直通车", bg="yellow")
    B3.pack()

    L4 = Label(win, text=txt4, bg="lightgrey", font="宋体 16")
    L4.pack()
    B4 = Button(win, text="卖油翁直通车")
    B4.pack()

    L5 = Label(win, text=txt5, bg="lightgrey",  font="宋体 16")
    L5.pack()
    B5 = Button(win, text="卖油翁直通车")
    B5.pack()

    L6 = Label(win, text=txt6, bg="lightgrey",  font="宋体 16")
    L6.pack()
    B6 = Button(win, text="卖油翁直通车")
    B6.pack()

    Lu = Label(win, text="更新处", fg="blue", bg="lightblue", font="黑体 16")
    Lu.pack()

    Thks = Label(win, text="特别鸣谢：感谢东华之光——钟世杰对‘卖油翁’绰号的贡献，这给予我莫大的帮助！", fg="green", bg="lightgreen")
    Thks.pack()

    def change1(event):
        global href1
    
        webbrowser.open(href1)

    def change2(event):
        global href2
    
        webbrowser.open(href2)

    def change3(event):
        global href3
    
        webbrowser.open(href3)

    def change4(event):
        global href4
    
        webbrowser.open(href4)

    def change5(event):
        global href5
    
        webbrowser.open(href5)

    def change6(event):
        global href6
    
        webbrowser.open(href6)

    def changea(event):
        global win
    
        win.attributes("-alpha", 0.3)

    def changeb(event):
        global win
    
        win.attributes("-alpha", 1.0)

    def mupdate(event):
        global win, resp, res, soup, d1, d2, d3, d4, d5, d6, d7, ul, ul1, ul2, l1, l2, li1, li2, li3, li4, li5, li6, a1, a2, a3, a4, a5, a6, txt1, txt2, txt3, txt4, txt5, txt6, href1, href2, href3, href4, href5, href6, L1, B1, L2, B2, L3, B3, L4, B4, L5, B5, L6, B6, Lu 

        resp = requests.get("https://www.hao123.com")
        resp.encoding = "utf-8"
        res = resp.text
        soup = BeautifulSoup(res, "html.parser")

        d1 = soup.find(name="div", class_="index-page s-sbg1")
        d2 = d1.find(name="div", class_="index-page-inner ewc s-sbg2")
        d3 = d2.find(name="div", class_="header")
        d4 = d3.find(name="div", class_="hotsearchCon")
        d5 = d4.find(name="div", id="hotsearch-box")
        d6 = d5.find(name="div", class_="hotsearchtop")
        d7 = d6.find(name="div", class_="allhot-item")

        ul = d7.find_all(name = "ul", class_="boxhot")
        ul1 = ul[0]
        ul2 = ul[1]

        l1 = ul1.find_all(name="li")
        l2 = ul2.find_all(name="li")
        li1 = l1[0]
        li2 = l1[1]
        li3 = l1[2]
        li4 = l2[0]
        li5 = l2[1]
        li6 = l2[2]

        a1 = li1.find(name="a")
        a2 = li2.find(name="a")
        a3 = li3.find(name="a")
        a4 = li4.find(name="a")
        a5 = li5.find(name="a")
        a6 = li6.find(name="a")

        txt1 = "1." + a1.text
        txt2 = "2." + a2.text
        txt3 = "3." + a3.text
        txt4 = "4." + a4.text
        txt5 = "5." + a5.text
        txt6 = "6." + a6.text

        href1= a1["href"]
        href2= a2["href"]
        href3= a3["href"]
        href4= a4["href"]
        href5= a5["href"]
        href6= a6["href"]

        L1.configure(text=txt1)
        L2.configure(text=txt2)
        L3.configure(text=txt3)
        L4.configure(text=txt4)
        L5.configure(text=txt5)
        L6.configure(text=txt6)
    
        tkinter.messagebox.showinfo("提示", "更新成功！")

    def aupdate():
        global win, resp, res, soup, d1, d2, d3, d4, d5, d6, d7, ul, ul1, ul2, l1, l2, li1, li2, li3, li4, li5, li6, a1, a2, a3, a4, a5, a6, txt1, txt2, txt3, txt4, txt5, txt6, href1, href2, href3, href4, href5, href6, L1, B1, L2, B2, L3, B3, L4, B4, L5, B5, L6, B6, Lu 

        resp = requests.get("https://www.hao123.com")
        resp.encoding = "utf-8"
        res = resp.text
        soup = BeautifulSoup(res, "html.parser")

        d1 = soup.find(name="div", class_="index-page s-sbg1")
        d2 = d1.find(name="div", class_="index-page-inner ewc s-sbg2")
        d3 = d2.find(name="div", class_="header")
        d4 = d3.find(name="div", class_="hotsearchCon")
        d5 = d4.find(name="div", id="hotsearch-box")
        d6 = d5.find(name="div", class_="hotsearchtop")
        d7 = d6.find(name="div", class_="allhot-item")

        ul = d7.find_all(name = "ul", class_="boxhot")
        ul1 = ul[0]
        ul2 = ul[1]

        l1 = ul1.find_all(name="li")
        l2 = ul2.find_all(name="li")
        li1 = l1[0]
        li2 = l1[1]
        li3 = l1[2]
        li4 = l2[0]
        li5 = l2[1]
        li6 = l2[2]

        a1 = li1.find(name="a")
        a2 = li2.find(name="a")
        a3 = li3.find(name="a")
        a4 = li4.find(name="a")
        a5 = li5.find(name="a")
        a6 = li6.find(name="a")

        txt1 = "1." + a1.text
        txt2 = "2." + a2.text
        txt3 = "3." + a3.text
        txt4 = "4." + a4.text
        txt5 = "5." + a5.text
        txt6 = "6." + a6.text

        href1= a1["href"]
        href2= a2["href"]
        href3= a3["href"]
        href4= a4["href"]
        href5= a5["href"]
        href6= a6["href"]

        L1.configure(text=txt1)
        L2.configure(text=txt2)
        L3.configure(text=txt3)
        L4.configure(text=txt4)
        L5.configure(text=txt5)
        L6.configure(text=txt6)

        t = threading.Timer(1, aupdate)
        t.start()

    def tishi(event):
        global win

        tkinter.messagebox.showinfo("使用提示", "提示：\n1.数据自运行程序后将会自动刷新，若想手动刷新数据请单击‘更新处’文本\n2.双击窗口可以改变透明度，在窗体内滑动鼠标滚轮以恢复正常\n3.双击右键可以调节窗口大小，再次双击会重新锁定\n4.单击滚轮可再次唤醒提示")

    def size(event):
        global win, counter
    
        if counter % 2 == 1:
            win.resizable(1,1)

        else:
            win.resizable(0,0)
    
        counter += 1

    def bold1a(event):
        global L1

        L1.configure(font="宋体 16 bold")

    def bold1b(event):
        global L1

        L1.configure(font="宋体 16")

    def bold2a(event):
        global L2

        L2.configure(font="宋体 16 bold")

    def bold2b(event):
        global L2

        L2.configure(font="宋体 16")

    def bold3a(event):
        global L3

        L3.configure(font="宋体 16 bold")

    def bold3b(event):
        global L3

        L3.configure(font="宋体 16")

    def bold4a(event):
        global L4

        L4.configure(font="宋体 16 bold")

    def bold4b(event):
        global L4

        L4.configure(font="宋体 16")

    def bold5a(event):
        global L5

        L5.configure(font="宋体 16 bold")

    def bold5b(event):
        global L5

        L5.configure(font="宋体 16")

    def bold6a(event):
        global L6

        L6.configure(font="宋体 16 bold")

    def bold6b(event):
        global L6

        L6.configure(font="宋体 16")

    def boldua(event):
        global Lu

        Lu.configure(font="黑体 16 underline")

    def boldub(event):
        global Lu

        Lu.configure(font="黑体 16")

    aupdate()

    B1.bind("<Button-1>", change1)
    L1.bind("<Enter>", bold1a)
    L1.bind("<Leave>", bold1b)
    B2.bind("<Button-1>", change2)
    L2.bind("<Enter>", bold2a)
    L2.bind("<Leave>", bold2b)
    B3.bind("<Button-1>", change3)
    L3.bind("<Enter>", bold3a)
    L3.bind("<Leave>", bold3b)
    B4.bind("<Button-1>", change4)
    L4.bind("<Enter>", bold4a)
    L4.bind("<Leave>", bold4b)
    B5.bind("<Button-1>", change5)
    L5.bind("<Enter>", bold5a)
    L5.bind("<Leave>", bold5b)
    B6.bind("<Button-1>", change6)
    L6.bind("<Enter>", bold6a)
    L6.bind("<Leave>", bold6b)
    Lu.bind("<Button-1>", mupdate)
    Lu.bind("<Enter>", boldua)
    Lu.bind("<Leave>", boldub)

    win.bind("<Button-2>", tishi)
    win.bind("<Double-Button-3>", size)
    win.bind("<Double-Button-1>", changea)
    win.bind("<MouseWheel>", changeb)

win.mainloop()
