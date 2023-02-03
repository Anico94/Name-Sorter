import sys

class TextFileReader:
  def __init__(self, file_name):
    self.file_name = file_name

  def list_of_lines(self):
    with open(self.file_name, mode = 'r') as file:
      lines = file.read()

      lines_list = lines.splitlines()
      return lines_list


class TextFileWriter: 
  def __init__(self, list):
    self.list = list

  def generate_text_file(self, new_file_name):
    with open(new_file_name, mode='w',newline='') as file:
      for i, line in enumerate(self.list):
        if(i != len(self.list)-1):
          file.write(line + '\n')
        else:
          file.write(line)


class NameSorter:
  def __init__(self, list_of_names):
    self.list_of_names = list_of_names

  def sort_by_last_name(self):

    # initilise 2 empty list 
    # 1) List that is constructed with all the names with the last name moved to the start (this can then be sorted)
    # 2) Once names are sorted we can reconstruct names with given names at the start but the list will be sorted
    last_names_first_list = []
    sorted_names = []

    # break each name into a list of given names and last name
  
    for full_name in self.list_of_names:
      split_names = full_name.split(' ')
      #reorder with last name at the front
      person_name_last_first = split_names.pop() + " " + " ".join(split_names)
      last_names_first_list.append(person_name_last_first)
    
    last_names_first_list.sort()

    for full_name_last_first in last_names_first_list:
      split_names = full_name_last_first.split(' ')
      #reconstruct name moving last name to the end
      last_name = split_names.pop(0)
      person_full_name = " ".join(split_names) + " " + last_name
      sorted_names.append(person_full_name)
    
    return sorted_names
  

if __name__ == '__main__':
  try:
    file_path = sys.argv[1] # allows user to pass an additional argument in the command line (list to sort)
    try:
      names_list = TextFileReader(file_path).list_of_lines()
      sorted_names = NameSorter(names_list).sort_by_last_name()
      print(*sorted_names, sep='\n')
      new_file = TextFileWriter(sorted_names).generate_text_file('sorted-names.txt')
    except:
      print('Not a valid file please pass a .txt as the command line argument')
  except:
    print('Text file of names to be passed as a command line argument')



