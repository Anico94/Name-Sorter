class Person:
  """
  A class to represent a person by there name
  """
  def __init__(self,name):
    self.name = name
    name_parts = name.split(" ")
    self.given_names = " ".join(name_parts[:-1])
    self.last_name = name_parts[-1]