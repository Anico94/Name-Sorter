import unittest
from name import Name

class TestTxtFileReader(unittest.TestCase):
  def setUp(self):
    self.name = Name('Beau Tristan Bentley')
    
  def test_output_of_last_name(self):
   self.assertEqual(self.name.last_name, "Bentley")
  
  def test_output_of_given_names(self):
    self.assertEqual(self.name.given_names,"Beau Tristan")

  def test_output_of_full_name(self):
    self.assertEqual(self.name.name, 'Beau Tristan Bentley')