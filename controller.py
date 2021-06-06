from core.helpers.fileHelpers import writeLog
from core.verification.check_drives import checkDrives
# from core.styles.colors import printText, typedText, printValue
from core.helpers.getApprovedIdentificators import getApprovedIdentificators
from core.helpers.getPresets import getPresets
from core.scanners.driveScanner import scanDrives
from core.helpers.format import formatDrives
from core.helpers.filter import getToCheckedDrives
from core.verification.check_drives import checkDrives
from time import sleep


approvedIdentificators = getApprovedIdentificators()

pathToLogFile = writeLog()

presets = getPresets()

while True:
    drives = scanDrives()
    drives = formatDrives(drives)

    to_check = getToCheckedDrives(drives, presets)

    sleep(1)

    checkDrives(to_check, approvedIdentificators, pathToLogFile)