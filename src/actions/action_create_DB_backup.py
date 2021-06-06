from core.helpers.fileHelpers import copyDB
from tqdm import tqdm as Bar
from core.styles.colors import printText


srcFile, dstFile = copyDB()

with Bar(total=len(srcFile.read())) as bar:
    srcFile.seek(0)
    while True:
        char = srcFile.read(1)
        if not char: break
        dstFile.write(char)
        bar.update()
    srcFile.close(); dstFile.close()

printText('Backup is done.')