def find_xmas(grid):
    count = 0
    
    X_DIRS = [(1, 1), (2, 2), (0, 2), (2, 0)]
    def check_patterns(r, c):
        if not (0 <= r + 2 < len(grid) and 0 <= c + 2 < len(grid[0])):
            return False
        
        PATTERN=["MASSM","MASMS","SAMSM","SAMMS"]
        return any(
                (grid[r][c] == p[0] and 
                grid[r+X_DIRS[0][0]][c+X_DIRS[0][1]] == p[1] and 
                grid[r+X_DIRS[1][0]][c+X_DIRS[1][1]] == p[2] and 
                grid[r+X_DIRS[2][0]][c+X_DIRS[2][1]] == p[3] and
                grid[r+X_DIRS[3][0]][c+X_DIRS[3][1]] == p[4]) for p in PATTERN)
                
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if check_patterns(r, c):
                count += 1
    return count

print(find_xmas(open("i.txt").readlines()))