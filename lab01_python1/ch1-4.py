print('*** Minesweeper ***')
pre = [ word.split(' ') for word in input('Enter input(5x5) : ').split(',') ]
print('\n')
for arr in pre:
  print(arr)
print('\n')

def increment_surround(mine, row, col):
    if (row == 0 and col == 0):
      mine[row][col+1] += 1
      mine[row+1][col] += 1
      mine[row+1][col+1] += 1
    elif (row == 0 and col == 4):
      mine[row][col-1] += 1
      mine[row+1][col-1] += 1
      mine[row+1][col] += 1
    elif (row == 4 and col == 0):
      mine[row-1][col] += 1
      mine[row-1][col+1] += 1
      mine[row][col+1] += 1
    elif (row == 4 and col == 4):
      mine[row-1][col] += 1
      mine[row-1][col-1] += 1
      mine[row][col-1] += 1
    elif (row == 0):
      mine[row][col-1] += 1
      mine[row][col+1] += 1
      mine[row+1][col-1] += 1
      mine[row+1][col] += 1
      mine[row+1][col+1] += 1
    elif (row == 4):
      mine[row][col-1] += 1
      mine[row][col+1] += 1
      mine[row-1][col-1] += 1
      mine[row-1][col] += 1
      mine[row-1][col+1] += 1
    elif (col == 0):
      mine[row-1][col] += 1
      mine[row-1][col+1] += 1
      mine[row][col+1] += 1
      mine[row+1][col] += 1
      mine[row+1][col+1] += 1
    elif (col == 4):
      mine[row-1][col-1] += 1
      mine[row-1][col] += 1
      mine[row][col-1] += 1
      mine[row+1][col-1] += 1
      mine[row+1][col] += 1
    else:
      mine[row][col-1] += 1
      mine[row][col+1] += 1
      mine[row+1][col-1] += 1
      mine[row+1][col] += 1
      mine[row+1][col+1] += 1
      mine[row-1][col-1] += 1
      mine[row-1][col] += 1
      mine[row-1][col+1] += 1
      
    
new_pre = [[], [], [], [], []]
for ele, new_ele in zip(pre, new_pre):
    for char in ele:
      if (char == '-'):
        new_ele.append(0)
      elif (char == '#'):
        new_ele.append(-1000)

for row, arr in enumerate(new_pre):
  for col, ele in enumerate(arr):
    if (new_pre[row][col]) < 0:
      increment_surround(new_pre, row, col)
  
for i, arr in enumerate(new_pre):
  for j, ele in enumerate(arr):
    if ele < 0:
      new_pre[i][j] = '#'
    else:
      new_pre[i][j] = str(new_pre[i][j])   

for arr in new_pre:
  print(arr)