sal=int(input("Enter the salary"))
tim=float(input("Enter the time"))
if tim>10:
    bonus=(10/100)*sal
    print(sal+bonus)
elif tim>6 and tim<10:
    bonus=(8/100)*sal
    print(sal+bonus)
elif tim<6 and tim>0:
    bonus=(5/100)*sal
    print(sal+bonus)