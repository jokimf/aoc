def winnings(game:str) -> int:
    win_raw, have_raw = game.split('|')    
    win,have = set(win_raw.split(':')[1].strip().split(' ')), set(have_raw.strip().split(' '))
    winning_numbers = len(win.intersection(have))
    winnings = 2 ** (winning_numbers-1) if winning_numbers != 0 else 0
    return winnings

points = 0
with open('input.txt') as data:
    for line in data:
        line = line.replace('  ',' ')
        points += winnings(line)
print(points)