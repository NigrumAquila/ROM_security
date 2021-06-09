from tkinter import messagebox
import tkinter as tk
from core.helpers.fileHelpers import readDB


DBreader, pathToDB = readDB()


def remove(removableIdentificator):
    global DB
    DBreader.seek(0)
    lines = DBreader.readlines()

    lineFlag = False
    for line in lines:
        separator = line.find(':')
        lineIdentificator = line[:separator]
        if lineIdentificator == removableIdentificator: 
            lineFlag = True
            break

    if lineFlag != True:
        messagebox.showerror(title='Remove ROM', message='Identificator not found in DB.', parent=remover_window)

    else:
        DBwriter = open(pathToDB, "w")

        for line in lines:
            separator = line.find(':')
            lineIdentificator = line[:separator]
            if lineIdentificator == removableIdentificator: continue
            DBwriter.write(line)

        DBwriter.close()

        messagebox.showinfo(title='Remove ROM', message='ROM removed successfully.', parent=remover_window)


def on_close():
    DBreader.close()
    remover_window.destroy()


remover_window = tk.Toplevel()
remover_window.title('Remove ROM')

helpLabel = tk.Label(remover_window, text="Enter ROM ID in DB")
removableIdentificator = tk.Entry(remover_window, width=30)
btnRemove = tk.Button(master=remover_window, text='Remove', command=lambda: remove(removableIdentificator.get()))

helpLabel.grid(row=0, columnspan=2, pady=(10,20))
removableIdentificator.grid(row=1,column=0, padx=(10, 0), pady=(0,10))
btnRemove.grid(row=1, column=1, sticky='nsew', padx=(10, 10), pady=(0,10))

remover_window.protocol('WM_DELETE_WINDOW', on_close)