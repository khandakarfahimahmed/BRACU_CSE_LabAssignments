class Panda:
    def __init__(self,a,b,c):
        self.name = a
        self.gender = b
        self.age = c
    def sleep(self,*v):
        self.v = v
        if self.v==():
            return self.name+"'s"+" duration is unknown thus should have only bamboo leaves"
        else:
            if self.v[0]>=3:
                if self.v[0]<=5:
                    return self.name +" sleeps " +str(v[0]) +" hours daily and should have Mixed Veggies"
            if self.v[0]>=6 and self.v[0]<=8:
                return self.name+" sleeps "+str(v[0])+" hours daily and should have Eggplant & Tofu"
            elif self.v[0]>=9 and self.v[0]<=11:
                return self.name+" sleeps "+str(v[0])+" hours daily and should have Broccoli Chicken"
            else:
                return self.name+" sleeps "+str(v[0])+" hours daily and should have bamboo leaves"

panda1 = Panda("Kunfu","Male", 5)
panda2=Panda("Pan Pan","Female",3)
panda3=Panda("Ming Ming","Female",8)
print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))
print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))
print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())
