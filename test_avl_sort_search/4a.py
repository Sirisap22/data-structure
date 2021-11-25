count = 0

def shell_sort(arr, size):
    global count
    margin = size//2
    while margin > 0:
        for i in range(margin, size):
            count += 1
            t = arr[i]
            k = i
            while k >= margin and arr[k  - margin] > t:
                arr[k] = arr[k - margin]
                k -= margin
            
            arr[k] = t
        margin = margin//2

print(" *** Shell sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
shell_sort(A, len(A))
print()
print(A)
print("Data comparison =", count)