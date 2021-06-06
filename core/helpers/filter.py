def getToCheckedDrives(drives, presets):

    to_check = [drive for drive in drives if drive not in presets]
    
    # print('На проверку: ', to_check)

    return to_check