class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer
    
    def getData(self):
        return self.value

    def getNext(self):
        return self.pointer

    def setData(self, newData):
        self.value = newData

    def setNext(self, newPointer):
        self.pointer = newPointer

d = Node('d')
c = Node('c', d)
b = Node('b', c)
a = Node('a', b) # 선형 노드, a가 최상위 노드인 식

print(a.getData())
print(a.getNext().getData()) # 포인터의 값 출력