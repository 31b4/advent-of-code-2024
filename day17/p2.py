# 2,4, 1,5, 7,5, 0,3, 4,0, 1,6, 5,5, 3,0
"""
b = a % 8
b = b ^ 5
c = a >> b
a = a >> 3
b = b ^ c
b = b ^ 6
out(b % 8)
if a != 0: jump 0
"""
#-------------------------ONLY WORKING FOR MY INPUT--------------------------
with open("i.txt") as f:
    lines = f.read().splitlines()
    program = list(map(int, lines[4].split(": ")[1].split(',')))
print(program)

def backtrack(program, ans):
    if program == []: return ans
    for b in range(8):
        a = ans << 3 | b
        #b = a % 8
        b = b ^ 5
        c = a >> b
        #a = a >> 3
        b = b ^ c
        b = b ^ 6
        if b % 8 == program[-1]:
            #return backtrack(program[:-1],a)
            sub = backtrack(program[:-1],a)
            if sub is None:
                continue
            return sub

print(backtrack(program,0))