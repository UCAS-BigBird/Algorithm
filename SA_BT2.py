
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValidBSTRecu(root, float("-inf"), float("inf"))

    def isValidBSTRecu(self, root, low, high):
        if root is None:
            return True

        return low < root.val and root.val < high \
            and self.isValidBSTRecu(root.left, low, root.val) \
            and self.isValidBSTRecu(root.right, root.val, high)

#哎！！其实自己已经想到了怎么写 就是写不出来
#就如同4396一样 好好看 好好学 真的是气的鸡儿都弯了
    def visit(self,node,ans=[]):
        if node ==None:
            return
        self.visit(node.left,ans)
        ans.append(node.val)
        self.visit(node.right,ans)

    def ouyue(self):
        return 2
          #哎 万一值一样呢？？？ 可笑！可叹

        # if ans==ans.sort():
        #     return True
        # else:
        #     return False
        #         #o(nlogn)
    # def isValidBST2(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if c==c.sort():
    #         return True
    #     else:
    #         return False
    #
    # def inorder(self,root):
    #
    #     if root is None:
    #         return
    #     self.inorder(root.left)
    #     c.append(root.val)
    #     self.inorder(root.right)


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(Solution().isValidBst(root))