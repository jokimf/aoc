with open('data.txt') as data:
    a = []
    for row in data:
        a.append(row.strip('\n'))

length = len(a[0])


def check_if_visible(fc, fr, v):
    return all([int(a[fr][col]) < v for col in range(0, fc)]) or \
           all([int(a[fr][col]) < v for col in range(fc + 1, length)]) or \
           all([int(a[row][fc]) < v for row in range(0, fr)]) or \
           all([int(a[row][fc]) < v for row in range(fr + 1, length)])


sum = 0
s = [[True, True, True, True, True],
     [True, True, True, False, True],
     [True, True, False, True, True],
     [True, False, True, False, True],
     [True, True, True, True, True]]
for row in range(0, length):  # list
    for col in range(0, length):  # string
        check = check_if_visible(int(col), int(row), int(a[row][col]))
        sum += int(check)
print(sum)
