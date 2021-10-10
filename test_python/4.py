print("*** String Rotation ***")
left, right = input("Enter 2 strings : ").split(' ')
count = 1

def rotate_left(s):
    s = s[-1]+s[:-1]
    return s
def rotate_right(s):
    s = s[1:]+s[0]
    return s

new_l = rotate_left(left)
new_r = rotate_right(right)


while new_l != left or new_r != right:
    if count <= 5:
        print(f"{count} {new_l} {new_r}")
    new_l = rotate_left(new_l)
    new_r = rotate_right(new_r)
    count += 1
if count > 6:
    print(" . . . . .")
print(f"{count} {new_l} {new_r}")

print(f"Total of  {count} rounds.")