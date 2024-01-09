class Cat:
    def __init__(self,a=None,b = None):
        self.a = a
        self.b = b
    def printCat(self):
        if self.a!=None and self.b!=None:
            print(self.a,"cat is",self.b)
        elif self.a!=None:
            print(self.a,"cat is sitting")
        else:
            print("White cat is sitting")
    def changeColor(self,x):
        self.a = x

c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
