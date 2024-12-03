import re

with open("input.txt") as data:
    cleaned = []
    for i, randomchars in enumerate("".join([line for line in data]).split("don't()")):
        valid = randomchars.split("do()")
        if i == 0:
            cleaned += valid
        else:
            cleaned += valid[1:]
<<<<<<< HEAD
c = 0
for line in cleaned:
    a = re.findall(r"mul\([0-9]+\,[0-9]+\)", line)
    b = [list(map(int, re.compile(r"\d+").findall(x))) for x in a]
    c += sum([x*y for x, y in b])
print(c)
=======
    c = 0
    for line in cleaned:
       a = re.findall(r"mul\([0-9]+\,[0-9]+\)", line)
       b = [list(map(int, re.compile(r"\d+").findall(x))) for x in a]
       c += sum([x*y for x, y in b])
    print(c)
>>>>>>> e130c845af8694ac5fe1748e3ee84b846afe0021
