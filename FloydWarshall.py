import numpy as np

def floyd_warshall(W):
    n = len(W) 
    D = np.copy(W)
    
    for k in range(n):  
        for i in range(n):  
            for j in range(n):  
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    
    return D

W = [
    [0, 5, np.inf, 30], 
    [np.inf, 0, 5, 20],  
    [np.inf, np.inf, 0, 5],  
    [np.inf, np.inf, np.inf, 0]  
]

shortest_paths = floyd_warshall(W)
    
print("Shortest path matrix:")
print(shortest_paths)
