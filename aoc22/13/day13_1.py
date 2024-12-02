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
    value = 0
    pair = 1
    left, right = '', ''
    for row in data:
        row = row.strip('\n')
        if row == '':
            continue

        if left != '':
            right = eval(row)
        else:
            left = eval(row)

        if left != '' and right != '':
            # eval
            das = compare(left, right)
            print(left, right, das)
            if das == -1:
                value += pair

            # Reset 😂
            pair += 1
            left, right = '', ''
print(value)
