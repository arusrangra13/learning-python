class Acount:
    def __init__(self,bal,accno):
        self.balance=bal
        self.accno=accno
        # debited method
    def debit(self,amount):
        self.balance -=amount
        print("Rs.",amount,"was debited")
        print("total balance = ",self.get_balance())

            # credit method
    def credet(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Acount(10000,232323)
acc1.debit(1000)
acc1.credet(5000)       
