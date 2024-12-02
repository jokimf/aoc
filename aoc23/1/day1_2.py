def to_n(ins):
    if len(ins) == 1:
        return int(ins)
    else:
        return {'one': 1, 'two': 2, 'three': 3, 'four': 4,
                'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}[ins]


with open('input.txt') as data:
    lf = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
          'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine']
    suma = 0
    for line in data:
        best_index = 100000000
        best_1 = None
        best_2 = None
        indeces = {}
        for x in lf:
            index = line.find(x)
            if index < best_index and index >= 0:
                best_1 = to_n(x)
                best_index = index

        best_index = 10000000
        for x in [y[::-1] for y in lf]:
            index = line[::-1].find(x)
            if index < best_index and index >= 0:
                best_2 = to_n(x[::-1])
                best_index = index

        toadd = int(str(best_1) + str(best_2))
        suma += toadd
    print(suma)
