inp = input().split(' ')
filtered = []
is_valid = False
for ele in inp:
    if ele == '-1':
        is_valid = True
        break
    else:
        filtered.append(ele)

    
if is_valid:
    ans = None
    for ele in filtered:
        if filtered.count(ele) > int(len(filtered)/2):
            ans = ele

    if ans is not None:
        print(ans)
    else:
        print('not found')

else:
    print("NOT VALID")