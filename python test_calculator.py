#test function
def multiply(a, b):
    return a * b


#First test

import unittest

class TestMultiply(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        # Multiplying two positive numbers should return the correct product
        result = multiply(4, 6)
        self.assertEqual(result, 24)

    def test_multiply_negative_numbers(self):
        # Multiplying two negative numbers should return a positive product
        result = multiply(-3, -5)
        self.assertEqual(result, 15)

    def test_multiply_by_zero(self):
        # Any number multiplied by zero should be zero
        result = multiply(10, 0)
        self.assertEqual(result, 0)

# This allows the test suite to run when the file is executed.
if __name__ == "__main__":
    unittest.main()
