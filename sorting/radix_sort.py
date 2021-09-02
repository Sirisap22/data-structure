from collections import deque
arr = [ 1, 34, 23, 44, 2, 6 ,18]

def get_digit(number, n):
  return number // 10**n % 10

def radix_sort(arr):
  m = len(str(max(arr)))
  queqe = deque(arr)
  for nth in range(1, m+1):
    d = {i: deque() for i in range(10)}
    while (len(queqe) > 0):
      num = queqe.popleft()
      digit = 0
      if len(str(num)) > nth:
        digit = get_digit(num, nth)
      d[digit].append(num)
    for i in range(10):
      while (len(d[i]) > 0):
        queqe.append(d[i].popleft())
  return list(queqe)
print(radix_sort(arr))





