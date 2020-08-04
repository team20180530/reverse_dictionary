from Mars import *
import unittest

output_value = {
  'I': {
    'deserve': {
      'to': {
         'be': 'hired'
      }
    }
  }
}

class TestMars(unittest.TestCase):
    def testReverse(self):
        self.assertTrue(One().reverse() == output_value)

if __name__ == '__main__':
    unittest.main()