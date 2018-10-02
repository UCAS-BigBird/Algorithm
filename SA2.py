#这里需要注意的是  一定需要注意[0:2] 后面的序号是结束停止 千万不要犯这种错误

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                sum=sum+prices[i+1]-prices[i]
        return sum
c=Solution().maxProfit([1,2,3,4,5])
print(c)

