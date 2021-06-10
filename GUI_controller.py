from core.helpers.checkAdmin import checkAdmin

checkAdmin()

import tkinter as tk
from core.gui.drawControllerButtons import drawControllerButtons
from src.controller.functions import getStatus


controllerApp = tk.Tk()
controllerApp.title('ROM Controller')
controllerApp.geometry('260x70')
# controllerApp.configure(background='white')

label = tk.Label(text=getStatus(), fg='sky blue')
label.grid(row=0, sticky='', columnspan=2)

drawControllerButtons(controllerApp)


def on_close():
    from src.controller.functions import stop; stop()
    controllerApp.destroy()
    exit()


controllerApp.protocol('WM_DELETE_WINDOW', on_close)
controllerApp.mainloop()