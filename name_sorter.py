import sys
from name_sorter_class import NameSorter as ns
from txt_file_reader import TxtFileReader as tfr
from txt_file_writer import TxtFileWriter as tfw

if __name__ == '__main__':
    try:
        file_path = sys.argv[1] # allows user to pass an additional argument in the command line (list of names to sort)
        names_list = tfr(file_path).list_of_lines()
        sorted_names = ns().sort_by_last_name(names_list)
        print(*sorted_names, sep='\n') #prints the sorted names to the console
        new_file = tfw(sorted_names).generate_text_file('sorted_names.txt')
    except:
        print("A text (.txt) file of names to be passed as a command line argument")