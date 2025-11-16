import tkinter as tk
from tkinter import ttk


class App(tk.Frame):

    COUNTRIES = [
        "UK",
        "France",
        "Germany",
        "Italy",
    ]

    GENDER = [
        "Male",
        "Female",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Variables to store selections

        self.gender_intvar = tk.IntVar()
        self.country_strvar = tk.StringVar()
        self.programming_java_boolvar = tk.BooleanVar()
        self.programming_python_boolvar = tk.BooleanVar()

        # Contents of our left column

        self.title_label = tk.Label(self, text="Registration Form")
        self.full_name_label = tk.Label(self, text="Full Name")
        self.email_label = tk.Label(self, text="Email")
        self.gender_label = tk.Label(self, text="Gender")
        self.country_label = tk.Label(self, text="Country")
        self.programming_label = tk.Label(self, text="Programming")
        self.submit_button = tk.Button(
            self,
            text="Submit",
            command=self.submit_button_pressed
        )


        # Contents of our right column

        self.full_name_entry = tk.Entry(self, width=30)
        self.email_entry = tk.Entry(self, width=30)
        self.male_radio_button = tk.Radiobutton(self,
                                                text=self.GENDER[0],
                                                value=0,
                                                variable=self.gender_intvar
                                                )

        self.female_radio_button = tk.Radiobutton(self,
                                                  text=self.GENDER[1],
                                                  value=1,
                                                  variable=self.gender_intvar
                                                  )

        self.country_combobox = ttk.Combobox(
            self,
            state="readonly",
            width=10,
            values=self.COUNTRIES,
            textvariable=self.country_strvar,
        )

        self.programming_java_checkbutton = tk.Checkbutton(self,
                                                           text="Java",
                                                           variable=self.programming_java_boolvar
                                                           )

        self.programming_python_checkbutton = tk.Checkbutton(self,
                                                             text="Python",
                                                             variable=self.programming_python_boolvar
                                                             )

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

        self.full_name_entry.grid(row=1, column=1, columnspan=3)
        self.email_entry.grid(row=2, column=1, columnspan=3)
        self.male_radio_button.grid(row=3, column=1, sticky=tk.W)
        self.female_radio_button.grid(row=3, column=2, sticky=tk.W)
        self.country_combobox.grid(row=4, column=1, columnspan=2)
        self.programming_java_checkbutton.grid(row=5, column=1, sticky=tk.W)
        self.programming_python_checkbutton.grid(row=5, column=2, sticky=tk.W)

        # Some formatting

        self.title_label.config(font=("Arial", 24))
        self.submit_button.config(bg="red")

        # Format the columns

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=1)


    def submit_button_pressed(self):
        print(f'State: {self.get_state()}')

    @property
    def full_name(self):
        return self.full_name_entry.get()

    @property
    def email(self):
        return self.email_entry.get()

    @property
    def gender(self):
        return self.GENDER[self.gender_intvar.get()]


    @property
    def country(self):
        return self.country_combobox.get()

    @property
    def programming_languages(self):
        languages = []

        if self.programming_java_boolvar.get():
            languages.append("Java")

        if self.programming_python_boolvar.get():
            languages.append("Python")

        return languages


    def get_state(self):
        return {'name': self.full_name,
                'email': self.email,
                'country': self.country,
                'gender': self.gender,
                'languages': self.programming_languages
                }


root = tk.Tk()
root.title("Registration Form")

app = App(root)

app.pack()

root.mainloop()