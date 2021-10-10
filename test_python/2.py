print(" *** Perfect Number Verification ***")
n = int(input("Enter number : "))

def solve(n):
    factors = []
    for i in range(1, n//2+1):
        if n%i == 0:
            factors.append(i)
    
    if sum(factors) == n:
        return True, factors
    
    return False, factors

if n > 0:
    is_perfect, factors = solve(n)
    if is_perfect:
        print(f"{n} is a PERFECT NUMBER.")
    else:
        print(f"{n} is NOT a perfect number.")
    print(f"Factors : {factors}")
else:
    print("Only positive number !!!")