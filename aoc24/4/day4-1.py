def has_neighbour_at_direction(row_i, symbol_i, neighbour, direction):
    try:
        if "u" in direction: 
            row_i -= 1
        if "d" in direction:
            row_i += 1
        if "l" in direction:
            symbol_i -= 1
        if "r" in direction:
            symbol_i += 1
        if symbol_i < 0 or row_i < 0:
            return False, 0, 0
        return matrix[row_i][symbol_i] == neighbour, row_i, symbol_i
    except IndexError:
        return False, 0, 0

with open('input.txt') as data:
    matrix = []
    for line in data:
        matrix.append(list(line.strip("\n")))
c = 0
for row_i, row in enumerate(matrix):
    for symbol_i, symbol in enumerate(row):
        if symbol == 'X':
            for dire in ["u","d","l","r","ul","ur","dl","dr"]:
                v, new_r, new_s = has_neighbour_at_direction(row_i, symbol_i, "M", dire)
                if v:
                    v, new_r, new_s = has_neighbour_at_direction(new_r, new_s, "A", dire)
                    if v:
                        v, new_r, new_s = has_neighbour_at_direction(new_r, new_s, "S", dire)
                        if v:
                            c += 1
print(c)

