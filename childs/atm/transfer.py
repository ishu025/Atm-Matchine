def transfer(user_phone):
    print("\n=== MONEY TRANSFER ===")

    receiver_phone = input("Enter receiver phone number: ")
    transfer_amount = int(input("Enter transfer amount: "))

    if transfer_amount <= 0:
        print("Transfer amount must be greater than 0!")
        return

    file = open("database/users.dat", "r")
    data = file.readlines()
    file.close()

    sender_balance = None
    receiver_balance = None

    sender_index = None
    receiver_index = None

    for i in range(1, len(data), 4):

        if data[i].strip() == user_phone:
            sender_balance = int(data[i + 2].strip())
            sender_index = i

        if data[i].strip() == receiver_phone:
            receiver_balance = int(data[i + 2].strip())
            receiver_index = i

    if receiver_balance is None:
        print("Receiver does not exist!")
        return

    if transfer_amount > sender_balance:
        print("Insufficient balance!")
        return

    sender_balance -= transfer_amount
    receiver_balance += transfer_amount

    data[sender_index + 2] = str(sender_balance) + "\n"
    data[receiver_index + 2] = str(receiver_balance) + "\n"

    file = open("database/users.dat", "w")
    file.writelines(data)
    file.close()

    print("Transfer successful!")
    print(f"Transferred ₹{transfer_amount}")
    print(f"Your new balance is ₹{sender_balance}")