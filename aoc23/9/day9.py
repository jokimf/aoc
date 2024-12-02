with open('input.txt') as data:
    values = []
    for line in data:
        values.append([int(x) for x in line.strip().split(' ')])

def det_diff(seq):
    d = []
    for i in range(len(seq)-1):
        d.append(seq[i+1] - seq[i])
    return d

total = 0
for sequence in values:
    all_diffs = [sequence]
    while any(n != 0 for n in sequence):
        diffs = det_diff(sequence)
        all_diffs.append(diffs)
        sequence = diffs
    total += sum([x[-1] for x in all_diffs])
print(total)
