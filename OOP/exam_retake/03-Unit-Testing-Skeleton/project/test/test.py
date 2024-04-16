import unittest
from project.restaurant import Restaurant


class TestRestaurant(unittest.TestCase):
    def setUp(self):
        self.reast = Restaurant('Marko', 10)
        self.reast_with_waiters = Restaurant('RW', 10)
        self.reast_with_waiters.waiters = [{"name": "Pesho"}, {"name": "Gosho"}]

    def test_init_with_correct_info(self):
        self.assertEqual(self.reast.name, 'Marko')
        self.assertEqual(self.reast.capacity, 10)
        self.assertEqual(self.reast.waiters, [])

    def test_with_no_name(self):
        with self.assertRaises(ValueError) as ve:
            Restaurant(None, 10)
        self.assertEqual("Invalid name!", str(ve.exception))

    def test_with_whitespace_name(self):
        with self.assertRaises(ValueError) as ve:
            Restaurant(' ', 10)
        self.assertEqual("Invalid name!", str(ve.exception))

    def test_with_negative_capacity(self):
        with self.assertRaises(ValueError) as ve:
            Restaurant('Marko', -10)
        self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_get_waiters_with_no_restrictions(self):
        self.assertEqual([{"name": "Pesho"}, {"name": "Gosho"}],
                         self.reast_with_waiters.get_waiters())

    def test_get_waiters_with_restrictions(self):
        self.assertEqual([],
                         self.reast_with_waiters.get_waiters(min_earnings=5))

    def test_add_waiter_with_full_capacity(self):
        self.reast_with_waiters.capacity = 2
        actual = self.reast_with_waiters.add_waiter('Kiro')
        self.assertEqual('No more places!', actual)

    def test_add_waiter_with_existing_name(self):
        actual = self.reast_with_waiters.add_waiter('Pesho')
        self.assertEqual('The waiter Pesho already exists!', actual)

    def test_add_waiter_with_correct_name(self):
        actual = self.reast_with_waiters.add_waiter('Kiro')
        self.assertEqual('The waiter Kiro has been added.', actual)
        self.assertEqual([{'name': 'Pesho'}, {'name': 'Gosho'},
                          {'name': 'Kiro'}],
                         self.reast_with_waiters.waiters)

    def test_remove_waiter_with_existing_name(self):
        actual = self.reast_with_waiters.remove_waiter('Pesho')
        self.assertEqual('The waiter Pesho has been removed.', actual)
        self.assertEqual([{'name': 'Gosho'}], self.reast_with_waiters.waiters)

    def test_remove_waiter_with_not_existing_name(self):
        actual = self.reast_with_waiters.remove_waiter('Kiro')
        self.assertEqual('No waiter found with the name Kiro.', actual)
        self.assertEqual([{'name': 'Pesho'}, {'name': 'Gosho'}],
                         self.reast_with_waiters.waiters)

    def test_get_total_earnings(self):
        self.assertEqual(0, self.reast.get_total_earnings())
        self.assertEqual(0, self.reast_with_waiters.get_total_earnings())

    def test_get_total_earnings_with_actual_earnings(self):
        self.reast_with_waiters.waiters = [{"name": "Pesho", "total_earnings": 10},
                                           {"name": "Gosho", "total_earnings": 20}]
        self.assertEqual(30, self.reast_with_waiters.get_total_earnings())



if __name__ == '__main__':
    unittest.main()
