arr = list(map(int, input().split()))

max_count = 0
most_frequent = arr[0]

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[j] == arr[i]:
            count += 1
    if count > max_count:
        max_count = count
        most_frequent = arr[i]

print(most_frequent)
