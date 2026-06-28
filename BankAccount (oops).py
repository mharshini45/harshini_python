class BankAccount:
    def __init__(self,Account_no, Name,Balance):
        self.a=Account_no
        self.n=Name
        self.b=Balance
        print("Welcome to the bank")
        print("check the details mentioned below")
        print()
    def Deposit(self):
        print("-------DEPOSIT------")
        print("The details.....")
        print("\n-----ACCOUNT DETAILS-----")
        print("Account_no:",self.a)
        print("Name:",self.n)
        g=input("is that the mentioned account details are right (Y/N):")
        if g=='Y':
            c=int(input("enter the amount of deposit:"))
            self.b=self.b+c
            print("Amount that has been deposited is:",self.b)
        else:
            print("visit the head office for doing the deposit ")
    def Withdrawl(self):
        print("-------WITHDRAW-------")
        print("The details of the accountent.....")
        print("\n-----ACCOUNT DETAILS-----")
        print("Account_no",self.a)
        print("Name:",self.n)
        v=input("is that the mentioned account details are right (Y/N):")
        if v=='Y':
            d=int(input("enter the amount of withdrawl:"))
            self.b=self.b-d
            print("Amount of withdrawl is:",self.b)
        else:
            print("visit the head office for doing the withdrawl")
    def Bank_fee(self):
        print("bank fee on deposit or on withdraw is:",self.b*5/100)
    def display(self):
        print("\n-----ACCOUNT DETAILS-----")
        print("ACCOUNT_NO:",self.a)
        print("NAME:",self.n)
        print("BALANCE:",self.b)
        print("your transactions have been done successfully")
        print("Thank you for visiting our bank")
s=BankAccount(2345678,'Harshini',25000)
s.Deposit()
s.Withdrawl()
s.Bank_fee()
s.display()
        
    
    
        
        
    
