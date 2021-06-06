from core.helpers.fileHelpers import readDB, getTimeOfCreationAndModification
from core.styles.colors import printTextAndValue


DB, pathToDB = readDB()
creationTime, modificationTime = getTimeOfCreationAndModification(pathToDB)


printTextAndValue('Created: ', creationTime)
printTextAndValue('Last modified: ', modificationTime)

for line in DB:
    leftSeparator = line.find("'")
    rightSeparator = line.find("'", leftSeparator + 1)
    DB_identificator = line[:leftSeparator - 2]
    ROM_identificator = line[leftSeparator + 1:rightSeparator]
    printTextAndValue(DB_identificator, ROM_identificator)

DB.close()