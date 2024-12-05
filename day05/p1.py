x = open("i.txt").read().split("\n\n")

d = {}
for n in x[0].splitlines():
    x1, x2 = map(int, n.split("|"))
    if x1 in d:
        d[x1].append(x2)
    else:
        d[x1] = [x2]

updates = [list(map(int, n.split(","))) for n in x[1].splitlines()]

total = 0
for update in updates:
    valid = True
    for i, page in enumerate(update):
        if page in d:
            for must_come_after in d[page]:
                if must_come_after in update:
                    if update.index(must_come_after) <= i:
                        valid = False
                        break
    
    if valid:
        middle = update[len(update)//2]
        total += middle

print(total)