import re

x = open("i.txt").read()
ans = 0

for match in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', x):
    x, y = map(int, match.groups())
    ans += x * y

print(ans)