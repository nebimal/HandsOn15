def initialize_single_source(graph, source):
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[source] = 0
    return dist, prev

def relax(u, v, w, dist, prev):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        prev[v] = u

def bellman_ford(graph, source):
    dist, prev = initialize_single_source(graph, source)
    
    for i in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                relax(u, v, weight, dist, prev)
    
    for u in graph:
        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                return False 
    
    return True, dist, prev

def print_shortest_path(prev, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()
    
    if path[0] == start:
        return path
    else:
        return "No path found"

graph = {
    'S': [('T', 6), ('Y', 7)],
    'T': [('X', 5), ('Y', 8), ('Z', -4)],
    'X': [('T', -2)],
    'Y': [('X', -3), ('Z', 9)],
    'Z': [('S', 2), ('X', 7)]
}

source_node = 'S'
result = bellman_ford(graph, source_node)

if result is False:
    print("Negative weight cycle detected!")
else:
    _, dist, prev = result
    print("Shortest distances from source node", source_node)
    for node in dist:
        print(f"Distance to {node}: {dist[node]}")
    end_node = 'Z'
    print(f"Shortest path from {source_node} to {end_node}: {print_shortest_path(prev, source_node, end_node)}")
