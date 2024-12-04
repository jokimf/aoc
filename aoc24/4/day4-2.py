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
            return False
        return matrix[row_i][symbol_i] == neighbour
    except IndexError:
        return False
    
def check_for_MAS(check_dir, dire, opposite, cross_1, cross_2):
    if dire == check_dir:
        if has_neighbour_at_direction(row_i, symbol_i, "S", opposite):
            if has_neighbour_at_direction(row_i, symbol_i, "M", cross_1) and has_neighbour_at_direction(row_i, symbol_i, "S", cross_2) or \
                has_neighbour_at_direction(row_i, symbol_i, "M", cross_2) and has_neighbour_at_direction(row_i, symbol_i, "S", cross_1):
                return True
    return False

with open('input.txt') as data:
    matrix = []
    for line in data:
        matrix.append(list(line.strip("\n")))
c = 0
for row_i, row in enumerate(matrix):
    for symbol_i, symbol in enumerate(row):
        if symbol == 'A':
            for dire in ["ul","ur","dl","dr"]:
                if has_neighbour_at_direction(row_i, symbol_i, "M", dire):
                    if any((check_for_MAS(dire, "ul", "dr", "ur", "dl"), 
                         check_for_MAS(dire, "ur", "dl", "ul", "dr"),
                         check_for_MAS(dire, "dl", "ur", "ul", "dr"),
                         check_for_MAS(dire, "dr", "ul", "ur", "dl"))):
                        c += 1
                        break

print(c)

