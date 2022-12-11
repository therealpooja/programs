
class Laptop:
    def __init__(self,name,processor):
        self.name=name
        self.processor=processor
    
    def printoutput(self):
        print("My laptop name is :",self.name,"and the processor is :",self.processor)

    
    
        
    
#instance is where the object is created
laptop1 = Laptop("ggg","bh")
laptop2=Laptop("HP","i9")
#pass method-if we dont have anything to write in it
def printoutput(self):
    
    print("My laptop name is:",self.name,"and the processor is :",self.processor)
    print(id(laptop1))
    print(id(laptop2))
laptop1.printoutput()
laptop2.printoutput()