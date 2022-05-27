class Account:
    def __init__(self,accountname,accountnumber,balance,amount):
        self.accountname=accountname
        self.accountnumber=accountnumber
        self.amount=amount
        self.balance=balance
       
    def deposite(self):
       self.balance+=self.amount
       return f"hello you deposited {self.balance}"
    def withdwal(self):
      self.balance-=self.amount
      return f"hello your withdrwal is {self.balance}"


        



        