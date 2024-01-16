"""Testcases for Base Class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testBase(unittest.TestCase):
  """Test Class for Base class"""
  def setUp(self):
    Base.__Base__nb_objects = 0

  def test_1_0(self):
    """Create new instances: check for id."""
    b0 = Base()
    self.assertEqual(b0.id, 1)

  def test_1_1(self):
    """test for type an instance"""
    b3 = Base()
    self.assertEqual(type(b3), Base)

if __name__ == '__main__':
  unittest.main()
