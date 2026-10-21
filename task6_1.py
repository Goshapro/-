def bin_search(a, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def bin_search_func(f, y, left, right, eps):
    while right - left > eps:
        mid = (left + right) / 2.0
        if f(mid) < y:
            left = mid
        else:
            right = mid
    return (left + right) / 2.0


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    print(bin_search(arr, 7))

    f = lambda x: x ** 3
    print(bin_search_func(f, 27, 0, 5, 1e-6))
