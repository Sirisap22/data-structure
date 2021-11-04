arr, compares = input('Enter Input : ').split('/') 

# Tree as a Implicit Array

arr = list(map(int, arr.split(' ')))
compares = [ [ int(ele) for ele in eles.split(' ')] for eles in compares.split(',')]
print(sum(arr))

def traverse(root):
    global summa
    summa += arr[root]

    left_node = 2*root+1
    right_node = 2*root+2
    if left_node < len(arr):
        traverse(2*root+1)
    if right_node < len(arr):
        traverse(2*root+2)

for compare in compares: 
    power_1 = 0
    power_2 = 0

    idx_1 = compare[0]
    idx_2 = compare[1]

    summa = 0
    traverse(idx_1)
    power_1 = summa

    summa = 0
    traverse(idx_2)
    power_2 = summa

    if power_1 > power_2:
        print(f'{idx_1}>{idx_2}')
    elif power_1 < power_2:
        print(f'{idx_1}<{idx_2}')
    else:
        print(f'{idx_1}={idx_2}')

