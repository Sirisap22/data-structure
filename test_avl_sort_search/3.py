count = 0
def bubble_sort(arr):
    global count
    for end in range(len(arr)-1, 0, -1):
        is_swaped = False
        for i in range(end):
            count += 1
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_swaped = True
        
        if not is_swaped:
            break


print(" *** Bubble sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
bubble_sort(A)
print()
print(A)
print("Data comparison =", count)