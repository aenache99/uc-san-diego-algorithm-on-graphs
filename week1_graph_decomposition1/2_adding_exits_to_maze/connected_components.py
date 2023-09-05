import sys


def explore(v, adj, visited):
    visited[v] = True
    for neighbor in adj[v]:
        if not visited[neighbor]:
            explore(neighbor, adj, visited)


def number_of_components(adj):
    n = len(adj)
    visited = [False] * n
    component_count = 0

    for v in range(n):
        if not visited[v]:
            explore(v, adj, visited)
            component_count += 1

    return component_count


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

    print(number_of_components(adj))
