from abc import ABC

class Load(ABC):

    def getFileData(self, fileName):
        pass

    def getLastLines(self, fileName, numerOfLines):
        pass

