l = [list(map(int,x.split())) for x in open("i.txt")]

print(sum(any(all(d<b-a<u for a,b in zip(s,s[1:])) for d,u in[(0,4),(-4,0)])for s in l))