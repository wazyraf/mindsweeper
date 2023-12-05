#play_page.py
import tkinter as tk

class PlayPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="This is the Play page")
        label.pack(pady=10, padx=10)
