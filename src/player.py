# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.items = []

  
  def __str__(self):
    r = f"{self.name} has these items:\n"
    for n in enumerate(self.items, start = 1):
      r += f"    {n}\n"
    return r

  def __repr__(self): # generally for programmer consumption
    return f'Items: ({repr(self.items)})'


