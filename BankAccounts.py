from BalanceException import BalanceException
from Abstract_Bank_Accounts import Absract_Bank_Accounts
from AccountException import AccountException

class BankAccounts(Absract_Bank_Accounts):
    def __init__(self,name,Amount):
        super().__init__(name,Amount)
        print(f"\nAccount {self.name} successfully created")
    
    def getBalance(self):
        print(f"\nAccount {self.name} Balance = ${self.balance:.2f}")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete.")

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return 
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}\nThe cost including fee of your transfer is ${amount + self.fee:.2f}")
    
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdrawn complete.")
            self.getBalance()
        except BalanceException as Error:
            print(f"\nWithdraw interrupted: {Error}")

    # def CheckAccount(self,account):
    #     if account not in locals():
    #         raise AccountException(f"Account {account} is not available. Please Create that Account First")
    #     else:
    #         return

    def transfer(self,amount,account):
        try:
            print('\n******\n\nBeginning Transfer.. 🚀')
            self.viableTransaction(amount)
            # self.CheckAccount(account)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!\n")
        except BalanceException as BalanceError:
            print(f'\nTransfer interrupted. {BalanceError}')
        