import re;print(sum([sum([x*y for x, y in [list(map(int, re.compile(r"\d+").findall(x))) for x in re.findall(r"mul\([0-9]+\,[0-9]+\)", l)]]) for l in open('input.txt')]))
