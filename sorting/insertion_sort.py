def insertion_sort(arr):
    for i in range(1, len(arr)):
        insert_ele = arr[i]
        for j in range(i, -1, -1):
            if insert_ele < arr[j-1] and j > 0:
                arr[j] = arr[j-1]
            else:
                arr[j] = insert_ele
                break

arr = [5, 6, 2, 3, 0, 1, 4]
insertion_sort(arr)
print(arr)


