def quick_sort(arr, left, right):
    if left == right-1:
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        return

    if left < right:
        pivot = arr[right]
        i, j = left, right-1
        while i < j:
            while i < right and arr[i] <= pivot:
                i += 1
            while j > left and arr[j] >= pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        if right != i:
            arr[right], arr[i] = arr[i], pivot  

        quick_sort(arr, left, i-1)
        quick_sort(arr, i+1, right)

arr = [5, 1, 4, 9, 6, 3, 8, 2, 7, 0]
quick_sort(arr, 0, len(arr)-1)
print(arr)
