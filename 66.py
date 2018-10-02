def plusone(digits):
    sum=0
    for i in digits:
       sum=sum*10+i
    return [int(x) for x in str(sum+1)]

a=plusone([9])
print(a)
