# More about range function

a = list(range(10))
print("a : ", a)
print("Index 2 item is = ", a[2])

for i in range(10):
    print(i)


# range(start, stop, step)
# range(start, stop)

b = list(range(10))
c = list(range(5, 10))
d = list(range(10, 21))


print("b : ", b)
print("c : ", c)
print("d : ", d)

e = list(range(0, 20, 2))
print("Step 2 : ", e)

f = list(range(5, 30, 5))
print("Step 5 : ", f)

even = list(range(2, 101, 2));
# print("Even 1-100 : ", even)


h = list(range(10, 0, -2));
print("Reverse : ", h)


for i in range(4, -6, -2):
    print(i)

