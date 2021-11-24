def insertion(l):
    for i in range(1, len(l)):
        iEle = l[i]
        for j in range(i, -1, -1):
            if iEle < l[j-1] and j > 0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break

