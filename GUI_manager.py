import tkinter as tk
from core.constants.actionConstants import ACTION_choice
from core.gui.invoke_action import invoke_action
from core.gui.drawButtons import drawButtons
from core.helpers.format import formatActionUnderscoreToSpace


managerApp = tk.Tk()
managerApp.title('DB Manager')
        
drawButtons(managerApp)


def on_close():
    managerApp.destroy()
    exit()

managerApp.protocol('WM_DELETE_WINDOW', on_close)
managerApp.mainloop()