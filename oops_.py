class Person:
    def __init__(self):
        self.name = "Pooja"
        self.age = 18
    def updatename(self,name):
        self.name = name
     
person1 = Person()
person2 = Person()
person1.updatename("abc")
#person2.name="Sweta"
print(person1.name)
print(person2.name)
    