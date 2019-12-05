class Item:
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc

  def __str__(self):
    return f"name: {self.name} "

  def __repr__(self): # generally for programmer consumption
    return f'name: {self.name}'
  