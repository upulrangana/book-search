"""text widget of tkinter

Creates a window with a text box
when you hit ctrl + s it will print the
content of the text box in the console
"""

from tkinter import Tk
import tkinter as tk


root = Tk()


def start(event):
    print(text.get("0.0", tk.END))


text = tk.Text(root)
text.pack()
text.bind("<Control - s>", start)
root.mainloop()