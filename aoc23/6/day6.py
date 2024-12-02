import re
import math

def beats(push_time, time, goal_distance):
    my_distance = push_time * (time - push_time)
    return my_distance > goal_distance


with open('input.txt') as data:
    time_and_distance = []
    for line in data:
        time_and_distance.append([int(x) for x in re.findall(r'[0-9]+',line)])
races = list(zip(*time_and_distance))

race_possibilities = []
for time, goal_distance in races:
    counter = 0
    for push_time in range(time):
        if beats(push_time, time, goal_distance):
            counter +=1
    race_possibilities.append(counter)
print(race_possibilities)
print(math.prod(race_possibilities))
