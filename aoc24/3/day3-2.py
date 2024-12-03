import re

with open("input.txt") as data:
    cleaned = []
    for i, randomchars in enumerate("".join([line for line in data]).split("don't()")):
        valid = randomchars.split("do()")
        if i == 0:
            cleaned += valid
        else:
            cleaned += valid[1:]
print(sum([sum([x*y for x, y in [list(map(int, re.compile(r"\d+").findall(x))) for x in re.findall(r"mul\([0-9]+\,[0-9]+\)", l)]]) for l in cleaned]))

