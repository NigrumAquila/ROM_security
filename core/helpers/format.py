from tkinter import Label


def formatDrives(drives):
    
    for index, drive in enumerate(drives):
        drives[index] = drive[:2]

    # print('Подсоединенные диски: '+ ' '.join([str(item) for item in drives]))
    
    return drives


def formatAction(action):
    action = action.replace(' ', '_')
    return action