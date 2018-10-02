# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        思路1：
        '''
        if not head or not head.next:
            return True
        newlist=[]
        fast=slow=head
        while fast and fast.next:
            newlist.insert(0,slow.val)
            slow=slow.next
            fast=fast.next.next
        if fast:
            slow=slow.next
        for val in newlist:
            while slow!=None:
                if slow.val!=val:
                    return False
                slow=slow.next
        return True

    def isPalindrome2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """


