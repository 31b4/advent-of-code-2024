def read_input(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def find_antennas(grid):
    antennas = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            char = grid[y][x]
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

antinodes = set()


def antinode(an1, an2,n,m):
    x1, y1 = an1
    x2, y2 = an2
    newx = x2 + (x2 - x1)
    newy = y2 + (y2 - y1)
    if newx >= 0 and newx < n and newy >= 0 and newy < m:
        antinodes.add((newx,newy))

def solve(filename):
    grid = read_input(filename)
    antennas = find_antennas(grid)
    for a in antennas:
        antenna = antennas[a]
        for i in range(len(antenna)):
            for j in range(i):
                node1 = antenna[i]
                node2 = antenna[j]
                antinode(node1, node2,len(grid),len(grid[0]))
                antinode(node2, node1,len(grid),len(grid[0]))
                
    for i,x in enumerate(grid):
        for j,c in enumerate(x):
            if (i,j) in antinodes:
                print("#", end="")
            else:
                print(c,end='')
        print()
    return len(antinodes)

if __name__ == "__main__":
    res = solve("i.txt")
    print(res)
