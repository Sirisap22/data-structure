s = input("Enter Input : ")

def check_increasing(s):
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]):
            return False
    
    return True

def check_decreasing(s):
    for i in range(len(s)-1):
        if int(s[i]) < int(s[i+1]):
            return False
    
    return True

def check_duplicate(s):
    count = {}

    for c in s:
        if c in count:
            return True
        else:
            count[c] = True
    
    return False

def check_all_duplicate(s):
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            return False 
    
    return True
            

is_increasing = check_increasing(s)
is_decreasing = check_decreasing(s)
is_duplicate = check_duplicate(s)
is_all_same = check_all_duplicate(s)

if is_all_same:
    print("Repdrome")
elif is_increasing and not is_duplicate:
    print("Metadrome")
elif is_increasing and is_duplicate:
    print("Plaindrome")
elif is_decreasing and not is_duplicate:
    print("Katadrome")
elif is_decreasing and is_duplicate:
    print("Nialpdrome")
else:
    print("Nondrome")