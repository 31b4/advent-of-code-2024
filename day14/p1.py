def parse(line):
    p, v = line.split()
    return [int(x) for x in p[2:].split(',') + v[2:].split(',')]

robots = [parse(line) for line in open('i.txt')]
W, H = 101, 103

for _ in range(100):
    robots = [[((x + vx) % W), ((y + vy) % H), vx, vy] for x,y,vx,vy in robots]

q = [0] * 4
for x,y,_,_ in robots:
    if x != W//2 and y != H//2:
        q[(2 if y > H//2 else 0) + (1 if x > W//2 else 0)] += 1

print(q[0] * q[1] * q[2] * q[3])