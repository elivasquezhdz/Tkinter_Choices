import tkinter as tk
from tkinter import ttk
import datetime as dt

def add_label():
    choice1 = choices.get() + " " +  str(dt.datetime.now()).split(".")[0] + " " + name_entry.get()
    label1 = tk.Label(root, text=choice1)
    label1.pack()

root = tk.Tk()
root.title("ComboBox Choices")

choices_label = tk.Label(root, text="Select Choice:")
choices_label.pack()
choices = ttk.Combobox(root, values=["A", "B", " C"])
choices.pack()

name_label = tk.Label(root ,text = " Name")
name_label.pack()
#.grid(row = 0,column = 0)
name_entry  = tk.Entry(root)#.grid(row = 0,column = 1)
name_entry.pack()
add_button = tk.Button(root, text="Add Labels", command=add_label)
add_button.pack()

root.mainloop()