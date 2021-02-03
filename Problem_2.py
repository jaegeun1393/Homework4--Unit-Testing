#Problem 2
import unittest

def find_avg(lst):
  if len(lst) != 1:
    total = 0
    for x in lst:
      total = total + x

    total = total / len(lst)
    return total
  else:
    return lst[0]


class CustomTests(unittest.TestCase): 
  def test_vol_1(self):
    lst = [3, 4, 5, 5, 7, 8, 9, 9]
    print(find_avg(lst))

  def test_vol_2(self):
    lst = ["3", "d", "5"]
    print(find_avg(lst))
  
  def test_vol_3(self):
    lst = [0]
    print(find_avg(lst))

if __name__ == '__main__':  
    unittest.main(verbosity=2)