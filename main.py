from tkinter import *

Frame = Tk()


def MainForm(window):
    window.title("Систему управления поливом")
    window.geometry("1024x700+450+100")
    window.resizable(False, False)
    window.mainloop()


MainForm(Frame)