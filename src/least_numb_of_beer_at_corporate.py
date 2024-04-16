def create_preference_matrix(employees, num_of_beers, preferences):
    matrix = []
    preferences = preferences.replace(" ", "")
    for x in range(employees):
        row = []
        for y in range(num_of_beers):
            row.append('')
        matrix.append(row)

    for i in range(employees):
        for j in range(num_of_beers):
            if preferences[i * num_of_beers + j] == 'Y':
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

    return find_least_preferred_row(matrix, num_of_beers)


def row_with_all_zero(row):
    for preference in row:
        if preference != 0:
            return False
    return True


def find_least_preferred_row(matrix, num_of_beers):
    row_with_least_preference = None
    for row in matrix:
        if row_with_all_zero(row):
            continue

        least_num_of_ones_in_row = sum(row)
        if least_num_of_ones_in_row <= num_of_beers:
            num_of_beers = least_num_of_ones_in_row
            row_with_least_preference = row

    if row_with_least_preference is None:
        return 0

    return find_least_num_of_beers(matrix, row_with_least_preference)


def find_least_num_of_beers(matrix, row_with_least_preference):
    least_num_of_beers = 1
    for row in matrix:
        if row_with_all_zero(row):
            continue

        for i in range(len(row_with_least_preference)):
            if row[i] == 1 and row_with_least_preference[i] == 1:
                break
        else:
            least_num_of_beers += 1
            for i in range(len(row)):
                if row[i] == 1:
                    row_with_least_preference[i] = 1
                    break
    return least_num_of_beers
