arr = list(map(int, input("Enter Input : ").split(" ")))

def bubble_sort_recursive(arr, i):

    is_swap = False

    def inner_loop(k): 
        nonlocal arr, i, is_swap
        if k == len(arr)-i-1:
            return
        
        if arr[k] > arr[k+1]:
            arr[k+1], arr[k] = arr[k], arr[k+1]
            is_swap = True
        inner_loop(k+1)
    
    inner_loop(0)

    if not is_swap or i == len(arr):
        return arr

    bubble_sort_recursive(arr, i+1)

    return arr
    
print(bubble_sort_recursive(arr, 0))