import unittest
from sortPackage import sort

class TestSortFunction(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(sort(100, 100, 100, 10), "STANDARD")

    def test_bulky(self):
        self.assertEqual(sort(160, 50, 50, 10), "SPECIAL")

    def test_heavy(self):
        self.assertEqual(sort(100, 100, 100, 25), "SPECIAL")

    def test_rejected(self):
        self.assertEqual(sort(160, 100, 100, 25), "REJECTED")

    def test_edge_cases(self):
        self.assertEqual(sort(150, 50, 50, 19.99), "SPECIAL")
        self.assertEqual(sort(100, 100, 100, 20), "SPECIAL")
        self.assertEqual(sort(100, 100, 100, 19.99), "STANDARD")

if __name__ == "__main__":
    unittest.main()
