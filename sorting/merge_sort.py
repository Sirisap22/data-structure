def merge(arr, left, right, right_end):
    start = left
    left_end = right-1
    merged_arr = []
    while left <= left_end and right <= right_end:
        if arr[left] < arr[right]:
            merged_arr.append(arr[left])
            left += 1
        else:
            merged_arr.append(arr[right])
            right += 1

    while left <= left_end:
        merged_arr.append(arr[left])
        left += 1
    while right <= right_end:
        merged_arr.append(arr[right])
        right += 1

    for ele in merged_arr:
        arr[start] = ele
        start += 1
        if start > right_end:
            break


def merge_sort(arr, left, right):
    mid = left + (right-left)//2
    if left < right:
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid+1, right)


arr = [5, 3, 6, 1, 2, 7, 8, 4]
print(arr)
merge_sort(arr, 0, len(arr)-1)
print(arr)
