import unittest
import os
from txt_file_writer import TxtFileWriter as tfw

class TestTextFileWriter(unittest.TestCase):
  def setUp(self):
    self.string_list = ['file line1','file line2','file line3']
    tfw(self.string_list).generate_text_file('test.txt')
    
  def test_generate_text_file(self):
    with open('test.txt', mode='r', newline='') as file:
      file_string = file.read()
      self.assertEqual(file_string, "file line1\nfile line2\nfile line3")

  def test_new_file_contains_same_number_of_lines_as_list_passed_in(self):
    with open('test.txt', mode='r', newline='') as file:
      file_lines = file.readlines()
      self.assertEqual(len(file_lines), len(self.string_list))
    
  def tearDown(self):
    os.remove('test.txt')

if __name__ == '__main__':
  unittest.main()