print("*** Odd Even ***")
t, arr, s=input("Enter Input : ").split(',')

def odd_even(arr, s):
  if t == 'L':
    arr = arr.split(' ')
    if s == 'Odd':
      return [x for i, x in enumerate(arr) if i%2 == 0]
    else:
      return [x for i, x in enumerate(arr) if i%2 != 0]
  else:
    if s == 'Odd':
      return ''.join([x for i, x in enumerate(arr) if i%2 == 0])
    else:
      return ''.join([x for i, x in enumerate(arr) if i%2 != 0])

print(odd_even(arr, s))
