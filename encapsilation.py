class Protected:
    def __init__(self):
        self._protectedVar = 0
        
obj = Protected()
obj._protectedVar = 24
print(obj._protectedVar)

class Protected:

    def __init__(self):
        self._privateVar = 111

    def getPrivate(self):
        print(self._privateVar)

    def setPrivate(self, private):
        self._privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(1998)
obj.getPrivate()
