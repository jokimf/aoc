# 7:5K, 6:4K, 5:FH, 4:3K, 3:2P, 2:1P, 1:HI
def determine_hand_type(hand:str):
    hand_set = set(hand)
    unique_cards = len(hand_set)
    if unique_cards == 1:
        return 7
    elif unique_cards == 2:
        #FH or 4K
        example_element = hand_set.pop()
        hand_set.add(example_element)
        return 6 if hand.count(example_element) in [1,4] else 5
    elif unique_cards == 3:
        #3K or 2P
        for e in hand_set:
            if hand.count(e) == 3:
                return 4
        return 3
    elif unique_cards == 4:
        return 2
    else:
        return 1 

value = {
    'A':14,
    'K':13,
    'Q':12,
    'J':11,
    'T':10,
    '9':9,
    '8':8,
    '7':7,
    '6':6,
    '5':5,
    '4':4,
    '3':3,
    '2':2,
}

def same_strength_check(hand, other):
    for i in range(len(hand)):
        if value[hand[i]] == value[other[i]]:
            continue
        return value[hand[i]] > value[other[i]]
    raise RuntimeError(f'Two of the same hands detected, which should be impossible: {hand} / {other}')


ranking = []
with open('input.txt') as data:
    laziness = {}
    for line in data:
        hand, bid = line.strip('\n').split(' ')
        bid = int(bid)
        laziness[hand] = bid
        hand_value = determine_hand_type(hand)

        for i, other_hand in enumerate(ranking):
            other_hand_value = determine_hand_type(other_hand)
            if other_hand_value < hand_value:
                 ranking.insert(i, hand)
                 break
            elif other_hand_value == hand_value:
                if same_strength_check(hand, other_hand):
                    ranking.insert(i, hand)
                    break
        else:
            ranking.append(hand)

ranking.reverse()
total = 0
for i, x in enumerate(ranking):
    bonus = laziness[x] * (i + 1)
    total += bonus
print(ranking)
print(total)