def bubble_sort(arr):
  for end in range(len(arr)-1, 0, -1):
    is_swaped = False
    for i in range(end):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        is_swaped = True
    if not is_swaped:
      break

arr = [5,6,2,3,0,1,4]
bubble_sort(arr)
print(arr)