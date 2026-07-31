"""
Problem 4: Grade
Take the marks as input. Print the grade based on the marks.

Grade Chart:

80–100 → A+
70–79 → A
60–69 → A-
50–59 → B
40–49 → C
33–39 → D
Below 33 → F  """



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