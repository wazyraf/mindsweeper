# account_page.py
import tkinter as tk

class AccountPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="This is the Account page")
        label.pack(pady=10, padx=10)
