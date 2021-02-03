#Problem 3
import unittest

def call_full_name(first, last):
  if len(first) > 0:
    if len(last) > 0:
      full_name = first + " " + last
      return full_name


class CustomTests(unittest.TestCase): 
  def test_vol_1(self):
    print(call_full_name("jaegeun","oh"))

  def test_vol_2(self):
    print(call_full_name("Alex",""))
  
  def test_vol_3(self):
    print(call_full_name(4, 5))

if __name__ == '__main__':  
    unittest.main(verbosity=2)