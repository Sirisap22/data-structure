arr = list(map(int, input("Enter Input : ").split(" ")))

def selection_sort_ignore_negative(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            continue

        min_val = [-1, float('inf')]
        for k in range(i, len(arr)):
            if arr[k] < 0:
                continue

            if min_val[1] > arr[k]:
                min_val[0] = k
                min_val[1] = arr[k]
        
        arr[i], arr[min_val[0]] = arr[min_val[0]], arr[i]


    return arr

for ele in selection_sort_ignore_negative(arr):
    print(f'{ele} ', end='')
print()
