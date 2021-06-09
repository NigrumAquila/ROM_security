from core.constants.interfaceConstants import GUI_ACTION_MODULE_SPACE
from core.helpers.format import formatActionSpaceToUnderscore
from core.removers.removeModule import removeModule
import inspect



def invoke_action(action):
    action = formatActionSpaceToUnderscore(action['text'])
    
    __import__(GUI_ACTION_MODULE_SPACE + action)
    removeModule(GUI_ACTION_MODULE_SPACE + action)