l = list(map(int,list(open("i.txt").read())))

t = ""
id = 0

for i,x in enumerate(l):
    if i % 2:  # free space
        t += x*"卐"
    else:  # block
        t += chr(id) * x
        id += 1

current = list(t)

while current[-1] == "卐":
    current.pop()

files = []
last = current[0]
fl = 0
for i, char in enumerate(current):
    if char != last:
        if last != "卐":
            files.append((last*fl, i-fl))
        fl = 1
    else:
        fl += 1
    last = char
if last != "卐":
    files.append((last*fl, len(current)-fl))

while len(files) > 0:
    last_len = len(files[-1][0])
    try:
        first_dot = ''.join(current).index("卐"*last_len, 0, files[-1][1])
    except:
        files.pop()
        continue
        
    fc = files[-1][0]
    fp = files[-1][1]
    
    current[first_dot:first_dot+last_len] = list(fc)
    current[fp:fp+last_len] = ["卐"]*last_len
    
    files.pop()

ans = 0
for i,x in enumerate(current):
    if x == "卐":
        continue
    ans += i*ord(x)

print(ans)
