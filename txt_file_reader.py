from os import path

class TxtFileReader:
  """
  Class that reads a text file
  """
  def __init__(self, file_name):
    self.file_name = file_name
    if (path.exists(file_name) == False):
      raise Exception('This file does not exist in the current directory') 

  def list_of_lines(self):
    with open(self.file_name, mode = 'r') as file:
      lines = file.read()
      lines_list = lines.splitlines()
      if(len(lines_list) == 0):
        raise Exception('The file is empty')
      return lines_list