import unittest
import hw1

class TestHw1(unittest.TestCase):
    def test_triangle(self):
        cases = [((5, 5, 5), 'Equilateral'),
                 ((2, 2, 3), 'Isosceles'),
                 ((3, 4, 5), 'Scalene'),
                 ((4, 1, 2), 'Not a triangle'),
                 ((-1, 5, 5), 'Value of a is not in the range of permitted values'),
                 ((5, -1, 5), 'Value of b is not in the range of permitted values'),
                 ((5, 5, -1), 'Value of c is not in the range of permitted values'),
                 ((201, 5, 5), 'Value of a is not in the range of permitted values'),
                 ((5, 201, 5), 'Value of b is not in the range of permitted values'),
                 ((5, 5, 201), 'Value of c is not in the range of permitted values')]

        for value, result in cases:
            self.assertEqual(hw1.triangle(*value), result)

if __name__ == '__main__':
    unittest.main()
