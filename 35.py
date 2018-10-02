class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max = nums[0]
        for data in nums:
            sum += data
            if sum > max:
                max = sum

            if sum < 0:
                sum = 0
        return max

c=Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(c)