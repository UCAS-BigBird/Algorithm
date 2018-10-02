#需要注意的是 这就涉及到了一个二进制的问题
#n&&1  输出结果是二进制的1  所以 在+的时候 一定要注意要用int来进行处理分析。
# 至于思路还是很简单的


class Solution(object):

    def method(a):
        c=0
        for i in bin(a):
            if i=='1':
                c=c+1
        return c

    def hammingWeight(self, n):
        if n==0:
           return 0
        else:
            m=0
            while n>0:
                m=m+int(n&1)
                n=n>>1
            return m

a=Solution().hammingWeight(11)
print(a)
