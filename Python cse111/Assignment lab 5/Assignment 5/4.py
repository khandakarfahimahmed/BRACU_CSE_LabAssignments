class Joker:
    def __init__(self,a,b,c):
        self.name = a
        self.power = b
        self.is_he_psycho = c
j1 = Joker("Heath Ledger", "Mind Game", False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print("=====================")
j2 = Joker("Joaquin Phoenix", "Laughing out Loud", True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print("=====================")
if j1 == j2:
    print("same")
else:
    print("different because, every object has it's own unique location what can not be same with other objects.")
j2.name = "Heath Ledger"
if j1.name == j2.name:
    print("same because, values can be same.")
else:
    print("different")
