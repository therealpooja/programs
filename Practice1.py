#write a python programming to find the max of 3 no
no1=int(input("Enter the first no"))
no2=int(input("Enter hte second no"))
no3=int(input("Enter the third no"))
if  no1>no2 and no1>no3:
    print("no1 is the maximum")
elif no2>no1 and no2>no3:
    print("no2 is the maximum")
elif no3>no1 and no3>no2:
    print("no3 is the maximum")
else:
    print("Every no is equal")