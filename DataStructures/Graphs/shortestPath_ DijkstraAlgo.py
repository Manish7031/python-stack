## Shortest Path in Weighted Graphs 
import heapq

graph = {}

def add_node(v):
    if v in graph:
        print("Node already exists in graph!")
    graph[v] = []

def add_edges(v1, v2, weight):
    if v1 not in graph:
        print(v1, "Node does not exist in graph!")
    elif v2 not in graph:
        print(v2, "Node does not exist in graph!")
    else:
        graph[v1].append([v2, weight])
        graph[v2].append([v1, weight])

def dijkstra(graph, start):
    distance = {item:float("inf") for item in graph}
    distance[start] = 0
    queue = [(0, start)]
    previous = {node: None for node in graph}
    while queue:
        current_dist, current_node = heapq.heappop(queue)
        if current_dist > distance[current_node]:
            continue
        for node, weight in graph[current_node]:
            new_dist = current_dist + weight
            if new_dist < distance[node]:
                distance[node] = new_dist
                previous[node] = current_node
                heapq.heappush(queue, (new_dist, node))
    return distance, previous

def shortest_path(parent_node, target):
    path = []
    current = target
    while current:
        path.append(current)
        current = parent_node[current]
    return path[::-1]
       

add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")
add_node("H")
add_node("I")
add_edges("A", "B", 1)
add_edges("A", "D", 4)
add_edges("A", "F", 7)
add_edges("B", "C", 3)
add_edges("C", "D", 5)
add_edges("C", "E", 4)
add_edges("C", "H", 5)
add_edges("D", "I", 3)
add_edges("D", "G", 2)
add_edges("H", "G", 1)

print(graph)
source = "A"
end = "I"
if source not in graph:
    print(source, "Node does not exist in graph!")
elif end not in graph:
    print(end, "Node does not exist in graph!")
else:
    smallest_dist, parent_node = dijkstra(graph, source)
    for i in smallest_dist:
        print("Shortest distance from", source, "to", i, "is:", smallest_dist[i])
       # print("Shortest distance from", source, "to", i, "is:", smallest_dist[end])
        print("Shortest path from", source, "to", i, "is:",shortest_path(parent_node, i))
        print("*******************************************")


    