def winnings(game:str, game_number:int) -> int:
    win_raw, have_raw = game.split('|')    
    win,have = set(win_raw.split(':')[1].strip().split(' ')), set(have_raw.strip().split(' '))
    winning_numbers = len(win.intersection(have))
    
    for i in range(winning_numbers):
        multipliers[game_number+1+i] = multipliers[game_number+1+i] + 1

points = 0
with open('input.txt') as data:
    multipliers = {x: 1 for x in range(1,213)}
    total = 0
    for index, line in enumerate(data):
        card = index + 1
        line = line.replace('  ',' ')
        
        for executions in range(multipliers[card]):
            winnings(line, card)
            total+=1

print(total, multipliers) # takes about 3 minutes but if it works it works gell