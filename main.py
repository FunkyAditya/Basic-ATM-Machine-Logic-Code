import time


print("Welcome To KalaDhan Bank \n")

time.sleep(0.5)

cardnumber = int(input("Enter Card Number : "))
right = 123456789
balance = 100

if cardnumber == right:
    pin = int(input("Enter Pin : "))
    if pin == 4321:
        print("Welcome Aditya Prakash \n")
        options =  int(input("Select \n * 1) WithDrawal \n * 2) Check Balance \n * 3) Logout \n"))
        if options == 1:
            amount = int(input("Enter Ammount For Withdrawal : $"))
            if amount > balance:
                    print("Gareeb Gamdu")
                    time.sleep(0.5)
            elif balance >= amount:
                    print("Processing...\n Successful")
                    print("Thanks For Using Our Services")
                    time.sleep(0.5)
            else:
                    print("Enter Valid Value")
        elif options == 2:
                print("$" + str(balance))
                print("Thanks For Using Our Services")
                time.sleep(0.5)
        else:
                print("Logout Successful")
                print("Thanks For Using Our Services")
                time.sleep(0.5)

else:
    print("Wrong Card Number")

time.sleep(1)





