# Breadth first search traversal in graph BFS
# weigted, unweighted , undirected grapgh

graph = {}

def add_node(v):
    if v in graph:
        print("Node already exists in graph!")
    graph[v] = []

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



visited = set()
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
print("**** BFS Traversal ***** ")
BFS("A", graph, visited)

## check connected graph
for i in list(graph):
    if i not in visited:
        print("Graph is disconnected!")
        break
else:
    print("Graph is connected!")
    
