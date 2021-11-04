arr, compares = input('Enter Input : ').split('/') 

# Tree as a Implicit Array

arr = list(map(int, arr.split(' ')))
compares = [ [ int(ele) for ele in eles.split(' ')] for eles in compares.split(',')]
print(sum(arr))

def genChilds(init, func1, func2):
    childs = [init]
    odd_idx = func1(init)
    while odd_idx < len(arr):
        childs.append(odd_idx)
        odd_idx = func1(odd_idx)
   
    even_idx = func2(init)
    while even_idx < len(arr):
        childs.append(even_idx)
        even_idx = func2(even_idx)
    
    return childs

for compare in compares: 
    power_1 = 0
    power_2 = 0

    idx_1 = compare[0]
    idx_2 = compare[1]

    power_1 = sum(map(lambda x: arr[x], genChilds(idx_1, lambda x: 2*x+1, lambda x: 2*x+2)))
    power_2 = sum(map(lambda x: arr[x], genChilds(idx_2, lambda x: 2*x+1, lambda x: 2*x+2)))
 
    if power_1 > power_2:
        print(f'{idx_1}>{idx_2}')
    elif power_1 < power_2:
        print(f'{idx_1}<{idx_2}')
    else:
        print(f'{idx_1}={idx_2}')

