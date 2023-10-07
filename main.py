from Abstract_Bank_Accounts import Absract_Bank_Accounts
from BalanceException import BalanceException
from BankAccounts import BankAccounts
from CreateMainAccount import CreateMainAccount
from CreateSavingsAccount import CreateSavingsAccount
from SavingsAcct import SavingsAcct

def main():
    print("\nWelcome to the ATM Simulator\n")
    
    while True:
        print("\nOptions:")
        print("1. Create Main Account")
        print("2. Main Account Check Balance")
        print("3. Deposit to Main Account ")
        print("4. Withdraw from Main Account")
        print("5. Transfer from Main Account to Savings Account")
        print("6. Create Savings Account")
        print("7. Savings Account Check Balance")
        print("8. Deposit to Savings Account")
        print("9. Withdraw from Savings Account")
        print("10.Transfer from Savings Account to Main Account ")
        print("11. Quit")

        choice = input("\nEnter your choice (1/2/3/4/5/6/7/8/9/10/11): ")

        if choice == '1':
            main_account = CreateMainAccount()
        elif choice == '2':
            if 'main_account' not in locals():
                print("Create the main account first!")
            else:
                main_account.getBalance()
        elif choice == '3':
            if 'main_account' not in locals():
                print("Create the main account first!")
            else:
                amount = float(input("\nInput the amount to deposit : $"))
                main_account.deposit(amount)
        elif choice == '4':
            if 'main_account' not in locals():
                print("\nCreate Main Account First!")
            else:
                amount = float(input('\nInput Amount to Withdraw : $'))
                main_account.withdraw(amount)
        elif choice == '5':
            if 'main_account' not in locals():
                print("\nPlease Create main_account first")
            elif 'saving_account' not in locals():
                print("\nPlease Create saving account first")
            else:
                account_name = input("Please input the account Name : ")
                amount = float(input('\nInput Amount to Transfer : $')) 
                if account_name == saving_account.name:
                    main_account.transfer(amount,saving_account)
                else:
                    print(f"Please create account {account_name} first")

        elif choice == '6':
            saving_account = CreateSavingsAccount()

        elif choice == '7':
            if 'saving_account' not in locals():
                print("Please create saving accounts first")
            else:
                saving_account.getBalance()
        elif choice == '8':
            if 'saving_account' not in locals():
                print("Please create saving accounts first")
            else:
                deposit_amount = float(input('Please input the amount to deposit to saving accounts : $'))
                saving_account.deposit(deposit_amount)
        
        elif choice == '9':
            if 'saving_account' not in locals():
                print("Please create Saving Accounts First")
            else:
                withdrawn_deposit = float(input("Please Input the amount to withdraw to saving accounts : $"))
                saving_account.withdraw(withdrawn_deposit)
        elif choice == '10':
            if 'saving_account' not in locals():
                print("Please create Saving Accounts First")
            else:
                account_name = input("Please input the account Name : ")
                amount = float(input('Please input the amount to transfer to main account : $'))
                if 'main_account' not in locals():
                    print(f"Please Create {account_name} as main account  First")
                else:
                    if account_name == main_account.name:
                        saving_account.transfer(amount,main_account)
                    else:
                        pass

        elif choice == '11':
            print("Thank you for using ATM Simulator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
