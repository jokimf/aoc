import aocu.util as u
import itertools

print(sum(int(x < y) for x, y in itertools.pairwise(u.load("./aoc21/1/input.txt", int))))
