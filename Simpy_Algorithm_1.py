class Solution(object):
    def method(self,nums):
        if len(nums)<=1:
            return nums
        else:
            i=0
            for j in range(1,len(nums)):
                if nums[j] != nums[i]:
                   i+=1
                   nums[i]=nums[j]
            return nums

a=Solution().method([1,1])
print(a)