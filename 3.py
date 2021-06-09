import win32api


def scanDrives():
    
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    
    return drives

print(scanDrives())