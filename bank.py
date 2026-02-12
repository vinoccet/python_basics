class Bank:
    ACCOUNT_COUNT=0
    def __init__(self,account):
        self.account=account
        self.__balance=0
        Bank.ACCOUNT_COUNT+=1

    def deposit(self, amount):
        if amount > 0:
            self.__balance+=amount
            print(f"amount deposited {self.__balance}")
        else:
            print("invalid amount provide positive value")    

    def withdraw(self,amount_to_withdraw):
        if amount_to_withdraw >0 and amount_to_withdraw<self.__balance:
            self.__balance-=amount_to_withdraw
            print(f"balance after withdrawal {self.__balance}")
        else:
            raise AttributeError(f"check your balance before withdraw {self.__balance}")    
    @staticmethod
    def is_valid_interest_rate(interest_rate):
        return interest_rate>0 and interest_rate<5

bank1=Bank("A001")
bank2=Bank("B001")
bank1.deposit(100)
bank1.withdraw(90)
print(bank1.ACCOUNT_COUNT)
print(Bank.is_valid_interest_rate(2))