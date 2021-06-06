from os import stat
from datetime import datetime
from os.path import exists


def log(message, file_path):

    log_file = None
    if exists(file_path):
        log_file = open(file_path, 'a')
        if stat(file_path).st_size > 0:
            log_file.write('\n')
    else:
        log_file = open(file_path, 'w')

    incident = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    log_file.write(message + ': ' + incident)
    log_file.close()