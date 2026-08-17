from childs.welcome import welcome
from childs.register import register
from childs.login import login
from childs.atm.atm import atm
while True:
    welcome()

    choice = int(input(
        "Enter Your Choice: __"
    ))
    if choice == 1:
        register()
    elif choice  == 2:
        if login():
            atm()
    elif choice == 3:
        break
    else:
        print(
           "Err ! invalid input" 
        )
        continue