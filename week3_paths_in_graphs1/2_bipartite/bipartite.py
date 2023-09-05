import sys
from queue import Queue


def bipartite(adj):
    n = len(adj)
    colors = [-1] * n  # Initialize colors to -1 (unvisited)

    for start_vertex in range(n):
        if colors[start_vertex] == -1:
            colors[start_vertex] = 0  # Assign color 0 to the start vertex
            queue = Queue()
            queue.put(start_vertex)

            while not queue.empty():
                vertex = queue.get()

                for neighbor in adj[vertex]:
                    if colors[neighbor] == -1:
                        colors[neighbor] = 1 - colors[vertex]  # Assign the opposite color
                        queue.put(neighbor)
                    elif colors[neighbor] == colors[vertex]:
                        return 0  # Not bipartite, adjacent vertices have the same color

    return 1  # Bipartite


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
    print(bipartite(adj))
