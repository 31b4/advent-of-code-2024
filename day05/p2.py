x = open("i.txt").read().split("\n\n")

d = {}
for n in x[0].splitlines():
    x1, x2 = map(int, n.split("|"))
    if x1 in d:
        d[x1].append(x2)
    else:
        d[x1] = [x2]

updates = [list(map(int, n.split(","))) for n in x[1].splitlines()]

def is_valid(nums):
    for i, n in enumerate(nums):
        if n in d:
            for must_after in d[n]:
                if must_after in nums:
                    if nums.index(must_after) <= i:
                        return False
    return True

def fix_order(nums):
    result = list(nums)
    
    changed = True
    while changed:
        changed = False
        for i in range(len(result)):
            if result[i] in d.keys():
                for must_after in d[result[i]]:
                    if must_after in result:
                        j = result.index(must_after)
                        if j < i:
                            print(result[i], result[j])
                            result[i], result[j] = result[j], result[i]
                            changed = True
                            break
    
    return result

total = 0
for update in updates:
    if not is_valid(update):
        print(update)
        fixed = fix_order(update)
        print(fixed)
        middle = fixed[len(fixed)//2]
        total += middle

print(total)