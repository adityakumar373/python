class Account:
    def __init__(self,acc,balance):
        self.acc=acc
        self.balance=balance
    def debit(self,amt):
        if(self.balance>=amt):
         self.balance-=amt
         print("Rs.",amt,"is debited")
        else:
         print("Not sufficient amount in account")
    def credit(self,amt):
        if(amt>0):
            self.balance+=amt
            print("Rs.",amt,"is credited")
        else:
            print("not an appropriate amount")        
    def showbalance(self):
        print("total balance in",self.acc,"account is:",self.balance)        
acc1=Account(123543412,5000)
acc1.showbalance()
acc1.debit(3000)
acc1.credit(38000)
acc1.showbalance()        