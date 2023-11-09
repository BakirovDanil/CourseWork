from tkinter import *

import time
from future.moves.tkinter import ttk
from gevent import threading

import Objects

Frame = Tk()
times = ttk.Label()
times.place(x=850, y=650)
greenhouse = IntVar()
WaterTime = IntVar()
wateringInterval = IntVar()
temperature = DoubleVar()
humidity = IntVar()
impurityLevel = IntVar()


# Область для отображения схемы системы полива
def CanvasForm(window):
    canvas = Canvas(bg="#99FF99", width=1000, height=450)
    canvas.place(x=12, y=12)
    rec1=canvas.create_rectangle(12, 12, 162, 250)
    rec2=canvas.create_rectangle(272, 12, 422, 250)
    rec3=canvas.create_rectangle(532, 12, 682, 250)


def tick(data):
    times['text'] = data
    times.after(1000, tick)


def MainForm(window):
    window.title("Система управления поливом")
    window.geometry("1024x700+450+100")
    window.resizable(False, False)
    MenuForm1 = Objects.MenuFrom()
    MenuForm1.Sozdanie(window)
    Labels1 = Objects.Label()
    Labels1.Sozdanie(window)
    CanvasForm(window)
    Entrys1 = Objects.Entry(greenhouse, WaterTime, wateringInterval, temperature, humidity, impurityLevel)
    Entrys1.Sozdanie(window)
    window.mainloop()


MainForm(Frame)
