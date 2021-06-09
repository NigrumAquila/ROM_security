from os import stat
from os.path import splitext, getctime, getmtime, exists
from time import ctime


def writeLog():
    file_path = __pickFile(ask='saveas', title='Select log file')

    if not exists(file_path):
        if file_path[-4:] != '.log':
            file_path = file_path + '.log'
        open(file_path, 'w').close()


    filename, file_extension = splitext(file_path)
    if file_extension != '.log':
        file_path = filename + file_extension + '.log'
    
    return file_path


def writeROM():
    ROM_directory = __pickFile(ask='directory', title='Select root folder of ROM')
    ROM_file_path = ROM_directory + '/' + 'ROM_security'
    ROM_file = None

    if exists(ROM_file_path):
        ROM_file = open(ROM_file_path, 'a')
        if stat(ROM_file_path).st_size > 0:
            ROM_file.write('\n')
    else: ROM_file = open(ROM_file_path, 'w')

    return ROM_file


def writeDB(path=''):
    if path == '': path = __pickFile(ask='openfilename', title='Select DB')
    if path == '': raise Exception('File not selected.')

    filename, file_extension = splitext(path)
    while file_extension != '.db':
        path = __pickFile(title='Wrong file selected. Please select a file with extension ".db".', ask='openfilename')
        filename, file_extension = splitext(path)
        if path == '': raise Exception('File not selected.')

    file = open(path, 'a')
    
    if stat(path).st_size > 0:
        file.write('\n')
    
    return file, path


def readDB(path=''):
    if path == '': path = __pickFile(ask='openfilename', title='Select DB')
    if path == '': raise Exception('File not selected.')

    filename, file_extension = splitext(path)
    while file_extension != '.db':
        path = __pickFile(title='Wrong file selected. Please select a file with extension ".db".', ask='openfilename')
        filename, file_extension = splitext(path)
        if path == '': raise Exception('File not selected.')

    file = open(path, 'r')
    return file, path 


def addDB(path=''):
    if path == '': path = __pickFile(ask='saveas')
    if path == '': raise Exception('File not selected.')
    
    filename, file_extension = splitext(path)
    if file_extension != '.db':
        path = filename + file_extension + '.db'

    open(path, 'a').close()


def copyDB(path=''):
    if path == '': path = __pickFile(ask='openfilename', title='Select DB')
    if path == '': raise Exception('File not selected.')
    
    filename, file_extension = splitext(path)
    while file_extension != '.db':
        path = __pickFile(title='Wrong file selected. Please select a file with extension ".db".', ask='openfilename')
        filename, file_extension = splitext(path)
        if path == '': raise Exception('File not selected.')

    pathDstFile = __pickFile(title='Save as', ask='saveas')
    if pathDstFile == '': raise Exception('File not selected.')

    filename, file_extension = splitext(pathDstFile)
    if file_extension != '.db':
        pathDstFile = filename + file_extension + '.db'
    srcFile = open(path, 'rb'); dstFile = open(pathDstFile, 'wb')
    return srcFile, dstFile


def getTimeOfCreationAndModification(path=''):
    if path == '': path = __pickFile(ask='openfilename')
    if path == '': raise Exception('File not selected.')

    creationTime = ctime(getctime(path))
    modificationTime = ctime(getmtime(path))
    return creationTime, modificationTime


def __pickFile(title='Open', ask=''):
    from tkinter import filedialog, Tk

    if not 'root' in locals(): 
        root = Tk()
        root.attributes("-topmost", True)
        root.withdraw()

    if ask == 'saveas': 
        if title == 'Open': title = 'Save as'
        ask = filedialog.asksaveasfilename(title=title)
    elif ask == 'openfilename': 
        if title == 'Open': title = 'Open file'
        ask = filedialog.askopenfilename(title=title)
    elif ask == 'directory':
        if title == 'Open': title = 'Select directory'
        ask = filedialog.askdirectory(title=title)
    
    return ask