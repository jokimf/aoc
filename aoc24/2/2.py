def is_safe(a,b):
    return abs(a - b) < 4

with open('input.txt') as data:
    b = 0
    for line in data:
        a = line.split(" ")
        a = list(map(int, a))
        x = list(zip(a,a[1:]))
        mode = "asc" if x[0][0] < x[0][1] else "desc"
        fail = False
        for z in x:
            if z[0] < z[1] and mode == "asc" and is_safe(z[0], z[1]):
                continue
            elif z[0] > z[1] and mode == "desc" and is_safe(z[0], z[1]):
                continue
            else:
                fail = True
                break
        if not fail:
            b = b + 1

    print(b)


