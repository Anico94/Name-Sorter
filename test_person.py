import unittest
from person import Person

class TestTxtFileReader(unittest.TestCase):
  def setUp(self):
    self.person = Person('Beau Tristan Bentley')
    
  def test_output_of_last_name(self):
   self.assertEqual(self.person.last_name, "Bentley")
  
  def test_output_of_given_names(self):
    self.assertEqual(self.person.given_names,"Beau Tristan")

  def test_output_of_full_name(self):
    self.assertEqual(self.person.name, 'Beau Tristan Bentley')