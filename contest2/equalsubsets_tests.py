import unittest
from equalsubsets import find_equal_sums
class TestFindEqualSums(unittest.TestCase):
    def test_single_case_no_solution(self):
        n = 1
        test_cases = ["1 2 3"]
        expected = []
        self.assertEqual(find_equal_sums(n, test_cases), expected)

    def test_single_case_with_solution(self):
        n = 1
        test_cases = ["1 2 3 4 5 5"]
        expected = [("1 2 3", "4 5"), ("1 2 5", "3 5"), ("1 4 5", "2 3 5"), ("2 3 5", "1 4 5"), ("3 5", "1 2 5"), ("4 5", "1 2 3")]
        self.assertEqual(find_equal_sums(n, test_cases), expected)

    def test_multiple_cases(self):
        n = 2
        test_cases = ["1 2 3", "1 2 3 4 5 5"]
        expected = [("1 2 3", "4 5"), ("1 2 5", "3 5"), ("1 4 5", "2 3 5"), ("2 3 5", "1 4 5"), ("3 5", "1 2 5"), ("4 5", "1 2 3")]
        self.assertEqual(find_equal_sums(n, test_cases), expected)

if __name__ == '__main__':
    unittest.main()