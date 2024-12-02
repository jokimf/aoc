# destination range start, source range start, range length
import sys
import itertools

with open('input.txt') as data:
    inp = data.read()

transformations = []
a = []
maps = [line for line in inp.split('\n') if all([sym.isnumeric() or sym == ' ' for sym in line])]
for tr in maps[1:]:
    if tr != '':
        a.append(tr)
    else:
        transformations.append(a)
        a = []
transformations.append(a)

old_seeds = [int(x) for x in inp.split('\n')[0].strip().split(':')[1].strip().split(' ')]
#seeds = list(itertools.chain(*[list(range(x, x+y)) for x,y in list(zip(old_seeds[::2], old_seeds[1::2]))])) # bluescreen me
seeds=[2]
pairs = list(zip(old_seeds[::2], old_seeds[1::2]))
pairs = sorted(pairs,key=lambda x:x[0])
print(pairs)

lowest = sys.maxsize
all_seeds = []
maxim = len(seeds)
for i, seed in enumerate(seeds):
    print(f'{i}/{maxim}')
    transformed_seed = seed
    for transformation in transformations:
        found = False
        for lv_map in transformation:
            if found:
                break
            s_dst, s_src, s_range = [int(x) for x in lv_map.split(' ')]
            if s_src <= transformed_seed < s_src + s_range:
                transformed_seed = transformed_seed - s_src + s_dst
                found = True
    all_seeds.append(transformed_seed)
print(all_seeds)
print(min(all_seeds))