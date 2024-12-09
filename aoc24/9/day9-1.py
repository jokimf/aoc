def flatten(xss):
    return [x for xs in xss for x in xs]


with open("input.txt") as data:
    data = [list(map(int, list(line.strip("\n")))) for line in data][0]

id = 0
new = []
for i, number in enumerate(data):
    if i % 2 == 0:
        new.append([id]*number)
        id += 1
    else:
        if number > 0:
            new.append(["."]*number)
new = flatten(new)
final = []
c = 0
for front in new:
    if front == ".":
        o = "."
        while o == ".":
            o = new.pop()
        final.append(o)
        c += 1
    else:
        final.append(front)
print(sum([i*x for i, x in enumerate(final) if x != "."]))
