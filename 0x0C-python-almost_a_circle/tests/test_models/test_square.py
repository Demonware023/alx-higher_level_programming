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

        def test_getter(self):
            s1 = Square(5)
            self.assertEqual(s1.size, 5)

            s2 = Square(10)
            self.assertEqual(s2.size, 10)

        def test_setter(self):
            s1 = Square(5)
            s1.size = 8
            self.assertEqual(s1.size, 8)
            self.assertEqual(s1.width, 8)
            self.assertEqual(s1.height, 8)

            s2 = Square(10)
            s2.size = 3
            self.assertEqual(s2.size, 3)
            self.assertEqual(s2.width, 3)
            self.assertEqual(s2.height, 3)

        def test_invalid_setter(self):
            s1 = Square(5)
            with self.assertRaises(ValueError) as context:
                s1.size = -2
            self.assertTrue("width must be > 0" in str(context.exception))

            with self.assertRaises(TypeError) as context:
                s1.size = "xyz"
            self.assertTrue("width must be an intger" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
