age1=int(input("Enter the age of 1 person"))
age2=int(input("Enter the age of 2 person"))
age3=int(input("enter the age of 3 person "))
if age1>age2 and age1>age3:
    print("age1 is the oldest one")
elif age2>age3 and age2>age1:
    print("age2 is the oldest one")
elif age3>age1 and age3>age2:
    print("age3 is the oldest one")
if age1<age2 and age1<age3:
    print("age1 is the age2 is youngest one")
elif age2<age1 and age2<age3:
    print("age2 is the age2 is youngest")
elif age3<age1 and age3<age2:
    print("age3 is the age2 is youngest")
else :
    print("all are of same age")

    