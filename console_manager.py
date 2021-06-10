import core.encoding.toUTF8
from core.constants.actionConstants import ACTION_choice
from core.constants.interfaceConstants import EXIT, ACTION_MODULE_SPACE
from core.helpers.dictionaryHelpers import dictionaryKeyParser, dictionaryGetValueKeySeparated
from core.removers.removeModule import removeModule
from core.styles.colors import warning, end


while True:
    case = input('Select action: ' + dictionaryGetValueKeySeparated(ACTION_choice) + '; e - EXIT: ').lower()
    for action in ACTION_choice.keys():
        if case == ACTION_choice[action]:
            __import__(ACTION_MODULE_SPACE + dictionaryKeyParser(ACTION_choice, case))
            removeModule(ACTION_MODULE_SPACE + dictionaryKeyParser(ACTION_choice, case))
    
    if case == EXIT:
        end('Execution completed.')

    elif case not in ACTION_choice.values():
        warning('Select action.')