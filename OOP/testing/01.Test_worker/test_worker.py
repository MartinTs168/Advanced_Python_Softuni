import unittest
from worker import Worker


class WorkerTests(unittest.TestCase):

    def setUp(self):
        self.worker = Worker("TestGuy", 2500, 100)

    def test_init(self):
        self.assertEqual(self.worker.name, "TestGuy")
        self.assertEqual(self.worker.salary, 2500)
        self.assertEqual(self.worker.energy, 100)
        self.assertEqual(self.worker.money, 0)

    def test_rest_method_should_increase_energy_by_one(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(self.worker.energy, expected_energy)

    def test_worker_when_worker_has_energy_expect_money_increase_energy_decrease(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(self.worker.money, expected_money)
        self.assertEqual(self.worker.energy, expected_energy)

    def test_work_when_worker_does_not_have_energy_raises_exception(self):
        self.worker.energy = 0  # arrange

        with self.assertRaises(Exception) as ex:
            self.worker.work()  # act

        self.assertEqual('Not enough energy.', str(ex.exception))  # assert

    def test_get_info_should_return_string_in_the_correct_format(self):
        self.worker.money = 100

        expected_message = 'TestGuy has saved 100 money.'
        actual_message = self.worker.get_info()

        self.assertEqual(actual_message, expected_message)


if __name__ == "__main__":
    unittest.main()
