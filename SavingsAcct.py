from FeeAccount import FeeAccount
from BalanceException import BalanceException

class SavingsAcct(FeeAccount):
    def __init__(self, name,Amount,  interestRate):
        super().__init__(name,Amount)
        self.interestRate = interestRate
    
    def calculateInterest(self):
       AmountAfterInterest = self.balance * self.interestRate
       return AmountAfterInterest
    
    def deposit(self, amount):
        AmountAfterInterest = self.calculateInterest()
        amount = amount + AmountAfterInterest
        self.balance += amount
        print("\nDeposit completed.")

   