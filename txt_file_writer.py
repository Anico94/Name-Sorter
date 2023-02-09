class TxtFileWriter: 
  """
  Class that writes a list to a text file
  each list item on a new line
  
  """

  def generate_text_file(self, list: list[str], new_file_name: str) -> None:
    with open(new_file_name, mode='w') as file:
      for i, line in enumerate(list):
        if(i != len(list)-1):
          file.write(line + '\n')
        else:
          file.write(line)