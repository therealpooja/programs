class Person:
    def __init__(self,name,age):
       self.__name= name    
       self.__age= age
person1=Person("Pooja",35)
print(person1._Person__name)