class Player:

  def __init__(self,name):
    self._name = name
    self.score = 0

  def win_point(self):
    self.score += 1
  
  def get_score(self):
    return self.score