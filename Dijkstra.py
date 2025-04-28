import heapq

def initialize_single_source(graph, source):
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[source] = 0
    return dist, prev

def relax(u, v, w, dist, prev):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        prev[v] = u

def dijkstra(graph, source):
    dist, prev = initialize_single_source(graph, source)

    queue = [(0, source)] 
    heapq.heapify(queue)
    visited = set()  
    
    while queue:
        current_dist, u = heapq.heappop(queue)
        if u in visited:
            continue
        
        visited.add(u)
        
        for v, weight in graph[u]:
            relax(u, v, weight, dist, prev)
            if v not in visited:
                heapq.heappush(queue, (dist[v], v))
    
    return dist, prev

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
    'A': [('B', 4), ('C', 3), ('E', 7)],
    'B': [('A', 4), ('C', 6), ('D', 5)],
    'C': [('A', 3), ('B', 6), ('D', 11), ('E', 8)],
    'D': [('B', 5), ('C', 11), ('E', 2), ('G', 10), ('F', 2)],
    'E': [('A', 7), ('C', 8), ('D', 2), ('G', 5)],
    'F': [('D', 2), ('G', 3)],
    'G': [('D', 10), ('E', 5), ('F', 3)]
}
    
source_node = 'A'
dist, prev = dijkstra(graph, source_node)

print("Shortest distances from source node", source_node)
for node in dist:
    print(f"Distance to {node}: {dist[node]}")
    
end_node = 'G'
print(f"Shortest path from {source_node} to {end_node}: {print_shortest_path(prev, source_node, end_node)}")
