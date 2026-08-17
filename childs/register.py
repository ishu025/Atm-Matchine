import phonenumbers
def register():
    name = input("Enter your name: ")
    phone = input("Enter phone number: ")
    number = phonenumbers.parse(phone, "IN")

    if phonenumbers.is_valid_number(number):
        print("Valid phone number")
    else:
        print("Invalid phone number")
        return

    pin = input("Create PIN: ")

    file = open("database/users.dat","r")
    data = file.readlines()
    file.close()

    for i in range(1, len(data), 4):
        if data[i].strip() == phone:
            print(
                "This Phone Number is already exist, Err !"
            )
            return

    balance = 200

    file = open("database/users.dat", "a")

    file.write(name + "\n")
    file.write(phone + "\n")
    file.write(pin + "\n")
    file.write(str(balance) + "\n")

    file.close()

    print("Registration successful!")
    print("You received ₹200.")