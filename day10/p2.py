from collections import deque

def get_neighbors(grid, x, y):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    height, width = len(grid), len(grid[0])
    neighbors = []
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if (0 <= new_x < height and 0 <= new_y < width):
            neighbors.append((new_x, new_y))
    return neighbors

def count_distinct_paths(grid, start_x, start_y):
    paths = 0
    queue = deque([(start_x, start_y, 0, [(start_x, start_y)])])
    
    while queue:
        x, y, current_height, path = queue.popleft()
        
        if grid[x][y] == 9:
            paths += 1
            continue
            
        for next_x, next_y in get_neighbors(grid, x, y):
            if (next_x, next_y) in path:
                continue
                
            if grid[next_x][next_y] == current_height + 1:
                new_path = path + [(next_x, next_y)]
                queue.append((next_x, next_y, grid[next_x][next_y], new_path))
    
    return paths

def solve(grid):
    height, width = len(grid), len(grid[0])
    res = 0
    
    for x in range(height):
        for y in range(width):
            if grid[x][y] == 0:
                rating = count_distinct_paths(grid, x, y)
                res += rating
    return res

grid = None
with open("i.txt") as f:
    grid = [[int(x) for x in line.strip()] for line in f]
res = solve(grid)
print(res)