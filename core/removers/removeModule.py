def removeModule(moduleName): del getattr(__import__('sys'), 'modules')[moduleName]
