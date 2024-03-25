import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("George", "dog", "wuf")

    def test_correct_init(self):
        self.assertEqual("George", self.mammal.name)
        self.assertEqual("dog", self.mammal.type)
        self.assertEqual("wuf", self.mammal.sound)

    def test_get_kingdom_returns_correct_format(self):
        expected = "animals"
        result = self.mammal.get_kingdom()
        self.assertEqual(expected, result)

    def test_make_sound_returns_correct_format_and_information(self):
        expected = "George makes wuf"
        result = self.mammal.make_sound()
        self.assertEqual(expected, result)

    def test_info_returns_correct_format_and_information(self):
        expected = "George is of type dog"
        result = self.mammal.info()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
