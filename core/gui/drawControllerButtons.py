import tkinter as tk
from core.constants.controllerConstants import CONTROLLER_choice, CONTROLLER_functions


def drawControllerButtons(controllerApp):
    for index, action in enumerate(CONTROLLER_choice):
        # exec(f"globals()['btn_{action}'] = tk.Button(text='{action}', padx=10, pady=10, command=lambda: CONTROLLER_functions['{action}'])")
        exec(f"globals()['btn_{action}'] = tk.Button(text='{action}', padx=10, pady=10, command=CONTROLLER_functions['{action}'])")
        exec(f"btn_{action}.grid(row=1, column=index, sticky='nsew')")