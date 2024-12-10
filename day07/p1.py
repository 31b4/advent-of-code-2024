data = []
with open("i.txt") as f:
    for line in f:
        key, values = line.strip().split(":")
        key = int(key)
        values = [int(x) for x in values.strip().split()]
        data.append((key,values))

p1 = 0
for res,nums in data:
    sv = nums[0]
    
    def solve(numbers, operators):
        result = numbers[0]
        for i in range(len(operators)):
            if operators[i] == '+':
                result += numbers[i + 1]
            else:  # '*'
                result *= numbers[i + 1]
        return result
    
    def gen(numbers):
        n = len(numbers) - 1
        for i in range(2 ** n):
            operators = []
            for j in range(n):
                operators.append('+' if (i & (1 << j)) else '*')
            result = solve(numbers, operators)
            if result == res:
                return res
        return 0
    
    p1 += gen(nums)
        
print(p1)