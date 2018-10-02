#给定 nums = [2, 7, 11, 15], target = 13
#因为 nums[0] + nums[1] = 2 + 7 = 9
#所以返回 [0, 1]
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic=dict()
        for index,values in enumerate(nums):
            res=target-values
            if res in dic:
               return [dic[res],index]
            else:
                dic[values]=index
c=Solution().twoSum([2,7,11,15],13)
print(c)

