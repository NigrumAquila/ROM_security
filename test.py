from tkinter import filedialog, Tk

if not 'root' in locals(): 
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()

file_path = filedialog.asksaveasfilename()
# file = open(file_path, 'w')
open(file_path, 'w').close()
# file.close()