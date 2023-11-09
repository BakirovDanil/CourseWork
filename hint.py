import time
import tkinter as tk


class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.showToolTip)
        self.widget.bind("<Leave>", self.hideToolTip)

    def showToolTip(self, event):
        self.tooltipWindow = tk.Toplevel(self.widget)
        self.tooltipWindow.wm_overrideredirect(True)
        self.tooltipWindow.wm_geometry(f"+{event.x_root}+{event.y_root + 20}")
        self.tooltipContainer = tk.Frame(self.tooltipWindow, bg='black')
        self.tooltipContainer.pack()
        self.tooltipLabel = tk.Label(self.tooltipContainer, text=self.text, bg='black', fg='white')
        self.tooltipLabel.pack()

    def hideToolTip(self, event):
        self.tooltipWindow.destroy()
