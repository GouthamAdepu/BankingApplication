def manage_account():
    print("Welcome to Banking Application")

    balance = 1500
    withdrawal = 200

    if balance >= withdrawal:
        balance = balance - withdrawal
        print("Withdrawal successful")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")

manage_account()