raw = open("i.txt").readlines()

l = sorted(int(x.split()[0]) for x in raw)
r = sorted(int(x.split()[1]) for x in raw)

print(sum(abs(l[i] - r[i]) for i in range(len(l))))