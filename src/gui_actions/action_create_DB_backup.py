from tkinter import messagebox
from core.helpers.fileHelpers import copyDB
from tqdm import tqdm as Bar
from core.styles.colors import printText


srcFile, dstFile = copyDB()

while True:
    char = srcFile.read(1)
    if not char: break
    dstFile.write(char)
srcFile.close(); dstFile.close()

messagebox.showinfo(title='Backup DB', message='Backup is done.')