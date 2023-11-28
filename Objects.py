from tkinter import ttk
from abc import ABC

import hint


def on_key_press(event):
    if event.char.lower() not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\x08']:
        return "break"
    elif event.char == '.' in event.widget.get():
        return "break"


def ParametrsLabel(labels):
    for i in labels:
        i['foreground'] = 'blue'
        i['font'] = ('TimesNewRoman', 12)


class Figure(ABC):
    def Sozdanie(self, window):
        pass


class Label(Figure):
    def Sozdanie(self, window):
        greenhouse = ttk.Label(text="Обслуживаемые теплицы")
        temperature = ttk.Label(text="Температура \n(в градусах Цельсия)")
        humidity = ttk.Label(text="Уровень влажности \n(в процентах)")
        scheme = ttk.Label(text="Схема системы полива")
        instruction = ttk.Label(text="Описание работы")
        GH1 = ttk.Label(text="Теплица 1")
        GH2 = ttk.Label(text="Теплица 2")
        labels = [greenhouse, temperature, humidity, scheme, GH1, GH2, instruction]
        ParametrsLabel(labels)
        # Работа с созданными полями
        greenhouse.place(x=40, y=450)
        # Работа с созданными полями
        temperature.place(x=40, y=490)
        # Работа с созданными полями
        humidity.place(x=40, y=550)
        # работа с созданными полями
        scheme.place(x=150, y=10)
        # работа с созаднными полями
        GH1.place(x=350, y=450)
        GH2.place(x=490, y=450)
        # работа с созданными полями
        instruction.place(x=680, y=10)


class Entry(Figure):
    def __init__(self, temperature, humidity, tempa1, humi1, tempa2, humi2):
        self.temperature = temperature
        self.humidity = humidity
        self.tempa1 = tempa1
        self.humi1 = humi1
        self.tempa2 = tempa2
        self.humi2 = humi2

    def Sozdanie(self, window):
        temperature = ttk.Entry(width=20, textvariable=self.temperature)
        humidity = ttk.Entry(width=20, textvariable=self.humidity)
        tempa1 = ttk.Entry(width=20, textvariable=self.tempa1, state="readonly")
        humi1 = ttk.Entry(width=20, textvariable=self.humi1, state="readonly")
        tempa2 = ttk.Entry(width=20, textvariable=self.tempa2, state="readonly")
        humi2 = ttk.Entry(width=20, textvariable=self.humi2, state="readonly")
        entrys = [temperature, humidity]
        for i in entrys:
            i.bind("<Key>", on_key_press)
        temperature.place(x=210, y=490)
        hint.ToolTip(temperature, "Поле для установки требуемой температуры")
        humidity.place(x=210, y=550)
        hint.ToolTip(humidity, "Поле для установки требуемого уровня влажности")
        tempa1.place(x=350, y=490)
        hint.ToolTip(tempa1, "Действительное значение температуры в теплице 1")
        humi1.place(x=350, y=550)
        hint.ToolTip(humi1, "Действительное значение влажности в теплице 1")
        tempa2.place(x=490, y=490)
        hint.ToolTip(tempa2, "Действительное значение температуры в теплице 2")
        humi2.place(x=490, y=550)
        hint.ToolTip(humi2, "Действительное значение влажности в теплице 2")


def CheckButton(checkbutton1, checkbutton2):
    checkbutton1.place(x=255, y=450)
    checkbutton2.place(x=285, y=450)
