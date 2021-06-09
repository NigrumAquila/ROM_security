from tkinter import messagebox
from core.helpers.fileHelpers import readDB
from re import match


DB, path = readDB()

pattern = "\d+:\s'[^']+'$"

DB_is_correct = True

identificators = []

for index, line in enumerate(DB):
    if match(pattern, line) == None:
        messagebox.showerror(title='Check integrity', message='DB is corrupted - invalid string. Error in line: ' + str(index + 1))
        DB_is_correct = False
        break
    
    separator = line.find(':')
    identificator = line[:separator]
    
    if identificator in identificators:
        messagebox.showerror(title='Check integrity', message='DB is corrupted - duplicate identifier. Error in line: ' + str(index + 1))
        DB_is_correct = False
        break

    identificators.append(identificator)

if DB_is_correct:
    messagebox.showinfo(title='Check integrity', message='Database is correct.')