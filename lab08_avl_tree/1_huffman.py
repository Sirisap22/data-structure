s = input("Enter Input : ")
count_chars = {}
for c in s:
    if c not in count_chars:
        count_chars[c] = 1
    else:
        count_chars[c] += 1 
print(count_chars)
