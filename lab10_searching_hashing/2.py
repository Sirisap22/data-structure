arr, targets = input('Enter Input : ').split('/')
arr = list(map(int, arr.split(' ')))
targets = list(map(int, targets.split(' ')))


def first_greater_value(arr, target):
    if len(arr) == 0:
        return None
    
    arr.sort()

    if arr[0] > target:
        return arr[0]
    if arr[-1] < target:
        return 'No First Greater Value'

    low = 0
    high = len(arr) - 1 

    while low <= high:
        mid = low + (high - low)//2

        if arr[mid] <= target:
            low = mid + 1
        else:
            ans = arr[mid]
            high = mid - 1
    
    return ans




for target in targets:
    print(first_greater_value(arr, target))
