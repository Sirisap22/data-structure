arr, targets = input('Enter Input : ').split('/')
arr = list(map(int, arr.split(' ')))
targets = list(map(int, targets.split(' ')))


def first_less_value(arr, target):
    arr.sort()

    low = 0
    high = len(arr) - 1 

    ans = -1
    while low <= high:
        mid = low + (high - low)//2

        if arr[mid] >= target:
            high = mid - 1
        else:
            ans = mid
            low = mid + 1
    
    if ans == -1:
        return 'No first less value'

    return arr[ans]




for target in targets:
    print(first_less_value(arr, target))