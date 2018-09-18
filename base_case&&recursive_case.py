#这边需要注意的是return 直接带值跑了
def count(i):
    print(i)
    if i<=1:
        return
    else:
        count(i-1)
'''
def test(i):
    return
    print(i)
c=test(2)
print(c)
'''

def Max_Same_number(a,b):
    if a%b==0:
        if b==1:
            return "无最大公约数"
        else:
            return b

    else:
        return Max_Same_number(b,a%b)
#需要注意的是此处一定要有一个返回值
#下面使用的一个map函数相当漂亮的解决了这个问题
#同时max min比较大小 也非常有感觉
a,b=map(int,input("请输入你的值").split())
Max=max(a,b)
Min=min(a,b)
c=Max_Same_number(Max,Min)
print(c)