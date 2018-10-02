#number=[2,7,11,15] target=9
class Solution():
    def method(self,number,target):
        for i in range(len(number)):
            for j in range(i+1,len(number)):
                if number[i]+number[j]==target:
                    return i,j
        return False
    def method2(self,number,target):
        dic=dict()
        for index,value in enumerate(numbler):
            sub=target-value
            if sub in dic:
                return [dic[sub],index]
            else:
                dic[value]=index


c=Solution().method([1,2,3,4,5],9)
print(c)