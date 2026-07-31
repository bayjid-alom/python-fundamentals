# Problem 1: Square or Rectangle
# Take the length and breadth of a rectangle as input. Check whether it is a square or not.

length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))

if length == breadth:
    print("It is a square.")
else:
    print("It is a rectangle.")
