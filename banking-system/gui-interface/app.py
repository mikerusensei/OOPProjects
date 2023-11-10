import tkinter as tk
from datetime import datetime
from functions import *
from widgetgenerator import *

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
        LabelGeneratorPack(self)\
            .set_text(f"{current_date:%A, %B %d, %Y}")\
            .set_anchor("w")\
            .build()

        time_label = LabelGeneratorPack(self)\
            .set_text(current_time)\
            .set_anchor("w")\
            .build()
        current_time(time_label)

        LabelGeneratorPack(self)\
            .set_text(f"\n\n{greet()}")\
            .set_anchor("w")\
            .build()
        
        LabelGeneratorPack(self)\
            .set_text("Welcome to FooBar's Bank\n\n\n")\
            .set_anchor("w")\
            .build()
        
        LabelGeneratorPack(self)\
            .set_text("\n\n\n[OPTIONS]")\
            .set_anchor("w")\
            .build()

    def __add_button(self):
        ButtonGeneratorPack(self)\
            .set_text("Create Account")\
            .set_command(None)\
            .set_anchor("w")\
            .build()

        ButtonGeneratorPack(self)\
            .set_text("Log In")\
            .set_command(None)\
            .set_anchor("w")\
            .build()

        ButtonGeneratorPack(self)\
            .set_text("Exit")\
            .set_command(self.destroy)\
            .set_anchor("w")\
            .build()
        
    def run(self):
        self.mainloop()