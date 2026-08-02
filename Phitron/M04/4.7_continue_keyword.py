# Continue - skip this item



# By using for loop (Continue)

# for i in range(5, 16, 1):
#     if i % 5 == 0:
#         continue
#     print(i)

"""
Skiped : 5,10,15  🔻 (i % 5 == 0) 
6
7
8
9
11
12
13
14
"""







# By using while loop (Continue)
# Increament ব্যবহার না করলে ইনফিনিট লুপ চলতে থাকবে । ফলে একসময় কম্পিউটার ক্র্যাশ করবে।

a = 1
while a <=10:
    a = a + 1
    if(a == 5):
        continue
    print(a)

"""
2
3
4
--Skiped
6
7
8
9
10
11
"""
