class Dir:
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.sub = []
        self.files = []

    def __repr__(self):
        return f'{self.name}:{self.files + self.sub}'

    def __int__(self):
        return sum([int(z) for z in self.sub]) + sum([int(y) for y in self.files])


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __repr__(self):
        return f'{self.name}-{self.size}'

    def __int__(self):
        return self.size


root = Dir('/', None)
current: Dir = root
all_dirs = [root]
with open('data.txt') as data:
    for x in data:
        x = x.strip('\n')
        a = x.split(' ')
        if a[0].startswith('$'):
            if a[1] == 'cd':  # $ cd dsa
                if a[2] == '/':  # cd /
                    current = root
                elif a[2] == '..':
                    current = current.parent
                else:
                    current = [x for x in current.sub if x.name == a[2]][0]

        elif a[0].isnumeric():  # 23123 gfddg
            current.files.append(File(a[1], int(a[0])))
        else:  # dir dasdsa
            new_dir = Dir(a[1], current)
            current.sub.append(new_dir)
            all_dirs.append(new_dir)

print(sum([int(x) for x in all_dirs if int(x) <= 100000]))

# Part2
max_capacity = 70000000
update_requires = 30000000
used_space = int(root)
free_space = max_capacity - used_space
needed_space = update_requires - free_space

best_dir = None
minim = 10000
for x in all_dirs:
    if needed_space - int(x) <= 0:
        if best_dir is None or int(x) < minim:
            best_dir = x
            minim = int(x)
print(minim)
