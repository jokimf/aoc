from itertools import combinations
matrix = []
unique_letters = set()
with open("input.txt") as data:
    for line in data:
        matrix.append(list(line.strip("\n")))
        unique_letters |= set(line.strip("\n"))
unique_letters.remove(".")


def find(letter):
    locations = []
    for i, line in enumerate(matrix):
        for j, symbol in enumerate(line):
            if matrix[i][j] == letter:
                locations.append((i, j))
    return locations


l = {x: find(x) for x in unique_letters}

unique_locations = set()
for letter, locations in l.items():
    for x in locations:
        unique_locations.add(x)
    if len(locations) == 0:  # and letter not in ["a"]:
        continue
    for (c1x, c1y), (c2x, c2y) in combinations(locations, 2):
        relative_x = c1x - c2x
        relative_y = c1y - c2y
        f, fail = 0, 0
        while True:
            f += 1
            antinode_1 = (c1x + relative_x * f), (c1y + relative_y * f)
            antinode_2 = (c2x + -1 * relative_x * f), (c2y + -1 * relative_y * f)
            for x, y in [antinode_1, antinode_2]:
                if not any([x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix)]):
                    unique_locations.add((x, y))
                    fail = 0
                else:
                    fail += 1
            if fail >= 4:
                break
print(len(unique_locations))
