class TextFileWriter: 
  """
  #TODO add doc string here
  
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