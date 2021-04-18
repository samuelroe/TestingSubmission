from src.Customers import Customers
class LogIn:
    def getPassword(self,emailAddress):
        customers = Customers()
        customerData = customers.loadCustomers()
        password = ""
        counter = 0
        while password == "" and counter < len(customerData):
            if emailAddress == customerData[counter][0]:
                password = customerData[counter][3]
            counter += 1
        return password

    def logIn(self):
        emailAddress = input("Enter your email address")
        password = self.getPassword(emailAddress)
        if password == "":
            print("You are not a user")
        else:
            if input("Enter password") == password:
                print("You are logged in")
            else:
                print("Wrong password, no second chances")
