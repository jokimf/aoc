from collections import defaultdict


def is_line_allowed(line: list[int], rules) -> bool:
    not_allowed_anymore = set()
    for number in line:
        if number not in not_allowed_anymore:
            not_allowed_anymore |= rules.get(number, set())
        else:
            return False
    return True


def identify_wrong_index(line: list[int], rules) -> bool:
    not_allowed_anymore = set()
    for index, number in enumerate(line):
        if number not in not_allowed_anymore:
            not_allowed_anymore |= rules.get(number, set())
        else:
            return index
    return None


with open("input.txt") as data:
    rules, all_sequences = defaultdict(set), []
    for line in data:
        if "|" in line:
            a, b = list(map(int, line.strip("\n").split("|")))
            rules[b].add(a)
        elif "," in line:
            all_sequences.append([int(n) for n in line.strip("\n").split(",")])

incorrect = []
for line in all_sequences:
    if not is_line_allowed(line, rules):
        incorrect.append(line)


new = []
for line in incorrect:
    while True:
        wrong_index = identify_wrong_index(line, rules)
        if wrong_index is not None:
            wrong_number = line[wrong_index]
            line[wrong_index] = line[wrong_index - 1]
            line[wrong_index - 1] = wrong_number
        else:
            break
    new.append(line)

c = 0
for line in new:
    if is_line_allowed(line, rules):
        c += line[len(line) // 2]
print(c)
