# graph insertation

nodes = []
graph = []
node_count = 0
class Graph:
    def __init__(self):
        self.nodes = nodes
        self.graph = graph

    def add_node(self, v):
        global node_count
        if v in nodes:
            print("Node already exists")
        else:
            node_count  = node_count + 1
            nodes.append(v)
            for n in graph:
                n.append(0)
            temp = []
            for i in range(node_count):
                temp.append(0)
            graph.append(temp)
    
    def print_graph(self):
        for i in range(node_count):
            for j in range(node_count):
                print(format(graph[i][j],"<3"), end=" ")
            print()
    
    def add_edges(self, v1, v2):
        if v1 not in nodes and v2 not in nodes:
            print("Node does not exist")
        else:
            index1 = nodes.index(v1)
            index2 = nodes.index(v2)
            graph[index1][index2] = 1
            graph[index2][index1] = 1
        
    def weighted_edge(self, v1, v2, weight):
        if v1 not in nodes and v2 not in nodes:
            print("Node does not exist")
        else:
            index1 = nodes.index(v1)
            index2 = nodes.index(v2)
            graph[index1][index2] = weight
            #graph[index2][index1] = weight
        

print("before adding nodes")
print(nodes)
print(graph)
g = Graph()
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_edges("A", "B")
g.weighted_edge("A", "B", 10)
g.weighted_edge("B", "C", 5)
print("After adding nodes")
print(nodes)
print(graph)
g.print_graph()
