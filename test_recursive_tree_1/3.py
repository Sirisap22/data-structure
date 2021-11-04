s = input('Enter Input : ')

save = s
special = '!?.; “”’'

def normalize(s, special):
    if len(special) == 0:
        return s
    
    s = s.replace(special[0], '')

    return normalize(s, special[1:])

s = normalize(s.lower(), special)

def is_palindrome(s):
    return s == reverse(s)

def reverse(s):
    if len(s) <= 1:
        return s
    
    return s[-1] + reverse(s[:-1])

if is_palindrome(s):
    print(f'\'{save}\' is palindrome')
else:
    print(f'\'{save}\' is not palindrome')

    
