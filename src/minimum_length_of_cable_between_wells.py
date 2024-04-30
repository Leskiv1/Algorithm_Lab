import csv


def kruskal(graph, vertexes):
    sorted_graph = sorted(graph, key=lambda item: int(item[2]))
    parent = []
    rank = []
    for i in range(0, vertexes + 1):
        parent.append(i)
        rank.append(0)
    result = 0
    edges_in_tree = 0
    connection = 0

    while edges_in_tree < vertexes - 1 and connection < len(sorted_graph):
        vertex_1, vertex_2, weight = sorted_graph[connection]
        connection = connection + 1
        parent_vertex_1 = find(parent, vertex_1)
        parent_vertex_2 = find(parent, vertex_2)

        if parent_vertex_1 != parent_vertex_2:
            edges_in_tree = edges_in_tree + 1
            result += int(weight)
            union(parent, rank, parent_vertex_1, parent_vertex_2)
    if edges_in_tree < vertexes - 1:
        return -1
    else:
        return result


def find(parent, root):
    if parent[root] != root:
        parent[root] = find(parent, parent[root])
    return parent[root]


def union(parent, rank, root_vertex_1, root_vertex_2):
    if root_vertex_1 != root_vertex_2:
        if rank[root_vertex_1] < rank[root_vertex_2]:
            parent[root_vertex_1] = root_vertex_2
        elif rank[root_vertex_1] > rank[root_vertex_2]:
            parent[root_vertex_2] = root_vertex_1
        else:
            parent[root_vertex_2] = root_vertex_1
            rank[root_vertex_1] += 1


def read(input_file):
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
