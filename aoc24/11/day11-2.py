from functools import cache


@cache
def blink(stone_value, iteration) -> int:
    if iteration == 0:
        return 1
    elif stone_value == 0:
        return blink(1, iteration-1)
    elif len(str(stone_value)) % 2 == 0:
        middle_index = len(str(stone_value))//2
        return blink(int(str(stone_value)[:middle_index]), iteration-1) + blink(int(str(stone_value)[middle_index:]), iteration-1)
    else:
        return blink(stone_value * 2024, iteration-1)

print(sum(blink(s, 75) for s in list(map(int, open("input.txt").read().split(" ")))))
