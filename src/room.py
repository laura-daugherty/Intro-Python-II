# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc
    self.n_to = None
    self.e_to = None
    self.s_to = None
    self.w_to = None
    self.items = []
  
  def __str__(self):
    r = f"{self.name} has these items:\n"
    for n in enumerate(self.items, start = 1):
      r += f"    {n}\n"
    return r

  def __repr__(self): # generally for programmer consumption
    return f'Items: ({repr(self.items)})'

  def addItem(self, item):
    self.items.append(item)
