'''
在这里 不失一般性的指出
record.get 函数 处理的极为精彩与巧妙

不妨我们来看看下面这个函数
D={'name':'Runoob','Age':27}
c=D.get('sex',0)
很显然D中没有这个元素 所以返回0
D={'name':'Runoob','Age':27}
D['sex']=D.get('sex',0)+1
print(D)
{'name': 'Runoob', 'Age': 27, 'sex': 1}
当发现sex为1的时候，很显然 就有了新的可能
非常非常的巧妙

这里在补充一个popitem  通过随机返回字典中的一对键值
site={'name':'菜鸟教程','alexa':10000,'url':'www.runoob.com'}
pop_obj=site.popitem()
print(pop_obj[0]) #其实在这里态度已经非常鲜明了
print(type(pop_obj))

list1 = ['Google', 'Runoob', 'Taobao']
list_pop=list1.pop(1)
print "删除的项为 :", list_pop
print "列表现在为 : ", list1

pop 是可以pop指定的值 一定要注意！
'''
def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        record={}
        for num in nums:
            record[num]=record.get(num,0)+1
            if record[num]>=2:
                record.pop(num)
        return record.popitem()[0]

###  精彩绝伦


