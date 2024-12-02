with open('data.txt') as data:
    sum = 0
    best = []
    for item in data:
        if item == "\n":
            best.append(sum)
            sum = 0
        else:
            sum = int(item) + int(sum)
    best.sort()
    print(best)
