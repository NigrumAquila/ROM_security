import tkinter as tk
from core.constants.interfaceConstants import EXIT, GUI_ACTION_MODULE_SPACE
from core.constants.actionConstants import ACTION_choice
from core.removers.removeModule import removeModule
from core.gui.invoke_action import invoke_action

window = tk.Tk()
window.title('DB Manager')

window.rowconfigure(0, minsize=60, weight=1)
window.columnconfigure([0, 1, 2, 3, 4, 5], minsize=100, weight=1)

btn_add_ROM = tk.Button(master=window, text="add ROM", command=lambda: invoke_action(btn_add_ROM))
btn_add_ROM.grid(row=0, column=0, sticky="nsew")

btn_remove_ROM = tk.Button(master=window, text="remove ROM", command=lambda: invoke_action(btn_remove_ROM))
btn_remove_ROM.grid(row=0, column=1, sticky="nsew")

btn_check_integrity = tk.Button(master=window, text="check integrity", command=lambda: invoke_action(btn_check_integrity))
btn_check_integrity.grid(row=0, column=2, sticky="nsew")

btn_get_info = tk.Button(master=window, text="get info", command=lambda: invoke_action(btn_get_info))
btn_get_info.grid(row=0, column=3, sticky="nsew")


btn_create_DB = tk.Button(master=window, text="create DB", command=lambda: invoke_action(btn_create_DB))
btn_create_DB.grid(row=0, column=4, sticky="nsew")

btn_create_DB_backup = tk.Button(master=window, text="create DB backup", command=lambda: invoke_action(btn_create_DB_backup))
btn_create_DB_backup.grid(row=0, column=5, sticky="nsew")

window.mainloop()
