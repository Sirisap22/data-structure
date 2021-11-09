arr = list(map(int, input("Enter Input : ").split(" ")))

def bubble_sort(arr):
    is_swap = False
    for i in range(len(arr)):
        for k in range(len(arr)-i-1):
            if arr[k] > arr[k+1]:
                arr[k+1], arr[k] = arr[k], arr[k+1]
                is_swap = True
        
        if not is_swap:
            break
    
    return arr

print((bubble_sort(arr)))