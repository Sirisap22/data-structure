count = 0

def shell_sort(arr):

    global count 
    margin = 3

    while margin > 0:
        i = 0
        j = margin

        while j < len(arr):
            count += 1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
            k = i

        while k - margin > -1:
            count += 1 
            if arr[k-margin] > arr[k]:
                arr[k-margin], arr[k] = arr[k], arr[k-margin]
            
            k -= 1
        
        margin = margin//2

print(" *** Shell sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
shell_sort(A)
print()
print(A)
print("Data comparison =", count)