import heapq


class Edge():
    def __init__(self, weight, start, end):
        self.start = start
        self.weight = weight
        self.end = end


class Node():
    def __init__(self, name):
        self.name = name
        self.predecessor = None
        self.adjacencylist = []
        self.minDistance = float("inf")
        self.visited = False

    def __lt__(self, other):
        return self.minDistance < other.minDistance


class Djikshtra():
    def __init__(self):
        self.heap = []

    def calculate(self, vertex):
        vertex.minDistance = 0
        heapq.heappush(self.heap, vertex)

        while self.heap:
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited is True:
                continue
            for edge in actual_vertex.adjacencylist:
                u = edge.start
                v = edge.end
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecessor = u
                    heapq.heappush(self.heap, v)
            actual_vertex.visited = True

    @staticmethod
    def get_shortest(vertex):
        print("the shortest path to vertex is %s" % str(vertex.minDistance))
        actual = vertex
        while actual is not None:
            print("%s" % actual.name)
            actual = actual.predecessor


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

edge1 = Edge(5, node1, node2)
edge2 = Edge(8, node1, node8)
edge3 = Edge(9, node1, node5)
edge4 = Edge(15, node2, node4)
edge5 = Edge(12, node2, node3)
edge6 = Edge(4, node2, node8)
edge7 = Edge(7, node8, node3)
edge8 = Edge(6, node8, node6)
edge9 = Edge(5, node5, node8)
edge10 = Edge(4, node5, node6)
edge11 = Edge(20, node5, node7)
edge12 = Edge(1, node6, node3)
edge13 = Edge(13, node6, node7)
edge14 = Edge(3, node3, node4)
edge15 = Edge(11, node3, node7)
edge16 = Edge(9, node4, node7)

node1.adjacencylist.append(edge1)
node1.adjacencylist.append(edge2)
node1.adjacencylist.append(edge3)
node2.adjacencylist.append(edge4)
node2.adjacencylist.append(edge5)
node2.adjacencylist.append(edge6)
node8.adjacencylist.append(edge7)
node8.adjacencylist.append(edge8)
node5.adjacencylist.append(edge9)
node5.adjacencylist.append(edge10)
node5.adjacencylist.append(edge11)
node6.adjacencylist.append(edge12)
node6.adjacencylist.append(edge13)
node3.adjacencylist.append(edge14)
node3.adjacencylist.append(edge15)
node4.adjacencylist.append(edge16)

algo = Djikshtra()
algo.calculate(node1)
algo.get_shortest(node7)
