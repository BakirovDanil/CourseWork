from tkinter import *

from future.moves.tkinter import ttk

Frame = Tk()


# Область для отображения схемы системы полива
def CanvasForm(window):
    canvas = Canvas(bg="#99FF99", width=1000, height=450)
    canvas.place(x=12, y=12)
    #canvas.create_rectangle(20, 20, 60, 200)


def ParametrsLabel(label):
    label['foreground'] = 'blue'
    label['font'] = ('TimesNewRoman', 12)
    label['foreground'] = 'blue'


# Функция для создания Label на форме
def Labels():
    greenhouse = ttk.Label(text="Количество обслуживаемых \nтеплиц")
    WaterTime = ttk.Label(text="Время полива")
    wateringInterval = ttk.Label(text="Время между поливами")
    temperature = ttk.Label(text="Температура")
    humidity = ttk.Label(text="Уровень влажности")
    impurityLevel = ttk.Label(text="Количество удобрений")
    # Работа с созданными полями
    greenhouse.place(x=40, y=490)
    ParametrsLabel(greenhouse)
    # Работа с созданными полями
    WaterTime.place(x=40, y=550)
    ParametrsLabel(WaterTime)
    # Работа с созданными полями
    wateringInterval.place(x=40, y=610)
    ParametrsLabel(wateringInterval)
    # Работа с созданными полями
    temperature.place(x=500, y=490)
    ParametrsLabel(temperature)
    # Работа с созданными полями
    humidity.place(x=500, y=550)
    ParametrsLabel(humidity)
    # Работа с созданными полями
    impurityLevel.place(x=500, y=610)
    ParametrsLabel(impurityLevel)


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
    Labels()
    CanvasForm(window)
    window.mainloop()


MainForm(Frame)
