class Fruit:
    def __init__(self, formalin=False, name=''):
        self.__formalin = formalin
        self.name = name
    def getName(self):
        return self.name
    def hasFormalin(self):
        return self.__formalin
class testFruit:
    def test(self, f):
        print('----Printing Detail----')
        if f.hasFormalin():
            print('Do not eat the',f.getName(),'.')
            print(f)
        else:
            print('Eat the',f.getName(),'.')
            print(f)
class Mango(Fruit,testFruit):
    def __init__(self,formalin=True,name="Mango"):
        self.name=name
        self.formalin=formalin
    def hasFormalin(self):
        return self.formalin
    def __str__(self):
        if self.formalin==True:
            return(self.name+"s are  bad for you")
        else:
            return(self.name+"s are good for you")
class Jackfruit(Fruit,testFruit):
    def __init__(self,formalin=False,name="JackFruit"):
        self.name=name
        self.formalin=formalin
    def hasFormalin(self):
        return self.formalin
    def __str__(self):
        if self.formalin==True:
            return(self.name+"s are bad for you")
        else:
            return(self.name+"s are good for you")

m = Mango()
j = Jackfruit()
t1 = testFruit()
t1.test(m)
t1.test(j)
