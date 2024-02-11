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

        def test_update_with_args(self):
            s1 = Square(5)
            s1.update(10)
            self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

            s1.update(1, 2)
            self.assertEqual(str(s1), "[Square] (1) (0/0 - 2")

            s1.update(1, 2, 3)
            self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

	    s1.update(1, 2, 3, 4)
            self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        def test_update_with_kwargs(self):
            s1 = Square(5)
            s1.update(x=12)
            self.assertEqual(str(s1), "[Square] (1) 12/0 - 5")

	    s1.update(size=7, y=1)
            self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

            s1.update(size=7, id=89, y=1)
            self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

        def test_update_mixed(self):
            s1 = Square(5)
            s1.update(10, 2, y=3)
            self.assertEqual(str(s1), "[Square] (10) 0/3 - 2")

if __name__ == '__main__':
    unittest.main()
