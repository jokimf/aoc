maps = [str(x) for x in [0,1,2,3,4,5,6,7,8,9]]
with open('input.txt') as data:
    suma = 0
    best_index = 10000000
    for line in data:
        for symbol in maps:
            first = line.find(symbol)
            if first < best_index and first >= 0:
                best_index = first
                best_1 = symbol
        print(line, best_index,best_1)

    best_index = 100000000
    for line in data:
        line = reversed(line)
        for symbol in maps:
            first = line.find(symbol)
            if first < best_index and first >= 0:
                best_index = first
                best_2 = symbol
        suma += int(best_1 + best_2)
        print(best_1 + best_2, line)

print(suma)
