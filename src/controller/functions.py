import tkinter as tk
from tkinter import messagebox
from threading import Thread
import __main__
from core.helpers.fileHelpers import writeLog
from core.verification.check_drives import checkDrives
from core.helpers.getApprovedIdentificators import getApprovedIdentificators
from core.scanners.driveScanner import scanDrives
from core.helpers.format import formatDrives
from core.helpers.filter import getToCheckedDrives
from core.verification.check_drives import checkDrives
from time import sleep, ctime


def new_thread(task):
    thread = Thread(target=task)
    thread.start()

def start():
    global trigger
    if 'trigger' in globals() and trigger == True: return
    trigger = True


    approvedIdentificators = getApprovedIdentificators()
    pathToLogFile = writeLog()

    def getExclusions():
        # global presets
        presets = exclusions.get()
        presets = presets.split(',')
        for index, preset in enumerate(presets):
            presets[index] = preset.upper() + ':'
        
        messagebox.showinfo(title='info', message='Program running')
        # messagebox.showinfo(title='info', message=presets)
        window.destroy()
        # new_thread(run(presets))
        __main__.label['text'] = getStatus()
        __main__.label['fg'] = '#0f0'
        
        # Thread(target=run(presets)).start()
        Thread(target=run, args=(presets,)).start()
        
    window = tk.Toplevel(__main__.controllerApp)
    window.title("Start programm")
    windowLabel = tk.Label(window, text ="Enter exclusions (separated by commas. e.g: 'c,d,e')", pady=10)
    windowLabel.grid(row=0, column=0, sticky='nsew')
    exclusions = tk.Entry(window, width=15)
    exclusions.grid(row=0, column=1)
    windowButton = tk.Button(window, text='Confirm', command=getExclusions)
    windowButton.grid(row=0, column=2, padx=(10, 10))
    
    
    # exclusions = getExclusions()
    def run(presets):
        while trigger:
            drives = scanDrives()
            drives = formatDrives(drives)

            to_check = getToCheckedDrives(drives, presets)

            sleep(1)

            checkDrives(to_check, approvedIdentificators, pathToLogFile)


def stop():
    global trigger
    trigger = False
    __main__.label['text'] = getStatus()
    __main__.label['fg'] = '#f00'

def getStatus():
    if 'trigger' in globals():
        global trigger
        if trigger:
            return 'Programm status: active'
        return 'Programm status: not active'
    else:
        return 'Programm status: not active'