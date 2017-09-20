from gascore import *
from disk import *


def valid_pay():

    msg = """ How Will You Pay:
    \t1. Prepay
    \t2. Pay After
    """
    while True:
        payment = input(msg)
        if payment == '1' or payment == '2':
            return (payment)
        else:
            print('Error Try Again')


def addup(payment, code):
    if payment == '1':
        money = int(input('How Much You Buying?\n'))
        amount = add_prepay(money, code, menu)
    elif payment == '2':
        gallons = int(input('How Much Was Pumped?\n'))
        amount = add_payafter(code, menu, gallons)
    return amount


def user_main():
    payment = valid_pay()

    selection = """ Select Code Of Gas Type:
        \t1. Regular: 2.08
        \t2. Midgrade: 2.23
        \t3. Premium: 2.36
    """
    code = input(selection)

    amount = addup(payment, code)

    logit(code, amount, payment)

    inventory = load_inventory()

    message = write_message(inventory, code, amount)

    open_tank(message)


def admin_main():
    code = '1234'
    while True:
        password = input("What is the password?\n")
        if password == code:

            inventory = load_inventory()

            name = input("Hi What Is Your Name\n")

            print('Hello {} You Have Clearance\n'.format(name))

            decision = """ Admin Decisions
            \t1. Refill The Tanks
            \t2. Check The Revenue
            \t3. Open Log
            \t4. Look At Tanks
            """

            choice = input(decision)

            if choice.strip() == '1'.strip():
                message = refill(inventory)
                open_tank(message)
                read_tank()
                break

            elif choice.strip() == '2'.strip():
                text = open_log()
                print(revenue(text))
                break

            elif choice.strip() == '3'.strip():
                with open("log.txt", "r") as file:
                    print(file.read())
                    break

            elif choice.strip() == '4'.strip():
                with open("tank.txt", "r") as tanks:
                    print(tanks.read())
                    break

            else:
                print("Error we are starting over")
        else:
            print("Invalid Password!!\n")

    write_log(name, choice)


def main():
    while True:
        choice = input("Are you admin or user?\n").title()
        if choice == "Admin":
            admin_main()
            break
        elif choice == "User":
            user_main()
            break
        else:
            print("Invalid Choice!!!\n")


if __name__ == '__main__':
    main()