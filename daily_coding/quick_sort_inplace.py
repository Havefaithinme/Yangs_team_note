# quick sort inplace.
# Time Complexity: O(nlogn)
# Space Complexity: O(logn) due to the recursive nature of the sorting.
def quick_sort(arr):
    # divide and conquer.
    def sort(low, high):
        if low >= high:
            return
        mid = partition(low, high)
        sort(0, mid-1)
        sort(mid, high)
    # for inplace sorting.

    def partition(low, high):
        pivot = arr[(low+high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1
        return low
    return sort(0, len(arr)-1)
