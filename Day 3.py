# Python 3.8, 19 December 2020

# Advent of Code 2020, Day 3 - See Directions/Day 3 Directions.txt for background.

tree_map = [line.strip() for line in open('Data Input\\Day 3 Input.txt', 'r')]

height = len(tree_map)
width = len(tree_map[0])


def tree_count(right: int, down: int) -> int:
    """Returns number of trees in tree_map given a slope."""

    trees = 0

    # Iterates through tree_map, locates correct horizontal index via modulo operator. Index // down will correlate
    # correct horizontal index if downward slope is > 1.

    for index, line in enumerate(tree_map):
        if index % down == 0 and tree_map[index][index // down * right % width] == '#':
            trees += 1

    return trees


# Part 1 - Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees
# would you encounter?

print(tree_count(3, 1))

# Part 2 - What do you get if you multiply together the number of trees encountered on each of the listed slopes?
# (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)

print(tree_count(1, 1) * tree_count(3, 1) * tree_count(5, 1) * tree_count(7, 1) * tree_count(1, 2))
