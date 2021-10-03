s = input("Enter Input : ")

def isPalindrome(s, b, l):
    if b >= l:
        return True
    return s[b] == s[l] and isPalindrome(s, b+1, l-1)

if isPalindrome(s, 0, len(s)-1):
    print(f"'{s}' is palindrome")
else:
    print(f"'{s}' is not palindrome")