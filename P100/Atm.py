class Atm:
    def init(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    
    def CashWithDrawl(self):
        print("Login Accepted, WithDrawl Authorised")
    
    def BalanceEnquiry(self):
        print("Login Accepted, Details Below")
    
    def error(self):
        print("Details Incorrect, Please try again")