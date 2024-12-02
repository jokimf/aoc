def distance(x, y, cx, cy):
    return sum(abs(val1 - val2) for val1, val2 in [(x, cx), (y, cy)])


sensors = []
with open('data.txt') as pdf:
    for line in pdf:
        a = line.split(' ')
        x = int(a[2].split('=')[1].strip(','))
        y = int(a[3].split('=')[1].strip(':'))
        cx = int(a[8].split('=')[1].strip(','))
        cy = int(a[9].split('=')[1])
        sensors.append((x, y, cx, cy, distance(x, y, cx, cy)))

row = 2000000


def can_reach(x, y, tx, ty, DISTANZ):
    return distance(x, y, tx, ty) <= DISTANZ


limit = max(
    [max(abs(pfd[0] + pfd[4]), abs(pfd[0] - pfd[4]), abs(pfd[1] + pfd[4]), abs(pfd[1] - pfd[4])) for pfd in sensors])
inter = set()
for af, s in enumerate(sensors):
    for i in range(-limit, limit):
        if can_reach(i, row, s[0], s[1], s[4]) and not (i == s[2] and row == s[3]):
            inter.add(i)
    print(s)
print(len(inter))
# 4861076