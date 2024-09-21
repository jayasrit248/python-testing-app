import unittest
from multiply import multiplication
class MultiplyTestcase(unittest,Testcase):
  def test_1(self):
    result = multiplication(3,4)
    self.assertEqual(result,12)
    def test_2(self):
      result = multiplication(3, -4)
      self.assertEqual(result,-12)
      def test_3(self):
        result = multiplication(-3,-4)
        self.assertEqual(result,12) 
if__name_=='__main__":
unittest.main()
