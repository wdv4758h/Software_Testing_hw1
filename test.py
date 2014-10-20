import unittest
import hw1

class TestHw1(unittest.TestCase):

    error_msg = '[parameter] {} [correct] {} [fail] {}'

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
            fresult = hw1.triangle(*value)
            self.assertEqual(fresult, result,
                    self.error_msg.format(repr(value), result, fresult))

    def test_next_date(self):
        cases = [
                 # equivalence class
                 ((6, 15, 1912),   '6/16/1912'),
                 ((-1, 15, 1912),  'month not in 1 ... 12'),
                 ((13, 15, 1912),  'month not in 1 ... 12'),
                 ((6, -1, 1912),   'day not in 1 ... 31'),
                 ((6, 32, 1912),   'day not in 1 ... 31'),
                 ((6, 15, 1811),   'year not in 1812 ... 2012'),
                 ((6, 15, 2013),   'year not in 1812 ... 2012'),
                 ((-1, 15, 1912),  'month not in 1 ... 12'),
                 ((6, -1, 1912),   'day not in 1 ... 31'),
                 ((6, 15, 1811),   'year not in 1812 ... 2012'),
                 ((-1, -1, 1912),  'month not in 1 ... 12\nday not in 1 ... 31'),
                 ((6, -1, 1811),   'day not in 1 ... 31\nyear not in 1812 ... 2012'),
                 ((-1, 15, 1811),  'month not in 1 ... 12\nyear not in 1812 ... 2012'),
                 ((-1, -1, 1811),  'month not in 1 ... 12\nday not in 1 ... 31\nyear not in 1812 ... 2012'),

                 # boundary
                 ((1, 1, 1812),  '1/2/1812'),
                 ((1, 1, 1813),  '1/2/1813'),
                 ((1, 1, 1912),  '1/2/1912'),
                 ((1, 1, 2011),  '1/2/2011'),
                 ((1, 1, 2012),  '1/2/2012'),
                 ((1, 2, 1812),  '1/3/1812'),
                 ((1, 2, 1813),  '1/3/1813'),
                 ((1, 2, 1912),  '1/3/1912'),
                 ((1, 2, 2011),  '1/3/2011'),
                 ((1, 2, 2012),  '1/3/2012'),
                 ((1, 15, 1812), '1/16/1812'),
                 ((1, 15, 1813), '1/16/1813'),
                 ((1, 15, 1912), '1/16/1912'),
                 ((1, 15, 2011), '1/16/2011'),
                 ((1, 15, 2012), '1/16/2012'),
                 ((1, 30, 1812), '1/31/1812'),
                 ((1, 30, 1813), '1/31/1813'),
                 ((1, 30, 1912), '1/31/1912'),
                 ((1, 30, 2011), '1/31/2011'),
                 ((1, 30, 2012), '1/31/2012'),
                 ((1, 31, 1813), '2/1/1813'),
                 ((1, 31, 1912), '2/1/1912'),
        ]

        for value, result in cases:
            fresult = hw1.next_date(*value)
            self.assertEqual(fresult, result,
                    self.error_msg.format(repr(value), result, fresult))

    def test_commision(self):
        cases = [
                 # equivalence class
                 ((10, 10, 10), '$100'),
                 ((-1, 40, 45), 'Program terminates'),
                 ((-2, 40, 45), 'locks not in 1 ... 70'),
                 ((71, 40, 45), 'locks not in 1 ... 70'),
                 ((35, -1, 45), 'stocks not in 1 ... 80'),
                 ((35, 81, 45), 'stocks not in 1 ... 80'),
                 ((35, 40, -1), 'barrels not in 1 ... 90'),
                 ((35, 40, 91), 'barrels not in 1 ... 90'),
                 ((-2, 40, 45), 'locks not in 1 ... 70'),
                 ((35, -1, 45), 'stocks not in 1 ... 80'),
                 ((35, 40, -2), 'barrels not in 1 ... 90'),
                 ((-2, -1, 45), 'locks not in 1 ... 70'),
                 ((-2, -1, 45), 'locks not in 1 ... 70\nstocks not in 1 ... 80'),
                 ((-2, 40, -1), 'locks not in 1 ... 70\nstocks not in 1 ... 90'),
                 ((35, -1, -1), 'locks not in 1 ... 80\nstocks not in 1 ... 90'),
                 ((-2, -1, -1), 'locks not in 1 ... 70\nlocks not in 1 ... 80\nstocks not in 1 ... 90'),
        ]

        for value, result in cases:
            fresult = hw1.commision(*value)
            self.assertEqual(fresult, result,
                    self.error_msg.format(repr(value), result, fresult))

if __name__ == '__main__':
    unittest.main()
