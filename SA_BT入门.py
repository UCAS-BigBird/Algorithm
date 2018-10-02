# class Node(object):
#     def __init__(self,item=None):
#         Node.item=item
#         Node.lchild=None
#         Node.rchild=None
#  这个写完以后 将会记忆尤新，理由很简单 Node里面的元素 全被共享  导致self.root值发生重大变化
# class Node:
#     def __init__(self,item):
#         self.item = item
#         self.child1 = None
#         self.child2 = None
#下面这个例子 自己就是看不出来 可怜 可叹！

class Node(object):
    def __init__(self,item=None):
        self.item=item
        self.lchild=None
        self.rchild=None

class Tree(object):
    def __init__(self,root=None):
        self.root=root

    def add(self,item):
        node=Node(item)
        if self.root is None:
            self.root=node
        else:
            queue=[self.root]
            while queue:
                cur_node=queue.pop(0)
                if cur_node.lchild is None:
                    cur_node.lchild=node
                    return
                else:
                    queue.append(cur_node.lchild)
                if cur_node.rchild is None:
                    cur_node.rchild=node
                    return
                else:
                    queue.append(cur_node.rchild)

    def breadth_travel(self):
        if self.root is None:
                return
        queue=[self.root]
        while queue:
                c=queue.pop(0)
                print(c.item,end='')
                if c.lchild is not None:
                    queue.append(c.lchild)
                if c.rchild is not None:
                    queue.append(c.rchild)

    def preorder(self,node):
        if node is None:
            return
        print(node.item,end='')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.item,end='')
        self.inorder(node.rchild)

    def afterorder(self,node):
        if node is None:
            return
        self.afterorder(node.lchild)
        self.afterorder(node.rchild)
        print(node.item,end='')


c=Tree()
c.add(0)
c.add(1)
c.add(2)
c.add(3)
c.add(4)
c.add(5)
c.add(6)
c.add(7)
c.add(8)
c.add(9)

c.breadth_travel()
print('\n')
c.preorder(node=c.root)
print('\n')
c.inorder(node=c.root)
print('\n')
c.afterorder(node=c.root)