stacks = [[], [], [], [], [], [], [], [], []]


def move(n, f, to):
    a = stacks[f][-n:]
    a.reverse()
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

    for line in data:
        if line[0] == 'm':
            split = line.split(' ')
            move(int(split[1]), int(split[3]) - 1, int(split[5]) - 1)

    print([x[-1] for x in stacks])
