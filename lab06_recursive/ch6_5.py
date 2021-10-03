
def staircase(n):
    def helper(cur_n):
        nonlocal n
        if cur_n == 0:
            return
        print('_'*(cur_n-1)+'#'*(n-cur_n+1))
        helper(cur_n-1)
    def helper_2(cur_n):
        nonlocal n
        if cur_n == n:
            return
        print('_'*cur_n + '#'*(n-cur_n))
        helper_2(cur_n+1)
        
    if n == 0:
        return "Not Draw!"
    elif n > 0:
        helper(n)
    else:
        n = -1*n
        helper_2(0)
    return ''

print(staircase(int(input("Enter Input : "))))