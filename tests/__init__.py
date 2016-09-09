import unittest
from code import mysum,  httpreq
from requests.exceptions import MissingSchema

class TestMath(unittest.TestCase):
  def test_sum(self):
    self.assertEqual(mysum(1, 2), 3)

  def test_failed_request(self):
    with self.assertRaises(MissingSchema):
      httpreq('github.com')
  
  def test_broken_test(self):
    self.assertEqual(1, 2)

if __name__ == '__main__':
  unittest.main()

