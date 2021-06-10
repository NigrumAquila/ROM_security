import time
from threading import Thread
import __main__


def new_thread():
    thread = Thread(target=start).start()


def start():
    global trigger
    if 'trigger' in globals() and trigger == True: return

    trigger = True
    __main__.label['text'] = getStatus()
    __main__.label['fg'] = '#0f0'
    
    while trigger:
        print(time.ctime())
        time.sleep(1)

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