n = int(input('Enter Input : '))
size = (n+2) * 2
canvas = [[None for _ in range(size)] for _ in range(size)]

def triangle(left, right, base, offset_row, offset_col):
  for i in reversed(range(1, base)):
    for k in range(base):
      if k < i:
        canvas[offset_row+base-1-i][offset_col+k] = left
      else:
        canvas[offset_row+base-1-i][offset_col+k] = right

def straight_line(symbol, base, offset_row, offset_col):
  for i in range(base):
      canvas[offset_row][offset_col+i] = symbol

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
triangle('.', '#', base, 0, 0)
triangle('+', '.', base, base+1, base)
straight_line('#', base, base-1, 0)
straight_line('+', base, base, base)
square('#', '+', base, 0, base)
square('+', '#', base, base, 0)

for arr in canvas:
  for ele in arr:
    print(ele, end='')
  print()