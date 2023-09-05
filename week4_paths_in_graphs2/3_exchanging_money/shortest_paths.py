import sys


def bellman_ford(adj, cost, s, distance, reachable, shortest):
    n = len(adj)
    distance[s] = 0

    # Relax edges repeatedly (V-1 times)
    for _ in range(n - 1):
        for u in range(n):
            for i, v in enumerate(adj[u]):
                if distance[v] > distance[u] + cost[u][i]:
                    distance[v] = distance[u] + cost[u][i]

    # Detect vertices that are reachable from the source
    visited = [False] * n
    queue = []
    for u in range(n):
        if distance[u] < float('inf'):
            queue.append(u)
            visited[u] = True

    while queue:
        u = queue.pop(0)
        reachable[u] = 1
        for v in adj[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True

    # Relax once more to check for negative cycles affecting reachability
    for u in range(n):
        for i, v in enumerate(adj[u]):
            if distance[v] > distance[u] + cost[u][i]:
                queue.append(v)

    # Mark vertices that are part of negative cycles
    while queue:
        u = queue.pop(0)
        shortest[u] = 0
        for v in adj[u]:
            if shortest[v]:
                queue.append(v)


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
    s = data[0] - 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    bellman_ford(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if not reachable[x]:
            print('*')
        elif not shortest[x]:
            print('-')
        else:
            print(distance[x])
