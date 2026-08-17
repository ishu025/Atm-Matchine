from childs.atm.check import check
from childs.atm.transfer import transfer
def atm():
    print("\n=== ATM ===")
    print("1. Check Balance")
    print("2. Transfer Money")
    print("3. Exit")
    choice = input("Choice: ")
    if choice == "1":
        print("Balance check")
        check()
    elif choice == "2":
        print("Money transfer")
        transfer()
    elif choice == "3":
        print("Exit ATM")

atm()