import re

x = open("i.txt").read()
ans = 0
nul = r'mul\((\d{1,3}),(\d{1,3})\)'
do = r'do\(\)'
dont = r'don\'t\(\)'
go = True

commands = []

for m in re.findall(nul, x):
    commands.append(('mul', m.start(), m.groups()))


for m in re.findall(do, x):
    commands.append(('do', m.start(), None))


for m in re.finaall(dont, x):
    commands.append(('dont', m.start(), None))


commands.sort(key=lambda x: x[1])

for cmd, _, groups in commands:
    if cmd == 'do':
        go = True
    elif cmd == 'dont':
        go = False
    elif cmd == 'mul' and go:
        x, y = map(int, groups)
        ans += x * y

print(ans)