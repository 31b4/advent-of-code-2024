data = []
with open("i.txt") as f:
    for line in f:
        key, values = line.strip().split(":")
        key = int(key)
        values = [int(x) for x in values.strip().split()]
        data.append((key,values))

p2 = 0
for res, nums in data:
    def solve(numbers, operators):
        result = numbers[0]
        i = 0
        while i < len(operators):
            if operators[i] == '||':
                result = int(str(result) + str(numbers[i + 1]))
            elif operators[i] == '+':
                result += numbers[i + 1]
            else:  # '*'
                result *= numbers[i + 1]
            i += 1
        return result
    
    def gen(numbers):
        n = len(numbers) - 1
        for i in range(3 ** n):
            operators = []
            temp = i
            for _ in range(n):
                op = temp % 3
                operators.append('+' if op == 0 else '*' if op == 1 else '||')
                temp //= 3
            result = solve(numbers, operators)
            if result == res:
                return res
        return 0
    
    p2 += gen(nums)
        
print(p2)