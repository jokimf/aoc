with open('data.txt') as data:
    best = 0
    sum = 0
    for item in data:
        if item == "\n":
            best = max(sum, best)
            sum = 0
        else:
            sum = int(item) + int(sum)
    print(best)
