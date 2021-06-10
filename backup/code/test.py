import tkinter as tk
from tkinter import messagebox
import time
import threading


app = tk.Tk()
app.title('DB Manager')

app.rowconfigure(0, minsize=60, weight=1)
app.columnconfigure([0, 1, 2, 3, 4, 5], minsize=100, weight=1)

def test():
    def message():
        param = exclusions.get()
        messagebox.showinfo(title='info', message=param)
    
    newWindow = tk.Toplevel(app)
    newWindow.title("New Window")
    newWindowLabel = tk.Label(newWindow, text ="This is a new window")
    newWindowLabel.grid(row=0, column=0, sticky='nsew')
    exclusions = tk.Entry(newWindow, width=15)
    exclusions.grid(row=0, column=1)
    newWindowButton = tk.Button(newWindow, text='message', command=message)
    newWindowButton.grid(row=0, column=2)

label = tk.Label(app, text ="This is the main window")
label.grid(row=0, column=0)

btn_test = tk.Button(master=app, text='test', command=test)
btn_test.grid(row=1, column=0, sticky='nsew')


app.mainloop()