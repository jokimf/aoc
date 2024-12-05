from collections import defaultdict


def is_line_allowed(line: list[int], rules) -> bool:
    not_allowed_anymore = set()
    for number in line:
        if number not in not_allowed_anymore:
            not_allowed_anymore |= rules.get(number, set())
        else:
            return False
    return True


with open("input.txt") as data:
    rules, all_sequences = defaultdict(set), []
    for line in data:
        if "|" in line:
            a, b = list(map(int, line.strip("\n").split("|")))
            rules[b].add(a)
        elif "," in line:
            all_sequences.append([int(n) for n in line.strip("\n").split(",")])

c = 0
for line in all_sequences:
    if is_line_allowed(line, rules):
        c += line[len(line) // 2]
print(c)
