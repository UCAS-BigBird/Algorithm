'''
book=dict()
book['apple']=0.67
book['milk']=1.49
book['avocado']=1.49
print(book)
print(book['avocado'])
'''
'''
voted={}
def check_voter(name):
    #在下面这个问题中， voted.get（函数） 返回元素的值
    if voted.get(name):
        print("kick him out")
    else:
        voted[name]=True
        print("let them vote")
check_voter('ouyue')
check_voter('ouyue')
'''
'''
c={'ouyue':'headsome','lp':'ugly'}
print(c.get('ouyue'))
print(c.get('lp'))
'''
cache={}
def get_page(url):
    if cache.get(url):
        return cache[url]

