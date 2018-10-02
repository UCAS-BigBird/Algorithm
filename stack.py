#coding:utf-8
class Stack(object):
    def __init__(self):
        self.__list=[]
    def Push(self,item):
        self.__list.append(item)
    def Pop(self):
        if self.__list!=[]:
           return self.__list.pop()
        else:
            return None
a=Stack()
a.Push(1)

print(a.Pop())