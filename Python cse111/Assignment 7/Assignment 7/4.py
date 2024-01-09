import math
class Circle:
    def __init__(self,r):
        self.__r=r
    def getRadius(self):
        return self.__r
    def area(self):
        return math.pi*self.__r*self.__r
    def __add__(self, other):
        temp=self.__r+other.__r
        return Circle(temp)

#==================================
c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" ,c1.area())

c2 = Circle(5)
print("Second circle radius:" ,c2.getRadius())
print("Second circle area:" ,c2.area())

c3 = c1 + c2
print("Third circle radius:" ,c3.getRadius())
print("Third circle area:" ,c3.area())
