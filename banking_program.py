balance = 0


def show_balance():
    print(f"your bank balance is: {balance}")


def deposit():
    global balance
    money = int(input("enter the amount that you want to deposit:"))
    if money < 0:
        print("Deposit a value higher than 0")
    else:
        balance = balance + money
        print(f"Your amount of {money} is deposited in your account")


def withdraw():
    global balance
    money = int(input("enter the amount of money that you want to withdraw:"))
    if money > balance:
        print("you cannot withdraw an amount which exceeds your bank balance")
    elif money <= 0:
        print("money lower than 0 cannot be withdrawn from the account")
    else:
        balance = balance-money
        print(f"Rs. {money} is withdrawn from your account")


while True:
    print("--------THIS IS A BANKING PROGRAM--------")
    print("enter your choice:\n")
    choice = int(input(
        " 1: Deposit Money\n 2: Withdraw Money\n 3: Display Bank Balance\n 4: Exit\n"))
    match choice:
        case 1:
            deposit()
        case 2:
            withdraw()
        case 3:
            show_balance()
        case 4:
            print("Thank you! Have a nice day....")
            break
