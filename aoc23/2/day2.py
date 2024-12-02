
constraints = [12, 13, 14]  # rgb


def parse_reveals(inputa: str):
    cubes = inputa.split(',')
    [x.strip('\n') for x in cubes]
    r, g, b = 0, 0, 0
    for cube in cubes:
        cube = cube.strip()
        value, name = cube.split(' ')
        if name == 'red':
            r = int(value)
        elif name == 'green':
            g = int(value)
        elif name == 'blue':
            b = int(value)
    return r, g, b


def is_possible(game: str):
    game.strip('\n')
    _, a = game.split(':')
    reveals = a.split(';')

    r_1, g_1, b_1 = 0, 0, 0
    for reveal in reveals:
        r, g, b = parse_reveals(reveal)
        r_1 = max(r_1, r)
        g_1 = max(g_1, g)
        b_1 = max(b_1, b)

    return r_1 <= constraints[0] and g_1 <= constraints[1] and b_1 <= constraints[2]


with open('input.txt') as data:
    suma = 0
    for gameid, game in enumerate(data):
        game = game.strip('\n')
        if is_possible(game):
            suma += int(gameid) + 1
    print(suma)
