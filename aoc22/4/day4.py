with open('data.txt') as data:
    exercise_a = 0
    exercise_b = 0
    for line in data:
        both = line.split(',')
        fst, snd = both[0].split('-')
        fst = int(fst)  # scuffed
        snd = int(snd)
        a, b = both[1].split('-')
        a = int(a)
        b = int(b)
        if fst <= b and snd >= a or b <= fst and snd <= a:
            exercise_a += 1
        if fst <= a and snd >= b or a <= fst and snd <= b:
            exercise_b += 1
print(exercise_a, exercise_b)
