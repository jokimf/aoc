# This is the worst code I have ever written

def is_safe(a,b):
    print(f"Checking {a} and {b}, result={abs(a - b) < 4 and a != b}")
    return abs(a - b) < 4 and a != b

with open('input.txt') as data:
    b = 0
    for i, line in enumerate(data):
        a = line.split(" ")
        a = list(map(int, a))
        all_pairs = list(zip(a,a[1:]))
        for mode in ["asc", "desc"]:
            previous_pair = None
            fail_used = False
            fail = False
            for index, pair in enumerate(all_pairs):
                pair = list(pair)
                if previous_pair is not None:
                    if previous_pair[0] < pair[1] and mode == "asc" and is_safe(previous_pair[0], pair[1]):
                        previous_pair = None
                        continue
                    if previous_pair[0] > pair[1] and mode == "desc" and is_safe(previous_pair[0], pair[1]):
                        previous_pair = None
                        continue
                    if index == 1 and previous_pair[1] < pair[1] and mode == "asc" and is_safe(pair[1], previous_pair[1]):
                        previous_pair = None
                        continue
                    if index == 1 and previous_pair[1] > pair[1] and mode == "desc" and is_safe(pair[1], previous_pair[1]):
                        previous_pair = None
                        continue
                    fail = True
                    previous_pair = None
                    break

                if pair[0] < pair[1] and mode == "asc" and is_safe(pair[0], pair[1]):
                    continue
                elif pair[0] > pair[1] and mode == "desc" and is_safe(pair[0], pair[1]):
                    continue
                else:
                    if not fail_used:
                        fail_used = True
                        previous_pair = pair
                        continue
                    fail = True
                    break
            if not fail:
                b = b + 1
    print(b)
