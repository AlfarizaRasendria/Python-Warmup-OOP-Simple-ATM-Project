class Absract_Bank_Accounts:
    def __init__(self,name,Amount):
        self.name = name
        self.balance = Amount
    
    def getBalance(self):
        pass

    def deposit(self,amount):
        pass

    def viableTransaction(self,amount):
        pass

    def withdraw(self,amount):
        pass

    def transfer(self,amount,account):
        pass
