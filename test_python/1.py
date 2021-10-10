print(" *** Multiples of 3 or 5 or 7 ***")
n = int(input("Enter number : "))

def solve(n):
    if n < 3:
        return 0
    ans = 0
    for i in range(3, n):
        if i%3 == 0 or i%5 == 0 or i%7 == 0:
            ans += i
    return ans
if n > 0:
    print(f"Result : {solve(n)}")
else:
    print("Only positive number !!!")

