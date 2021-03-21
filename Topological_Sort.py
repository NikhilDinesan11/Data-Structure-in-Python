from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def top_sort(self,v,visited,stack):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                self.top_sort(i,visited,stack)
        stack.append(v)

    def topologicalSort(self):
        visited=[False]*self.v
        stack=[]
        for i in range(self.v):
            if visited[i]==False:
                self.top_sort(i,visited,stack)
        print(stack[::-1])
g=Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is a topological Graph")
g.topologicalSort()