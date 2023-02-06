import unittest
import os
from txt_file_reader import TxtFileReader as tfr
from os import path

class TestTextFileReader(unittest.TestCase):
    
  def test_read_in_list_of_lines(self):
    with open('test.txt', mode='w', newline='') as file:
        file.write("file line1\nfile line2\nfile line3")
    list_of_file_lines = tfr('test.txt').list_of_lines()
    self.assertEqual(list_of_file_lines, ['file line1','file line2','file line3'])
    os.remove('test.txt')

  def test_file_contains_no_lines_of_names(self):
    with open('test.txt', mode='w',newline="") as file:
      file.write("")
    with self.assertRaises(Exception):
      len(tfr('test.txt').list_of_lines()) == 0
    os.remove('test.txt')

  def test_file_doesnt_exists_in_the_directory(self):
      with self.assertRaises(Exception):
        path.exists(tfr('test.txt').file_name) == False

if __name__ == '__main__':
  unittest.main()