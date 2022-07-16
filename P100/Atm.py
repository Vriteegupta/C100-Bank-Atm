class Atm:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def check_balance(self):
        print("Your Account Balance Is 50000")

    def withdraw(self, amount):
        new_amount = 50000-amount
        print("You Have Withdrawn Rs."+str(amount)+". Your Remaining Balance is Rs."+str(new_amount))

def main():
    card = input("Enter Your Card Number:")
    pin = input("Enter Your Pin Number:")

    new_user = Atm(card, pin)

    print("Choose Your Activity")
    print("1. Balance enquiry 2. Cash withdrawal")

    activity = int(input("Enter Your Activity Number:"))

    if(activity == 1):
        new_user.check_balance()

    elif(activity == 2):
        amount = int(input("Enter The Amount That You Would Wish To Withdraw:"))
        new_user.withdraw(amount)
    
    else:
        print("Enter A Valid Number")

main()