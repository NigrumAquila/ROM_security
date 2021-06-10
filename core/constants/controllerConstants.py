from threading import Thread
from src.controller.functions import start, stop, new_thread


CONTROLLER_choice = {
    'start': '1',
    'stop': '2',   
}

CONTROLLER_functions = {
    # 'start': lambda: Thread(target=start).start(), 
    'start': new_thread, 
    'stop': stop
}