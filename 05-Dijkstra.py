#     ASTU 

graph = [
    [0, 7, 9, 0, 0, 14],
    [7, 0, 10, 15, 0, 0],
    [9, 10, 0, 11, 0, 2],
    [0, 15, 11, 0, 6, 0],
    [0, 0, 0, 6, 0, 9],
    [14, 0, 2, 0, 9, 0]
]

n = 6

dist = [9999] * n    #([999,999,999,999,999,999])
parent = [-1] * n    #([-1,-1,-1,-1,-1,-1])
visited = [0] * n

source = 0
dist[source] = 0        #([0,999,999,999,999,999]) 

def extract_min():
    return min((dist[i], i) for i in range(n) if not visited[i])[1]

def relax(u, v):
    if dist[v] > dist[u] + graph[u][v]:
        dist[v] = dist[u] + graph[u][v]
        parent[v] = u

for _ in range(n):
    u = extract_min()  
    for v in range(n):
        if graph[u][v] != 0 and not visited[v]:
            relax(u, v)
    visited[u] = 1

print(f"Shortest distances from source {source}: {dist}")
parent = [p + 1 if p != -1 else -1 for p in parent]
print(f"Parent nodes: {parent}")


#                    DIVYANSH    (PARENT VALUES ARE WRONG)

# graph = [
#     [0, 7, 9, 0, 0, 14],
#     [7, 0, 10, 15, 0, 0],
#     [9, 10, 0, 11, 0, 2],
#     [0, 15, 11, 0, 6, 0],
#     [0, 0, 0, 6, 0, 9],
#     [14, 0, 2, 0, 9, 0]
# ]

# n = len(graph)
# dist = n * [9999]
# parent = n * [-1]
# visited = n * [0]
# source = 0

# dist[source] = 0


# def extract_min():
#     # Find the unvisited node with the smallest distance
#     return min((dist[i], i) for i in range(n) if not visited[i])[1]


# def relax(u, v):
#     if dist[v] > dist[u] + graph[u][v]:
#         dist[v] = dist[u] + graph[u][v]
#         parent[v] = u


# def Dikstra():
#     for i in range(0, n):
#         u = extract_min()

#         for j in range(0, n):
#             if graph[u][j] != 0 and visited[j] != 1:
#                 relax(u, j)
#         visited[u] = 1


# Dikstra()

# print("dISTANCE: "+str(dist))
# print("pARENT: "+str(parent))



#                    GPT
# import sys

# def dijkstra(graph, src):
#     num_vertices = len(graph)
#     distances = [sys.maxsize] * num_vertices  # Initialize distances to infinity
#     distances[src] = 0  # Distance to the source is 0
#     visited = [False] * num_vertices  # Track visited vertices

#     for _ in range(num_vertices):
#         # Find the vertex with the smallest distance that hasn't been visited
#         min_distance = sys.maxsize
#         min_vertex = -1

#         for vertex in range(num_vertices):
#             if not visited[vertex] and distances[vertex] < min_distance:
#                 min_distance = distances[vertex]
#                 min_vertex = vertex

#         # Mark the chosen vertex as visited
#         visited[min_vertex] = True

#         # Update distances for adjacent vertices
#         for neighbor in range(num_vertices):
#             if (
#                 graph[min_vertex][neighbor] > 0 and  # There's an edge
#                 not visited[neighbor] and  # Neighbor hasn't been visited
#                 distances[min_vertex] + graph[min_vertex][neighbor] < distances[neighbor]
#             ):
#                 distances[neighbor] = distances[min_vertex] + graph[min_vertex][neighbor]

#     return distances


# # Define the graph
# graph = [
#     [0, 7, 9, 0, 0, 14],
#     [7, 0, 10, 15, 0, 0],
#     [9, 10, 0, 11, 0, 2],
#     [0, 15, 11, 0, 6, 0],
#     [0, 0, 0, 6, 0, 9],
#     [14, 0, 2, 0, 9, 0]
# ]

# # Source vertex
# source = 0

# # Run Dijkstra's algorithm
# distances = dijkstra(graph, source)

# # Print the results
# print(f"Shortest distances from vertex {source}:")
# for vertex, distance in enumerate(distances):
#     print(f"Vertex {vertex} -> Distance: {distance}")

