# main.py
import tkinter as tk
from mainpages import play_page
from mainpages import settings_page
from mainpages import account_page
from PIL import ImageTk, Image
from tkinter import *



class MainPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Draw it")
        self.pack()

        #get screen width and height - for windowed full-screen
        #screen_width = self.master.winfo_screenwidth()
        #creen_height = self.master.winfo_screenheight()

        self.master.geometry("800x600")

        l = Label(root, text = "DRAW IT")
        l.config(font = ("Arial", 20), bg= '#373535', height = 4, fg = 'white')
        l.pack()

        global img
        global small_image
        img = tk.PhotoImage(file = "background.png")
        small_image = img.subsample(2,2)
        lbl = Label(image = small_image)
        lbl.pack()

        colour1 = 'white'
        colour2 = 'green'
        colour3 = 'gray'
        colour4 = 'black'
        

        play_button = tk.Button(
            root,
            background=colour1, 
            foreground=colour4,
            activebackground=colour3,
            activeforeground=colour4,
            highlightthickness=2,
            highlightbackground=colour2,
            highlightcolor='white',
            width=10,
            height = 1,
            border=0, 
            cursor='hand1',
            text = 'PLAY',
            font=('Arial', 15, 'bold'),
            command=lambda: self.show_frame(play_page.PlayPage)
        )
        play_button.place(relx = 0.25, rely = 0.4)
        #button1.grid(column=0, row=0)
        play_button.lift()

        settings_button = tk.Button(
            root,
            background=colour1, 
            foreground=colour4,
            activebackground=colour3,
            activeforeground=colour4,
            highlightthickness=2,
            highlightbackground=colour2,
            highlightcolor='white',
            width=10,
            height = 1,
            border=0, 
            cursor='hand1',
            text = 'SETTINGS',
            font=('Arial', 15, 'bold'),
            command=lambda: self.show_frame(settings_page.SettingsPage)
        )
        settings_button.place(relx = 0.25, rely = 0.5)
        #button1.grid(column=0, row=0)
        settings_button.lift()

        account_button = tk.Button(
            root,
            background=colour1, 
            foreground=colour4,
            activebackground=colour3,
            activeforeground=colour4,
            highlightthickness=2,
            highlightbackground=colour2,
            highlightcolor='white',
            width=10,
            height = 1,
            border=0, 
            cursor='hand1',
            text = 'ACCOUNT',
            font=('Arial', 15, 'bold'),
            command=lambda : self.show_frame(account_page.AccountPage)
        )
        account_button.place(relx = 0.25, rely = 0.6)
        #button1.grid(column=0, row=0)
        account_button.lift()

        #play_button = tk.Button(self, text="Play", command=lambda: self.show_frame(play_page.PlayPage))
        #settings_button = tk.Button(self, text="Settings", command=lambda: self.show_frame(settings_page.SettingsPage))
        #account_button = tk.Button(self, text="Account", command=lambda: self.show_frame(account_page.AccountPage))

        #play_button.pack(pady=10, padx=10)
        #settings_button.pack(pady=10, padx=10)
        #account_button.pack(pady=10, padx=10)

    def show_frame(self, page):
        for widget in self.winfo_children():
            widget.destroy()
        frame = page(self)
        frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg = '#373535')
    main_page = MainPage(master=root)
    main_page.mainloop()
