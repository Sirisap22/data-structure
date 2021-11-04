print(' *** Natural sum ***')

def natural_sum(n):
    if n <= 1:
        print(f'{num} = ', end='')
        return 1
    print(f'{num - n+1} + ', end='')
    return n + natural_sum(n-1)

num = int(input("Enter number : ")) 
print("%.d" %(natural_sum(num)))