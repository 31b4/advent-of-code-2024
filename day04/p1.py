def find_xmas(grid):
    count = 0
    
    ALL_DIRS = [(-1, 0), (-1, -1), (1, 0), (-1, 1), (0, -1), (1, -1), (0, 1), (1, 1)]
    
    def check_direction(r, c, dr, dc):
        if not (0 <= r + 3*dr < len(grid) and 0 <= c + 3*dc < len(grid[0])):
            return False
        return (grid[r][c] == 'X' and 
                grid[r+dr][c+dc] == 'M' and 
                grid[r+2*dr][c+2*dc] == 'A' and 
                grid[r+3*dr][c+3*dc] == 'S')
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for dr, dc in ALL_DIRS:
                if check_direction(r, c, dr, dc):
                    count += 1
    
    return count

print(find_xmas(open("i.txt").readlines()))