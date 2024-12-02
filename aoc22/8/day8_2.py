import math

with open('data.txt') as data:
    a = []
    for row in data:
        a.append(row.strip('\n'))

length = len(a[0])


def distance(lista, v):
    pfd = []
    for x in lista:
        if int(x) >= v:
            pfd.append(int(x))
            break
        else:
            pfd.append(int(x))
    return len(pfd)


def det_viewing_score(fc, fr, v):
    left = []
    for col in range(0, fc):
        left.append(int(a[fr][col]))
    left.reverse()
    right = []
    for col in range(fc + 1, length):
        right.append(int(a[fr][col]))
    top = []
    for row in range(0, fr):
        top.append(int(a[row][fc]))
    top.reverse()
    down = []
    for row in range(fr + 1, length):
        down.append(int(a[row][fc]))

    return distance(left, v) * distance(right, v) * distance(top, v) * distance(down, v)


maxi = 0
for row in range(0, length):  # list
    for col in range(0, length):  # string
        check = det_viewing_score(int(col), int(row), int(a[row][col]))
        # print(int(col), int(row), int(a[row][col]), check)
        if check > maxi:
            maxi = check
print(maxi)
