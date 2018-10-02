#这里可以补充一个小技巧，可以用来思考，思考的问题是
#如何判断这个索引在不在这个字典里面
#很显然的是 利用 if some in a：
#通过if 语句判断来解决相关问题
#这里我学到了什么？
#学到了 如何利用 j in {} 字典
#快速判断这个元素是否存在

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        map={}
        for i in nums1:
            map[i]=map.get(i,0)+1
        for j in nums2:
            if j in map and map[j]>0:
                res.append(j)
                map[j]-=1
        return res
a=Solution().intersect([4,9,5],[9,4,9,8,4])
print(a)