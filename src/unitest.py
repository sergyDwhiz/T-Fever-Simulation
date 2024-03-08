import unittest
import numpy as np

class TestSimulateDiff(unittest.TestCase):
    def test_deriv(self):
        from simulate_diff import deriv

        # Test case: S=500, I=100, R=50, N=1000, beta=0.2, gamma=0.1
        y = (500, 100, 50)
        t = 0
        N = 1000
        beta = 0.2
        gamma = 0.1

        # Expected output: dSdt=-10, dIdt=10, dRdt=10
        expected_output = (-10, 10, 10)

        # Call the function with the test case
        output = deriv(y, t, N, beta, gamma)

        # Check that the output is as expected
        np.testing.assert_allclose(output, expected_output, rtol=1e-5)

if __name__ == '__main__':
    unittest.main()