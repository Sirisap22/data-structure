arr, box_num = input("Enter Input : ").split("/")
arr = list(map(int, arr.split(" ")))
box_num = int(box_num)

def put_to_box(start_idx, weight):
    cur_idx = start_idx
    while weight - arr[cur_idx] >= 0:
        weight -= arr[cur_idx]
        cur_idx += 1
        if cur_idx >= len(arr):
            break

    return cur_idx

def is_valid(weight):
    cur_idx = 0

    for _ in range(box_num):
        cur_idx = put_to_box(cur_idx, weight)
        if cur_idx >= len(arr):
            return True

    if cur_idx >= len(arr):
        return False

w = max(max(arr), sum(arr)//box_num)
while True:
    if is_valid(w):
        break
    w += 1

print(f"Minimum weigth for {box_num} box(es) = {w}")
