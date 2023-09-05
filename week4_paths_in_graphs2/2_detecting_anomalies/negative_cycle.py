import sys
from collections import namedtuple
from typing import List


Test = namedtuple("Test", "n m edges ans")


class Vertex:
    def __init__(self, vertex, dist):
        self.vertex = vertex
        self.dist = dist


class Edge:
    def __init__(self, v_start, v_end, weight):
        self.v_start = v_start
        self.v_end = v_end
        self.weight = weight


class Graph:
    def __init__(self, num_vertices: int, num_edges: int, edges: List[Edge]):
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.edges = edges

        self.adj_list = self.get_adj_list(self.num_vertices, self.edges)

    @staticmethod
    def get_adj_list(num_vertices: int, edges: List[Edge]) -> dict:
        adj_list = {i: [] for i in range(num_vertices)}
        for edge in edges:
            adj_list[edge.v_start].append((edge.v_end, edge.weight))
        return adj_list

    def bfs(self, start, visited, component):
        queue = [start]
        while queue:
            cur = queue.pop(0)
            visited[cur] = True
            component.append(cur)
            for child, _ in self.adj_list[cur]:
                if not visited[child]:
                    queue.append(child)

    def find_strongly_connected_components(self):
        dfs_order = []
        visited = [False for _ in range(self.num_vertices)]
        for v in range(self.num_vertices):
            if not visited[v]:
                self.bfs(v, visited, dfs_order)

        reversed_edges = [Edge(edge.v_end, edge.v_start, edge.weight) for edge in self.edges]
        reversed_graph = Graph(self.num_vertices, self.num_edges, reversed_edges)

        # strongly connected components
        scc = []
        visited = [False for _ in range(self.num_vertices)]
        while dfs_order:
            cur = dfs_order.pop()
            if not visited[cur]:
                component = []
                reversed_graph.bfs(cur, visited, component)
                scc.append(component)
        return scc

    def has_negative_cycles_multiple_scc(self):
        negative_cycles = False

        scc = self.find_strongly_connected_components()

        dist = [sys.maxsize for _ in range(self.num_vertices)]

        for comp in scc:
            # start vertex
            dist[comp[0]] = 0

        edges_between_scc = set()
        for edge in self.edges:
            scc_start = None
            scc_end = None
            for i, comp in enumerate(scc):
                if edge.v_start in comp:
                    scc_start = i
                if edge.v_end in comp:
                    scc_end = i
            if scc_start != scc_end:
                edges_between_scc.add((edge.v_start, edge.v_end))

        for _ in range(self.num_vertices):
            for edge in self.edges:
                if (edge.v_start, edge.v_end) not in edges_between_scc:
                    cur_dist = dist[edge.v_end]
                    new_dist = dist[edge.v_start] + edge.weight
                    if new_dist < cur_dist:
                        dist[edge.v_end] = new_dist
                        negative_cycles = True

        return negative_cycles

    def has_negative_cycles_one_scc(self):
        dist = [sys.maxsize for _ in range(self.num_vertices)]
        dist[0] = 0

        for _ in range(self.num_vertices):
            relaxed = False  # Flag to track if any relaxation occurred
            for edge in self.edges:
                cur_dist = dist[edge.v_end]
                new_dist = dist[edge.v_start] + edge.weight
                if new_dist < cur_dist:
                    dist[edge.v_end] = new_dist
                    relaxed = True  # Relaxation occurred

            # If no relaxation occurred in this iteration, there are no negative cycles
            if not relaxed:
                return False

        return True  # Negative cycle found


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0:2]
    data = data[2:]
    edges_ = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    edges = []
    for ((a, b), w) in edges_:
        edges.append(Edge(a - 1, b - 1, w))

    graph = Graph(n, m, edges)
    print(1 if graph.has_negative_cycles_one_scc() else 0)
