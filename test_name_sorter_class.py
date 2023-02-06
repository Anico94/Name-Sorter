import unittest
from name_sorter_class import NameSorter as ns

class TestNameSorter(unittest.TestCase):
  def test_sort_by_last_name(self):
    sorted_name_list = ns().sort_by_last_name(['Janet Parsons', 'Marin Alvarez', 'Leo Gardner'])
    self.assertEqual(sorted_name_list, ['Marin Alvarez','Leo Gardner','Janet Parsons'])
    
  def test_sort_names_with_the_same_last_name(self):
    sorted_name_list = ns().sort_by_last_name(['Hunter Uriah Mathew Clarke','Hunter Mathew Clarke', 'Hunter Clarke','Hunter Uriah Clarke'])
    self.assertEqual(sorted_name_list,['Hunter Clarke','Hunter Mathew Clarke','Hunter Uriah Clarke','Hunter Uriah Mathew Clarke'])

  def test_sort_names_all_same(self):
    sorted_names_list = ns().sort_by_last_name(['Janet Parsons','Janet Parsons','Janet Parsons'])
    self.assertEqual(sorted_names_list, ['Janet Parsons','Janet Parsons','Janet Parsons'])

if __name__ == '__main__':
  unittest.main()



