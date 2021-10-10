n = [ int(i) for i in input("Enter number end with (-1) : ").split(' ')]

count = {}
is_valid = False
size = 0
for ele in n:
    if ele == -1:
        is_valid = True
        break
    if ele in count.keys():
        count[ele] += 1
    else:
        count[ele] = 1
    size += 1

if not is_valid:
    print("Invalid INPUT !!!")
else:
    ans = None
    for key, value in count.items():
        if value > int(size/2):
            ans = key
    
    if ans is None:
        print("Not found")
    else:
        print(ans)
        


