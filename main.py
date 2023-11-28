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
nadpis = PhotoImage(file="Надпись.png")
nadpis_image = nadpis.subsample(1,1)
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
# создание еще одного объекта для размещения текста
canvas1 = Canvas(bg="#FFFFFF", width=620, height=360)
canvas1.place(x=450, y=35)
# размещение фотографий на canvas
teplica1 = canvas.create_image(10, 30, anchor=NW, image=python_image)
teplica2 = canvas.create_image(160, 30, anchor=NW, image=python_image)
nasos = canvas.create_image(340, 230, anchor=NW, image=nasos_image)
nadpis = canvas1.create_image(10, 30, anchor=NW, image=nadpis_image)
# размещение труб на canvas
truba1 = canvas.create_rectangle(42, 160, 50, 275)
truba2 = canvas.create_rectangle(192, 160, 200, 275)
Daemon_Trube = canvas.create_rectangle(42, 275, 350, 283)
# создание checkbutton
checkbutton1 = tk.Checkbutton(text="1", variable=greenhouse1)
checkbutton2 = tk.Checkbutton(text="2", variable=greenhouse2)
check = [checkbutton1, checkbutton2]
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


def zapusk():
    thread_list = []
    if Proverka.Proverka(temperature, humidity):
        button1["state"] = "normal"
        if greenhouse1.get() == 1:
            thr1 = Threads.Thr1(thr11, temperature, humidity, tempa1, humi1)
            thr1.start()
            thread_list.append(thr1)
            button["state"]="disabled"
        if greenhouse2.get() == 1:
            thr2 = Threads.Thr2(thr22, temperature, humidity, tempa2, humi2)
            thr2.start()
            thread_list.append(thr2)
            button["state"] = "disabled"
        elif greenhouse1.get() == 0 and greenhouse2.get() == 0:
            messagebox.showerror("Ошибка", "Выберите хоть одну теплицу")
    return thread_list


def stop_other_threads():
    threads = zapusk()
    control_thread = Threads.ControlThread(threads, button,button1)
    control_thread.start()


def MainForm(window):
    window.title("Система управления поливом. Студент группы ЭАС-412С, Бакиров Данил")
    window.geometry("1100x700+450+100")
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
button1["state"]="disabled"
update_time1()
MainForm(Frame)
