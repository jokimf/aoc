import re

with open("input.txt") as data:
    cleaned = []
    for i, randomchars in enumerate("".join([line for line in data]).split("don't()")):
        valid = randomchars.split("do()")
        if i == 0:
            cleaned += valid
        else:
            cleaned += valid[1:]
    c = 0
    for line in cleaned:
       a = re.findall(r"mul\([0-9]+\,[0-9]+\)", line)
       b = [list(map(int, re.compile(r"\d+").findall(x))) for x in a]
       c += sum([x*y for x, y in b])
    print(c)