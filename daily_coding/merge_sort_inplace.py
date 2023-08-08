def merge_sort(arr):
    def sort(low, high):
        if high - low <= 1:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)
        print(arr)

    def merge(low, mid, high):
        temp = []
        left, right = low, mid
        while left < mid and right < high:
            if arr[left] < arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        while left < mid:
            temp.append(arr[left])
            left += 1
        while right < high:
            temp.append(arr[right])
            right += 1
        for i in range(low, high):
            arr[i] = temp[i-low]

    return sort(0, len(arr))


if __name__ == "__main__":
    li = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    merge_sort(li)
    print(li)
