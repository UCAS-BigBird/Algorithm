
# class Solution():
#     def two_sum(self,nums,target):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                      return  i,j
#         print('sorry')

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         dic=dict()
#         for index,number in enumerate(nums):
#             Res=target-number
#             if Res in dic:
#                 return [dic[Res],index]
#             else:
#                 dic[number]=index
#其实这个设计非常的巧妙


# class Solution(object):
#     def removeDuplicates(self,nums):
#         if not nums:
#             return 0
#         new=0
#         for i in range(1,len(nums)):
#             if nums[i]!=nums[new]:
#                 new=new+1
#                 nums[new]=nums[i]
#         return new+1
# class Solution(object):
#     def removeDuplicates(self,nums):
#         new=[]
#         for i in nums:
#             if i not in new:
#                 new.append(i)
#         nums=new
#         print(nums)
#         return  len(new)
# c=Solution().removeDuplicates([1,2,3,4,1])
# print(c)
#
# class Solution:
#     def removeElement(self, nums, val):
#         if nums==[]:
#             return 0
#         new=0
#         for i in range(1,len(nums)):
#             if nums[i]!=val:
#                 new=new+1
#                 nums[new]=nums[i]
#         return new+1
# c=Solution().removeElement(nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2)
# print(c)













        # if not nums:
        #     return 0
        # index=0
        #
        # for i in range(1,len(nums)):
        #     if nums[i]!=nums[index]:
        #         index=index+1
        #         nums[index]=num[i]
        #
        # return  index+1
