import random
import threading as th
import time

from future.moves.tkinter import messagebox


# Функции для каждого возможного сценария
class Thr1(th.Thread):
    def __init__(self, stop_event, temperature, humidity, entry1, entry2):
        th.Thread.__init__(self)
        self.stopped = stop_event
        self.temperature = temperature
        self.humidity = humidity
        self.entry1 = entry1
        self.entry2 = entry2
        self.stopped = stop_event

    def run(self):
        TEMP = random.randint(20, 27)
        HUMI = random.randint(20, 90)
        temperature1 = self.temperature.get()
        humidity1 = self.humidity.get()
        while not self.stopped.is_set():
            TEMP = round(TEMP, 2)
            HUMI = round(HUMI, 2)
            if HUMI > humidity1 and TEMP < temperature1:
                print("Значение температуры в теплице 1: " + str(TEMP))
                self.entry1.set(TEMP)
                print("Значени влажности в теплице 1: " + str(HUMI))
                self.entry2.set(HUMI)
                random_number1 = random.uniform(0.1, 0.5)
                TEMP += random_number1
                random_number2 = random.uniform(2, 4)
                HUMI -= random_number2
            elif HUMI < humidity1 and TEMP > temperature1:
                print("Значение температуры в теплице 1: " + str(TEMP))
                self.entry1.set(TEMP)
                print("Значени влажности в теплице 1: " + str(HUMI))
                self.entry2.set(HUMI)
                random_number1 = random.uniform(0.1, 0.5)
                TEMP -= random_number1
                random_number2 = random.randint(10, 13)
                HUMI += random_number2
            elif HUMI < humidity1 and TEMP < temperature1:
                print("Значение температуры в теплице 1: " + str(TEMP))
                self.entry1.set(TEMP)
                print("Значени влажности в теплице 1: " + str(HUMI))
                self.entry2.set(HUMI)
                random_number1 = random.uniform(0.1, 0.5)
                TEMP += random_number1
                random_number2 = random.randint(10, 13)
                HUMI += random_number2
            elif HUMI > humidity1 and TEMP > temperature1:
                print("Значение температуры в теплице 1: " + str(TEMP))
                self.entry1.set(TEMP)
                print("Значени влажности в теплице 1: " + str(HUMI))
                self.entry2.set(HUMI)
                random_number1 = random.uniform(0.1, 0.5)
                TEMP -= random_number1
                random_number2 = random.randint(2, 4)
                HUMI -= random_number2
            else:
                print("Значение температуры в теплице 1: " + str(TEMP))
                self.entry1.set(TEMP)
                print("Значени влажности в теплице 1: " + str(HUMI))
                self.entry2.set(HUMI)
                random_number1 = random.uniform(0.1, 0.5)
                TEMP += random_number1
                random_number2 = random.uniform(2, 4)
                HUMI -= random_number2
            time.sleep(1)


class Thr2(th.Thread):  # Создаём экземпляр потока Thread
    def __init__(self, stop_event, temperature, humidity, entry1, entry2):
        th.Thread.__init__(self)
        self.temperature = temperature
        self.humidity = humidity
        self.entry1 = entry1
        self.entry2 = entry2
        self.stopped = stop_event
        self.daemon = True  # Указываем, что этот поток - демон

    def run(self):
        TEMP = random.randint(20, 27)
        HUMI = random.randint(20, 90)
        temperature1 = self.temperature.get()
        humidity1 = self.humidity.get()
        while not self.stopped.is_set():
            TEMP = round(TEMP, 2)
            HUMI = round(HUMI, 2)
            if HUMI > humidity1 and TEMP < temperature1:
                print("Значение температуры в теплице 2: " + str(TEMP))
                self.entry1.set(TEMP)
                print("Значени влажности в теплице 12: " + str(HUMI))
                self.entry2.set(HUMI)
                random_number1 = random.uniform(0.1, 0.5)
                TEMP += random_number1
                random_number2 = random.uniform(2, 4)
                HUMI -= random_number2
            elif HUMI < humidity1 and TEMP > temperature1:
                print("Значение температуры в теплице 2: " + str(TEMP))
                self.entry1.set(TEMP)
                print("Значени влажности в теплице 2: " + str(HUMI))
                self.entry2.set(HUMI)
                random_number1 = random.uniform(0.1, 0.5)
                TEMP -= random_number1
                random_number2 = random.randint(10, 13)
                HUMI += random_number2
            elif HUMI < humidity1 and TEMP < temperature1:
                print("Значение температуры в теплице 2: " + str(TEMP))
                self.entry1.set(TEMP)
                print("Значени влажности в теплице 2: " + str(HUMI))
                self.entry2.set(HUMI)
                random_number1 = random.uniform(0.1, 0.5)
                TEMP += random_number1
                random_number2 = random.randint(10, 13)
                HUMI += random_number2
            elif HUMI > humidity1 and TEMP > temperature1:
                print("Значение температуры в теплице 2: " + str(TEMP))
                self.entry1.set(TEMP)
                print("Значени влажности в теплице 2: " + str(HUMI))
                self.entry2.set(HUMI)
                random_number1 = random.uniform(0.1, 0.5)
                TEMP -= random_number1
                random_number2 = random.randint(2, 4)
                HUMI -= random_number2
            time.sleep(1)


