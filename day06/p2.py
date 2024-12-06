import time

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



def simulate_path(grid, cord, DIR):
    pos = cord
    dir = DIR
    visited_states = set()
    positions = set()

    while True:
        state = (pos, dir)
        if state in visited_states:
            return True, positions
        visited_states.add(state)
        positions.add(pos)

        newx = pos[0] + DIRECTIONS[dir][0]
        newy = pos[1] + DIRECTIONS[dir][1]
        
        if not in_bounds(grid, newx, newy):
            return False, positions
            
        if grid[newx][newy] == "#":
            dir = (dir + 1) % 4
        else:
            pos = (newx, newy)
            

start_time = time.time()

valid_positions = []
for i in range(len(l)):
    for j in range(len(l[0])):
        if l[i][j] == "." and (i,j) != cord:
            l[i][j] = "#"
            is_loop, _ = simulate_path(l, cord, DIR)
            if is_loop:
                valid_positions.append((i,j))
            l[i][j] = "."

result = len(valid_positions)
execution_time = time.time() - start_time

print(result)
print(f"Time: {execution_time:.3f} seconds")