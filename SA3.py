#按道理来说 列表是不可以越界的，但是下方这个例子 还是非常鲜明的给出了答案
# nums[6:] 通过这种方式来写 是完全可以的 相当于返回了一个空


class Solution():
    def method1(self,nums,k):
          k=k%len(nums)
          nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]
          return nums
    
    def method2(self,nums,k):
          k=k%len(nums)
          while k>0:
              k=k-1
              nums.insert(0,nums.pop())
          return nums

c=Solution().method2([1,2,3,4,5],2)
print(c)
