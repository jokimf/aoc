with open('input.txt') as data:
    a, b = [], []
    for row in data:
        x, y = row.split("   ")
        a.append(int(x))
        b.append(int(y))
a, b = sorted(a), sorted(b)
print(sum([abs(h-g) for g, h in zip(a, b)]))
