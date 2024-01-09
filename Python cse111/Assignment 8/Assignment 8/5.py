class Animal:
    def __init__(self,sound):
        self.__sound = sound
    def makeSound(self):
        return self.__sound
class Printer:
    def printSound(self, a):
        print(a.makeSound())
class Dog(Animal,Printer):
    def __init__(self,a):
        super().__init__(a)
class Cat(Animal,Printer):
    def __init__(self,a):
        super().__init__(a)

d1 = Dog('bark')
c1 = Cat('meow')
a1 = Animal('Animal does not make sound')
pr = Printer()
pr.printSound(a1)
pr.printSound(c1)
pr.printSound(d1)
