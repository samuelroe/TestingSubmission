import unittest
from src.ReadCSVFile import ReadCSVFile
from src.Customers import Customers
from src.Stub.loadStub import LoadStub
from unittest.mock import MagicMock
class LoadFileTest(unittest.TestCase):



    def test_FirstItem(self):
        readCSVFile = ReadCSVFile()
        self.assertEqual("emailAddress", readCSVFile.getFileData("customer.csv")[0][0])
    def test_loadCustomers(self):
        customers = Customers()
        self.assertEqual("emailAddress", customers.loadCustomers()[0][0])
    def test_lastLine(self):
        readCSVFile = ReadCSVFile()
        self.assertEqual(["e.kelly.1@research.gla.ac.uk","Ethan","Kelly","9876"], readCSVFile.getLastLines("customer.csv", 1))
    def test_cutomersformat(self):
        customers = Customers()
        self.assertEqual("derek.somerville@glasgow.ac.uk ", customers.formatCustomers().split("\n")[0])



    def test_loadCustomersStub(self):
        customers = Customers()
        customers.setReadCSVFile(LoadStub())
        self.assertEqual("Samuel", customers.loadCustomers()[0][0])



    def test_LastLineMock(self):
        readCSVFile = ReadCSVFile()
        propertydata = []
        propertydata.append("emailAddress, firstName, lastName, password")
        propertydata.append("test1:testemail, testfirst, testlast, testpassword")
        propertydata.append("test2:testemail2, testfirst2, testlast2, testpassword2")
        readCSVFile.getFileData = MagicMock(return_value = propertydata)
        self.assertEqual("test2:testemail2, testfirst2, testlast2, testpassword2", readCSVFile.getLastLines("customer.csv", 1))



