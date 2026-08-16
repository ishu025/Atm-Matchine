det = {
    "pin": 1234,
    "name": "Aryan Raj",
    "Accnumber": 1234567890,
    "CurrentMoney": 5000,
}
while True:
    print("***Mini-ATM***")
    acn = int(input(f"input the account number of your._"))
    if acn == det["Accnumber"]:
        pinn = int(input("Enter Your Pin;_"))
        if pinn == det["pin"]:
            print(f"Name : {det['name']}")
            print(f"Account Number : {det['Accnumber']}")
            print("**********")
            print("1 : check balance")
            print("2: withdraw money")
            print("3 : Exit")
            option = int(input("Enter : "))
            if option == 1:
                print(f"Your Current balance is : {det['CurrentMoney']}")
            elif option == 2:
                Another_account_number = int(
                    input("Enter the Account number:")
                )
                Transfer_ammount = int(input("Enter transfer ammount: "))
                if det["CurrentMoney"] >= Transfer_ammount:
                    det["CurrentMoney"] -= Transfer_ammount
                    print(f"Money transfer ammmount {Transfer_ammount} to {Another_account_number} sucessfully")
                elif  det["CurrentMoney"] < Transfer_ammount:
                    print("Error! Not enough money to reansfer")
                    print("Check Your balance")
            else:
                print("You exitex sucessfully")
        else:
            print("Error! incorrect pin")
    else:
        print("incorrect Account number")
        print("acccess denied!!")