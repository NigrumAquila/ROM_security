import subprocess

def removeDevice(driveLetter):
    subprocess.call('mountvol ' + driveLetter + ' /p')

    
# subprocess.call('mountvol ' + driveLetter +':' + ' /p')
# subprocess.call(['runas', '/user:Asus', 'mountvol D: /p'])
# subprocess.Popen('print "a" ', shell=True, stdout=subprocess.PIPE)