def Sell(saleprices):
    if len(saleprices)<=1:
        return 0
    else:
        min=saleprices[0]
        profit=0
        for n in saleprices:
            if n>min:
               profit=max(profit,n-min)
            else:
                min=n
        return profit
c=Sell([1,2,3,4,-1,10])
print(c)