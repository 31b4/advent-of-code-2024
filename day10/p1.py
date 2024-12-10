from collections import deque

def read_input(filename):
    with open(filename) as f:
        return [[int(x) for x in line.strip()] for line in f]

def get_neighbors(grid, x, y):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    height, width = len(grid), len(grid[0])
    neighbors = []
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if (0 <= new_x < height and 0 <= new_y < width):
            neighbors.append((new_x, new_y))
    return neighbors

def count_reachable_nines(grid, start_x, start_y):
    visited = set()
    reachable_nines = set()
    queue = deque([(start_x, start_y, 0)])  # (x, y, current_height)
    
    while queue:
        x, y, current_height = queue.popleft()
        
        if (x, y) in visited:
            continue
            
        visited.add((x, y))
        
        if grid[x][y] == 9:
            reachable_nines.add((x, y))
            
        for next_x, next_y in get_neighbors(grid, x, y):
            if (next_x, next_y) not in visited:
                if grid[next_x][next_y] == current_height + 1:
                    queue.append((next_x, next_y, grid[next_x][next_y]))
    
    return len(reachable_nines)

def solve(grid):
    height, width = len(grid), len(grid[0])
    res = 0
    
    for x in range(height):
        for y in range(width):
            if grid[x][y] == 0:
                score = count_reachable_nines(grid, x, y)
                res += score
                
    return res


    
grid = None
with open("i.txt") as f:
    grid = [[int(x) for x in line.strip()] for line in f]
res = solve(grid)
print(res)