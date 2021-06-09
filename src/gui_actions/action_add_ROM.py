from tkinter import messagebox
from os import stat
from core.helpers.fileHelpers import readDB, writeROM, writeDB
from core.math.generateIdentificator import generateIdentificator


new_ROM_identificator = generateIdentificator()
DB, pathToDB = readDB()

for line in DB:
    leftSeparator = line.find("'") + 1
    rightSeparator = line.find("'", leftSeparator)
    ROM_identificator_duplicate_candidate = line[leftSeparator:rightSeparator]

    while new_ROM_identificator == ROM_identificator_duplicate_candidate:
        new_ROM_identificator = generateIdentificator()

DB.seek(0)

DB_next_identificator = 1

if stat(pathToDB).st_size > 0:
    DB_last_line = DB.readlines()[-1:][0]
    separator = DB_last_line.find(':')
    DB_last_identificator = int(DB_last_line[:separator])
    DB_next_identificator = DB_last_identificator + 1

DB.close()

ROM_file = writeROM()

ROM_file.write(new_ROM_identificator)
ROM_file.close()

DB, pathToDB = writeDB(pathToDB)
writable_row = str(DB_next_identificator) + ': ' + "'" + new_ROM_identificator + "'"
DB.write(writable_row)
DB.close()


messagebox.showinfo(title='Add ROM', message='ROM added successfully.')