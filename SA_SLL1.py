# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#这里介绍一种非常吊的思路
#通常来说链表删除 位置定到前一个位置，然后next.next=next
#但是我完全可以把下一个节点复制，然后把他丢掉

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next

