from matchers import And, HasAtLeast, PlaysIn,Not,HasFewerThan,Or,All

class QueryBuilder:
  def __init__(self,query=All()) -> None:
    self.query = query

  def playsIn(self,team):
    return QueryBuilder(And(self.query,PlaysIn(team)))
  
  def hasAtLeast(self,value,attr):
    return QueryBuilder(And(self.query,HasAtLeast(value,attr)))
  
  def hasFewerThan(self,value,attr):
    return QueryBuilder(And(self.query,HasFewerThan(value,attr)))
  
  def oneOf(self,m1,m2):
    return QueryBuilder(Or(m1,m2))

  def build(self):
    return self.query