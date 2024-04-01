import unittest

from Advanced_and_OOP.OOP.workshop_custom_hashtable.hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.h = HashTable()

    def test_init(self):
        self.assertEqual([None, None, None, None], self.h._HashTable__keys)
        self.assertEqual([None, None, None, None], self.h._HashTable__values)
        self.assertEqual(4, self.h._HashTable__length)

    def test_count(self):
        self.assertEqual(4, len(self.h))
        self.assertEqual(self.h._HashTable__length, len(self.h))


if __name__ == '__main__':
    unittest.main()
