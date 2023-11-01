import tkinter as tk
from datetime import datetime
from time import strftime
from functions import current_time, greet

current_date = datetime.now()

class GUIBank(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(anchor='w')

    def display(self):
        self.title('Bank GUI')
        self.geometry('500x500')
        self.resizable(False, False)
        self.welcome()
        self.mainloop()

    def welcome(self):
        date_label = tk.Label(self.main_frame, text=f"{current_date:%A, %B %d, %Y}")
        date_label.pack(anchor='w')

        time_label = tk.Label(self.main_frame, text=current_time)
        time_label.pack(anchor='w')
        current_time(time_label)

        greet_label = tk.Label(self.main_frame, text=f"\n\n{greet()}")
        greet_label.pack(anchor='w')

        welcome_label = tk.Label(self.main_frame, text="Welcome to FooBar's Bank\n\n\n")
        welcome_label.pack(anchor='w')

        option_label = tk.Label(self.main_frame, text='\n\n\n[OPTIONS]')
        option_label.pack(anchor='w')
        
        create_button = tk.Button(self.main_frame, text="Create an account",
                               command=self.create_account)
        create_button.pack(anchor='w')

        login_button = tk.Button(self.main_frame, text='Log In')
        login_button.pack(anchor='w')

        exit_button = tk.Button(self.main_frame, text='Exit',
                             command=self.exit)
        exit_button.pack(anchor='w')

        for widget in self.main_frame.winfo_children():
            widget.config(font=("Calibri", 16))

    def create_account(self):
        self.iconify()
        ca_window = tk.Toplevel()
        ca_window.title("Create an Account")
        ca_window.resizable(False, False)
        ca_frame = tk.Frame(ca_window)
        ca_frame.pack(anchor='w')
        
        welcome_label = tk.Label(ca_frame, text="[CREATE AN ACCOUNT]")
        welcome_label.grid(row=0, column=0)

        credential_label = tk.Label(ca_frame, text='\n[ACCOUNT CREDENTIAL]\n')
        credential_label.grid(row=1, column=0)

        username_label = tk.Label(ca_frame, text='Prefer Username: ')
        username_label.grid(row=2, column=0)

        username_input = tk.Entry(ca_frame)
        username_input.grid(row=2, column=1)
        
        password_label = tk.Label(ca_frame, text='Prefer Password: ')
        password_label.grid(row=3, column=0)

        password_entry = tk.Entry(ca_frame)
        password_entry.grid(row=3, column=1)

        personal_info_label = tk.Label(ca_frame, text='\n[PERSONAL INFORMATION]\n')
        personal_info_label.grid(row=4, column=0)

        lastname_label = tk.Label(ca_frame, text='Last Name: ')
        lastname_label.grid(row=5, column=0)

        lastname_entry = tk.Entry(ca_frame)
        lastname_entry.grid(row=5, column=1)

        givenname_label = tk.Label(ca_frame, text='Given Name: ')
        givenname_label.grid(row=6, column=0)

        givenname_entry = tk.Entry(ca_frame)
        givenname_entry.grid(row=6, column=1)

        middlename_label = tk.Label(ca_frame, text='Middle Name: ')
        middlename_label.grid(row=7, column=0)

        middlename_entry = tk.Entry(ca_frame)
        middlename_entry.grid(row=7, column=1)

        other_info_label = tk.Label(ca_frame, text='\n[OTHER INFORMATION]\n')
        other_info_label.grid(row=8, column=0)

        birthdate_label = tk.Label(ca_frame, text='Birthdate: ')
        birthdate_label.grid(row=9, column=0)

        birthdate_entry = tk.Entry(ca_frame)
        birthdate_entry.grid(row=9, column=1)

        gender_label = tk.Label(ca_frame, text='Sex: ')
        gender_label.grid(row=10, column=0)

        gender_combo = tk.Entry(ca_frame)
        gender_combo.grid(row=10, column=1)

        for widget in ca_frame.winfo_children():
            widget.config(font=("Calibri", 14))

    def login(self):
        pass

    def exit(self):
        self.destroy()
