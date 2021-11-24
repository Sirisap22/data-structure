def selection_sort(arr):
    for end in range(len(arr)-1, -1, -1):
        largest_idx = 0
        for i in range(1, end+1):
            if arr[i] > arr[largest_idx]:
                largest_idx = i

        arr[end], arr[largest_idx] = arr[largest_idx], arr[end]


arr = [5, 6, 2, 3, 0, 1, 4]
selection_sort(arr)
print(arr)
