def split_array(array):
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    return left, right


def mergesort(array):
    if len(array) < 2:
        return array
    left, right = split_array(array)

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    left_pos, right_pos = 0, 0
    result = []

    while left_pos < len(left) and right_pos < len(right):
        if left[left_pos] < right[right_pos]:
            result.append(left[left_pos])
            left_pos += 1
        else:
            result.append(right[right_pos])
            right_pos += 1
    result.extend(left[left_pos:])
    result.extend(right[right_pos:])
    return result


def find_min_max_elements(array):
    sort_arr = mergesort(array)
    min_index = -1
    max_index = -1
    for i in range(len(array)):
        if array[i] != sort_arr[i]:
            min_index = i
            break
    for i in range(1, len(array)):
        if array[-i] != sort_arr[-i]:
            max_index = len(array) - i
            break
    return min_index, max_index


arr = [5, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 17]

print(find_min_max_elements(arr))
