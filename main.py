import tkinter
from datetime import datetime
from tkinter import *

from future.moves.tkinter import ttk
from gevent import threading

import Objects
import Threads

# создание объекта окна
Frame = Tk()
# создание объекта для фотографии
teplica = PhotoImage(file="теплица.png")
nasos = PhotoImage(file="nasos.png")
python_image = teplica.subsample(6, 6)
nasos_image = nasos.subsample(6, 6)
# создание Label для вывода времени
times = ttk.Label()
times.place(x=930, y=670)
times['foreground'] = 'green'
times['font'] = ('time1sNewRoman', 14)
times['background'] = 'black'
# создание переменных, которые будут хранить значение checkbutton
greenhouse1 = IntVar()
greenhouse2 = IntVar()
greenhouse3 = IntVar()
greenhouse4 = IntVar()
# создание переменных, куда будут вноситься значения пользователя
WaterTime = IntVar()
wateringInterval = IntVar()
temperature = DoubleVar()
humidity = IntVar()
impurityLevel = IntVar()
# создание объекта для отрисовки формы
canvas = Canvas(bg="#99FF99", width=630, height=350)
canvas.place(x=5, y=35)
# размещение фотографий на canvas
teplica1 = canvas.create_image(10, 30, anchor=NW, image=python_image)
teplica2 = canvas.create_image(160, 30, anchor=NW, image=python_image)
teplica3 = canvas.create_image(310, 30, anchor=NW, image=python_image)
teplica4 = canvas.create_image(460, 30, anchor=NW, image=python_image)
nasos = canvas.create_image(510, 230, anchor=NW, image=nasos_image)
# размещение труб на canvas
truba1 = canvas.create_rectangle(42, 160, 50, 275)
truba2 = canvas.create_rectangle(192, 160, 200, 275)
truba3 = canvas.create_rectangle(342, 160, 350, 275)
truba4 = canvas.create_rectangle(492, 160, 500, 275)
Daemon_Trube = canvas.create_rectangle(42, 275, 520, 283)
# создание checkbutton
checkbutton1 = tkinter.Checkbutton(text="1", variable=greenhouse1)
checkbutton2 = tkinter.Checkbutton(text="2", variable=greenhouse2)
checkbutton3 = tkinter.Checkbutton(text="3", variable=greenhouse3)
checkbutton4 = tkinter.Checkbutton(text="4", variable=greenhouse4)


def update_time1():
    times.config(text=f"{datetime.now():%H:%M:%S}")
    Frame.after(100, update_time1)


def func1():
    print("Thread 1 running")


def func2():
    print("Thread 2 running")


def func3():
    print("Thread 3 running")


def func4():
    print("Thread 4 running")


def zapusk(var1, var2, var3, var4):
    threads = []
    if var1.get() == 1:
        thr1 = threading.Thread(target=func1, daemon=True)
        threads.append(thr1)
    if var2.get() == 1:
        thr2 = threading.Thread(target=func2, daemon=True)
        threads.append(thr2)
    if var3.get() == 1:
        thr3 = threading.Thread(target=func3, daemon=True)
        threads.append(thr3)
    if var4.get() == 1:
        thr4 = threading.Thread(target=func4, daemon=True)
        threads.append(thr4)

    for thread in threads:
        thread.start()


def MainForm(window):
    window.title("Система управления поливом")
    window.geometry("1024x700+450+100")
    window.resizable(False, False)
    Labels1 = Objects.Label()
    Labels1.Sozdanie(window)
    Entrys1 = Objects.Entry(WaterTime, wateringInterval, temperature, humidity, impurityLevel)
    Entrys1.Sozdanie(window)
    Objects.CheckButton(checkbutton1, checkbutton2, checkbutton3, checkbutton4)
    window.mainloop()


# кнопка запуска системы
button = ttk.Button(text="Запуск системы",
                    command=lambda: zapusk(greenhouse1, greenhouse2, greenhouse3, greenhouse4))
button.place(x=850, y=490)
update_time1()
MainForm(Frame)
