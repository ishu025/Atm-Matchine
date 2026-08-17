def check(user_phone):

    file = open("database/users.dat", "r")
    data = file.readlines()
    file.close()

    for i in range(1, len(data), 4):

        if data[i].strip() == user_phone:

            balance = data[i + 2].strip()

            print(f"Your Current balance is ₹{balance}")
            return