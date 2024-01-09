class RealNumber:
    def __init__(self, r=0):
        self.__realValue = r
    def getRealValue(self):
        return self.__realValue
    def setRealValue(self, r):
        self.__realValue = r
    def ping(self):
        print('I am in RealNumber class')
    def __str__(self):
        return 'RealPart: '+str(self.getRealValue())
class ComplexNumber(RealNumber):
    def __init__(self,a=1.0,b=1.0):
        self.__realValue = float(a)
        self.__imaginaryvalue = float(b)
        super().__init__(self.__realValue)
    def __str__(self):
        return 'RealPart: '+str(self.getRealValue())+'\n'+'ImaginaryPart: '+str(self.__imaginaryvalue)





cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5,7)
print(cn2)
print('---------')
