def get_valid_neighbour(row, col):
    val = m[row][col]
    total = 0
    if val == 9:
        return 1
    for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_row, new_col = row+x, col+y
        if new_row < 0 or new_row > len(m)-1 or new_col < 0 or new_col > len(m)-1:
            continue
        if m[new_row][new_col] == val + 1:
            total += get_valid_neighbour(new_row, new_col)
    return total


m = []
trailheads = []
with open("input.txt") as data:
    for index, line in enumerate(data):
        m.append(list(map(int, line.strip("\n"))))
        for sy_i, symbol in enumerate(line):
            if symbol == "0":
                trailheads.append((index, sy_i))
print(sum(get_valid_neighbour(*trailhead) for trailhead in trailheads))
