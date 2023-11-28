from tkinter.messagebox import showerror, showinfo
import random
import threading as th
import time

from future.moves.tkinter import messagebox


# Функции для каждого возможного сценария
class Thr1(th.Thread):  # Создаём экземпляр потока Thread
    def __init__(self, temperature, humidity, entry1, entry2, stop_event):
        th.Thread.__init__(self)
        self.temperature = temperature
        self.humidity = humidity
        self.entry1 = entry1
        self.entry2 = entry2
        self.stopped = stop_event
        self.daemon = False  # Указываем, что этот поток - демон

    def run(self):
        TEMP = 20
        HUMI = 100
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
    def __init__(self, temperature, humidity, entry1, entry2, stop_event):
        th.Thread.__init__(self)
        self.temperature = temperature
        self.humidity = humidity
        self.entry1 = entry1
        self.entry2 = entry2
        self.stopped = stop_event
        self.daemon = True  # Указываем, что этот поток - демон

    def run(self):
        TEMP = 20
        HUMI = 100
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
    def __init__(self, threads_to_stop):
        super().__init__()
        self.threads_to_stop = threads_to_stop

    def run(self):
        for thread in self.threads_to_stop:
            thread.stopped.set()
        result = messagebox.showinfo("Остановка потоков", "Другие потоки остановлены. Нажмите ОК для возобновления.")
        if result == "ok":
            for thread in self.threads_to_stop:
                thread.stopped.clear()
                thread.run()

