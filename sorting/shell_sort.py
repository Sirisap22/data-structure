def shell_sort(arr, diminish_seq):
    for num in diminish_seq:
        for i in range(num, len(arr)):
            insert_ele = arr[i] 
            for j in range(i, -1, -num):
                if insert_ele < arr[j-num] and j >= num:
                    arr[j] = arr[j-num]
                else:
                    arr[j] = insert_ele
                    break


arr = [10, 11, 1, 13, 2, 6, 4, 12, 5, 8, 7, 9, 3]
seq = [5, 3, 1] # [109, 41, 19, 5, 1]
shell_sort(arr, seq)
print(arr)
