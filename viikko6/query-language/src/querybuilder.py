class Pino:
    def __init__(self):
        self.alkiot = []

    def push(self, alkio):
        self.alkiot.append(alkio)

    def pop(self):
        return self.alkiot.pop()

    def empty(self):
        return len(self.alkiot) == 0

class QueryBuilder:
  def __init__(self):
      self.query = Pino()

  def pino(self):
    return self.query