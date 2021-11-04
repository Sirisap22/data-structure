arr = list(map(int, input().split(' ')))

def findmax(arr):
    if len(arr) <= 1:
        return arr[0]
    
    if arr[0] > arr[1]:
        arr[1] = arr[0]
    
    return findmax(arr[1:])
print(f'max = {findmax(arr)}')
    