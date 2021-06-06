from core.styles.colors import warning
from core.removers.removeDevice import removeDevice
from core.helpers.log import log


def checkDrives(to_check, approvedIdentificators, pathToLogFile):
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
                message = 'Key not found.'
                warning(message)
                removeDevice(checked_disk)
                log(message, pathToLogFile)
            
        except FileNotFoundError:
            message = 'File not found.'
            warning(message)
            removeDevice(checked_disk)
            log(message, pathToLogFile)

        except IOError:
            message = 'Failed to open file.'
            warning(message)
            removeDevice(checked_disk)
            log(message, pathToLogFile)

        except OSError:
            message = 'Possible privilege problem.'
            warning(message)
            removeDevice(checked_disk)
            log(message, pathToLogFile)