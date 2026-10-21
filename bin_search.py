def bin_search(f, y, left, right, eps):
    while right - left > eps:
        mid = (left + right) / 2
        if f(mid) < y:
            left = mid
        else:
            right = mid
    return (left + right) / 2

f = lambda x: x ** 3
print(bin_search(f, 27, 0, 100, 1e-9))
