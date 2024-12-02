
constraints = [12, 13, 14]  # rgb


def parse_reveals(inputa: str):
    cubes = inputa.split(',')
    [x.strip('\n') for x in cubes]
    r, g, b = 0, 0, 0
    # print(cubes)
    for cube in cubes:
        cube = cube.strip()
        value, name = cube.split(' ')
        if name == 'red':
            r = int(value)
        elif name == 'green':
            g = int(value)
        elif name == 'blue':
            b = int(value)
    # print('retunring', r, g, b)
    return r, g, b


def is_possible(game: str):
    game.strip('\n')
    useless, a = game.split(':')
    reveals = a.split(';')

    r_1, g_1, b_1 = 0, 0, 0
    for reveal in reveals:
        r, g, b = parse_reveals(reveal)
        # print(r, g, b)
        r_1 = max(r_1, r)
        g_1 = max(g_1, g)
        b_1 = max(b_1, b)

    # print(useless, r_1, g_1, b_1)
    return r_1 * g_1 * b_1


with open('input.txt') as data:
    suma = 0
    for gameid, game in enumerate(data):
        game = game.strip('\n')
        power = is_possible(game)
        print(power)
        suma += power
    print(suma)
