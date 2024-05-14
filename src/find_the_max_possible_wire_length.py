import math
from typing import List
import csv


def find_length_of_electric_cable(w: float, heights: List[float]) -> float:
    """
    We have to find the maximum possible cable length between electric pillars, for this we use the Pythagorean theorem.
    One of our katet is always fixed (w), so the hypotenuse (cable length) will be always be max,
    when the other is max. The unknown katet will always be either the height of the current_pillar - 1,
    or the abs(subtraction of the heights of the current_pillar and next_pillar).

    :param w: The distance between the pillars
    :param heights: The maximum possible height of each pillar
    :return: float: the maximum possible cable length between electric pillars, with two digits after the decimal point
    """

    result = 0
    for i in range(0, len(heights) - 1):
        current_pillar = heights[i]
        next_pillar = heights[i + 1]

        if current_pillar == 0 or next_pillar == 0:
            return 0

        if current_pillar >= next_pillar:
            length_of_electric_wire = math.sqrt((current_pillar - 1) ** 2 + w ** 2)
            heights[i + 1] = 1

        else:

            if next_pillar - current_pillar <= current_pillar - 1 or i == 0:
                length_of_electric_wire = math.sqrt((next_pillar - 1) ** 2 + w ** 2)
                heights[i] = 1

            else:
                length_of_electric_wire = math.sqrt((next_pillar - current_pillar) ** 2 + w ** 2)

        result += length_of_electric_wire

    return float(f"{result:.2f}")


def read(input_file: str) -> List[List[str]]:
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
