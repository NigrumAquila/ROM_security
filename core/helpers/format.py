def formatDrives(drives):
    
    for index, drive in enumerate(drives):
        drives[index] = drive[:2]

    # print('Подсоединенные диски: '+ ' '.join([str(item) for item in drives]))
    
    return drives