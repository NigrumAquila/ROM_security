from tkinter import messagebox
import tkinter as tk
from core.helpers.fileHelpers import readDB, getTimeOfCreationAndModification
from core.styles.colors import printTextAndValue


DB, pathToDB = readDB()
creationTime, modificationTime = getTimeOfCreationAndModification(pathToDB)


def on_close():
    DB_info_window.destroy()

DB_info_window = tk.Toplevel()
DB_info_window.title('DB info')

text = tk.Text(DB_info_window, width=100, height=25)
text.pack(side=tk.LEFT)

text.insert('1.0', 'Created: ' + creationTime + '\n')
text.insert('2.0', 'Last modified: ' + modificationTime + '\n')

scroll = tk.Scrollbar(DB_info_window, command=text.yview)
scroll.pack(side=tk.LEFT, fill=tk.Y)
 
text.config(yscrollcommand=scroll.set)

for idx, line in enumerate(DB):
    text.insert('%s.0' % str(idx+3), line)

DB.close()

DB_info_window.protocol('WM_DELETE_WINDOW', on_close)