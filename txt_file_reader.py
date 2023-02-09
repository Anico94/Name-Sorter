from os import path

class TxtFileReader:
  """
  Class that reads a text file
  """

  def read_list_of_lines(self, file_name):
    if (path.exists(file_name) == False):
      raise Exception('This file does not exist in the current directory')
    with open(file_name, mode = 'r') as file:
      lines = file.read()
      lines_list = lines.splitlines()
      if(len(lines_list) == 0):
        raise Exception('The file is empty')
      return lines_list