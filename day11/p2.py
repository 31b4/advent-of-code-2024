from functools import cache

@cache
def rules(n):
    if n == 0:
        return [1]
    s = str(n)
    if len(s) % 2 == 0:
        l = len(s) // 2
        return [int(s[:l]), int(s[l:])]
    return [n * 2024]

@cache
def calc(stone, blinks):
    if blinks == 0:
        return 1
    new = rules(stone)
    return sum(calc(num, blinks - 1) for num in new)


res = 0
stones = list(map(int, open('i.txt').read().split()))
for stone in stones:
    res += calc(stone, 75)
print(res)