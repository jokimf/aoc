from functools import cmp_to_key


def compare(left, right) -> int:  # correct order is -1
    if isinstance(left, list) and isinstance(right, list):
        minimum = min(len(left), len(right))
        for i in range(minimum):
            a = compare(left[i], right[i])
            if a != 0:
                return a
        if len(left) > len(right):
            return 1
        elif len(left) < len(right):
            return -1
        else:
            return 0

    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, int) and isinstance(right, int):
        return -1 if left < right else 0 if left == right else 1


with open('data.txt') as data:
    allPFDs = []
    divider_packet1 = [[2]]
    divider_packet2 = [[6]]
    allPFDs.append(divider_packet1)
    allPFDs.append(divider_packet2)

    for row in data:
        row = row.strip('\n')
        if row != '':
            allPFDs.append(eval(row))
a = sorted(allPFDs, key=cmp_to_key(compare))
print((a.index(divider_packet1) + 1) * (a.index(divider_packet2) + 1))
