def find_unsort_arr(array):
    left_iter = 0
    right_iter = len(array) - 1
    while array[left_iter] <= array[right_iter]:
        if left_iter == right_iter:
            return -1, -1
        if array[left_iter] < array[left_iter + 1]:
           left_iter += 1
        elif array[right_iter] >= array[right_iter - 1]:
            right_iter -= 1
        else:
            break

    
    min_el, max_el = find_min_max_elements_in_unsort_arr(array[left_iter : right_iter])
    
    for i in range(left_iter - 1, -1, -1):
        if array[i] > min_el:
            left_iter -= 1
        else:
            break
            
    for i in range (right_iter + 1, len(array)):
        if array[i] < max_el:
            right_iter -= 1
        else:
            break

    return left_iter, right_iter

def find_min_max_elements_in_unsort_arr(arr):
    min_el = arr[0]
    max_el = arr[0]
    for i in range(1,len(arr) - 1):
        if min_el > arr[i]:
            min_el = arr[i]
    for i in range(1,len(arr)):
        if max_el < arr[i]:
            max_el = arr[i]
    return min_el, max_el



arr = [5, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 17]

print(find_unsort_arr(arr))
