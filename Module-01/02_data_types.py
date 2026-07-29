"""
Python Data Types :
1. Number
    - integer
    - float
    - complex
2. String
3. List
4. Tuple
5. Dictionary
6. Boolean - (true/false)
"""

roll = 241118
gpa = 3.98
name = "Bayjid Alom"
is_passed = True
# print(roll, gpa, name, is_passed)

print(type(name))   #<class 'str'>
print(type(roll))   #<class 'int'>
print(type(is_passed))    #<class 'bool'>




# User inputs
name = input("Enter your name : ")
print("Congratulations!", name)

age = input("Enter your age : ")
age = int(age)
print("Your age is :",age)
print(type(age))
