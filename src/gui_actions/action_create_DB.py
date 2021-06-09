from tkinter import messagebox
from core.helpers.fileHelpers import addDB


addDB()

messagebox.showinfo(title='Create DB', message='Database created.')