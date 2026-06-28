class Rectangle:
    def Area(self):
        self.w=12
        self.h=16
        A_rec=self.w*self.h
        print("area of the rectangle is:",A_rec)
    def Perimeter(self):
        P_rec=2*(self.w+self.h)
        print("perimeter of the rectangle is:",P_rec)
s=Rectangle()
s.Area()
s.Perimeter()     

class Person:
    def __init__(self,Name,Age):
        self.n=Name
        self.a=Age
        print("Welcome....")
        print()
    def intro(self):
        print(self.n)
        print(self.a)
Name=input("enter the name of the student:")
Age=int(input("enter the age:"))
d=Person(Name,Age)
d.intro()
        
    
    
