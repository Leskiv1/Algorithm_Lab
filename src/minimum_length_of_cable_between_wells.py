import csv
from typing import List


def kruskal(graph: List[List[int]], vertexes: int) -> int:
    """
    Implements Kruskal's algorithm to find the minimum spanning tree of a graph.
    Also, I use principle of the disjoint set where 'parent: List[int]' is the list  of each vertex's parent
    and 'rank: List[int]' is he list where shown how much children have each vertex.

    :param graph: the graph represented as a list of lists, where each inner list contains three elements: the first
    vertex, the second vertex, and the weight of the edge.
    :param vertexes: the number of vertices in the graph.
    :return: the total weight of the minimum spanning tree( minimum length of cable between wells) if it exists,
    otherwise -1
    """
    sorted_graph = sorted(graph, key=lambda item: int(item[2]))
    parent = []
    rank = []
    for i in range(0, vertexes + 1):
        parent.append(i)
        rank.append(0)
    result = 0
    edges_in_tree = 0
    iterator = 0

    while edges_in_tree < vertexes - 1 and iterator < len(sorted_graph):
        start_vertex, end_vertex, weight = sorted_graph[iterator]
        iterator += 1
        parent_start_vertex = find(parent, start_vertex)
        parent_end_vertex = find(parent, end_vertex)

        if parent_start_vertex != parent_end_vertex:
            edges_in_tree = edges_in_tree + 1
            result += int(weight)
            union(parent, rank, parent_start_vertex, parent_end_vertex)
    if edges_in_tree < vertexes - 1:
        return -1
    else:
        return result


def find(parent: List[int], root: int) -> int:
    """
    Finds the root of the given vertex in the disjoint set.

    :param parent: the list representing the parent of each vertex in the disjoint set.
    :param root: the vertex whose root needs to be found.

    :return parent[root]: the root of the given vertex.
    """
    if parent[root] != root:
        parent[root] = find(parent, parent[root])
    return parent[root]


def union(parent: List[int], rank: List[int], parent_start_vertex: int, parent_end_vertex: int):
    """
    Unites two disjoint sets by joining their roots.

    :param parent: The list representing the parent of each vertex in the disjoint set.
    :param rank: The list representing the rank(which vertex have more children) of each vertex in the disjoint set.
    :param parent_start_vertex: The root of the first disjoint set.
    :param parent_end_vertex: The root of the second disjoint set.
    """
    if parent_start_vertex != parent_end_vertex:
        if rank[parent_start_vertex] < rank[parent_end_vertex]:
            parent[parent_start_vertex] = parent_end_vertex
        elif rank[parent_start_vertex] > rank[parent_end_vertex]:
            parent[parent_end_vertex] = parent_start_vertex
        else:
            parent[parent_end_vertex] = parent_start_vertex
            rank[parent_start_vertex] += 1


def read(input_file: str) -> List[List[int]]:
    """
    Reads the input CSV file and performs preprocessing of data, removing the "K" character and trimming extra spaces
    in each cell.
    :param input_file:
    :return  List[List[int]]: A list of lists representing pairs of connected vertices and the distance between them.
    :return int: An integer representing the number of vertices.
    """
    with open(input_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        data = [row for row in csv_reader]
        if len(data) == 0:
            return -1

        modified_data = [[cell.replace('K', '').strip() for cell in row] for row in data]
        graph_data = [[int(x) for x in row] for row in modified_data]

    unique_vertices = set()
    for edge in graph_data:
        unique_vertices.update(edge[:2])

    vertexes = len(unique_vertices)

    return kruskal(graph_data, vertexes)
