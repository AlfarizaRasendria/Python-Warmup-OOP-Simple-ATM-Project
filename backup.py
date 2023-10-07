"""  elif choice == '2':
            amount = float(input("\nEnter the amount to deposit: $"))
            account1.deposit(amount)
        elif choice == '3':
            amount = float(input("\nEnter the amount to withdraw: $"))
            account1.withdraw(amount)
        elif choice == '4':
            if 'account2' not in locals():
                print("Create the second account before transferring funds.")
            else:
                amount = float(input("\nEnter the amount to transfer: $"))
                account1.transfer(amount, account2)
        elif choice == '5':
            account2 = CreateSavingsAccount()
        elif choice == '6':
            if 'account2' not in locals():
                print("Create the Savings account first before depositing to Savings Account.")
            else:
                if isinstance(account2, SavingsAcct):
                    amount = float(input("\nEnter the amount to deposit to Savings Account: $"))
                    account2.deposit(amount)
                    print("Interest added to Savings Account.")
                else:
                    print("Account 2 is not a Savings Account.") """