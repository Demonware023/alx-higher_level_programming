import unittest
from models.square import Square
from io import StringIO
import sys

class TestSquare(unittest.TestCase):

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
