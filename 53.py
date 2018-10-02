def maxSubarray(nums):
    if max(nums)<0:
        return max(nums)
    else:
        global_sum=0
        local_sum=0
        for i in nums:
            local_sum=max(0,local_sum+i)
            global_sum=max(global_sum,local_sum)
        return  global_sum

c=maxSubarray([1,2,3,4,5])
print(c)