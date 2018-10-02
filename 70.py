def method(n):
    a=1
    b=2
    while n-2:
         a,b=b,a+b
         n-=1
    return b
c=method(4)
print(c)