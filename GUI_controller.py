import threading
import tkinter as tk
from core.gui.drawControllerButtons import drawControllerButtons
from src.controller.functions import getStatus


controllerApp = tk.Tk()
controllerApp.title('ROM Controller')
controllerApp.geometry('250x70')

label = tk.Label(text=getStatus(), fg='sky blue')
label.grid(row=0, sticky='', columnspan=2)

drawControllerButtons(controllerApp)


def on_close():
    from src.controller.functions import stop; stop()
    controllerApp.destroy()
    exit()


controllerApp.protocol('WM_DELETE_WINDOW', on_close)
controllerApp.mainloop()