class Customer:
    def __init__(self,a):
        self.n = a

    def greet(self,*b):
        self.b = b
        if self.b == ():
            print("Hello!")
        else:
            print("Hello",self.b[0]+"!")
    def purchase(self,*args):
        self.args = args
        c = 0
        for a in args:
            c+=1
        print(self.n + ",","you purchased",c,"item(s):")
        for a in args:
            print(a)
customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")
