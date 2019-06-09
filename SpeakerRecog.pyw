import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from get_voice import get_voice
from pre_process import preprocess_and_save
from guess import get_test, pred, delete
import constants as c
import time


def creat_windows():
    win = tk.Tk()

    win.geometry("%dx%d+%d+%d"%(980, 750, 0, 0))
    win.title('英雄识别器')

    bg = tk.PhotoImage(file="interface/picture/bg.gif")

    canvas = tk.Label(win, image=bg)
    canvas.pack()

    global bg1, file_path
    file_path = "interface/picture/0.jpg"
    bg1_open = Image.open(file_path)
    bg1 = ImageTk.PhotoImage(bg1_open)

    enter = tk.PhotoImage(file="interface/picture/enter.gif")
    entrance = tk.Button(win, image=enter, width=500, height=250, command=lambda:main_windows(canvas))
    entrance.pack()
    
    win.mainloop()

def choosepic():  
    path_=askopenfilename()  
    path.set(path_)  
    img_open = Image.open(e1.get())  
    img=ImageTk.PhotoImage(img_open)  
    l1.config(image=img)  
    l1.image=img

def main_windows(canvas):
    m_win = tk.Toplevel()
    sw = m_win.winfo_screenwidth()
    sh = m_win.winfo_screenheight()
    ww, wh = 400, 400
    x, y = (sw-ww)/2, (sh-wh)/2
    m_win.geometry("%dx%d+%d+%d"%(ww, wh, x, y))
    m_win.title("开始录音")

    var = tk.StringVar()
    result = tk.Label(m_win, textvariable=var, bg='#C1FFC1', font=('微软雅黑', 20), width=25, height=3)
    result.place(x=0, y=0, anchor='nw')

    done = tk.Button(m_win, text='Begin!', width=11, height=3, bg='#FF8C00', command=lambda:work(var, canvas), font=('Ink Free', 50))
    done.place(x=0, y=400, anchor='sw')

def work(var, canvas):
    get_voice()
    preprocess_and_save("guess/wav/", "guess/npy/")
    x = get_test(c.GUESS_DIR)
    name, number = pred(x)
    var.set(name)
    delete()
    file_path = "interface/picture/{}.jpg".format(number)
    bg1_open = Image.open(file_path)
    bg1 = ImageTk.PhotoImage(bg1_open)
    canvas.configure(image=bg1)
    canvas.image=bg1

if __name__ == '__main__':
    creat_windows()

