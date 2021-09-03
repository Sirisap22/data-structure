def hbd(age):
    if (age%2 == 0):
        ans = (20, age//2)
    else:
        ans = (21, (age-1)//2)
    return (f"saimai is just {ans[0]}, in base {ans[1]}!")

year = input("Enter year : ")
print(hbd(int(year)))