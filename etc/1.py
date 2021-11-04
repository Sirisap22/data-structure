n_max = int(input())

summation = 0

def hamonic_sum(n):
    global summation
    if n == n_max:
        summation += 1/n
        print(f'1/{n} = {summation}')
        return
    
    summation += 1/n
    print(f'1/{n} + ', end='')
    
    hamonic_sum(n+1)


hamonic_sum(1)




