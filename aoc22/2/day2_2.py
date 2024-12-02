def path(their, you_have_to):
    if you_have_to == "X":  # x lose
        if their == "A":
            return score("A", "Z")
        if their == "B":
            return score("B", "X")
        if their == "C":
            return score("C", "Y")
    elif you_have_to == "Y":  # y draw
        if their == "A":
            return score("A", "X")
        if their == "B":
            return score("B", "Y")
        if their == "C":
            return score("C", "Z")
    elif you_have_to == "Z":  # z win
        if their == "A":
            return score("A", "Y")
        if their == "B":
            return score("B", "Z")
        if their == "C":
            return score("C", "X")


def score(my, theirs):
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
        sum += path(my, their)
    print(sum)
