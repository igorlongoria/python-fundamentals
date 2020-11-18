'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''
import unittest


def square(x):
    return x * x

def sum_squares(a, b, c):
    return (square(a) + square(b) + square(c))

sum_example_1 = (sum_squares(23,34,43))
sum_example_2 = (sum_squares(12,12,64))

class TestSum(unittest.TestCase):


    def test_square(self):
        self.assertEqual(square(3), 9, "Should be 9")

    def test_sum_squares(self):
        self.assertEqual(sum_squares(1, 2, 3), 14, "Should be 14")

    def test_sum_squares(self):
        self.assertGreater(sum_example_1, sum_example_2, "Sum_example_2 should be greater")

if __name__ == '__main__':
    unittest.main()