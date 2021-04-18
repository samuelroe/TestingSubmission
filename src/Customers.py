from src.ReadCSVFile import ReadCSVFile

class Customers:
    readCSVFile = ReadCSVFile()
    def setReadCSVFile(self, reader):
        self.readCSVFile = reader

    def loadCustomers(self):

        customerData = self.readCSVFile.getFileData("customer.csv")
        return customerData

    def formatCustomers(self):
        display = ""
        customerData = self.loadCustomers()
        for counter in range(1,len(customerData)):
            display += customerData[counter][0] + " \n"
        return display
