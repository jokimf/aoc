import re

with open('input.txt') as data:
    c = 0
    for line in data:
       a = re.findall(r"mul\([0-9]+\,[0-9]+\)", line)
       b = [list(map(int, re.compile(r"\d+").findall(x))) for x in a]
       c += sum([x*y for x, y in b])
    print(c)