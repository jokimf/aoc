import aocu.util as u
import itertools

n = list(u.load("./aoc21/1/input.txt", int))

print(sum(int(sum(x) < sum(y)) for x, y in itertools.pairwise(zip(n, n[1:], n[2:]))))
