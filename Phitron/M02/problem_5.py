"""
Problem 5: Leap Year Check
Take a year as input. Check whether the year is a leap year or not.

Rules:
If the year is divisible by both 400 and 100, it is a Leap Year.
If the year is divisible by 4 but not by 100, it is a Leap Year.
Otherwise, it is Not a Leap Year.
"""

year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    print("It is a leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")
