#第一种解法的思路看起来很难，实际与前面存在着一定的联系
#这里引入了id函数
#>>>a = 'runoob'
#>>> id(a)
#4531887632 储存id的值




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        map={}
        while head:
            if id(head) in map:
                return True
            else:
                map[id(head)]=True
            head=head.next
        return False

    def hasCycle2(self,head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
            if slow==fast:
                return True
        return False
