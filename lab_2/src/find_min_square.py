def least_square(n, w, h):
    if not 1 <= n <= 1012 or not 1 <= w <= 109 or not 1 <= h <= 109:
        return None

    k = 1
    element_w = 1
    element_h = 1

    while k <= n:
        if (element_w + 1) * w < (element_h + 1) * h:
            element_w += 1
        else:
            element_h += 1
        k = element_w * element_h + 1

    if element_w * w > element_h * h:
        return element_w * w
    else:
        return element_h * h

