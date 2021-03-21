class Vertex:
    def __init__(self,name):
        self.name=name
        self.node= None
class Edge:

    def __init__(self,weight,start,end):
        self.weight=weight
        self.start=start
        self.end=end

    # This function is used to compare objects
    # krushkal algo sorts the objects by weights
    def __lt__(self, other):
        return self.weight <other.weight
class Node:
    # node is the node in the tree representation of disjoint sets
    def __init__(self,rank,node_id,parent):
        self.rank=rank
        self.node_id=node_id
        self.parent=parent

class DisjointSet:
    def __init__(self,vertex_l):
        self.vertex_l=vertex_l
        self.root_node=[]
        self.make_set()

    def make_set(self):
        for v in self.vertex_l:
            node=Node(0,len(self.root_node),None)
            v.node=node
            self.root_node.append(node)
# aim of find() funcn is to find the root node which is representative
    def find(selfself,node):
        # first we have to find root node
        current_node=node
        while current_node.parent is not None:
            current_node=current_node.parent
        # apply path compression
        root=current_node
        current_node=node

        while current_node is not root:
            temp=current_node.parent
            current_node.parent=root
            current_node=temp
        return root.node_id

    def merge(self,node1,node2):
        index1=self.find(node1)
        index2=self.find(node2)

        # these nodes are in the same disjoint set
        if index1==index2:
            return
        root1=self.root_node[index1]
        root2=self.root_node[index2]

        if root1.rank <root2.rank:
            root1.parent=root2
        elif root1.rank > root2.rank:
            root2.parent=root1
        else:
            root1.rank+=1
            root2.parent=root1
class KrushkalAlgorithm:

    def __init__(self,vertex_l,edge_l):
        self.edge_l=edge_l
        self.vertex_l=vertex_l

    def spanningTree(self):
        disjoint_set=DisjointSet(self.vertex_l)
        mst=[]
        # mst algo
        self.edge_l.sort()

        for edge in self.edge_l:
            u=edge.start
            v=edge.end

            if disjoint_set.find(u.node) is not disjoint_set.find(v.node):
                mst.append(edge)
                disjoint_set.merge(u.node,v.node)
        for edge in mst:
            print(edge.start.name, '-',edge.end.name, '-', edge.weight)

vertex1 = Vertex("a")
vertex2 = Vertex("b")
vertex3 = Vertex("c")
vertex4 = Vertex("d")
vertex5 = Vertex("e")
vertex6 = Vertex("f")
vertex7 = Vertex("g")

edge1 = Edge(2, vertex1, vertex2)
edge2 = Edge(6, vertex1, vertex3)
edge3 = Edge(5, vertex1, vertex5)
edge4 = Edge(10, vertex1, vertex6)
edge5 = Edge(3, vertex2, vertex4)
edge6 = Edge(3, vertex2, vertex5)
edge7 = Edge(1, vertex3, vertex4)
edge8 = Edge(2, vertex3, vertex6)
edge9 = Edge(4, vertex4, vertex5)
edge10 = Edge(5, vertex4, vertex7)
edge11 = Edge(5, vertex6, vertex7)

vertexList = []
vertexList.append(vertex1)
vertexList.append(vertex2)
vertexList.append(vertex3)
vertexList.append(vertex4)
vertexList.append(vertex5)
vertexList.append(vertex6)
vertexList.append(vertex7)

edgeList = []
edgeList.append(edge1)
edgeList.append(edge2)
edgeList.append(edge3)
edgeList.append(edge4)
edgeList.append(edge5)
edgeList.append(edge6)
edgeList.append(edge7)
edgeList.append(edge8)
edgeList.append(edge9)
edgeList.append(edge10)
edgeList.append(edge11)

algorithm = KrushkalAlgorithm(vertexList,edgeList)
algorithm.spanningTree()
