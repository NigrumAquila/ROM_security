from tkinter import Label


def formatDrives(drives):
    
    for index, drive in enumerate(drives):
        drives[index] = drive[:2]

    # print('Подсоединенные диски: '+ ' '.join([str(item) for item in drives]))
    
    return drives


def formatActionSpaceToUnderscore(action):
    action = action.replace(' ', '_') 
    return action

def formatActionUnderscoreToSpace(action):
    action = action.replace('_', ' ') 
    return action