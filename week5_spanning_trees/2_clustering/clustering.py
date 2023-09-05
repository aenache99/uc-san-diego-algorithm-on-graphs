import sys
import math
import heapq


def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def clustering(x, y, k):
    n = len(x)
    edges = []

    # Calculate and store the pairwise distances between points
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance((x[i], y[i]), (x[j], y[j]))
            edges.append((distance, i, j))

    # Sort the edges by distance in ascending order
    edges.sort()

    # Initialize a disjoint-set data structure
    parent = list(range(n))
    rank = [0] * n

    def find_set(v):
        if v != parent[v]:
            parent[v] = find_set(parent[v])
        return parent[v]

    def union_sets(a, b):
        a = find_set(a)
        b = find_set(b)
        if a != b:
            if rank[a] < rank[b]:
                a, b = b, a
            parent[b] = a
            if rank[a] == rank[b]:
                rank[a] += 1

    # Kruskal's algorithm to find the minimum spanning tree (MST)
    mst_edges = []
    mst_weight = 0.0
    for distance, u, v in edges:
        if find_set(u) != find_set(v):
            mst_edges.append((distance, u, v))
            mst_weight += distance
            union_sets(u, v)

    # Find the (k-1) largest edges to remove
    max_spacing = 0.0
    for i in range(n - k + 1):
        max_spacing = mst_edges[i][0]

    return max_spacing


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
