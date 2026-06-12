import numpy as n
l1=[1,2,3,4,5,6,7,8,9,10]
a1=n.array(l1)
print(sum(a1))
print(max(a1))
print(min(a1))

#add 5 to every element in the array
for i in a1:
    print(i+5)
    
#multiply every element by 2
for i in a1:
    print(i*2)
    
#sum of even numbers in array
import numpy as n
l1=[1,2,3,4,5,6,7,8,9,10]
a1=n.array(l1)
s=0
for i in a1:
    if i%2==0:
        s+=i
print(s)

#reverse the array
import numpy as n
l1=[1,2,3,4,5,6,7,8,9,10]
a1=n.array(l1)
b=a1[::-1]
print(b)

#create two array and it's operation
import numpy as n
l1=[1,2,3,4]
l2=[5,6,7,8,9]
b1=n.array(l1)
b2=n.array(l2)
print(a1+a2)
print(a1-a2)
print(a1*a2)
print(a1/a2)
print(a2//a3)
#create a matrix of 3*3
import numpy as n
c=[1,2,3],[4,5,6],[7,8,9]
print(n.matrix(c))
print(sum(row))






























