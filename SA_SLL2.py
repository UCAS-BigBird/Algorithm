#head 如同一个指针 指向刚开始的地方
#P也一样
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=head
        newList=[]
        while p:
            newList.insert(0,p.val)
            p=p.next
        p=head#这个时候 要指回去了，一定要注意
        for i in newList:
            p.val=i
            p=p.next
        return head

    def reverseList2(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            # if head or head.next ==None:
            #     return head
            #上面这两句话 堪称经典，经典中的经典 居然犯下了if head 这种非常可爱的问题
            #让人忍不住笑出了声音！难怪我输出不了正确结果
            if head is None or head.next is None:
                return head
            p = head
            cur=None
            pre=None
            while(p):
                cur=p.next
                p.next=pre
                pre=p
                p=cur
            return pre
