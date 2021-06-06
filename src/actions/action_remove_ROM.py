from core.helpers.fileHelpers import readDB
from core.styles.colors import end, printText, typedText


DB, pathToDB = readDB()

removableIdentificator = typedText('Enter the number of the identifier to be deleted: ')

lines = DB.readlines()
DB.close()

lineFlag = False
for line in lines:
    separator = line.find(':')
    lineIdentificator = line[:separator]
    if lineIdentificator == removableIdentificator: 
        lineFlag = True
        break

if lineFlag != True: end('Identificator not found in DB.')

DB = open(pathToDB, "w")

for line in lines:
    separator = line.find(':')
    lineIdentificator = line[:separator]
    if lineIdentificator == removableIdentificator: continue
    DB.write(line)

DB.close()

printText('ROM removed successfully.')