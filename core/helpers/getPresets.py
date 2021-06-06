from core.styles.colors import typedText


def getPresets():

    presets = typedText('Enter drive names separated by commas: ')
    presets = presets.split(',')

    for index, preset in enumerate(presets):
        presets[index] = preset.upper() + ':'
    
    # print('Не нужно проверять: ' + ' '.join([str(item) for item in presets]))
    return presets