from collections import Counter

with open('input.txt') as data:
    a, b = [], []
    for row in data:
        x, y = row.split("   ")
        a.append(int(x))
        b.append(int(y))
    b = Counter(b)
print(sum([x * b[x] for x in a]))
