import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_initialization_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 3)
        self.assertEqual(b2.id, 4)

    def test_initialization_with_id(self):
        b1 = Base(10)
        b2 = Base(20)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 20)

    def test_id_incrementation(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(100)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 100)

    def test_to_json_string_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none_input(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_single_dict(self):
        input_dict = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        expected_json_string = '{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}'
        json_string = Base.to_json_string([input_dict])
        self.assertEqual(json_string.replace(' ', ''), expected_json_string.replace(' ', ''))

    def test_to_json_string_multiple_dicts(self):
        input_list = [
            {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8},
            {'id': 2, 'width': 8, 'height': 5, 'x': 5, 'y': 3}
        ]
        expected_json_string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},' \
                               '{"id": 2, "width": 8, "height": 5, "x": 5, "y": 3}]'
        json_string = Base.to_json_string(input_list)
        self.assertEqual(json_string.replace(' ', ''), expected_json_string.replace(' ', ''))

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected_content = '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
            self.assertEqual(content, expected_content)

    def test_save_to_file_no_objects(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(r1, r2)

    def test_create_square(self):
        s1 = Square(3, 1)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertIsInstance(s2, Square)
        self.assertEqual(s1, s2)

    def test_create_with_empty_dictionary(self):
        obj = Base.create()
        self.assertIsNone(obj)

    def test_create_with_invalid_class(self):
        obj = Base.create(width=10, height=5)
        self.assertIsNone(obj)

    def setUp(self):
        # Create sample data for testing
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)
        self.list_rectangles_input = [self.r1, self.r2]
        Rectangle.save_to_file(self.list_rectangles_input)

        self.s1 = Square(5)
        self.s2 = Square(7, 9, 1)
        self.list_squares_input = [self.s1, self.s2]
        Square.save_to_file(self.list_squares_input)

    def tearDown(self):
        # Clean up the created files
        file_names = ["Rectangle.json", "Square.json"]
        for file_name in file_names:
            if os.path.exists(file_name):
                os.remove(file_name)

    def test_load_from_file_rectangle(self):
        # Test loading rectangles from file
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), len(self.list_rectangles_input))
        for rect_in, rect_out in zip(self.list_rectangles_input, rectangles):
            self.assertEqual(rect_in.width, rect_out.width)
            self.assertEqual(rect_in.height, rect_out.height)
            self.assertEqual(rect_in.x, rect_out.x)
            self.assertEqual(rect_in.y, rect_out.y)

    def test_load_from_file_square(self):
        # Test loading squares from file
        squares = Square.load_from_file()
        self.assertEqual(len(squares), len(self.list_squares_input))
        for square_in, square_out in zip(self.list_squares_input, squares):
            self.assertEqual(square_in.size, square_out.size)
            self.assertEqual(square_in.x, square_out.x)
            self.assertEqual(square_in.y, square_out.y)

if __name__ == '__main__':
    unittest.main()
