from collections import deque


l = open("i.txt").read().splitlines()
l = [list(map(int, x.split(","))) for x in l]
print(l)

max_x = max(coord[0] for coord in l)
max_y = max(coord[1] for coord in l)
def P2():
    for find in range(1024,len(l)):
        grid = [["." for _ in range(max_y + 1)] for _ in range(max_x + 1)]

        for i in range(find):
            x,y = l[i]
            grid[x][y] = "#"
        print(find)
        #for row in grid:
        #    print("".join(row))

        def bfs(grid, start, end):
            rows, cols = len(grid), len(grid[0])
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            queue = deque([(start, 0)])
            visited = set()
            
            while queue:
                (x, y), dist = queue.popleft()
                
                if (x, y) == end:
                    return dist
                
                if (x, y) in visited or grid[x][y] == "#":
                    continue
                visited.add((x, y))
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                        queue.append(((nx, ny), dist + 1))
            
            return -1


        if bfs(grid, (0,0), (max_x, max_y)) == -1:
            return l[find-1]

print(P2())# 32 55