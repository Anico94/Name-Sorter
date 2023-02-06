import unittest
import os
from text_file_writer import TextFileWriter as tfw

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