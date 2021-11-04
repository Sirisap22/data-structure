a, b = [ int(i) for i in input().split(' ')]

def gcd(a, b):
    if a == 0:
        return abs(b)
    
    return gcd(b%a, a)

if int(a.replace('-', '')) < int(b.replace('-', '')) and int(a) != 0:
    c = int(a)
    a = int(b)
    b = c
ans = gcd(int(a), int(b))
if ans < 0:
    ans *= -1
print('The gcd of {} and {} is : {}'.format(a, b, ans)) if ans != 0 else print('Error! must be not all zero.')