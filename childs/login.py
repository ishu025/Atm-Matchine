def login():
    phone = input("Enter Your Phone number: ")
    pin = input("Enter Your Pin: ")

    file = open("database/users.dat", "r")
    data = file.readlines()
    file.close()

    for i in range(1, len(data), 4):
        if data[i].strip() == phone and data[i + 1].strip() == pin:
            print("Login successful")
            return phone

    print("Wrong phone or password! Try again.")
    return False