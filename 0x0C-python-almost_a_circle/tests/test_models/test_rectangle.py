import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch

class TestRectangle(unittest.TestCase):
    def test_constructor_defaults(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_constructor_custom_id(self):
        r = Rectangle(5, 10, id=20)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_getters_setters(self):
        r = Rectangle(5, 10)
        r.width = 7
        r.height = 15
        r.x = 3
        r.y = 5
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 5)

    def test_constructor_invalid_width(self):
        with self.assertRaises(TypeError) as context:
            Rectangle("10", 2)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_constructor_invalid_height(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, "2")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_constructor_invalid_x(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, 2, "3")
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_constructor_invalid_y(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, 2, 3, "4")
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_constructor_invalid_width_value(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(0, 2)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_constructor_invalid_height_value(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 0)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_constructor_invalid_x_value(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 2, -3)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_constructor_invalid_y_value(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 2, 3, -4)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_width_setter_invalid_value(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as context:
            r.width = -10
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_height_setter_invalid_value(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as context:
            r.height = -5
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_x_setter_invalid_value(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as context:
            r.x = -3
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_y_setter_invalid_value(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as context:
            r.y = -4
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        r1 = Rectangle(4, 6)
        expected_output = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

        r2 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r2.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display(self):
        r1 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

        r2 = Rectangle(3, 2, 1, 0)
        expected_output = " ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r2.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1, id=1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_update_with_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

        r.update(89, 2)
        self.assertEqual(r.width, 2)

        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)

        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)

    def test_update_with_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89)
        self.assertEqual(r.id, 89)

        r.update(width=2, height=3)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)

        r.update(x=4, y=5)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

if __name__ == '__main__':
    unittest.main()
