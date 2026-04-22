def bellman_ford(graph, V, source):
    # Step 1: Initialize distances from source to all other vertices as infinite
    dist = [float("Inf")] * V
    dist[source] = 0

    # Step 2: Relax all edges V - 1 times
    for _ in range(V - 1):
        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Step 3: Check for negative-weight cycles
    for u, v, w in graph:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return None

    return dist

# (u, v, weight)
edges = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]
print(f"Bellman-Ford Distances: {bellman_ford(edges, 5, 0)}")