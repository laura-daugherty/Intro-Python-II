class Item:
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc

  def __str__(self):
    return f"name: {self.name} "

  def __repr__(self): # generally for programmer consumption
    return f'name: {self.name}'
  
  def onTake(self, item):
    print(f"you have picked up a {item}")

  def onDrop(self, item):
    print(f"you have dropped your {item}")