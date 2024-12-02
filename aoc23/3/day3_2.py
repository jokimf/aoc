global_map = []


def find_neighbours(row, col):
    adjacencies = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbours = []
    for adj in adjacencies:
        new = adj[0] + row, adj[1] + col
        if new[0] < 0 or new[1] < 0 or new[0] >= len(global_map) or new[1] >= len(global_map):
            continue
        neighbours.append((global_map[new[0]][new[1]], new[0], new[1]))
    return set(neighbours)


def determine_number(row, col):
    number = ''
    # Check to the left
    new_col = col
    while True:
        if not new_col < 0 and global_map[row][new_col].isnumeric():
            number = global_map[row][new_col] + number
            new_col = new_col - 1
        else:
            break

    # Check to the right
    new_col = col + 1
    while True:
        if not new_col >= len(global_map) and global_map[row][new_col].isnumeric():
            number = number + global_map[row][new_col]
            new_col = new_col + 1
        else:
            break
    return number


numbers = set()
with open('input.txt') as data:
    # Create nested list for the whole input
    for line_index, line in enumerate(data):
        line = line.strip('\n')
        global_map.append(list(line))

# Iterate through nested list, look for *
for row in range(len(global_map)):
    for col in range(len(global_map)):
        if global_map[row][col] == '*':
            # If found, look at neighbours
            neighbours = find_neighbours(row, col)
            gear_neighbours = set()

            # Then determine numbers, disregard duplicates
            # (This fails if the same number borders the same gear :])
            for neighbour, nrow, ncol in neighbours:
                if neighbour.isnumeric():
                    n = determine_number(nrow, ncol)
                    gear_neighbours.add(n)
            
            if len(gear_neighbours) == 2:
                numbers.add(int(gear_neighbours.pop()) * int(gear_neighbours.pop()))

print(sum(numbers))