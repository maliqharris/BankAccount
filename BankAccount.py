class BankAccount:
    
    def __init__(self, int_rate, balance): 
       self.int_rate = int_rate
       self.balance = balance
    def deposit(self, amount):
        # if BankAccount.can_deposit(self.balance, amount):
        self.balance = self.balance + amount
        # else:
            # print("Still Negative")
        return self
    # @staticmethod
    # def can_deposit(balance, amount):
    #     if(balance + amount) < 0:
    #         return False
    #     else:
    #         return True
    def withdraw(self, amount):
        # if BankAccount.can_withdraw(self.balance,amount):
        self.balance = self.balance - amount
        # else:
            # print("insufficient Funds")
        return self
    # @staticmethod
    # def can_withdraw(balance, amount):
    #     if (balance - amount) < 0:
    #         return False
    #     else:
    #         return True
    def display_account_info(self):
        print("Interest Rate:",self.int_rate)
        print("Balance:",self.balance)
        
    def yield_interest(self):
        self.balance = self.balance - (self.balance * self.int_rate)
        return self
Account1 = BankAccount(.05, 100)
Account2 = BankAccount(.07, 5)
# Account1.deposit(10).deposit(10).deposit(10).withdraw(10).display_account_info()
Account2.deposit(100).deposit(100).withdraw(20).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_account_info()