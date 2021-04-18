from src.Stub.Load import Load

class LoadStub(Load):
    def getFileData(self, fileName):
        result = []
        result.append(["Samuel","Roe"])
        return result

    def getLastLines(self, fileName, numerOfLines):
        pass