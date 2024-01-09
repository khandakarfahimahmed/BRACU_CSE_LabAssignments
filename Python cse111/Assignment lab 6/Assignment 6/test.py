

t = input()

p = t[-1::-1]

a = ""
b = ""
for i in p:
    if i == ":":
        a = a+i
    if i == ")":
        a = a+"("
    if i == "(":
        a = a+")"

if ("::") in a:
    a = a.replace("::",":")

c1 = a.count(":)")
c2 = a.count("(:")
print(c1+c2-1)
