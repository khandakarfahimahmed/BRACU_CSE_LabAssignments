class Calculator:
    def __init__(self,):
        print("Lets Calculate!")
    def add(self,a,b):
        print("Result:",a+b)
    def subtract(self,a,b):
        print("Result:",a-b)
    def multiply(self,a,b):
        print("Result:",a*b)
    def devide(self,a,b):
        print("Result:",a/b)
obj = Calculator()
v1 = int(input("Enter a value: "))
op = input ("Enter an operator: ")
v2 = int(input("Enter another value: "))
print("Value 1:",v1)
print("Operator:",op)
print("Value 2:",v2)
if op == "+":
    obj.add(v1,v2)
elif op == "*":
    obj.multiply(v1,v2)
elif op == "/":
    obj.devide(v1,v2)
else:
    obj.subtract(v1,v2)
