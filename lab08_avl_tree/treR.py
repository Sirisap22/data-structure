import math
N, arr = input("Enter Input : ").split("/")
arr = list(map(int, arr.split(" ")))
N = int(N)

idx = N//2 + 1
if len(arr) != idx:
    print("Incorrect Input")
    exit(0)

st = [None for _ in range(N)]

for i, k in enumerate(range(idx-1, len(st))):
    st[k] = arr[i]

depth = math.ceil(math.log2(N))

for i in range(depth-2, -1, -1):
    for k in range(2**i):
        cur_idx = 2**i + k - 1

        child_left_idx = 2 * cur_idx + 1
        if child_left_idx >= len(st):
            break

        child_right_idx = 2 * cur_idx + 2

        if st[child_left_idx] < st[child_right_idx]:
            st[cur_idx] = st[child_left_idx]
            st[child_left_idx] = 0
            st[child_right_idx] -= st[cur_idx]
        else:
            st[cur_idx] = st[child_right_idx]
            st[child_right_idx] = 0
            st[child_left_idx] -= st[cur_idx]

st = list(map(lambda x: 0 if x is None else x , st))
print(sum(st))


