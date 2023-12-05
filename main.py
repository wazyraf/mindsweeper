# main.py
import tkinter as tk
from mainpages import play_page
from mainpages import settings_page
from mainpages import account_page

class MainPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Main Page")
        self.pack()

        #get screen width and height - for windowed full-screen
        #screen_width = self.master.winfo_screenwidth()
        #creen_height = self.master.winfo_screenheight()

        #set window size
        self.master.geometry(f'{800}x{600}')
        
        play_button = tk.Button(self, text="Play", command=lambda: self.show_frame(play_page.PlayPage))
        settings_button = tk.Button(self, text="Settings", command=lambda: self.show_frame(settings_page.SettingsPage))
        account_button = tk.Button(self, text="Account", command=lambda: self.show_frame(account_page.AccountPage))

        play_button.pack(pady=10, padx=10)
        settings_button.pack(pady=10, padx=10)
        account_button.pack(pady=10, padx=10)

    def show_frame(self, page):
        for widget in self.winfo_children():
            widget.destroy()
        frame = page(self)
        frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    main_page = MainPage(master=root)
    main_page.mainloop()
