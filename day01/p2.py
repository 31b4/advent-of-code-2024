from collections import Counter
raw = open("i.txt").readlines()

l = [int(x.split()[0]) for x in raw]
r = [int(x.split()[1]) for x in raw]

freq = Counter(r)
print(sum(num * freq[num] for num in l))