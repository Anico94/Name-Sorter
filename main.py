import sys
from name_sorter import NameSorter as ns
from text_file_reader import TextFileReader as tfr
from text_file_writer import TextFileWriter as tfw

if __name__ == '__main__':
    try:
        file_path = sys.argv[1] # allows user to pass an additional argument in the command line (list of names to sort)
        names_list = tfr(file_path).list_of_lines()
        sorted_names = ns(names_list).sort_by_last_name()
        print(*sorted_names, sep='\n')
        new_file = tfw(sorted_names).generate_text_file('sorted_names.txt')
    except:
        print("A text (.txt) file of names to be passed as a command line argument")