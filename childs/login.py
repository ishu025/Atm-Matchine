def login():
    phone = int(
        input(
            "Enter Your Phone number"
        )
    )
    pin = int(
        input(
            "Enter Your Pin:__"
        )
    )
    if phone == 8986119935 and pin == 2008 :
        print(
            "Login sucessfull"
        )
        return True
    else:
        print(
            "Wrong phone or passowrd! Try again."
        )
        return False