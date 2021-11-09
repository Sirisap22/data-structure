arr = input("Enter Input : ").split(" ")

def get_char(s):
    for c in s:
        if not c.isnumeric():
            return c

def merge(arr1, arr2):
    merged_arr = [None for _ in range(len(arr1) + len(arr2))]

    arr1_pointer = 0
    arr2_pointer = 0
    while arr1_pointer < len(arr1) and arr2_pointer < len(arr2):
        if ord(get_char(arr1[arr1_pointer])) < ord(get_char(arr2[arr2_pointer])): 
           merged_arr[arr1_pointer + arr2_pointer] = arr1[arr1_pointer]
           arr1_pointer += 1
        else:
           merged_arr[arr1_pointer + arr2_pointer] = arr2[arr2_pointer]
           arr2_pointer += 1
    
    remain_pointer = arr1_pointer + arr2_pointer
    if arr1_pointer < len(arr1):
        while remain_pointer < len(arr1) + len(arr2):
            merged_arr[remain_pointer] = arr1[arr1_pointer]
            remain_pointer += 1    
            arr1_pointer += 1

    
    elif arr2_pointer < len(arr2):
        while remain_pointer < len(arr1) + len(arr2):
            merged_arr[remain_pointer] = arr2[arr2_pointer]
            remain_pointer += 1    
            arr2_pointer += 1
    
    return merged_arr
            
        
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])

    return merge(arr1, arr2)

sorted_arr = merge_sort(arr)

for ele in sorted_arr:
    print(f"{ele} ", end="")
print()

