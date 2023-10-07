from BankAccounts import BankAccounts

def CreateMainAccount():
    mainAccount_Name = input("Enter a username for Main Account: ")
    main_Account_initial_balance = float(input("Enter initial balance for Main Account: $"))
    main_account = BankAccounts(mainAccount_Name,main_Account_initial_balance)
    return(main_account)
