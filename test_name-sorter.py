import unittest
from name_sorter import NameSorter as ns

class TestNameSorter(unittest.TestCase):
  def test_sort_by_last_name(self):
    sorted_name_list1 = ns(['Janet Parsons', 'Marin Alvarez', 'Leo Gardner']).sort_by_last_name()
    sorted_name_list2 = ns(['Hunter Uriah Mathew Clarke','Hunter Mathew Clarke', 'Hunter Clarke','Hunter Uriah Clarke']).sort_by_last_name()
    self.assertEqual(sorted_name_list1, ['Marin Alvarez','Leo Gardner','Janet Parsons'])
    self.assertEqual(sorted_name_list2,['Hunter Clarke','Hunter Mathew Clarke','Hunter Uriah Clarke','Hunter Uriah Mathew Clarke'])

if __name__ == '__main__':
  unittest.main()



