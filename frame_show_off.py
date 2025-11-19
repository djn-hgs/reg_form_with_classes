import math
import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
title_label = tk.Label(root, text="Trippy grid")
title_label.grid(row=0, column=0)

big_frame = tk.Frame(root)
big_frame.grid(row=1, column=0, sticky='nsew')

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=10)
root.columnconfigure(0, weight=1)

def title_change(new_text):
    title_label.configure(text=new_text)

class ButtonThatKnowsWhatItIs(tk.Button):
    def __init__(self, master, callback, x, y, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)

        self.x = x
        self.y = y
        self.callback = callback

    def get_pos(self):
        self.callback(f"I'm a button! {self.x} {self.y}")
        return self.x, self.y

def print_state(message):
    print("The main program gets the message:", message)

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            c = "hotpink"
        else:
            c = "darkgoldenrod"
        trippy_grid_frame = tk.Frame(big_frame, bg=c)
        trippy_grid_frame.grid(row=i, column=j, sticky="news")

        new_button = ButtonThatKnowsWhatItIs(trippy_grid_frame,
                                             print_state, i, j,
                               text="Click here",
                               bg=c
                               )
        new_button.config(command=new_button.get_pos)

        new_button.grid(sticky='news')
        trippy_grid_frame.rowconfigure(0, weight=1)
        trippy_grid_frame.columnconfigure(0, weight=1)

for i in range(8):
    big_frame.rowconfigure(i, weight=int(100*math.sin(math.pi *i/8)))
    big_frame.columnconfigure(i, weight=int(100*math.sin(math.pi* i/8)))


root.mainloop()