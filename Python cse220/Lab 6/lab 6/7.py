
def fib(n,a={}):
    if n in a:
        return a[n]
    if n==1:
        val = 1
    else:
        if n==2:
            val = 1
        else:
            if n>2:
                val = fib(n-1)+fib(n-2)
    a[n]=val
    return val
for i in range(1,10):
    print(i,"th =" , fib(i))
