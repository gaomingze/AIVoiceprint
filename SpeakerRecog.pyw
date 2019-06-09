import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from PIL import Image, ImageTk
from get_voice import get_voice
from pre_process import preprocess_and_save
from guess import get_test, pred, delete
import constants as c
import time
import os
import shutil
from play import play
import random


def creat_windows():
    win = tk.Tk()
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    ww, wh = 900, 750
    x, y = (sw-ww)/2, (sh-wh)/2
    win.geometry("%dx%d+%d+%d"%(ww, wh, x, y-40))

    win.title('英雄识别器')

    bg = tk.PhotoImage(file="interface/picture/bg.gif")

    canvas = tk.Label(win, image=bg)
    canvas.pack()

    global bg1, file_path
    file_path = "interface/picture/0.jpg"
    bg1_open = Image.open(file_path)
    bg1 = ImageTk.PhotoImage(bg1_open)

    logo_open = Image.open("interface/picture/logo.jpg").resize((250,250))
    enter = ImageTk.PhotoImage(logo_open)
    tk.Button(win, image=enter, width=250, height=250, command=answer).pack()
    tk.Button(win, text='选择音频', bg='#97FFFF', font=('Segoe Script', 22), width=16, height=2, command=lambda:open(var, canvas)).place(x=0, y=500)
    tk.Button(win, text='Random', bg='#8A2BE2', font=('Segoe Script', 22), width=16, height=2, command=lambda:random_open(var, canvas)).place(x=0, y=625)

    var = tk.StringVar()
    var.set('')
    tk.Label(win, textvariable=var, bg='#C1FFC1', font=('宋体', 25), width=19, height=2).place(x=ww, y=wh-250, anchor='ne')

    tk.Button(win, text='Begin!', width=11, height=2, bg='#FF8C00', command=lambda:work(var, canvas), font=('Ink Free', 40)).place(x=ww, y=wh, anchor='se')

    
    win.mainloop()

def choosepic():  
    path_=askopenfilename()  
    path.set(path_)  
    img_open = Image.open(e1.get())  
    img=ImageTk.PhotoImage(img_open)  
    l1.config(image=img)  
    l1.image=img

def work(var, canvas):
    get_voice()
    preprocess_and_save("guess/wav/", "guess/npy/")
    x = get_test(c.GUESS_DIR)
    name, number = pred(x)
    var.set(name)
    delete()
    file_path = "interface/picture/{}.jpg".format(number)
    bg1_open = Image.open(file_path).resize((980,500))
    bg1 = ImageTk.PhotoImage(bg1_open)
    canvas.configure(image=bg1)
    canvas.image = bg1

def open(var, canvas):
    file_path = filedialog.askopenfilename()
    shutil.copy(file_path, "guess/wav/unknown-common-1.wav")
    play(file_path)
    preprocess_and_save("guess/wav/", "guess/npy/")
    x = get_test(c.GUESS_DIR)
    name, number = pred(x)
    var.set(name)
    delete()
    file_path = "interface/picture/{}.jpg".format(number)
    bg1_open = Image.open(file_path).resize((980,500))
    bg1 = ImageTk.PhotoImage(bg1_open)
    canvas.configure(image=bg1)
    canvas.image = bg1

def random_open(var, canvas):
    folder_path = '_ALL_/'
    list = []
    global hero
    for hero in os.listdir(folder_path):
        list.append(hero)
    hero = random.sample(list, 1)
    list0 = []
    for skin in os.listdir(folder_path + ''.join(hero)):
        list0.append(skin)
    skin = random.sample(list0, 1)
    list1 = []
    for wav in os.listdir(folder_path + ''.join(hero) + '/' + ''.join(skin)):
        list1.append(wav)
    wav = random.sample(list1, 1)			
    file_path = folder_path + ''.join(hero) + '/' + ''.join(skin) + '/' + ''.join(wav)

    shutil.copy(file_path, "guess/wav/unknown-common-1.wav")
    play(file_path)
    preprocess_and_save("guess/wav/", "guess/npy/")
    x = get_test(c.GUESS_DIR)
    name, number = pred(x)
    var.set(name)
    delete()
    file_path = "interface/picture/{}.jpg".format(number)
    bg1_open = Image.open(file_path).resize((980,500))
    bg1 = ImageTk.PhotoImage(bg1_open)
    canvas.configure(image=bg1)
    canvas.image = bg1

def answer():
    m_win = tk.Toplevel()
    sw = m_win.winfo_screenwidth()
    sh = m_win.winfo_screenheight()
    ww, wh = 400, 150
    x, y = (sw-ww)/2, (sh-wh)/2
    m_win.geometry("%dx%d+%d+%d"%(ww, wh, x, y))
    m_win.title("答案揭晓")

    tk.Label(m_win, text='by JMUAIA').place(x=400, y=150, anchor='se')
    var1 = tk.StringVar()
    var1.set(''.join(hero))
    result = tk.Label(m_win, textvariable=var1, bg='#C1FFC1', font=('微软雅黑', 20), width=25, height=3)
    result.place(x=0, y=0, anchor='nw')

if __name__ == '__main__':
    creat_windows()

