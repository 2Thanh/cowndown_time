import time
from tkinter import *
from tkinter import messagebox
from threading import Thread
import threading
import pygame
from pygame import mixer


# creating Tk window
pygame.mixer.init()
def song():
    mixer.music.load('c:\\Users\\vulon\\OneDrive\\Tài liệu\\python\\tkinter\\slide\\Beach-Volley.wav')
    mixer.music.play()
root=Tk()
root.geometry("300x300")
hour=IntVar()
hour.set(0)
minute=IntVar()
minute.set(0)
second=IntVar()
second.set(0)
def thoi_gian():
    global hour,minute,second

    hourEntry=Entry(root,width=5,textvariable=hour,font="Times,14")
    minuteEntry=Entry(root,width=5,textvariable=minute,font="Times,14")
    secondEngtry=Entry(root,width=5,textvariable=second,font="Times,14")
    hourEntry.place(x=100,y=100)
    minuteEntry.place(x=150,y=100)
    secondEngtry.place(x=200,y=100)
    def start_coundown(giay,phut,gio):
        global hour,minute,second
        while giay>60 or phut>60:
            if second.get()>60:
                minute.set(minute.get()+(giay//60))
                giay%=60#lấy phần nguyên của giây chia 60
                second.set(giay)#lưu giây vào second
                phut+=minute.get()+(giay//60)# phải thay đổi phút cho lần elif kế tiếp
            elif  minute.get()>60:
                    hour.set(hour.get()+(minute.get()//60))
                    phut%=60
                    gio=hour.get()+(minute.get()//60)
                    minute.set(phut)
        i=0
        while giay>0:
            #while giay>1:
            time.sleep(1)
            giay-=1
            if giay<=0:
                if phut>0:
                    phut-=1
                    giay+=60
                else:
                    if gio>0:
                        gio-=1
                        phut+=60      
            if giay==0 and phut==0 and gio==0:
                song()
                second.set(0)
                minute.set(0)
                hour.set(0)      
            second.set(giay)
            minute.set(phut)
            hour.set(gio)
            root.update()
            secondEngtry.config(textvariable=second)
            minuteEntry.config(textvariable=minute)
            hourEntry.config(textvariable=hour)
            if giay==0 and phut==0 and gio==0:
                song()
            
        return 0
    start=Button(root,text="Start cowndown",pady=10,command=lambda:start_coundown(second.get(),minute.get(),hour.get()))#second.get là lấy giá trị của second
    start.place(x=100,y=150)
#threading thoi_gian
threading.Thread(target=thoi_gian).start()

quitgame=Button(root,text="Quit",pady=10,command=root.destroy)
quitgame.pack()
root.mainloop()
# def start_coundown(giay,phut,gio):

