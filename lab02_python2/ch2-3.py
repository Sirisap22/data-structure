print("*** Odd Even ***")
t, arr, s=input("Enter Input : ").split(',')
if t == 'L':
  arr = arr.split(' ')
  if s == 'Odd':
    print([x for i, x in enumerate(arr) if i%2 == 0])
  else:
    print([x for i, x in enumerate(arr) if i%2 != 0])
else:
  if s == 'Odd':
    print(''.join([x for i, x in enumerate(arr) if i%2 == 0]))
  else:
    print(''.join([x for i, x in enumerate(arr) if i%2 != 0]))
