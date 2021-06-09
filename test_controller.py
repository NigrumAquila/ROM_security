import tkinter as tk
from core.constants.interfaceConstants import EXIT, GUI_ACTION_MODULE_SPACE
from core.constants.actionConstants import ACTION_choice
from core.removers.removeModule import removeModule
from core.gui.invoke_action import invoke_action

import time
import threading

window = tk.Tk()
window.title('DB Manager')

trigger = False

def mine():
    global trigger

    if trigger: return
    
    trigger = True
    while trigger:
        print(time.ctime())
        time.sleep(1)

def stop():
    global trigger
    trigger = False

def end():
    global trigger
    trigger = False
    exit()

window.rowconfigure(0, minsize=60, weight=1)
window.columnconfigure([0, 1, 2, 3, 4, 5], minsize=100, weight=1)

btn_start = tk.Button(master=window, text='start', command=lambda: threading.Thread(target=mine).start())
btn_start.grid(row=0, column=0, sticky='nsew')

btn_stop = tk.Button(master=window, text='stop', command=stop)
btn_stop.grid(row=0, column=1, sticky='nsew')

btn_exit = tk.Button(master=window, text='exit', command=end)
btn_exit.grid(row=0, column=2, sticky='nsew')

def on_close():
    global trigger
    trigger = False
    window.destroy()
    # exit()

window.protocol('WM_DELETE_WINDOW', on_close)

window.mainloop()