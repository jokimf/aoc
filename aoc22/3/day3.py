def score2(string: str) -> int:
    score = ord(string) - 96 if string.islower() else ord(string) - 38
    print(f'scoring {score} for {string}')
    return score


with open('data.txt') as data:
    score = 0
    for item in data:
        item = item.strip('\n')
        length = len(item)
        first = item[:length // 2]
        scnd = item[length // 2:]
        print(item, length, first, scnd, len(first), len(scnd))
        intr = set(first).intersection(set(scnd)).pop()
        print(intr)
        score = score + score2(intr)
    print(score)
