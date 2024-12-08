from collections import Counter

def new_direction(x):
    v = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    return v[(v.index(x) + 1) % 4]


matrix = []
with open("input.txt") as data:
    for i, line in enumerate(data):
        matrix.append(line.strip("\n"))

        if "^" in line:
            current_coordinates = i, line.find("^")

dire = -1, 0
distinct = set()
distinct.add(current_coordinates)
while True:
    next_coordinates = current_coordinates[0] + dire[0], current_coordinates[1] + dire[1]
    try:
        if matrix[next_coordinates[0]][next_coordinates[1]] == "#":
            dire = new_direction(dire)
        else:
            current_coordinates = next_coordinates
            distinct.add(current_coordinates)
    except IndexError:
        break
print(len(distinct))
