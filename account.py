def manage_account():
    print("Welcome to Banking Application")

    balance = 1500
    minimum_balance = 1000

    if balance >= minimum_balance:
        print("Minimum balance maintained")
    else:
        print("Minimum balance not maintained")

    withdrawal = 200

    if balance - withdrawal >= minimum_balance:
        balance = balance - withdrawal
        print("Withdrawal successful")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance or minimum balance violation")

manage_account()