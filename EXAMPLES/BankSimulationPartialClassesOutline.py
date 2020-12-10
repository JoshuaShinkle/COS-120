class account:
    def __init__(self,paccNumber,pamount):
        pass
    
class savings(account):
    def __init__(self,pintRate,paccNumber,pamount):
        pass
    
class checking(account):
    def __init__(self,pintRate,poverDraft,paccNumber,pamount):
        pass
    
class credit(account):
    def __init__(self,pintRate,paccNumber,pamount,pLimit):
        pass
    
class customer:
    def __init__(self,pname,paddr,pssn):
        self.pname = pname
        self.paddr = paddr
        self.pssn = pssn
        pass
    
class teller:
    def __init__(self,pname,paddr,pssn,ppayRate):
        pass
    
class bank:
    def __init__(self):
        self.bank = bank
        self.customers = customers
        
    def addCustomers(self, pname):
        self.customers.append(pname)
        pass
    
    def showCustomers(self, customers):
        return customers

    def findAccounts(self, pname):
        pass
    
#1) Declare a bank
#2) Declare 4 customers
#3) Add three of the customers to the bank
#4) Show all of the customers for the bank
#5) Display all accounts for a customer who exists
#6) Display all accounts for a customer who does not exist
#7) Add a checking and a savings account for one of the customers
#8) Now display all accounts for the customer with the accounts you just added
Sovereign=bank()
Bob=customer("Bob","123 Main","123-45-0000")
Sue=customer("Sue","124 Main","123-45-1111")
Joe=customer("Joe","125 Main","123-45-2222")
Jamie=customer("Jamie","126 Main","123-45-5678")
Sovereign.addCustomers(Bob)
Sovereign.addCustomers(Sue)
Sovereign.addCustomers(Joe)
print("Show Customers",Sovereign.showCustomers())
print("Find accounts for Bob",Sovereign.findAccounts(Bob))
print("Find accounts for Jamie",Sovereign.findAccounts(Jamie))
Bob.add_savings(1000)
Bob.add_checking(100,50)
print("Find accounts for Bob",Sovereign.findAccounts(Bob))
