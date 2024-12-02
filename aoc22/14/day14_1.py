cave = {(500, 0): 'S'}


def draw_rocks(start: list, end: list):
    first = range(int(start[0]), int(end[0]) + 1) if int(start[0]) < int(end[0]) else range(int(end[0]),
                                                                                            int(start[0]) + 1)
    second = range(int(start[1]), int(end[1]) + 1) if int(start[1]) < int(end[1]) else range(int(end[1]),
                                                                                             int(start[1]) + 1)
    for x in first:
        for y in second:
            cave[(x, y)] = '#'


def is_blocked(current_position: tuple, direction: str):
    if direction == 'down':
        return (current_position[0], current_position[1] + 1) in cave
    elif direction == 'downleft':
        return (current_position[0] - 1, current_position[1] + 1) in cave
    elif direction == 'downright':
        return (current_position[0] + 1, current_position[1] + 1) in cave
    else:
        raise ValueError()


with open('data.txt') as data:
    for row in data:
        row = row.strip('\n').split(' -> ')
        for i in range(len(row) - 1):
            draw_rocks(row[i].split(','), row[i + 1].split(','))

abyss = False
position = (500, 0)
while not abyss:
    if position[1] > 10000:
        abyss = True
        break
    # Spawn new sand
    if not is_blocked(position, 'down'):
        position = (position[0], position[1] + 1)
    elif not is_blocked(position, 'downleft'):
        position = (position[0] - 1, position[1] + 1)
    elif not is_blocked(position, 'downright'):
        position = (position[0] + 1, position[1] + 1)
    else:
        cave[position] = 'o'
        position = (500, 0)
print(len([x for x in cave.values() if x == 'o']))
