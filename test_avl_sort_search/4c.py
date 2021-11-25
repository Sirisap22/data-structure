count = 0

def intervaled_insertion_sort(arr, interval):
    global count
    for i in range(1, len(arr), interval):
        val = arr[i]
        k = i - 1

        while k >= 0 and val < arr[k]:
            count +=1
            arr[k+1] = arr[k]
            k -= interval
        arr[k+1] = val

def shell_sort(arr, d_seq):
    for num in d_seq:
       intervaled_insertion_sort(arr, num) 

print(" *** Shell sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
shell_sort(A, [3, 1])
print()
print(A)
print("Data comparison = ", count)