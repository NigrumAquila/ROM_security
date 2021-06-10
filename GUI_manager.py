from core.helpers.checkAdmin import checkAdmin

checkAdmin()

import tkinter as tk
from core.gui.drawManagerButtons import drawManagerButtons


managerApp = tk.Tk()
managerApp.title('DB Manager')
        
drawManagerButtons(managerApp)


def on_close():
    managerApp.destroy()
    exit()


managerApp.protocol('WM_DELETE_WINDOW', on_close)
managerApp.mainloop()