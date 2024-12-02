from itertools import cycle
from math import lcm

def find_cycle(start:str) -> int:
    # Iterate through directions
    for count, direction in enumerate(cycle(directions)):
        # One transition
        start = lookup[start][0 if direction == 'L' else 1]

        # Return count if end is found
        if start.endswith('Z'):
            return count + 1

# Parse input
with open('input.txt') as data:
    directions = data.readline().strip('\n')
    data.readline()
    
    lookup = dict()
    for line in data:
        key, _, first, second = line.split(' ')
        first = first.replace('(','').replace(',','')
        second = second.strip(')\n')
        lookup[key] = (first,second)

# Determine starting nodes
starting_nodes = [node for node in lookup.keys() if node.endswith('A')]

# Find length offset from A to Z
cycle_lenghts = [find_cycle(node) for node in starting_nodes]

# Calculate lcm
print(lcm(*cycle_lenghts))