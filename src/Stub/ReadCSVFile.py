import csv
from src.Stub.Load import Load
class ReadCSVFile(Load):

    def getFileData(self,fileName):
        fileData = []
        with open("resource/" + fileName, 'rt')as dataFile:
            fileReader = csv.reader(dataFile)
            for row in fileReader:
                fileData.append(row)
        return fileData

    def getLastLines(self, fileName, numerOfLines):
        return self.getFileData(fileName)[-1 * numerOfLines]
