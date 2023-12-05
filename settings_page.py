# settings_page.py
import tkinter as tk

class SettingsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="This is the Settings page")
        label.pack(pady=10, padx=10)
