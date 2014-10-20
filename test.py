import unittest
import hw1

class TestHw1(unittest.TestCase):
    def test_triangle(self):
        cases = [
                 # equivalence class
                 ((5, 5, 5),   'Equilateral'),
                 ((2, 2, 3),   'Isosceles'),
                 ((3, 4, 5),   'Scalene'),
                 ((4, 1, 2),   'Not a triangle'),
                 ((-1, 5, 5),  'Value of a is not in the range of permitted values'),
                 ((5, -1, 5),  'Value of b is not in the range of permitted values'),
                 ((5, 5, -1),  'Value of c is not in the range of permitted values'),
                 ((201, 5, 5), 'Value of a is not in the range of permitted values'),
                 ((5, 201, 5), 'Value of b is not in the range of permitted values'),
                 ((5, 5, 201), 'Value of c is not in the range of permitted values'),
                 ((-1, 5, 5),  'Value of a is not in the range of permitted values'),
                 ((5, -1, 5),  'Value of b is not in the range of permitted values'),
                 ((5, 5, -1),  'Value of c is not in the range of permitted values'),
                 ((-1, -1, 5), 'Value of a,b is not in the range of permitted values'),
                 ((5, -1, -1), 'Value of b,c is not in the range of permitted values'),
                 ((-1, 5, -1), 'Value of a,c is not in the range of permitted values'),
                 ((-1, -1, -1),'Value of a,b,c is not in the range of permitted values'),

                 # boundary
                 ((100, 100, 1),   'Isosceles'),
                 ((100, 100, 2),   'Isosceles'),
                 ((100, 100, 100), 'Equilateral'),
                 ((100, 100, 199), 'Isosceles'),
                 ((100, 100, 200), 'Not a triangle'),
                 ((100, 1, 100),   'Isosceles'),
                 ((100, 2, 100),   'Isosceles'),
                 ((100, 100, 100), 'Equilateral'),
                 ((100, 199, 100), 'Isosceles'),
                 ((100, 200, 100), 'Not a triangle'),
                 ((1, 100, 100),   'Isosceles'),
                 ((2, 100, 100),   'Isosceles'),
                 ((100, 100, 100), 'Equilateral'),
                 ((199, 100, 100), 'Isosceles'),
                 ((200, 100, 100), 'Not a triangle'),
                 ((1, 1, 1),       'Equilateral'),
                 ((1, 1, 2),       'Not a triangle'),
                 ((1, 1, 100),     'Not a triangle'),
                 ((1, 1, 199),     'Not a triangle'),
                 ((1, 1, 200),     'Not a triangle'),
                 ((1, 2, 1),       'Not a triangle'),
                 ((1, 2, 2),       'Isosceles'),
                 ((1, 2, 100),     'Not a triangle'),
                 ((1, 2, 199),     'Not a triangle'),
                 ((1, 2, 200),     'Not a triangle'),
                 ((1, 100, 1),     'Not a triangle'),
                 ((1, 100, 2),     'Not a triangle'),
                 ((1, 100, 100),   'Isosceles'),
                 ((1, 100, 199),   'Not a triangle'),
                 ((1, 100, 200),   'Not a triangle'),
                 ((1, 199, 1),     'Not a triangle'),
                 ((1, 199, 2),     'Not a triangle'),
                 ((1, 199, 100),   'Not a triangle'),
                 ((1, 199, 199),   'Isosceles'),
                 ((1, 199, 200),   'Not a triangle'),
                 ((1, 200, 1),     'Not a triangle'),
                 ((1, 200, 2),     'Not a triangle'),
                 ((1, 200, 100),   'Not a triangle'),
                 ((1, 200, 199),   'Not a triangle'),
                 ((1, 200, 200),   'Isosceles'),
        ]

        for value, result in cases:
            self.assertEqual(hw1.triangle(*value), result)

if __name__ == '__main__':
    unittest.main()
