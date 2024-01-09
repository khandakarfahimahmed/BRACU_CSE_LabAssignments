class KeyIndex:
    def __init__(self,a):
        self.k = a
    def search(self,val):
        max =  self.k[0]
        min = self.k[0]
        for i in self.k:
            if i>max:
                max=i
            if i<min:
                min=i
        if min>=0:
            a = [0]*(max+1)
            for i in self.k:
                a[i] = a[i]+1
            if len(a)<val or val<min:
                print(False)
            else:
                if a[val]==0:
                    print(False)
                else:
                    print(True)

        else:
            max=0
            b = []
            x = min *(-1)
            for i in self.k:
                b.append(x+i)
            for i in b:
                if i>max:
                    max=i
            c = [0]*(max+1)
            for i in b:
                c[i] = c[i]+1
            if val<max and val>min:
                temp = val+len(self.k)
                if temp<len(c):
                    if c[temp]>0:
                        print(True)
                    else:
                        print(False)
            else:
                print(False)
    def sort(self):
        max =  self.k[0]
        min = self.k[0]
        for i in self.k:
            if i>max:
                max=i
            if i<min:
                min=i
        for i in self.k:
            if i>max:
                max=i
            if i<min:
                min=i
        if min>=0:
            a = [0]*(max+1)
            for i in self.k:
                a[i] = a[i]+1
            for i in range(0,len(a)):
                if a[i]>0:
                    for j in range(0,a[i]):
                        print(i)
        else:
            max=0
            b = []

            n = len(self.k)
            for i in range(n-1):
                for j in range(0, n-i-1):
                    if self.k[j] > self.k[j+1] :
                        self.k[j], self.k[j+1] = self.k[j+1], self.k[j]
            x = min *(-1)
            for i in self.k:
                b.append(x+i)
            for i in b:
                if i>max:
                    max=i
            c = [0]*(max+1)
            for i in b:
                c[i] = c[i]+1
            for i in self.k:
                print(i)



c1 = KeyIndex([4,5,2,9,2,6,10])
c1.search(-15)
c1.sort()
