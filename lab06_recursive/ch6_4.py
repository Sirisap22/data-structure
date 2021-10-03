def helper(l, idx):
    if idx == len(l)-1:
        print(l[idx])
        return
    print(f"{l[idx]} ", end='')
    helper(l, idx+1)

def print_nested_list(l, idx):
    helper(l[idx], 0)
    if idx == len(l)-1:
        return
    print_nested_list(l, idx+1)

def pantip(k, n, arr, paths):
    def go(arr, n, i, current_money, count, path):
        nonlocal paths
        if i == n:
            if current_money == 0:
                paths.append(path)
                count += 1
            return count
        
        path1 = path + [arr[i]] 
        count = go(arr, n, i+1, current_money-arr[i], count, path1)
        path2 = path[:]
        count = go(arr, n, i+1, current_money, count, path2)
        return count

    n = len(arr)
    count = go(arr, n, 0, k, 0, [])
    print_nested_list(paths, 0)
    return count


inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))