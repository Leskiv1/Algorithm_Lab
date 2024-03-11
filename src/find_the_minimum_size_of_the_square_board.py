def least_square(n, width, height):
    if not 1 <= n <= 1012 or not 1 <= width <= 109 or not 1 <= height <= 109:
        return None

    current_element = 1
    element_in_width = 1
    element_in_height = 1

    while current_element <= n:
        if (element_in_width + 1) * width < (element_in_height + 1) * height:
            element_in_width += 1

        else:
            element_in_height += 1
        current_element = element_in_width * element_in_height + 1

    if element_in_width * width > element_in_height * height:
        return element_in_width * width
    else:
        return element_in_height * height
