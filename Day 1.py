# Python 3.8, 19 December 2020

# Advent of Code 2020, Day 1 - See Directions/Day 1 Directions.txt for background.


def two_sum(input_data: list, target: int) -> int:
    """Returns product of two numbers in input data that sum to target."""

    index_dict = {}

    # Checks if target compliment is in dict as it populates dict. Uses dict for efficiency.

    for index, number in enumerate(input_data):
        if target - number in index_dict:
            return number * (target - number)
        index_dict[number] = index


def three_sum(input_data: list, target: int) -> int:
    """Returns product of three numbers in input data that sum to target"""

    # Convert list to dict for efficiency.

    index_dict = {number: index for index, number in enumerate(input_data)}

    # Essentially runs two_sum by creating a new target based on each key in dict. E.g. A + B + C = T, B + C = T - A

    for target_value in index_dict:
        for value in index_dict:
            if target - target_value - value in index_dict:
                return (target - target_value - value) * value * target_value


data = [int(line.strip()) for line in open('Data Input\\Day 1 Input.txt', 'r')]

# Part 1 - Find the two entries that sum to 2020; what do you get if you multiply them together?

print(two_sum(data, 2020))

# Part 2 - In your expense report, what is the product of the three entries that sum to 2020?

print(three_sum(data, 2020))
