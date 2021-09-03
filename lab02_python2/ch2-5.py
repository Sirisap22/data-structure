class Game():
  def __init__(self):
    self.memory = []
    self.cur_game = []

  def is_valid(self, w1, w2):
    if not (len(w1) >= 2 and len(w2) >= 2):
      return
    return w1[-2] == w2[0] and w1[-1] == w2[1]
  
  def run(self, game):
    for ele in game:
      if ele[0] == "P":
        action, word = ele.split(' ')
        nor_word = word.lower()
        if nor_word not in self.memory:
          if (len(self.memory) != 0):
            if (self.is_valid(self.memory[-1], nor_word)):
              self.memory.append(word.lower())
              self.cur_game.append(word)
              print(f"'{word}' -> {self.cur_game}")
            else:
              print(f"'{word}' -> game over")
              break
          else:
            self.memory.append(word.lower())
            self.cur_game.append(word)
            print(f"'{word}' -> {self.cur_game}")
      elif ele[0] == "R":
        self.memory = []
        self.cur_game = []
        print("game restarted")
      elif ele[0] == "X":
        break
      else:
        print(f"'{ele}' is Invalid Input !!!")
        break


print("*** TorKham HanSaa ***")
game = input("Enter Input : ").split(',')
Game().run(game)
