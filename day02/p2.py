l = [list(map(int,x.split())) for x in open("i.txt")]

def isSafe(s): return any(all(d<b-a<u for a,b in zip(s,s[1:])) for d,u in[(0,4),(-4,0)])

print(sum(any(isSafe(s[:i]+s[i+1:]) for i in range(len(s))) for s in l))