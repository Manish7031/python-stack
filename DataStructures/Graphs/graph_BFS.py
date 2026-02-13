# Breadth first search traversal in graph BFS
# weigted, unweighted , undirected grapgh
from collections import deque

graph = {}
graph1 = {} #for weekly connected graph

def add_node(v):
    if v in graph:
        print("Node already exists in graph!")
    else:
        graph[v] = []
        graph1[v] = []

def add_edges(v1, v2):
    if v1 not in graph:
        print(v1, "Node does not exist in graph!")
    elif v2 not in graph:
        print(v2, "Node does not exist in graph!")
    else:
        # list1 = [v2, weight]
        # list2 = [v1, weight]
        graph[v1].append(v2)
        graph[v2].append(v1)

def BFS(node, graph, visited):
    if node not in graph:
        print(node, "Node does not exist in graph!")
        return
    Queue = []
    Queue.append(node)
    visited.add(node)
    while Queue:
        current = Queue.pop(0)
        for i in graph[current]:
            for i in graph[current]:
                if i not in visited:
                    Queue.append(i)
                    visited.add(i)

## shortest path between nodes
def shortest_path(graph, node, target):
    if node not in graph:
        print(node, "Node does not exist in graph!")
    elif target not in graph:
        print(target, "Node does not exist in graph!")
    else:
        visited2 = {}
        Queue = deque()
        visited2[node] = None
        Queue.append(node)
        while Queue:
            current = Queue.popleft()
            if current == target:
                path = []
                while current:
                    path.append(current)
                    current = visited2[current]
                return path[::-1]
            for i in graph[current]:
                if i not in visited2:
                    visited2[i] = current
                    Queue.append(i)




visited = set()
visited1 = set()
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")

add_edges("A", "B")
add_edges("A", "C")
add_edges("B", "D")
#add_edges("A", "D")
add_edges("C", "D")
add_edges("B", "E")
add_edges("E", "D")
add_edges("D", "F") 

print(graph)
print("Shortest path between A and F is: ", shortest_path(graph, "A", "F"))
print("**** BFS Traversal ***** ")
BFS("A", graph, visited)

## check connected graph
for i in list(graph):
    if i not in visited:
        print("Graph is weekly connected *****")
        break
else:
    BFS("A", graph1, visited1)
    if visited == visited1:
        print("Graph is strongly connected!")
    print("Graph is weekly connected!")
    
