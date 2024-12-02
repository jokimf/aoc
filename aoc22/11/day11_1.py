monkeys = []


class Monkey:
    def __init__(self, starting_items, operation, test, if_true, if_false):
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.total_inspected = 0

    def __repr__(self):
        return f'{self.starting_items}, {self.operation}, {self.test}, {self.if_true}, {self.if_false}|'

    def throw_item_to(self, item, to):
        print(self.starting_items)
        print(f'Throwing {item} to {to}')
        global monkeys
        monkeys[to].starting_items.append(item)

    def take_turn(self):
        for item in self.starting_items:
            print(f'Inspecting {item}')
            self.total_inspected += 1
            item = self.operation(item)
            item = item // 3
            print(f'New weight: {item}')
            if item % self.test == 0:
                self.throw_item_to(item, self.if_true)
            else:
                self.throw_item_to(item, self.if_false)
        self.starting_items = []


input_file = 'data.txt'
with open(input_file) as data:
    s, o, t, ift, iff = None, None, None, None, None
    if input_file == 'data2.txt':
        operations = [lambda x: x + 3, lambda x: x * x, lambda x: x + 6, lambda x: x * 19]
    else:
        operations = [lambda x: x * 7, lambda x: x + 8, lambda x: x + 4, lambda x: x + 3, lambda x: x + 2,
                      lambda x: x + 6, lambda x: x * x, lambda x: x * 13]
    for row in data:
        x = row.strip('\n')
        if x.startswith("  S"):
            s = x[18:].split(', ')
            s = [int(x) for x in s]
        elif x.startswith("  O"):
            o = operations.pop()
        elif x.startswith("  T"):
            split = x[5:].split(' ')
            t = int(split[3])
        elif x.startswith("    If true: throw to monkey "):
            ift = int(x[29])
        elif x.startswith("    If false: throw to monkey "):
            iff = int(x[30])
        elif x == '':
            monkeys.append(Monkey(s, o, t, ift, iff))

print(monkeys)

for i in range(0, 20):
    print(f'Round {i}')
    for m in monkeys:
        print('Monkey')
        m.take_turn()

for m in monkeys:
    print(m.total_inspected)
