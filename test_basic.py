import basic    # The code to test
import unittest   # The test framework

exercise = basic.Exercises()


class Test_basic(unittest.TestCase):
    def test_multiply_or_sum(self):
        self.assertEqual(exercise.multiply_or_sum(3, 4), 12)

    def test_print_sum(self):
        self.assertEqual(exercise.print_sum(
            3), [[0, -1, -1], [1, 0, 1], [2, 1, 3]])

    def test_print_even_char(self):
        self.assertEqual(exercise.print_even_char("pynative"), "pntv")

    def test_remove_char(self):
        self.assertEqual(exercise.remove_char("pynative", 2), "native")

    def test_first_last_name_true(self):
        self.assertEqual(exercise.first_last_same([10, 20, 30, 40, 10]), True)

    def test_first_last_name_false(self):
        self.assertEqual(exercise.first_last_same([10, 20, 30, 40, 60]), False)

    def test_divisible_by_5(self):
        self.assertEqual(exercise.divisible_by_5(
            [10, 20, 33, 46, 55]), [10, 20, 55])

    def test_count_substring(self):
        self.assertEqual(exercise.count_substring(
            "Emma is good developer. Emma is a writer", "Emma"), 2)

    def test_check_palindrome_true(self):
        self.assertEqual(exercise.check_palindrome(121), True)

    def test_check_palindrome_false(self):
        self.assertEqual(exercise.check_palindrome(123), False)

    def test_mix_two_lists(self):
        self.assertEqual(exercise.mix_two_lists([10, 20, 25, 30, 35], [
                         40, 45, 60, 75, 90]), [25, 35, 40, 60, 90])

    def test_extract_digit_reverse(self):
        self.assertEqual(exercise.extract_digit_reverse(543),  "3 4 5")

    def test_calculate_income_tax(self):
        self.assertEqual(exercise.calculate_income_tax(45000),  6000)


if __name__ == '__main__':
    unittest.main()
