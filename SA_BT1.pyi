# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth1(self, root):

        if root==None:
            return 0
        depth=0
        q=[root]
        while q:
            depth=depth+1 #表示每一层加一
            for i in range(len(q)):
                if q[0].left is not None:
                    q.append(q[0].left)
                if q[0].right is not None:
                    q.append(q[0].right)
                del q[0]
        return depth

    def maxDepth2(self,root):
        if root is None:
            return 0
        return 1+max(self.maxDepth2(root.left),self.maxDepth2(root.right))