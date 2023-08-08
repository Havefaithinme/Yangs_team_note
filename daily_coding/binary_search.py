# time complexity : O(logN)
def binary_search(target, arr):
    arr.sort()
    lo, hi = 0, len(arr)-1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return

# return the first index of the target(if duplicated.)


def lower_bound(target, arr):
    arr.sort()
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


# return the first index of the number that is larger than the target.
def upper_bound(target, arr):
    arr.sort()
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


if __name__ == "__main__":
    li = [i for i in range(1, 10)]
    print(binary_search(3, li))
    print(binary_search(8, li))
    li2 = [i for i in range(1, 10)] + [i for i in range(8, 20)]
    print(li2)
    print(upper_bound(8, li2))
    print(lower_bound(9, li2))
