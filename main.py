from tkinter import *

import time
from future.moves.tkinter import ttk
import Objects

Frame = Tk()
times = ttk.Label()
times.place(x=850, y=650)
greenhouse = IntVar()
WaterTime = DoubleVar()
wateringInterval = DoubleVar()
temperature = DoubleVar()
humidity = DoubleVar()
impurityLevel = DoubleVar()


# Область для отображения схемы системы полива
def CanvasForm(window):
    canvas = Canvas(bg="#99FF99", width=1000, height=450)
    canvas.place(x=12, y=12)
    canvas.create_rectangle(12, 12, 162, 250)
    canvas.create_rectangle(272, 12, 422, 250)
    canvas.create_rectangle(532, 12, 682, 250)


def tick():
    times['text'] = time.strftime("%H:%M:%S")
    times.after(1000, tick)


def MenuForm(window):
    main_menu = Menu()
    main_menu.add_cascade(label="Система")  # меню "Система"
    main_menu.add_cascade(label="Таблицы")  # меню "Таблицы"
    main_menu.add_cascade(label="Графики")  # меню "Графики"
    main_menu.add_cascade(label="Инструкция")  # меню "Инструкция"
    main_menu.add_cascade(label="Выход")  # меню aka кнопка "Выход" - выход из системы
    window.config(menu=main_menu)


def MainForm(window):
    window.title("Система управления поливом")
    window.geometry("1024x700+450+100")
    window.resizable(False, False)
    MenuForm(window)
    Labels1 = Objects.Label()
    Labels1.Sozdanie(window)
    CanvasForm(window)
    Entrys1 = Objects.Entry(greenhouse, WaterTime, wateringInterval, temperature, humidity, impurityLevel)
    Entrys1.Sozdanie(window)
    window.mainloop()


tick()
MainForm(Frame)
