import sys
import heapq


def distance(adj, cost, s, t):
    n = len(adj)
    dist = [float('inf')] * n  # Initialize distances to infinity
    dist[s] = 0
    min_heap = [(0, s)]  # Priority queue to store (distance, vertex) pairs

    while min_heap:
        current_dist, current_vertex = heapq.heappop(min_heap)

        if current_dist > dist[current_vertex]:
            continue  # Skip if we have already found a shorter path

        for i, neighbor in enumerate(adj[current_vertex]):
            neighbor_vertex = adj[current_vertex][i]
            edge_weight = cost[current_vertex][i]

            if dist[current_vertex] + edge_weight < dist[neighbor_vertex]:
                dist[neighbor_vertex] = dist[current_vertex] + edge_weight
                heapq.heappush(min_heap, (dist[neighbor_vertex], neighbor_vertex))

    if dist[t] == float('inf'):
        return -1  # There is no path from s to t
    else:
        return dist[t]


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
