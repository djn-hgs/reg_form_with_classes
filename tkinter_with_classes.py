import tkinter as tk
from tkinter import ttk


class App(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Contents of our left column

        self.title_label = tk.Label(self, text="Registration Form")
        self.full_name_label = tk.Label(self, text="Full Name")
        self.email_label = tk.Label(self, text="Email")
        self.gender_label = tk.Label(self, text="Gender")
        self.country_label = tk.Label(self, text="Country")
        self.programming_label = tk.Label(self, text="Programming")
        self.submit_button = tk.Button(self, text="Submit")

        # Contents of our right column

        self.full_name_entry = tk.Entry(self, width=40)
        self.email_entry = tk.Entry(self, width=40)
        self.male_radio_button = tk.Radiobutton(self, text="Male", value=1)
        self.female_radio_button = tk.Radiobutton(self, text="Female", value=2)
        self.country_combobox = ttk.Combobox(self, state="readonly")
        self.programming_java_checkbutton = tk.Checkbutton(self, text="Java")
        self.programming_python_checkbutton = tk.Checkbutton(self, text="Python")

        # Boring bit - let's grid them all

        # Left column

        self.title_label.grid(row=0, column=0, columnspan=4, sticky=tk.W)
        self.full_name_label.grid(row=1, column=0, sticky=tk.W)
        self.email_label.grid(row=2, column=0, sticky=tk.W)
        self.gender_label.grid(row=3, column=0, sticky=tk.W)
        self.country_label.grid(row=4, column=0, sticky=tk.W)
        self.programming_label.grid(row=5, column=0, sticky=tk.W)
        self.submit_button.grid(row=6, column=0, sticky=tk.W)

        # Right column

        self.full_name_entry.grid(row=1, column=1, columnspan=4)
        self.email_entry.grid(row=2, column=1, columnspan=4)
        self.male_radio_button.grid(row=3, column=1)
        self.female_radio_button.grid(row=3, column=2)
        self.country_combobox.grid(row=4, column=1, columnspan=2)
        self.programming_java_checkbutton.grid(row=5, column=1)
        self.programming_python_checkbutton.grid(row=5, column=2)

        # Some formatting

        self.title_label.config(font=("Arial", 24))
        self.submit_button.config(bg="red")

        # Format the columns

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=1)

root = tk.Tk()
root.title("Registration Form")

app = App(root)

app.pack()

root.mainloop()