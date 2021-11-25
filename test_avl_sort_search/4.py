count = 0

def shell_sort(arr, d_seq):
    global count
    for num in d_seq:
        for i in range(num, len(arr)):
            insert_ele = arr[i]
            for k in range(i, -1, -num):
                count += 1
                if insert_ele < arr[k-num] and k >= num:
                    arr[k] = arr[k-num]
                else:
                    arr[k] = insert_ele
                    break

print(" *** Shell sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
shell_sort(A, [3, 1])
print()
print(A)
print("Data comparison = ", count)