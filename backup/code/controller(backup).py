from core.styles.colors import printText, typedText, printValue
import subprocess

# - принять 1 базу данных (по ней ориентироваться) 
######################################################################
from core.helpers.fileHelpers import readDB

approvedIdentificators = []
DB, pathToDB = readDB()
for line in DB:
    leftSeparator = line.find("'")
    rightSeparator = line.find("'", leftSeparator + 1)
    approvedIdentificators.append(line[leftSeparator + 1: rightSeparator])

for identificator in approvedIdentificators:
    printValue(identificator)
######################################################################


# - фильтровать по базе данных и предустановкам
######################################################################
presets = typedText('Enter drive names separated by commas: ')
presets = presets.split(',')

for index, preset in enumerate(presets):
    presets[index] = preset.upper() + ':'    

print('Не нужно проверять: ' + ' '.join([str(item) for item in presets]))
######################################################################

# - будет сканировать на подсоединенные диски
######################################################################
import win32api
from time import sleep

drives = []
def scanDrives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return drives

while True:
    drives = scanDrives()
    for index, drive in enumerate(drives):
        drives[index] = drive[:2]

    to_check = [drive for drive in drives if drive not in presets]

    sleep(1)
    print('Подсоединенные диски: '+ ' '.join([str(item) for item in drives]))
    print('На проверку: ', to_check)

######################################################################
    # - подсоединенные диски проверять по базе данных и файлу на диске
    for checked_disk in to_check:
        try:
            key_file = open(checked_disk + '/' + 'ROM_security', 'r')
            keys_in_file = key_file.readlines()

            keyFound = False
            for key in keys_in_file:
                if key in approvedIdentificators:
                    keyFound = True
                    break

            if not keyFound:
                subprocess.call('mountvol ' + checked_disk + ' /p')
            
        except FileNotFoundError:
            print('File not found.')
            subprocess.call('mountvol ' + checked_disk + ' /p')
        except IOError:
            print('Failed to open file.')
            subprocess.call('mountvol ' + checked_disk + ' /p')
        except OSError:
            print('Possible privilege problem.')
            subprocess.call('mountvol ' + checked_disk + ' /p')
