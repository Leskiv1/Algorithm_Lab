import math
from typing import List
import csv


def find_length_of_electric_cable(w: float, heights: List[float]) -> float:
    """
    We have to find the maximum possible cable length between electric pillars, for this we use the Pythagorean theorem.
    One of our katet is always fixed (w), so the hypotenuse (cable length) will be always be max,when the other is max.
    We have four variants the unknown katet: max_min_between_two_pills, min_max_between_two_pills,
    max_max_between_two_pills, min_min_between_two_pills

    :param w: The distance between the pillars
    :param heights: The maximum possible height of each pillar
    :return: float: the maximum possible cable length between electric pillars, with two digits after the decimal point
    """

    max_min = 0
    min_max = 0
    for i in range(0, len(heights) - 1):
        current_pillar = heights[i]
        next_pillar = heights[i + 1]

        if current_pillar == 0 or next_pillar == 0:
            return 0

        max_min_between_two_pills = min_max + math.sqrt((current_pillar - 1) ** 2 + w ** 2)
        min_max_between_two_pills = max_min + math.sqrt((next_pillar - 1) ** 2 + w ** 2)
        max_max_between_two_pills = min_max + math.sqrt(abs(next_pillar - current_pillar) ** 2 + w ** 2)
        min_min_between_two_pills = max_min + w

        min_max = max(min_max_between_two_pills, max_max_between_two_pills)
        max_min = max(max_min_between_two_pills, min_min_between_two_pills)

    result = max(min_max, max_min)

    return float(f"{result:.2f}")


def read(input_file: str) -> (float, List[float]):
    """
    Reads the input CSV file and performs preprocessing of data, where 'w' is the distance between the pillars
    and 'heights' is the maximum possible height of each pillar

    :param input_file: The first line is the distance between the pillars,
    the second line is the maximum possible height of each pillar
    :return  float: The distance between the pillars
    :return List[float]: The maximum possible height of each pillar
    """
    with open(input_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        data = [i for i in csv_reader]
        w, heights = float(data[0][0]), [float(num.strip()) for num in data[1]]

    return find_length_of_electric_cable(w, heights)
