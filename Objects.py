from tkinter import ttk
from abc import ABC


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
        WaterTime.place(x=255, y=550)
        wateringInterval.place(x=255, y=610)
        temperature.place(x=670, y=490)
        humidity.place(x=670, y=550)
        impurityLevel.place(x=670, y=610)
