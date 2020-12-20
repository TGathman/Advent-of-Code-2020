# Python 3.8, 19 December 2020

# Advent of Code 2020, Day 2 - See Directions/Day 2 Directions.txt for background.

import re

data = [line.strip() for line in open('Data Input\\Day 2 Input.txt', 'r')]

for index, item in enumerate(data):
    data[index] = re.split('-|: | ', item)

# Part 1 - How many passwords are valid according to their policies?

valid_passwords = 0

# data now stores passwords as such [['2', '6', 'a', 'aaaaa']]: index 0 = min, index 1 = max, index 2 = letter,
# index 3 = password.

for password in data:
    if int(password[0]) <= password[3].count(password[2]) <= int(password[1]):
        valid_passwords += 1

print(valid_passwords)

# Part 2 - How many passwords are valid according to the new interpretation of the policies?

valid_passwords = 0

# Converts indices, checks if target is in only one target index.

for password_data in data:

    index_1 = int(password_data[0]) - 1
    index_2 = int(password_data[1]) - 1
    target = password_data[2]
    password = password_data[3]

    if (password[index_1] == target and password[index_2] != target) or \
            (password[index_1] != target and password[index_2] == target):
        valid_passwords += 1

print(valid_passwords)
