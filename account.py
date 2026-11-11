def manage_account():
    print("Welcome to Banking Application")

    balance = 1500
    minimum_balance = 1000

    if balance >= minimum_balance:
        print("Minimum balance maintained")
    else:
        print("Minimum balance not maintained")

manage_account()