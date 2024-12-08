def new_direction(x):
    v = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    return v[(v.index(x) + 1) % 4]


blocks, checked = set(), set()


def try_for_infinity(m, current_coordinates, next_coordinates, dire, start):
    visited_on_this_try = set()
    block = current_coordinates[0] + dire[0], current_coordinates[1] + dire[1]
    if block == start or block in checked:
        return 0
    checked.add(block)
    m[block[0]][block[1]] = "#"  # Block path
    while True:
        next_coordinates = current_coordinates[0] + dire[0], current_coordinates[1] + dire[1]
        if next_coordinates[0] < 0 or next_coordinates[0] >= len(m) or next_coordinates[1] < 0 or next_coordinates[1] >= len(m):
            m[block[0]][block[1]] = "."  # Unblock
            return 0
        if (current_coordinates, dire) in visited_on_this_try:
            m[block[0]][block[1]] = "."  # Unblock
            blocks.add(block)
            return 1
        visited_on_this_try.add((current_coordinates, dire))
        
        if m[next_coordinates[0]][next_coordinates[1]] == "#":
            dire = new_direction(dire)
        else:
            current_coordinates = next_coordinates  # advance


matrix = []
with open("input.txt") as data:
    for i, line in enumerate(data):
        matrix.append(list(line.strip("\n")))
        if "^" in line:
            current_coordinates = i, line.index("^")
            start = i, line.index("^")

dire = -1, 0
c = 0
while True:
    next_coordinates = current_coordinates[0] + dire[0], current_coordinates[1] + dire[1]
    if next_coordinates[0] < 0 or next_coordinates[0] >= len(matrix) or next_coordinates[1] < 0 or next_coordinates[1] >= len(matrix):
        break
    if matrix[next_coordinates[0]][next_coordinates[1]] == "#":
        dire = new_direction(dire)
    else:
        c += try_for_infinity(matrix, current_coordinates, next_coordinates, dire, start)
        current_coordinates = next_coordinates  # advance
print(c)

# for line in sorted(list(blocks)):
#     print(f"{line[0]},{line[1]}")
