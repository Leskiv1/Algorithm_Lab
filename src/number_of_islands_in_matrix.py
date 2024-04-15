def take_element_position_from_matrix(graph):
    if not graph:
        return 0
    visited = set()
    islands = 0
    for row_position in range(len(graph)):
        for column_position in range(len(graph[0])):
            if graph[row_position][column_position] != 0 and (row_position, column_position) not in visited:
                visited.add((row_position, column_position))
                islands += 1
                bfs((row_position, column_position), visited, graph)
    return islands


def bfs(element_coordinates, visited, graph):
    queue = [element_coordinates]
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    while queue:
        x, y = queue.pop(0)
        for x_axis, y_axis in direction:
            if (len(graph) > (x + x_axis) >= 0 and len(graph[0]) > (y + y_axis) >= 0
                    and graph[x + x_axis][y + y_axis] == 1 and (x + x_axis, y + y_axis) not in visited):
                queue.append((x + x_axis, y + y_axis))
                visited.add((x + x_axis, y + y_axis))