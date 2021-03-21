class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None
        self.size = 0

    def insertBeg(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail=self.head
            self.size+=1
        else:
            newNode = Node(data)
            newNode.next_node = self.head
            self.head.prev_node = newNode
            self.head = newNode
            newNode.prev_node=None
            self.size+=1

    def insertEnd(self, data):
        if self.tail is None:
            return
        else:
            newnode = Node(data)
            currentNode = self.tail
            currentNode.next_node=newnode
            newnode.prev_node=currentNode

    def traversingfrombeg(self):
        newnode = self.head
        while newnode is not None:
            print(newnode.data)
            newnode = newnode.next_node
        return

    def traversingfromend(self):
        newnode=self.tail
        while newnode is not None:
            print(newnode.data)
            newnode=newnode.prev_node

l=LinkedList()
l.insertBeg(1)
l.insertBeg(34)
l.insertBeg(4)
l.insertBeg(304)
l.insertBeg(43)
l.traversingfromend()
print()
l.traversingfrombeg()




