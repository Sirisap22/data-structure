print('*** Fun with Drawing ***')
n = int(input('Enter input : '))
size = 1+(n-1)*4
if (n == 1):
  print('#')
  exit()

matrix = [ [None for _ in range(size) ] for _ in range(size) ]
def draw_square(row, col, char, length):

  for i in range(length):
    matrix[row][col+i] = char
    matrix[row+length-1][col+i] = char
  for i in range(1, length-1):
    matrix[row+i][col] = char
    matrix[row+i][col+length-1] = char

cur_row = 0
cur_col = 0
cur_len = size
for i in range(int(size/2)):
  char = '#'
  if i%2 != 0:
    char = '.'
  draw_square(cur_row, cur_col, char, cur_len)

  cur_len -= 2
  cur_row += 1
  cur_col += 1
if n > 1 and size%2 != 0:
  matrix[int(size/2)][int(size/2)] = '#'

for arr in matrix:
  for ele in arr:
    print(ele, end='')
  print()