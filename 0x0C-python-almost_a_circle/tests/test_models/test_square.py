import unittest
from models.square import Square
from io import StringIO
import sys

class TestSquare(unittest.TestCase):
    def test_display(self):
        s1 = Square(5)
        expected_output = "#####\n#####\n#####\n#####\n#####\n"
        with StringIO() as output:
            sys.stdout = output
            s1.display()
            self.assertEqual(output.getvalue(), expected_output)

        s2 = Square(2, 2)
        expected_output = "  ##\n  ##\n"
        with StringIO() as output:
            sys.stdout = output
            s2.display()
            self.assertEqual(output.getvalue(), expected_output)

        s3 = Square(3, 1, 3)
        expected_output = '\n\n\n ###\n ###\n ###\n'
        with StringIO() as output:
            sys.stdout = output
            s3.display()
            self.assertEqual(output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
