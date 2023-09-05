import sys
from collections import deque


def distance(adj, s, t):
    # Initialize an array to keep track of visited vertices
    visited = [False] * len(adj)
    # Initialize a queue for BFS
    queue = deque()
    # Start from vertex s
    queue.append(s)
    visited[s] = True
    distance = [-1] * len(adj)  # Initialize distances to -1
    distance[s] = 0  # The distance from s to itself is 0

    while queue:
        vertex = queue.popleft()

        for neighbor in adj[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                distance[neighbor] = distance[vertex] + 1

    return distance[t]


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
