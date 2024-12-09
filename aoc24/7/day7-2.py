
from itertools import product
lines = dict()
with open("input.txt") as data:
    for line in data:
        result, values = line.split(": ")
        lines.update({int(result): list(map(int, values.split(" ")))})

def is_possible(result, values):
    operator_combinations = product("+*&", repeat=len(values) - 1)
    for operators in operator_combinations:
        intermediate = values[0]
        for value, operator in zip(values[1:], operators):
            operator = "" if operator == "&" else operator
            intermediate = eval(f"{intermediate}{operator}{value}")
            if result == intermediate:
                return result
    return 0


print(sum([is_possible(r, v) for r, v in lines.items()]))
