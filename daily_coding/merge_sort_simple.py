# divide and conquer.
# 1. divide the array into smallest piecies.
# 2. when the array is no longer divisible merge each array by comparing the leftmost elemnents until all array is merged.
# Time complexity: O(nlogn)
# Space Complexity: O(n) maybe?

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])

    sorted = []
    l = r = 0
    while l < len(left_sorted) and r < len(right_sorted):
        if left_sorted[l] < right_sorted[r]:
            sorted.append(left_sorted[l])
            l += 1
        else:
            sorted.append(right_sorted[r])
            r += 1
    if l < len(left_sorted):
        return sorted + left_sorted[l:]
    if r < len(right_sorted):
        return sorted + right_sorted[r:]
    return sorted


if __name__ == "__main__":
    print(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
