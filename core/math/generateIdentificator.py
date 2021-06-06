from random import randint


def generateIdentificator():
    number = randint(2**255, 2**256)
    hexNumber = hex(number)
    ROM_identificator = hexNumber[1:]
    return ROM_identificator