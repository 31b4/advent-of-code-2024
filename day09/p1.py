l = list(map(int,list(open("i.txt").read())))
blocks = [] #[id] = (start, end, num, id)

t = ""
id = 0

for i,x in enumerate(l):
    if i % 2:#free space
        t += x*"卐"
    else:#block
        t += chr(id) * x
        blocks.append((i,i+x,x,id))
        id += 1

current = list(t)
dot = 0
while True:
    while current[-1] == "卐":
        current.pop()
    try:
        dot = current.index("卐", dot)
    except:
        break
    current[dot] = current[-1]
    current.pop()

ans = 0
for i,x in enumerate(current):
    if x == "卐":
        break
    ans += i*ord(x)

print(ans)