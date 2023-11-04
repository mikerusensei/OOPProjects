import tkinter as tk
from datetime import datetime
from functions import *


current_date = datetime.now()

class GUIBank(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__add_label()
        self.__add_button()
        self.__config_window()

    def __config_window(self):
        self.title("Foobar's Bank")
        self.geometry('500x500')
        self.resizable(False, False)

        for widget in self.winfo_children():
            widget.config(font=("Calibri", 16))

    def __add_label(self):
        date_label = tk.Label(self, text=f"{current_date:%A, %B %d, %Y}")
        date_label.pack(anchor='w')

        time_label = tk.Label(self, text=current_time)
        time_label.pack(anchor='w')
        current_time(time_label)

        greet_label = tk.Label(self, text=f"\n\n{greet()}")
        greet_label.pack(anchor='w')

        welcome_label = tk.Label(self, text="Welcome to FooBar's Bank\n\n\n")
        welcome_label.pack(anchor='w')

        option_label = tk.Label(self, text='\n\n\n[OPTIONS]')
        option_label.pack(anchor='w')
        

    def __add_button(self):
        
        create_button = tk.Button(self, text="Create an account",
                                  )
        create_button.pack(anchor='w')

        login_button = tk.Button(self, text='Log In')
        login_button.pack(anchor='w')

        exit_button = tk.Button(self, text='Exit',
                                )
        exit_button.pack(anchor='w')
        
    def run(self):
        self.mainloop()