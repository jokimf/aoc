'''
    [C]             [L]         [T]
    [V] [R] [M]     [T]         [B]
    [F] [G] [H] [Q] [Q]         [H]
    [W] [L] [P] [V] [M] [V]     [F]
    [P] [C] [W] [S] [Z] [B] [S] [P]
[G] [R] [M] [B] [F] [J] [S] [Z] [D]
[J] [L] [P] [F] [C] [H] [F] [J] [C]
[Z] [Q] [F] [L] [G] [W] [H] [F] [M]
 1   2   3   4   5   6   7   8   9
'''
stacks = [[], [], [], [], [], [], [], [], []]


def move(n, f, to):
    a = stacks[f][-n:]
    stacks[to] += a
    stacks[f] = stacks[f][:len(stacks[f]) - n]


with open('data.txt') as data:
    first = []
    for line in data:
        if line[1].isnumeric():
            break
        else:
            first.insert(0, line.strip('\n').replace('[', '').replace('] ', '').replace('    ', ' ').replace(']', ''))

    for x in first:
        for i, symbol in enumerate(x):
            if symbol != ' ':
                stacks[i].append(symbol)

    # move 1 from 5 to 6
    for line in data:
        if line[0] == 'm':
            split = line.split(' ')
            move(int(split[1]), int(split[3]) - 1, int(split[5]) - 1)

    print([x[-1] for x in stacks])
