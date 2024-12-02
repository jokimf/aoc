import re

def beats(push_time, time, goal_distance):
    my_distance = push_time * (time - push_time)
    return my_distance > goal_distance


with open('input.txt') as data:
    time_and_distance = []
    for line in data:
        time_and_distance.append(re.findall(r'[0-9]+',line))
race = [int(''.join(x)) for x in time_and_distance]
print(time_and_distance)
print(race)

counter = 0
for push_time in range(race[0]):
    if beats(push_time, race[0], race[1]):
        counter +=1
print(counter)
