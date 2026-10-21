n = int(input())
arr = list(map(int, input().split()))

target_less = n // 2

for x in arr:
    count_less = 0
    for y in arr:
        if y < x:
            count_less += 1
    if count_less == target_less:
        print(x)
        break
