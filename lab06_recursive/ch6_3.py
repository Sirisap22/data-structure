num = int(input("Enter Number : "))

if num < 0:
    print("Only Positive & Zero Number ! ! !")
    exit(0)

power_of_2 = 2 ** (num)

def combination(n):
    if power_of_2 == 1:
        print(0)
        return

    def to_binary(s, num):
        if num >= 1:
            to_binary(s, num // 2)
        s.append(str(num%2))
        return ''.join(s)
    
    ss = to_binary([], n)
    if len(ss) < num:
        ss = str(0)*(num - len(ss)) + ss
    elif len(ss) > num:
        ss = ss[len(ss)-num:]
    print(ss)

    if n == power_of_2-1:
        return

    combination(n+1)

combination(0)

    
    