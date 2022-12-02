num1=float(input("Enter the first no"))
num2=float(input("Enter the second no"))
c=input("Enter the operator('=','-','*','/') you want:")
def add(num1,num2):
    print(num1+num2)
def subtract(num1,num2):
    print(num1-num2)
def multiplication(num1,num2):
    print(num1*num2)
def division(num1,num2):
    print(num1/num2)
if c=='+':
    add(num1,num2)
elif c=='-':
    subtract(num1,num2)
elif c=='*':
    multiplication(num1,num2)
elif c=='/':
    division(num1,num2)  
else:print("This is invalid")
    
    
