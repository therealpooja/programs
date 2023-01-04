
class A:
    def __init__(self):
        print("This is methodA")
    def method1(self):
        print("This is method 1")
class B(A):
    def __init__(self):
        super().__init__()
            
        print("This is methodB")

    def method2(self):
        print("This is method 2")
class C(B,A):
    def __init__(self):
        super().__init__()
        print("This is init of method 3")
    def method3(self):
        print("This is method 3")

objB=B()
objC=C()
objC.method1()
    