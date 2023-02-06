# Name Sorter - Python

A command line application that sorts a text file of names by the last name and then by any given first names.
Each name will occupy a single line in the text file. A name must have at least 1 given name and can have up to 3 given names.

# Running application

Depending on the installation method of python the command line application can be run using:

- python name_sorter.py unsorted-names-list.txt or
- python3 name_sorter.py unsorted-names-list.txt

The text file unsorted-names-list.txt should be save in the same directory as the name_sorter.py file.

Running this application will display the sorted names to the command line/ terminal and will create/overwrite a text file "sorted-names.txt" in the working directory.

## Unit Tests

Unit test have been writen in files beginning with "test\_"
These can be run in the terminal or command line with:

- pytest or
- py.test
