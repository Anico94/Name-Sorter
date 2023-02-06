class TxtFileWriter: 
  """
  Class that writes a list to a text file
  each list item on a new line
  
  """
  def __init__(self, list):
    self.list = list

  def generate_text_file(self, new_file_name):
    with open(new_file_name, mode='w',newline='') as file:
      for i, line in enumerate(self.list):
        if(i != len(self.list)-1):
          file.write(line + '\n')
        else:
          file.write(line)