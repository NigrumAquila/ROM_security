import tkinter as tk
from core.constants.interfaceConstants import EXIT, GUI_ACTION_MODULE_SPACE
from core.constants.actionConstants import ACTION_choice
from core.removers.removeModule import removeModule
from core.gui.invoke_action import invoke_action

window = tk.Tk()
window.title('DB Manager')

window.rowconfigure(0, minsize=60, weight=1)
window.columnconfigure([0, 1, 2, 3, 4, 5], minsize=100, weight=1)


window.mainloop()