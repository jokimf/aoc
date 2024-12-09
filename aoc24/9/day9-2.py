from collections import Counter


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
counter = Counter(new)
nextn = sorted([int(x) for x in counter.keys() if x != "."], reverse=True)

for num in nextn:
    dots = 0
    for index, symbol in enumerate(new):
        if symbol == num:
            break
        if symbol == ".":
            dots += 1
        else:
            dots = 0

        if dots == counter[num]:
            new = [x if x != num else "." for x in new]
            new = new[:index-dots+1] + [num] * dots + new[index+1:]
            break
print(sum([i*x for i, x in enumerate(new) if x != "."]))
