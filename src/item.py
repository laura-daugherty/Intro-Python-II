class Item:
  def __init__(self, name, desc, points):
    self.name = name
    self.desc = desc
    self.points = points

  def __str__(self):
    return f"name: {self.name} "

  def __repr__(self): # generally for programmer consumption
    return f'name: {self.name}'

  def onTake(self, item):
    print(f"you have picked up a {item}, it is worth {self.points}")

  def onDrop(self, item):
    print(f"you have dropped your {item}")

