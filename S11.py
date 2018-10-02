class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)==0:
            return 0
        h=len(matrix)
        w=len(matrix[0])
#下面这三行情诗 是交换矩阵  让其沿着对角方向进行变化
        for i in range(h):
            for j in range(i+1,h):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        for i in range(h):
            for j in range(w//2):
                matrix[i][w-1-j],matrix[i][j]=matrix[i][j],matrix[i][w-1-j]

        return matrix
c=Solution().rotate([
                        [1,2,3],
                        [4,5,6],
                        [7,8,9]
                    ])
print(c)