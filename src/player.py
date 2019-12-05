# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.items = []
    self.points = 0

  
  def __str__(self):
    r = f"{self.name} has these items:\n"
    for n in enumerate(self.items, start = 1):
      r += f"    {n}\n"
    print(f'{self.name} has this many points: {self.points}')
    return r

  def __repr__(self): # generally for programmer consumption
    return f'Items: ({repr(self.items)})'

  def addItem(self, item):
    self.items.append(item)

  def removeItem(self, item):
    self.items.remove(item)

  def addPoints(self, point):
    self.points = self.points + point

  def removePoints(self, point):
    self.points = self.points - point


