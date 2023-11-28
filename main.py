import threading
from datetime import datetime
from tkinter import *
import tkinter as tk

from future.moves.tkinter import ttk, messagebox

import Objects
import Proverka
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
# создание переменных, куда будут вноситься значения пользователя
temperature = DoubleVar()
humidity = IntVar()
# создание объекта для отрисовки формы
canvas = Canvas(bg="#99FF99", width=450, height=350)
canvas.place(x=5, y=35)
# размещение фотографий на canvas
teplica1 = canvas.create_image(10, 30, anchor=NW, image=python_image)
teplica2 = canvas.create_image(160, 30, anchor=NW, image=python_image)
nasos = canvas.create_image(340, 230, anchor=NW, image=nasos_image)
# размещение труб на canvas
truba1 = canvas.create_rectangle(42, 160, 50, 275)
truba2 = canvas.create_rectangle(192, 160, 200, 275)
Daemon_Trube = canvas.create_rectangle(42, 275, 350, 283)
# создание checkbutton
checkbutton1 = tk.Checkbutton(text="1", variable=greenhouse1)
checkbutton2 = tk.Checkbutton(text="2", variable=greenhouse2)
# переменные для вывода действительных значений для первой теплицы
tempa1 = tk.StringVar()
humi1 = tk.StringVar()
# переменные для вывода действительных значений для второй теплицы
tempa2 = tk.StringVar()
humi2 = tk.StringVar()
# сигнал остановки
thr11 = threading.Event()
thr22 = threading.Event()

def update_time1():
    times.config(text=f"{datetime.now():%H:%M:%S}")
    Frame.after(100, update_time1)


thr1 = Threads.Thr1(temperature, humidity, tempa1, humi1, thr11)
thr2 = Threads.Thr2(temperature, humidity, tempa2, humi2, thr22)


def stop_other_threads():
    control_thread = Threads.ControlThread([thr1, thr2])
    control_thread.start()


def zapusk():
    if Proverka.Proverka(temperature, humidity):
        if greenhouse1.get() == 1:
            thr1.start()
        if greenhouse2.get() == 1:
            thr2.start()


def MainForm(window):
    window.title("Система управления поливом")
    window.geometry("1024x700+450+100")
    window.resizable(False, False)
    Labels1 = Objects.Label()
    Labels1.Sozdanie(window)
    Entrys1 = Objects.Entry(temperature, humidity, tempa1, humi1, tempa2, humi2)
    Entrys1.Sozdanie(window)
    Objects.CheckButton(checkbutton1, checkbutton2)
    window.mainloop()


# кнопка запуска системы
button = ttk.Button(text="Запуск системы", command=zapusk)
# кнопка создния аварийной ситуации
button.place(x=650, y=490)
button1 = ttk.Button(text="Создать аварию", command=stop_other_threads)
button1.place(x=750, y=490)
update_time1()
MainForm(Frame)
