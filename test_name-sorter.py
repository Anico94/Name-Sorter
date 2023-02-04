import unittest
import os
from name_sorter import NameSorter as ns
from name_sorter import TextFileReader as tfr
from name_sorter import TextFileWriter as tfw

class TestNameSorter(unittest.TestCase):
  def test_sort_by_last_name(self):
    sorted_name_list = ns(['Alex Nico', 'Andrea Lawton', 'Peter Michael']).sort_by_last_name()
    self.assertEqual(sorted_name_list, ['Andrea Lawton','Peter Michael','Alex Nico'])


class TestTextFileReader(unittest.TestCase):
  def setUp(self):
    with open('test.txt', mode='w', newline='') as file:
        file.write("file line1\nfile line2\nfile line3")
    
  def test_list_of_lines(self):
    list_of_file_lines = tfr('test.txt').list_of_lines()
    self.assertEqual(list_of_file_lines, ['file line1','file line2','file line3'])

  def tearDown(self):
    os.remove('test.txt')


class TestTextFileWriter(unittest.TestCase):
  def setUp(self):
    string_list = ['file line1','file line2','file line3']
    tfw(string_list).generate_text_file('test.txt')
    
  def test_generate_text_file(self):
    with open('test.txt', mode='r', newline='') as file:
      file_string = file.read()
      self.assertEqual(file_string, "file line1\nfile line2\nfile line3")
    
  def tearDown(self):
    os.remove('test.txt')
  

if __name__ == '__main__':
  unittest.main()



