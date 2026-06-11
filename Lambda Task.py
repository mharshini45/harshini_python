'''#to find squ of a num
squ=lambda a:a**2
print(squ(2))

#to check even or odd
even_odd=lambda n:"even" if n%2==0 else "odd"
n=int(input("enter the num"))
print(even_odd(n))

#to find max of two num:
max_two=lambda a,b:"a is max" if a>b else "b is max"
a=int(input("enter the num:"))
b=int(input("enter the num:"))
print(max_two(a,b))

#to calculate the cube:
cube_num=lambda a:a**3
print(cube_num(3))

#to check pos or neg:
pos_neg=lambda s:"positive" if s>0 else "negative"
print(pos_neg(-2))

#to add two num
s=lambda a,b:a+b
print(s(2,3))

#sort string of tuple:
sort_string=lambda n:sorted(n)
n=("python","java","c++","harshu")
print(sort_string(n))

#sort list of tuple:
sort_list=lambda n:sorted(n)
n=[(1,2),(1,4),(4,1),(9,10),(7,5)]
print(sort_list(n))

#min in list
min_list=lambda a:min(a) 
a=[1,2,3]
print(min_list(a))

#sort dic by values
a={"name":"zarshu","food":"maggi"}
sort_dic=dict(sorted(a.items(),key=lambda b: b[1])) 
print(sort_dic)

#to cal simple int
si=lambda p,r,t:p*r*t/100
p=int(input("enter the num:"))
r=int(input("enter the num:"))
t=int(input("enter the num:"))
print(si(p,r,t))

#to rev a string
s=lambda a:a[::-1]
a=input("enter the string")
print(s(a))

#to check palindrome
d=lambda a:"it is a palindrome" if a[::-1]==a else "not a palindrome"
a=input("enter the string")
print(d(a))

#to find greatest of 3 num
f=lambda a,b,c:max(a,b,c)
a=int(input("enter the num:"))
b=int(input("enter the num:"))
c=int(input("enter the num:"))
print(f(a,b,c))'''

#to check string leng>5
g=lambda a:len(a)
a=input("enter the string")
print(g(a))




















