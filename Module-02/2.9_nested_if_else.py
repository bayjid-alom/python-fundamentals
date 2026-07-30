money = 300

if money >= 100:
    print("You can eat a burger.")
    if money >= 80:
        print("You can also drink a cold coffee.")
    else:
        print("You cannot afford a cold coffee.")

elif money >= 50:
    print("You can eat fuchka.")

elif money >= 20:
    print("You can buy a packet of chips.")

else:
    print("You do not have enough money to buy anything.")
