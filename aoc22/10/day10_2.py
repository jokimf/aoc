cycle = 0

pixel_i = -1
screen_str = ''
def screen(x):
    global pixel_i
    global screen_str
    pixel_i +=1
    if pixel_i > 39:
        pixel_i = 0
        screen_str += '\n'
    drawn = [x-1,x,x+1]
    if pixel_i in drawn:
        screen_str += '#'
    else:
        screen_str += '.'
    

with open('data.txt') as data:
    x = 1
    for i, row in enumerate(data):
        split = row.strip('\n').split(' ')
        cmd=split[0]
        value = split[1] if len(split)>1 else None
        if cmd == 'noop':
            cycle += 1
            screen(x)
        elif cmd == 'addx':
            cycle += 1
            screen(x)
            cycle += 1
            screen(x)
            # Finish cmd
            x += int(value)
print(screen_str)
# 40 wide, 6 high