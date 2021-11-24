def quick(l, left, right):
    if left == right+1:
        if l[left] > l[right]:
            l[left], l[right] = l[right], l[left]
            return
    if left < right:
        pivot = l[right]
       
        i, j = left, right-1
        while i < j:
            while i < right and l[i] <= pivot:
                i += 1
            while j > left and l[j] >= pivot:
                j -= 1
            if i < j:
                l[i], l[j] = l[j], l[i]
        if right is not i:
            l[right], l[i] = l[i], pivot  
        quick(l, left, i-1)
        quick(l, i+1, right)
