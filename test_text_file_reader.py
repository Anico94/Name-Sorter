import unittest
import os
from text_file_reader import TextFileReader as tfr

class TestTextFileReader(unittest.TestCase):
  def setUp(self):
    with open('test.txt', mode='w', newline='') as file:
        file.write("file line1\nfile line2\nfile line3")
    
  def test_list_of_lines(self):
    list_of_file_lines = tfr('test.txt').list_of_lines()
    self.assertEqual(list_of_file_lines, ['file line1','file line2','file line3'])

  def tearDown(self):
    os.remove('test.txt')

if __name__ == '__main__':
  unittest.main()