cycle = 0
total = 0
    

with open('data.txt') as data:
    signal_strength = 0 
    x = 1
    for i, row in enumerate(data):
        split = row.strip('\n').split(' ')
        cmd=split[0]
        value = split[1] if len(split)>1 else None
        if cmd == 'noop':
            cycle += 1
            print(f'C{cycle} begins (noop), x={x}')
            signal_strength = cycle * x
            if cycle in [20,60,100,140,180,220]:
                total += signal_strength
                print("ADDED1",cycle, signal_strength,total)
        elif cmd == 'addx':
            cycle += 1
            print(f'C{cycle} begins (addx1), x={x}')
            signal_strength = cycle * x
            if cycle in [20,60,100,140,180,220]:
                total += signal_strength
                print("ADDED2",cycle, signal_strength,total)
            cycle += 1
            signal_strength = cycle * x
            if cycle in [20,60,100,140,180,220]:
                total += signal_strength
                print("ADDED3",cycle, signal_strength,total)
            print(f'C{cycle} begins (addx2), x={x}')
            # Finish cmd
            x += int(value)
        print(f'After cycle {cycle}:{x}')
        #if cycle in [20,60,100,140,180,220]:
        #    total += signal_strength
        #    print(cycle, signal_strength,total)
print(total)

