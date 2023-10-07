from SavingsAcct import SavingsAcct

def CreateSavingsAccount():
    account_name = input("Enter a name for Savings Account: ")
    initial_balance = float(input("Enter initial balance for Savings Account: $"))
    interest_rate = float(input("Enter the annual interest rate for Savings Account (e.g., 0.05 for 5%): "))
    Saving_Account = SavingsAcct(account_name,initial_balance, interest_rate)
    return Saving_Account