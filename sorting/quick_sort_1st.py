def quick(l, left, right):
    if left == right+1:  # only 2 elements
        if l[left] > l[right]:
            l[left], l[right] = l[right], l[left]  # swap 			 return
    if left < right:
        pivot = l[left] 
        i, j = left+1, right
        while i < j:
            while i < right and l[i] <= pivot:
                i += 1
            while j > left and l[j] >= pivot:
                j -= 1
            if i < j:
                l[i], l[j] = l[j], l[i]  # swap
        if left is not j:
            l[left], l[j] = l[j], pivot  # swap pivot to index j
        quick(l, left, j-1)
        quick(l, j+1, right)


l = [5, 1, 4, 9, 6, 3, 8, 2, 7, 0]
quick(l, 0, len(l)-1)
print(l)
