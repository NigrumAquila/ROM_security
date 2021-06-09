from tkinter import messagebox
from core.helpers.fileHelpers import addDB
from core.styles.colors import printText

addDB()


messagebox.showinfo(title='Create DB', message='Database created.')