import basic    # The code to test
import unittest   # The test framework

exercise = basic.Exercises()


class Test_basic(unittest.TestCase):
    def test_multiply_or_sum(self):
        self.assertEqual(exercise.multiply_or_sum(3, 4), 12)


if __name__ == '__main__':
    unittest.main()
