import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch

class TestRectangle(unittest.TestCase):
    def test_constructor_defaults(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.id, 5)
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

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        expected = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_update(self):
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 3, 4, 5, 6)
        self.assertEqual(r.to_dictionary(), {'id': 2, 'width': 3, 'height': 4, 'x': 5, 'y': 6})

        r.update(height=10, width=20, id=3, x=30, y=40)
        self.assertEqual(r.to_dictionary(), {'id': 3, 'width': 20, 'height': 10, 'x': 30, 'y': 40})

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        
        # Save rectangles to file
        Rectangle.save_to_file([r1, r2])
        
        # Check if file exists
        self.assertTrue(os.path.exists("Rectangle.json"))
        
        # Read file and check content
        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected_content = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},' \
                                '{"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
            self.assertEqual(content.strip(), expected_content)

        # Clean up: delete the file after the test
        os.remove("Rectangle.json")

if __name__ == '__main__':
    unittest.main()
