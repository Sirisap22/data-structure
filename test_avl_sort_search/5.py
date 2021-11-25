def binarySearch(arr, left, right, x):
    while left < right:
        mid = (left + right)//2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            right = mid - 1
            print(f"checking left side ({arr[left]}-{arr[right]})")
        else:
            left = mid + 1
            print(f"checking right side ({arr[left]}-{arr[right]})")
    
    return -1 
        
 
 
print('--Binary Search--')
inp1 = input("Enter input list/search number : ").split("/")
inp = [int(e) for e in inp1[0].split()]
inp.sort()
print("sort with built-in function : "+str(inp))
x = int(inp1[1]) # find this one
 
result = binarySearch(inp, 0, len(inp)-1, x)
 
if result != -1:
    print(str(x)+" is present at index " + str(result))
else:
    print("Not found")