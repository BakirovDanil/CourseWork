from tkinter.messagebox import showerror


def Proverka(temperature, humidity):
    try:
        temperature1 = float(temperature.get())
        humidity1 = int(humidity.get())
        if 21 < temperature1 < 27 and 50 < humidity1 < 85:
            return True
        else:
            showerror(title="Ошибка",
                      message="Введенные данные некорректны. Проверьте установленные значения (температура должна находиться в диапазоне от 20 до 27 градусов, а влажность в диапазоне от 50 до 85 процентов)")
            temperature.set(0)
            humidity.set(0)
    except Exception as e:
        return False
