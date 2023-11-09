from tkinter import ttk, Menu
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
        greenhouse = ttk.Label(text="Количество обслуживаемых \nтеплиц")
        WaterTime = ttk.Label(text="Время полива")
        wateringInterval = ttk.Label(text="Время между поливами")
        temperature = ttk.Label(text="Температура")
        humidity = ttk.Label(text="Уровень влажности")
        impurityLevel = ttk.Label(text="Количество удобрений")
        labels = [greenhouse, WaterTime, wateringInterval, temperature, humidity, impurityLevel]
        ParametrsLabel(labels)
        # Работа с созданными полями
        greenhouse.place(x=40, y=490)
        # Работа с созданными полями
        WaterTime.place(x=40, y=550)
        # Работа с созданными полями
        wateringInterval.place(x=40, y=610)
        # Работа с созданными полями
        temperature.place(x=500, y=490)
        # Работа с созданными полями
        humidity.place(x=500, y=550)
        # Работа с созданными полями
        impurityLevel.place(x=500, y=610)


class Entry(Figure):
    def __init__(self, greenhouse, WaterTime, wateringInterval, temperature, humidity, impurityLevel):
        self.greenhouse = greenhouse
        self.WaterTime = WaterTime
        self.wateringInterval = wateringInterval
        self.temperature = temperature
        self.humidity = humidity
        self.impurityLevel = impurityLevel

    def Sozdanie(self, window):
        greenhouse = ttk.Entry(width=20, textvariable=self.greenhouse)
        WaterTime = ttk.Entry(width=20, textvariable=self.WaterTime)
        wateringInterval = ttk.Entry(width=20, textvariable=self.wateringInterval)
        temperature = ttk.Entry(width=20, textvariable=self.temperature)
        humidity = ttk.Entry(width=20, textvariable=self.humidity)
        impurityLevel = ttk.Entry(width=20, textvariable=self.impurityLevel)
        entrys = [greenhouse, WaterTime, wateringInterval, temperature, humidity, impurityLevel]
        for i in entrys:
            i.bind("<Key>", on_key_press)
        greenhouse.place(x=255, y=495)
        hint.ToolTip(greenhouse,"Поле для ввода количества теплиц")
        WaterTime.place(x=255, y=550)
        hint.ToolTip(WaterTime, "Поле для ввода времени полива")
        wateringInterval.place(x=255, y=610)
        hint.ToolTip(wateringInterval, "Поле для ввода интервала времени между поливом")
        temperature.place(x=670, y=490)
        hint.ToolTip(temperature, "Поле для установки требуемой температуры")
        humidity.place(x=670, y=550)
        hint.ToolTip(humidity, "Поле для установки требуемого уровня влажности")
        impurityLevel.place(x=670, y=610)
        hint.ToolTip(impurityLevel, "Поле для установки требуемого количества удобрений")


class MenuFrom(Figure):
    def Sozdanie(self, window):
        main_menu = Menu()
        main_menu.add_cascade(label="Система")  # меню "Система"
        main_menu.add_cascade(label="Таблицы")  # меню "Таблицы"
        main_menu.add_cascade(label="Графики")  # меню "Графики"
        main_menu.add_cascade(label="Инструкция")  # меню "Инструкция"
        main_menu.add_cascade(label="Выход", command=window.destroy)  # меню aka кнопка "Выход" - выход из системы
        window.config(menu=main_menu)
