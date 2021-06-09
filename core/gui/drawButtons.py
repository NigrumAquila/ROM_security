import tkinter as tk
from core.constants.actionConstants import ACTION_choice
from core.gui.invoke_action import invoke_action
from core.helpers.format import formatActionUnderscoreToSpace, formatActionSpaceToUnderscore

def drawButtons(managerApp):
    for index, action in enumerate(ACTION_choice):
        exec(f"globals()['btn_{action}'] = tk.Button(master=managerApp, text=formatActionUnderscoreToSpace('{action}'), padx=10, pady=10, command=lambda: invoke_action(btn_{action}))")
        exec(f"btn_{action}.grid(row=0, column=index, sticky='nsew')")