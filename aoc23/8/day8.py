from itertools import cycle

with open('input.txt') as data:
    directions = data.readline().strip('\n')
    data.readline()
    
    lu = dict()
    for line in data:
        key, _, first, second = line.split(' ')
        first = first.replace('(','').replace(',','')
        second = second.strip(')\n')
        lu[key] = (first,second)

lookup = 'AAA'
c = 0
for d in cycle(directions):
    lookup = lu[lookup][0 if d == 'L' else 1]
    c += 1
    if lookup == 'ZZZ':
        break
print(c)