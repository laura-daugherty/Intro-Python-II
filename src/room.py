# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc
    self.n_to = ""
    self.e_to = ""
    self.s_to = ""
    self.w_to = ""
