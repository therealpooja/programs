num=int(input())
a=0
b=1
i=0
while i<=num:
    c=a+b
    print(c)
    a=b
    b=c
    i+=1
