from core.helpers.fileHelpers import readDB
from re import match
from core.styles.colors import printTextAndValue, printText, warning, end


DB, path = readDB()

pattern = "\d+:\s'[^']+'$"

identificators = []

for index, line in enumerate(DB):
    if match(pattern, line) == None:
        warning('DB is corrupted - invalid string.')
        printTextAndValue('Error in line: ', str(index + 1))
        end()
    
    separator = line.find(':')
    identificator = line[:separator]
    
    if identificator in identificators:
        warning('DB is corrupted - duplicate identifier.')
        printTextAndValue('Error in line: ', str(index + 1))
        end()

    identificators.append(identificator)

printText('Database is correct.')