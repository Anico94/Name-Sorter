from os import path

class TextFileReader:
  """
  #TODO Add doc string
  
  """
  def __init__(self, file_name):
    self.file_name = file_name
    if (path.exists(file_name) == False):
      raise Exception('This file does not exist in the current directory') # Raise error 

  def list_of_lines(self):
    with open(self.file_name, mode = 'r') as file:
      lines = file.read()
      lines_list = lines.splitlines()
      if(len(lines_list) == 0):
        raise Exception('The file that has been passed has no contents')
      return lines_list