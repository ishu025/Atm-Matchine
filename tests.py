from getpass import getpass

# Account details
det = {
    "pin": 1234,
    "name": "Aryan Raj",
    "Accnumber": 1234567890,
    "CurrentMoney": 5000
}


def check_balance():
    print(f"\nYour current balance is: ₹{det['CurrentMoney']}")


def transfer_money():
    try:
        another_account = int(input("Enter target account number: "))

        if another_account == det["Accnumber"]:
            print("Error! You cannot transfer money to your own account.")
            return

        transfer_amount = int(input("Enter transfer amount: "))

        if transfer_amount <= 0:
            print("Error! Transfer amount must be greater than 0.")

        elif transfer_amount > det["CurrentMoney"]:
            print("Error! Insufficient funds.")
            print(f"Your balance is only: ₹{det['CurrentMoney']}")

        else:
            det["CurrentMoney"] -= transfer_amount

            print("\nTransaction Successful!")
            print(f"Amount transferred: ₹{transfer_amount}")
            print(f"Target account: {another_account}")
            print(f"Remaining balance: ₹{det['CurrentMoney']}")

    except ValueError:
        print("Error! Please enter numbers only.")


def atm():
    while True:
        print("\n" + "*" * 25)
        print("       MINI-ATM")
        print("*" * 25)

        try:
            acn = int(input("Enter your account number: "))
        except ValueError:
            print("Error! Account number must contain numbers only.")
            continue

        if acn != det["Accnumber"]:
            print("Incorrect Account Number. Access denied!")
            continue

        # Hidden PIN input
        try:
            pinn = int(getpass("Enter your PIN: "))
        except ValueError:
            print("Error! PIN must contain numbers only.")
            continue

        if pinn != det["pin"]:
            print("Error! Incorrect PIN.")
            continue

        print("\nLogin Successful!")
        print(f"Name           : {det['name']}")
        print(f"Account Number : {det['Accnumber']}")
        print("-" * 25)

        while True:
            print("\n1 : Check Balance")
            print("2 : Transfer Money")
            print("3 : Logout")
            print("4 : Exit")

            try:
                option = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice! Please enter a number.")
                continue

            if option == 1:
                check_balance()

            elif option == 2:
                transfer_money()

            elif option == 3:
                print("\nYou have been logged out successfully.")
                break

            elif option == 4:
                print("\nThank you for using Mini-ATM. Goodbye!")
                return

            else:
                print("Invalid option! Please select 1, 2, 3 or 4.")


# Start the ATM
atm()