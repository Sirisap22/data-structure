print("*** TorKham HanSaa ***")
game = input("Enter Input : ").split(',')
memory = []
cur_game = []
def is_valid(w1, w2):
  if not (len(w1) >= 2 and len(w2) >= 2):
    return
  return w1[-2] == w2[0] and w1[-1] == w2[1]
for ele in game:
  if ele[0] == "P":
    action, word = ele.split(' ')
    nor_word = word.lower()
    if nor_word not in memory:
      if (len(memory) != 0):
        if (is_valid(memory[-1], nor_word)):
          memory.append(word.lower())
          cur_game.append(word)
          print(f"'{word}' -> {cur_game}")
        else:
          print(f"'{word}' -> game over")
          break
      else:
        memory.append(word.lower())
        cur_game.append(word)
        print(f"'{word}' -> {cur_game}")
  elif ele[0] == "R":
    memory = []
    cur_game = []
    print("game restarted")
  elif ele[0] == "X":
    break
  else:
    print(f"'{ele}' is Invalid Input !!!")
    break

