def det(my, theirs):
    if my == "A":
        if theirs == "X":
            return 1 + 3
        elif theirs == "Y":
            return 2 + 6
        elif theirs == "Z":
            return 3 + 0
    elif my == "B":
        if theirs == "X":
            return 1 + 0
        if theirs == "Y":
            return 2 + 3
        if theirs == "Z":
            return 3 + 6
    elif my == "C":
        if theirs == "X":
            return 1 + 6
        elif theirs == "Y":
            return 2 + 0
        elif theirs == "Z":
            return 3 + 3


with open('data.txt') as data:
    sum = 0
    for line in data:
        my = line.split(" ")[0]
        their = line.split(" ")[1].strip("\n")
        sum += det(my, their)
    print(sum)
