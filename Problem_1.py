#Problem 1
import unittest

def cal_vol(a):
  if a >= 0:
    return a * a * a
  else:
    return False


class CustomTests(unittest.TestCase): 
  def test_vol_1(self):
    print(cal_vol(4))

  def test_vol_2(self):
    print(cal_vol(-4))
  
  def test_vol_3(self):
    print(cal_vol("s"))

if __name__ == '__main__':  
    unittest.main(verbosity=2)