with open('data.txt') as data:
    a = data.readline()
    for i in range(0, len(a)):
        print(a[i:i + 14], len(a[i:i + 14]), set(a[i:i + 14]), len(set(a[i:i + 14])))
        if len(a[i:i + 14]) == len(set(a[i:i + 14])):
            print(i + 14)
            break