class ControlThread(th.Thread):
    def __init__(self, threads_to_control, b1, b2):
        th.Thread.__init__(self)
        self.threads_to_control = threads_to_control
        self.b1 = b1
        self.b2 = b2

    def run(self):
        for thread in self.threads_to_control:
            thread.stopped.set()
        rand = random.randint(1, 6)
        if rand == 1:
            Passive(self.b1, self.b2)
            result = messagebox.showerror("Поломка датчика влажности в первой теплице.",
                                          "Работа система остановлена. Нажмите ОК чтобы произвести починку. Потом заново запустите систему")
            if result == "ok":
                time.sleep(2)
                messagebox.showinfo("Уведомление.",
                                    "Система восстановлена")
                Active(self.b1, self.b2)
                for thread in self.threads_to_control:
                    thread.stopped.clear()
        elif rand == 2:
            Passive(self.b1, self.b2)
            result = messagebox.showerror("Поломка датчика влажности во второй теплице.",
                                          "Работа система остановлена. Нажмите ОК чтобы произвести починку. Потом заново запустите систему")
            if result == "ok":
                time.sleep(2)
                messagebox.showinfo("Уведомление.",
                                    "Система восстановлена")
                Active(self.b1, self.b2)
                self.b1.state = "unable"
                self.b2.state = "unable"
                for thread in self.threads_to_control:
                    thread.stopped.clear()
        elif rand == 3:
            Passive(self.b1, self.b2)
            result = messagebox.showerror("Поломка датчика температуры в первой теплице.",
                                          "Работа система остановлена. Нажмите ОК чтобы произвести починку. Потом заново запустите систему")
            if result == "ok":
                time.sleep(2)
                messagebox.showinfo("Уведомление.",
                                    "Система восстановлена")
                Active(self.b1, self.b2)
                for thread in self.threads_to_control:
                    thread.stopped.clear()
        elif rand == 4:
            Passive(self.b1, self.b2)
            result = messagebox.showerror("Поломка датчика температуры во второй теплице.",
                                          "Работа система остановлена. Нажмите ОК чтобы произвести починку. Потом заново запустите систему")
            if result == "ok":
                time.sleep(2)
                messagebox.showinfo("Уведомление.",
                                    "Система восстановлена")
                Active(self.b1, self.b2)
                for thread in self.threads_to_control:
                    thread.stopped.clear()
        elif rand == 5:
            Passive(self.b1, self.b2)
            result = messagebox.showerror("Поломка электромагнитного клапана зоны в первой теплице'.",
                                          "Работа система остановлена. Нажмите ОК чтобы произвести починку. Потом заново запустите систему")
            if result == "ok":
                time.sleep(2)
                messagebox.showinfo("Уведомление.",
                                    "Система восстановлена")
                Active(self.b1, self.b2)
                for thread in self.threads_to_control:
                    thread.stopped.clear()
        elif rand == 6:
            Passive(self.b1, self.b2)
            result = messagebox.showerror("Поломка электромагнитного клапана зоны во второй теплице.",
                                          "Работа система остановлена. Нажмите ОК чтобы произвести починку. Потом заново запустите систему")
            if result == "ok":
                time.sleep(2)
                messagebox.showinfo("Уведомление.",
                                    "Система восстановлена")
                Active(self.b1, self.b2)
                for thread in self.threads_to_control:
                    thread.stopped.clear()


def Passive(b1, b2):
    b1["state"] = "disabled"
    b2["state"] = "disabled"


def Active(b1, b2):
    b1["state"] = "normal"
