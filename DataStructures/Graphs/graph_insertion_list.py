# grapgh insert using adjacency list

graph = {}

def add_node(v):
    if v  in graph:
        print("Node already exists in graph!")
    graph[v] = []

def add_edges(v1, v2, weight):
    if v1 not in graph and v2 not in graph:
        print("Node does not exist in graph!")
    else:
        list1 = [v2, weight]
        list2 = [v1, weight]
        graph[v1].append(list1)
        graph[v2].append(list2)

def delete_node(v):
    if v not in graph:
        print("Node does not exist in graph!")
    else:
        graph.pop(v)
        for i in graph:
            list1= graph[i]
            for j in list1:
                if v == j[0]:
                    list1.remove(j)
                    break

def delete_edge(v1, v2):
    if v1 not in graph:
        print(v1, "Node does not exist in graph!")
    elif v2 not in graph:
        print(v2, "Node does not exist in graph!")
    else:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        


add_node("A")
add_node("B")
add_edges("A", "B", 10)
print(graph)
delete_node("A")
print(f"after delete : {graph}")