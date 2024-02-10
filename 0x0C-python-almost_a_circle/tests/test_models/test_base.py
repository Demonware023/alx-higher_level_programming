import unittest
from models.base import base

class TestBase(unittest.TestCase):
    def test_initialization_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_init_with_id(self):
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

if __name__ == '__main__':
    unittest.main()
