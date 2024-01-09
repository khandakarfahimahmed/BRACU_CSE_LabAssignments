class FinalQ:
    def print(self,array,idx):
        if(idx<len(array)):
            profit = self.calcProfit(array[idx])

            if idx==len(array):
                return

            else:
                v1=str(array[idx])
                v2=str(profit)
                print(str(idx+1)+". "+"Investment: "+v1+";"+" Profit: "+v2)

            self.print(array,idx+1)



    def calcProfit(self,investment):
        def mult(a, b):
            if b!=0:
                return (a + mult(a, b - 1))
            if (b == 0):
                return 0
        if investment > 100000:
            a1 = investment - 100000
            a2 = (mult(8, 10))
            b1 = 100000 - 25000
            b2 = (mult(4.5, 10))
            profit = ((mult(a1, a2)) / 1000) + ((mult(b1, b2)) / 1000)
            return profit
        if investment <= 100000:
            x = investment - 25000
            y = (mult(4.5, 10))
            profit = (mult(x, y)) / 1000
            return profit

array=[25000,100000,250000,350000]
f = FinalQ()
f.print(array,0)
