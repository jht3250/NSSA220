my_age = 22
age_limit = 21
have_ID = True
bribe = 100

if (my_age >= age_limit) and (have_ID == True):
    print("You may enter this establishment")
    print("Now come in before I change my mind!")
elif (bribe >= 100):
    print("I suppose I can bend the rules a little")
    print("Now come in before I change my mind!")
else:
    print("None shall pass!")
    print("You don\'t have to go home, but you can\'t stay here")

print("This prints no matter what")