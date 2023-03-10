import unittest
from arithmetic_arranger import arithmetic_arranger


class TestArithmeticArranger(unittest.TestCase):

  def test_valid_input(self):
    problems = ["32 + 698", "3801 - 2"]
    expected_output = "  32      3801\n+ 698    -    2\n-----    ------"
    self.assertEqual(arithmetic_arranger(problems), expected_output)

  def test_invalid_input(self):
    problems = [
      "32 + 698", "3801 - 2", "4 + 4553", "123 + 49", "1234 - 9876",
      "1 + 2 + 3"
    ]
    expected_output = "Error: Too many problems."
    self.assertEqual(arithmetic_arranger(problems), expected_output)

  def test_invalid_operator(self):
    problems = ["32 ^ 698"]
    expected_output = "Error: Operator must be '+' or '-'."
    self.assertEqual(arithmetic_arranger(problems), expected_output)

  def test_invalid_number(self):
    problems = ["32 + 69a"]
    expected_output = "Error: Numbers must only contain digits."
    self.assertEqual(arithmetic_arranger(problems), expected_output)


if __name__ == '__main__':
  unittest.main()
