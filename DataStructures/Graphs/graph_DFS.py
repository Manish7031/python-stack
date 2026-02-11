# depth first search traversal in graph DFS
class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
    
    def dfs(self, node):
        if node not in self.visited:
            print(node)
            self.visited.add(node)
            for neighbor in self.graph[node]:
                self.dfs(neighbor)
    
# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
dfs_traversal = DFS(graph)


