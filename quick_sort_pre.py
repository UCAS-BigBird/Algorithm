#在这里翻了一个小错误 return None 弹出来的是None这个值

def sumx(arr):
    if arr==[]:
        return 0
    else:
        return arr[0] + sumx(arr[1:])


def count(arr):
    if arr==[]:
        return 0
    else:
        return 1+count(arr[1:])

def Max(arr):
    if len(arr)==2:
        max=arr[0] if arr[0]>=arr[1] else arr[1]
        return  max
    else:
        max=arr[0] if arr[0]>Max(arr[1:]) else Max(arr[1:])
        return  max

a=[3,8,5,0,3]
b=count(a)
c=sumx(a)
d=Max(a)
print(b,c,d)