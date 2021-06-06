from core.helpers.fileHelpers import readDB


def getApprovedIdentificators():
    approvedIdentificators = []
    
    DB, pathToDB = readDB()
    for line in DB:
        leftSeparator = line.find("'")
        rightSeparator = line.find("'", leftSeparator + 1)
        approvedIdentificators.append(line[leftSeparator + 1: rightSeparator])
    
    return approvedIdentificators