'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''
# This function will allow the user to add two variables.

# if user provides variables x = 2, y =3
#    print response
#        "The result is 5"

import unittest

class TestSum(unittest.TestCase):

    def test_sum_of_variables(self):
        self.assertEqual(sum(2,3), 5, "Should be 5")

if __name__ == '__main__':
    unittest.main()