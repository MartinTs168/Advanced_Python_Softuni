from cat import Cat
import unittest


class TestCat(unittest.TestCase):

    def setUp(self):
        self.cat = Cat("Tiger")

    def test_correct_init(self):
        self.assertEqual("Tiger", self.cat.name)
        self.assertEqual(0, self.cat.size)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)

    def test_eat_should_make_cat_sleepy_fed_and_increase_size(self):
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertEqual(expected_size, self.cat.size)
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

    def test_eat_when_fed_should_raise_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleep_makes_cat_not_sleepy(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_sleep_raises_exception_when_cat_is_not_fed(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == '__main__':
    unittest.main()
