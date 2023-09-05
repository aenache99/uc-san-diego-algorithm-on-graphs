import sys

sys.setrecursionlimit(200000)


def reverse_graph(adj):
    reversed_adj = [[] for _ in range(len(adj))]
    for v, neighbors in enumerate(adj):
        for neighbor in neighbors:
            reversed_adj[neighbor].append(v)
    return reversed_adj


def dfs1(adj, visited, stack, v):
    visited[v] = True
    for neighbor in adj[v]:
        if not visited[neighbor]:
            dfs1(adj, visited, stack, neighbor)
    stack.append(v)


def dfs2(adj, visited, v, component):
    visited[v] = True
    component.append(v)
    for neighbor in adj[v]:
        if not visited[neighbor]:
            dfs2(adj, visited, neighbor, component)


def number_of_strongly_connected_components(adj):
    reversed_adj = reverse_graph(adj)
    visited1 = [False] * len(adj)
    stack = []

    # First DFS pass to fill the stack
    for v in range(len(adj)):
        if not visited1[v]:
            dfs1(reversed_adj, visited1, stack, v)

    visited2 = [False] * len(adj)
    components = []

    # Second DFS pass to find strongly connected components
    while stack:
        v = stack.pop()
        if not visited2[v]:
            component = []
            dfs2(adj, visited2, v, component)
            components.append(component)

    return len(components)


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
