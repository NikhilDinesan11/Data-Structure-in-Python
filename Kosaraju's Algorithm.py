from collections import defaultdict


class Graph:

    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSutil(self, v, visited):
        # mark the current node as visited
        visited[v] = True
        print(v)
        # recur for other adjacent vertices for this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSutil(i, visited)

    def fillOrder(self, v, visited, stack):
        # mark the cuurnt node as visited
        visited[v] = True

        # recur for all other vertices

        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

        stack = stack.append(v)

    def getTranspose(self):
        g = Graph(self.v)
        # recur for all vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    # main func that prints all Scc

    def sCC(self):
        stack = []
        visited = [False] * (self.v)

        # fill the verices in stack according to their finishing time

        for i in range(self.v):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        print(stack)
        # create a reversed graph
        gr = self.getTranspose()

        # marking vertices as not visited
        visited = [False] * (self.v)

        # processing all vertices defined in stack
        while stack:
            i = stack.pop()

            if visited[i] == False:
                gr.DFSutil(i, visited)
                print()


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

print("Following are strongly connected components " + "in given graph")
g.sCC()
