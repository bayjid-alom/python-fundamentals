# While loop introduction
"""
while loop-এর ভেতরে এমনভাবে ভেরিয়েবল আপডেট করতে হবে যাতে একসময় শর্ত False হয়। নাহলে Infinite Loop (অসীম লুপ) তৈরি হবে।  """

a = 0
while a <= 10:
    print("From 0 : ", a)
    a = a + 1
    print(a)


x = 5
while x <= 10:
    x = x + 5
    print("Adding +5 :", x)
