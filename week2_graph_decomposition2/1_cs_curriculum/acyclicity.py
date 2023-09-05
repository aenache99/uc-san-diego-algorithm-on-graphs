import sys


def explore(v, adj, visited, stack):
    visited[v] = True
    stack[v] = True

    for neighbor in adj[v]:
        if not visited[neighbor]:
            if explore(neighbor, adj, visited, stack):
                return True
        elif stack[neighbor]:
            return True

    stack[v] = False
    return False


def acyclic(adj):
    n = len(adj)
    visited = [False] * n
    stack = [False] * n

    for v in range(n):
        if not visited[v]:
            if explore(v, adj, visited, stack):
                return 1

    return 0


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
