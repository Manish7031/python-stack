# graph insertation
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
    
# Example usage
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_edge('A', 'B')
print(g.graph)
