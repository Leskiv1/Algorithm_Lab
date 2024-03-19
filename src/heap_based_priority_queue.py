class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


def insert_node(array, node: Node):
    array.append(node)
    current_position = len(array) - 1
    while current_position > 0:
        parent_position = (current_position - 1) // 2
        if array[current_position].priority > array[parent_position].priority:
            array[current_position], array[parent_position] = array[parent_position], array[current_position]
            current_position = parent_position
        else:
            break


def delete_max_priority(array):
    if len(array) != 0:
        array[0], array[len(array) - 1] = array[len(array) - 1], array[0]
        array.pop()
        heapify(array, 0)
    else:
        return 0


def heapify(array, i):
    n = len(array)
    parent_position = i
    left_child_position = 2 * i + 1
    right_child_position = 2 * i + 2

    if left_child_position < n and array[left_child_position].priority > array[parent_position].priority:
        parent_position = left_child_position

    if right_child_position < n and array[right_child_position].priority > array[parent_position].priority:
        parent_position = right_child_position

    if parent_position != i:
        array[i], array[parent_position] = array[parent_position], array[i]
        heapify(array, parent_position)


def print_queue(array):
    final_queue = []
    if len(array) == 0:
        return 0
    else:
        for i in range(len(array)):
            final_queue.append(array[i].value)
        return final_queue


