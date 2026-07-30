"""
# Relational Operators : O/P:(true/false)

01. >   greater than
02. >=  greater than or equal
03. <   less than
04. <=  less than or equal
05. ==  equal
06. !=  not equal
"""

print(100 >= 150);
print(50 != 100)
print(10 < 20)
print(50 == 50)

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if(a > b and a > c):
    print(a , "is the largest number.")
elif(b > c and b > a):
    print(b, "is the largest number.")
else:
    print(c , "is the largest number.")

