## weekly and strongly connected components of a directed graph using DFS
# depth first search traversal in graph DFS
# weigted, unweighted , undirected grapgh

graph = {}
graph1 = {}

def add_node(v):
    if v in graph:
        print("Node already exists in graph!")
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

def DFS(node, visited, graph):
    if node not in graph:
        print(node, "Node does not exist in graph!")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i, visited, graph)


visited = set()
revvisited = set()
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")
add_edges("A", "B")
add_edges("A", "C")
add_edges("A", "D")
add_edges("D", "E")
#add_edges("B", "C")
add_edges("B", "E")
#add_edges("A", "D")
add_edges("C", "D")
add_edges("C", "F")
add_edges("E", "F")
add_edges("E", "G") 

print(graph)
DFS("A", visited, graph)
for i in list(graph):
    if i not in visited:
        print("**** weekly connected graph ****")
        ##DFS(i, visited, graph)  # visit all nodes in weekly connected graph
        break
else:
    DFS("A", revvisited, graph1)
    if visited == revvisited:
        print("**** strongly connected graph ****")
    print("**** weekly connected graph ****")

