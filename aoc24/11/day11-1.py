def blink(stones: list):
    blinked = []
    for stone in stones:
        if stone == 0:
            blinked.append(1)
        elif len(str(stone)) % 2 == 0:
            middle_index = len(str(stone))//2
            blinked.append(int(str(stone)[:middle_index]))
            blinked.append(int(str(stone)[middle_index:]))
        else:
            blinked.append(stone * 2024)
    return blinked


with open("input.txt") as data:
    for line in data:
        stones = list(map(int, line.split(" ")))

for i in range(25):
    stones = blink(stones)

print(len(stones))