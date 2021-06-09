import tkinter as tk
from core.constants.interfaceConstants import EXIT, GUI_ACTION_MODULE_SPACE
from core.constants.actionConstants import ACTION_choice
from core.removers.removeModule import removeModule
from core.gui.invoke_action import invoke_action

window = tk.Tk()
window.title('DB Manager')


for index, action in enumerate(ACTION_choice):
    exec(f"btn_{action} = tk.Button(master=window, text='{action}', command=lambda: invoke_action(btn_{action}))")
    exec(f"btn_{action}.grid(row=0, column=index, sticky='nsew')")

    
window.mainloop()
