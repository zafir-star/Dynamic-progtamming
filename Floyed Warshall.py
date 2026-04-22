def floyd_warshall(graph, V):
    dist = [row[:] for row in graph] # Copy input matrix

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

INF = float("Inf")
adj_matrix = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]
print("Floyd-Warshall Result Matrix:")
for r in floyd_warshall(adj_matrix, 4): print(r)