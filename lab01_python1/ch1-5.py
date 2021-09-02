n = int(input('Enter Input : '))
size = (n+2) * 2
canvas = [[None for _ in range(size)] for _ in range(size)]

def up_left(size):
  tri_base = int(size/2)
  for i in reversed(range(1, tri_base)):
    for k in range(tri_base):
      if k < i:
        canvas[tri_base-1-i][k] = '.'
      else:
        canvas[tri_base-1-i][k] = '#'

  for i in range(tri_base):
    canvas[tri_base-1][i] = '#'
  return

def down_right(size):
  tri_base = int(size/2)
  # offset start index
  offset = tri_base
  for i in range(tri_base):
    canvas[offset+0][offset+i] = '+'

  for i in reversed(range(1, tri_base)):
    for k in range(tri_base):
      if k < i:
        # not -1 because start at index 1
        canvas[offset+tri_base-i][offset+k] = '+'
      else:
        canvas[offset+tri_base-i][offset+k] = '.'

def square(inner, outer, base, offset_row, offset_col):
  for i in range(base):
    canvas[offset_row][offset_col+i] = outer
  inner_base = base-2
  for i in range(1, inner_base+1):
    canvas[offset_row+i][offset_col] = outer
    for k in range(1, inner_base+1):
      canvas[offset_row+i][offset_col+k] = inner
    canvas[offset_row+i][offset_col+base-1] = outer

  for i in range(base):
    canvas[offset_row+base-1][offset_col+i] = outer

base = int(size/2)
up_left(size)
down_right(size)
square('#', '+', base, 0, base)
square('+', '#', base, base, 0)
for arr in canvas:
  for ele in arr:
    print(ele, end='')
  print()