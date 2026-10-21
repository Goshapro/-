with open('input.txt', 'r') as f:
    nums = list(map(float, f.readline().split()))
    op = f.readline().strip()

res = nums[0]
for x in nums[1:]:
    if op == '+':
        res += x
    elif op == '-':
        res -= x
    elif op == '*':
        res *= x
    elif op == '/':
        res /= x

with open('output.txt', 'w') as f:
    f.write(str(res))
