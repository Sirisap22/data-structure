year = int(input("Enter year : "))
if (year%2 == 0):
    ans = (20, year//2)
else:
    ans = (21, (year-1)//2)
print(f"saimai is just {ans[0]}, in base {ans[1]}!")