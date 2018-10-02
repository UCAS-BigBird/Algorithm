class Solution():
    def method(self,rowindex):
        if rowindex==0:
            return [1]
        elif rowindex>=1:
            res = [[1]]
            for i in range(1,rowindex+1):
                    res.append(list(map(lambda x,y:x+y,res[-1]+[0],[0]+res[-1])))
            return res[-1]
c=Solution().method(1)
print(c)