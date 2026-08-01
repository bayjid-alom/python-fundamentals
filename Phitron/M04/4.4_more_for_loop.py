# More about for loop

a = "Hello World"  # string
# for letter in a:
#     print(letter)


bag = ["Onion", "Potato", 10, 20, 30, 40, 5, 0, 7, 3]
# for item in bag:
#     print(item)


list = [12, 45, 7, -3, 5, 6, 4]
# for i in list:
#     if i <= 10:
#         print(i)


for i in range(20):
    if i % 5 == 0 and i % 3 == 0:
        print(i)


sum = 0
for i in range(1, 21):
    sum = sum + i

print("Summation between 1-20 = ", sum)
