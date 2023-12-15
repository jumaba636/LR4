import unittest
from hello_function import hello

class HelloTestCase(unittest.TestCase):
   def test_hello(self):
        result = hello("shoxijaxon")
        self.assertEqual(result, "Hi, Shoxijaxon.")

if __name__ == '__main__':
    unittest.main()
