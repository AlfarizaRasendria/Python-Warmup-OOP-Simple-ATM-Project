from BankAccounts import BankAccounts
from BalanceException import BalanceException

class FeeAccount(BankAccounts):
    def __init__(self,name,Amount):
        super().__init__(name,Amount)
        self.fee = 5

    def withdraw(self, amount):
       try:
           self.viableTransaction(amount + self.fee)
           self.balance -= (amount + self.fee)
           print("\nWithdraw completed.")
           self.getBalance()
           return True
       except BalanceException as Error:
           print(f'\nWithdraw interrupted: {Error}') 
           return False
    

    def transfer(self,amount,account):
        try:
            print('\n******\n\nBeginning Transfer.. 🚀')
            self.viableTransaction(amount)
            # self.CheckAccount(account)
            Withdraw_Status = self.withdraw(amount)
            if Withdraw_Status == True:
                account.deposit(amount)
                print("\nTransfer complete!\n")
            else:
                print("\nTransfer Failed!\n")

        except BalanceException as BalanceError:
            print(f'\nTransfer interrupted. {BalanceError}')