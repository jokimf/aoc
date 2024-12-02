height_map = []
with open('data.txt') as data:
    for row in data:
        row = row.rstrip('\n')
        v = [ord(x) - 96 if x != 'E' and x != 'S' else 1 if x == 'S' else 26 for x in row]  # start: -13, goal: -27
        height_map.append(v)


def find_end():
    return 20, 72


def find_start():
    return 20, 0


def is_traversable(current, new):
    if current[0] < 0 or current[0] > 40 or current[1] < 0 or current[1] > 94 or \
            new[0] < 0 or new[0] > 40 or new[1] < 0 or new[1] > 94:
        return False
    return height_map[current[0]][current[1]] <= height_map[new[0]][new[1]] + 1


current = find_end()
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

bfs = dict()
bfs[current] = 0
check_next = {current}

while check_next:
    current = check_next.pop()
    for direction in directions:
        new_coordinates = current[0] + direction[0], current[1] + direction[1]
        if is_traversable(current, new_coordinates):
            if new_coordinates not in bfs or bfs[new_coordinates] > bfs[current] + 1:
                bfs[new_coordinates] = bfs[current] + 1
                check_next.add(new_coordinates)

haha = [bfs[x] for x in bfs if height_map[x[0]][x[1]] == 1]
haha.sort()
print(haha)