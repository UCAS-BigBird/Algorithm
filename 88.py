
#这里需要指出的是+ +号是元素相加

#这就是list ==[]

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        res = [[1]]
        for i in range(1, numRows):
            res.append(list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])))
        return res

a=Solution().generate(5)
print(a)
