class account:

    def __init__(self,):
        self.balance=1000
        self.ac=0

    def set(self):
        r = input("Enter your account number : ")
        self.ac=r

    def get(self):
        print self.ac
        print self.balance

    def retAc(self):
        return self.ac

    def withdraw(self,amt):
        if amt > self.balance:
            print("Insufficient Balance")
        self.balance=self.balance-amt

    def deposit(self,amt):
        self.balance = self.balance + amt

    def transfer(self, amt, x):
        if self.ac == x.ac:
            print "\nSender and beneficiary account numbers cannot be the same"
            return
        if amt > x.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - amt
            x.balance = x.balance + amt
            print "\nCurrent balance is %d and amount transfered is %d " %(self.balance,amt)
        #return x.check_bal()

    def check_bal(self):
        print(self.balance)

A=account()
B=account()
C=account()
D=account()

A.set()
B.set()
C.set()
D.set()

data = {'1111': b1 , '2222': b2, '3333': b3}

def check(ac):
    if ac == A.retAc():
        return A
    if ac == B.retAc():
        return B
    if ac == C.retAc():
        return C
    if ac == D.retAc():
        return D
#print type(list[0])
loop='Y'

while loop=='y'or loop=='Y':
    n=input('\nEnter your account number to do banking : ')

    #n=raw_input("Enter the acc")
    c=check(n)

    print '*' * 18
    print('1. WITHDRAW MONEY')
    print('2. DEPOSIT MONEY')
    print('3. TRANSFER MONEY')
    print('4. VIEW BALANCE')
    print '*' * 18

    ch=int(input('Enter your choice'))
    if ch==1:
        amt=input('Enter the amount to be withdrawn : ')
        c.withdraw(amt)
    elif ch==2:
        amt=input('Enter the amount to be deposited : ')
        c.deposit(amt)
    elif ch==3:
        amt=input('Enter the amount to be transfered : ')
        ben=input('Enter the beneficiory acct no : ')
        ben_check=check(ben)
        c.transfer(amt,ben_check)
    else:
        c.check_bal()
    loop=raw_input("Would you like to do another transaction? press Y ")