def find_longest_prefix_suffix(haystack, needle):
    longest_prefix_suffix = [0] * len(needle)
    prefix_iter = 0
    current_index = 1
    while current_index < len(needle):
        if needle[current_index] == needle[prefix_iter]:
            prefix_iter += 1
            longest_prefix_suffix[current_index] = prefix_iter
            current_index += 1
        else:
            if prefix_iter != 0:
                prefix_iter = longest_prefix_suffix[prefix_iter - 1]
            else:
                longest_prefix_suffix[current_index] = 0
                current_index += 1
    return kmp(haystack, needle, longest_prefix_suffix)


def kmp(haystack, needle, lps):
    indexes = []
    needle_iter = 0
    for haystack_iter in range(len(haystack)):
        if needle_iter > 0 and haystack[haystack_iter] != needle[needle_iter]:
            needle_iter = lps[needle_iter - 1]
        if haystack[haystack_iter] == needle[needle_iter]:
            needle_iter += 1
        if needle_iter == len(needle):
            indexes.append(haystack_iter - len(needle) + 1)
            needle_iter = 0
    if len(indexes) == 0:
        return None
    return indexes
