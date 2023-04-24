""" Листинг 7.12 Приложение «hello world» на Tkinter."""
import tkinter as tk 
from tkinter import ttk
import time

window = tk.Tk()
window.title("Hello word app")
window.geometry("200x100")

def say_hello():
    print("Hello!")
    time.sleep(10)

hello_button = ttk.Button(window, text="Say hello", command=say_hello)
hello_button.pack()

window.mainloop()
