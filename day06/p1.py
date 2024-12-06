l = open("i.txt").read().strip().splitlines()
cord= ()
for i,x in enumerate(l):
    for j,c in enumerate(x):
        if c == "^":
            cord = (i,j)

l = [list(line) for line in l]

l[cord[0]][cord[1]] = '.'


def in_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])
          
DIRECTIONS = [(0, 1),(1, 0),(0, -1),(-1, 0)]
DIR = 3  
visited = []
res = 0

visited.append(cord)
res += 1

while True:
    newx = cord[0] + DIRECTIONS[DIR][0]
    newy = cord[1] + DIRECTIONS[DIR][1]
    if not in_bounds(l, newx, newy):
        break
         
    if l[newx][newy] == ".":
        if (newx,newy) not in visited:
            visited.append((newx,newy))
            res += 1
    elif l[newx][newy] == "#":
        DIR = (DIR + 1) % 4
        newx = cord[0] + DIRECTIONS[DIR][0]
        newy = cord[1] + DIRECTIONS[DIR][1]
        if l[newx][newy] == "." and (newx,newy) not in visited:
            visited.append((newx,newy))
            res += 1

    cord = (newx,newy)
    
print(len(visited))