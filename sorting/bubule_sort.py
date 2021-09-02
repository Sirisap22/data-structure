arr = [ 1, 34, 23, 44, 2, 6 ,18]

for i in range(len(arr)):
  is_swap = False
  for k in range(len(arr)-i-1):
    if arr[k] > arr[k+1]:
      arr[k], arr[k+1] = arr[k+1], arr[k]
      is_swap = True
  if(not is_swap):
    break

print(arr)