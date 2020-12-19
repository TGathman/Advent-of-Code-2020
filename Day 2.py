import re

# Python 3.8, 19 December 2020

# Advent of Code 2020, Day 2 - See Directions/Day 2 Directions.txt for background.

data = []

# Store input in a list.

with open('Data Input\\Day 2 Input.txt', 'r') as file:
    for line in file:
        data.append(line.strip())

for index, item in enumerate(data):
    data[index] = re.split('-|: | ', item)

valid_passwords = 0

for password in data:
    if int(password[0]) <= password[3].count(password[2]) <= int(password[1]):
        valid_passwords += 1

print(valid_passwords)

valid_passwords = 0

for password_data in data:

    index_1 = int(password_data[0]) - 1
    index_2 = int(password_data[1]) - 1
    target = password_data[2]
    password = password_data[3]

    if (password[index_1] == target and password[index_2] != target) or \
            (password[index_1] != target and password[index_2] == target):
        valid_passwords += 1

print(valid_passwords)
