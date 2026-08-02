"""
ইনফিনিট লুপ হওয়ার দুইটি শর্ত :
Infinite Loop: (always true)
01. Condition never becomes False.
02. Loop variable is not updated (no increment/decrement).

🔻 Loop break command : Ctrl + C


Python-এ for Loop:
Python-এর for loop সাধারণত Infinite Loop হয় না, কারণ এটি নিজেই Loop Variable আপডেট করে।
Infinite Loop সাধারণত while loop-এ দেখা যায়।
"""




# Never work for infinite loop
# for i in range(12,):
#     print(i)




a = 10
while a >= 0:
    a = a - 1
    print(a)






# while True:
#     print("I love Python")




# while True:
#     name = input("Enter your name :")
#     if name == "Quit" or name == "q":
#         break
#     print("Hello", name, "Good Monging!")






