"""
Logical Operators :
01. and
02. or
03. not
"""

print(10 > 20 and 5 == 5)
print(20 < 10 or 50 >= 30)
print(not 10 > 20)  # true

marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Grade: A+")
elif marks >= 70:
    print("Grade: A")
elif marks >= 60:
    print("Grade: A-")
elif marks >= 50:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
elif marks >= 33:
    print("Grade: D")
else:
    print("Grade: F")
