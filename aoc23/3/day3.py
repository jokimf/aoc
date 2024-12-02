global_map = []


def find_neighbours(row, col):
    adjacencies = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbours = []
    for adj in adjacencies:
        new = adj[0] + row, adj[1] + col
        if new[0] < 0 or new[1] < 0 or new[0] >= len(global_map) or new[1] >= len(global_map):
            continue
        neighbours.append(global_map[new[0]][new[1]])
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
    return number, new_col


numbers = []
with open('input.txt') as data:

    # Add all known symbols to a set, also create nested list for the whole input
    symbols = set()
    for line_index, line in enumerate(data):
        line = line.strip('\n')
        global_map.append(list(line))
        for symbol in line:
            symbols.add(symbol)

# Filter unwanted symbols
symbols = symbols - {'0','1','2','3','4','5','6','7','8','9','.'}

# Iterate through nested list, look for numbers
for row in range(len(global_map)):
    new_col = 0
    for col in range(len(global_map)):
        if not global_map[row][col].isnumeric() or col <= new_col:
            continue

        # If number symbol is found, find neighbours
        neighbours = find_neighbours(row, col)
        if len(symbols & neighbours) != 0:

            # If number symbol has operator symbol as neighbour, figure out which whole number it belongs to
            # And make sure that this number is now disregarded in the future... >:(
            number, new_col = determine_number(row, col)
            numbers.append(number)

print(sum(map(int, numbers)))