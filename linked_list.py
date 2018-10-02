#coding:utf-8
#在这里需要注意的是 node是一个节点 self.__head 是一个空间
#所以要把值赋给空间
class Node(object):
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class SingleLinkList(object):
    def __init__(self,node=None):
        self.__head=node

    def is_empty(self):
        #链表是否为空
        return self.__head==None

    def length(self):
        #链表长度 cur 游标用来遍历节点
        cur=self.__head
        #count记录数量
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count

    def append(self, item):
        # 尾部添加元素 也叫做尾插法
        node=Node(item)
        if self.is_empty():
            self.__head=node
        else:
            cur=self.__head
            while cur.next != None:
                cur=cur.next
            cur.next=node

    def travel(self):
        #遍历整个链表
        cur=self.__head
        while cur!=None:
            print(cur.elem,end='')
            cur=cur.next
        print("")

    def add(self,item):
        #链表头部添加元素
        node=Node(item)
        node.next=self.__head
        self.__head=node

    def insert(self,pos,item):
        #指定位置插入元素
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            pre=self.__head
            count=0
            while count<(pos-1):
                count+=1
                pre=pre.next
            node=Node(item)
            node.next=pre.next
            pre.next=node


    def remove(self,item):
        #去除某个元素
        cur=self.__head
        pre=None
        while cur!=None:
            if cur.elem==item:
                if cur==self.__head:
                    self.__head=cur.next
                else:
                     pre.next=cur.next
                break
            else:
                pre=cur
                cur=cur.next


    def search(self,item):
        #找到某个元素
        cur=self.__head
        while cur!=None:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        return  False


if __name__=="__main__":
    ll=SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travel()
    ll.insert(2,10)
    ll.travel()
    ll.remove(8)
    ll.travel()