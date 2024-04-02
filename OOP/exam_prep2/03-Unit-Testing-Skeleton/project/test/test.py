import unittest
from project.railway_station import RailwayStation
from collections import deque


class TestRailwayStation(unittest.TestCase):
    def setUp(self):
        self.station = RailwayStation("Central")
        self.st_with_arrival_trains = RailwayStation("Central")
        self.st_with_arrival_trains.arrival_trains = deque(["Sofia-Pernik", "Pernik-Radomir"])
        self.st_with_departure_trains = RailwayStation("Central")
        self.st_with_departure_trains.departure_trains = deque(["Sofia-Pernik", "Pernik-Radomir"])

    def test_correct_init(self):
        self.assertEqual("Central", self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_invalid_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "A"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board_should_append_train_info_to_list(self):
        train_info = "Sofia-Pernik"
        self.station.new_arrival_on_board(train_info)
        self.assertIn(train_info, self.station.arrival_trains)

    def test_train_has_arrived_with_incorrect_train_info_should_return_given_message(self):
        train_info = "Pernik-Radomir"
        actual = self.st_with_arrival_trains.train_has_arrived(train_info)
        self.assertEqual(f"There are other trains to arrive before {train_info}.", actual)

    def test_train_has_arrived_correct_train_info_should_append_to_departure_trains_and_return_expected_message(self):
        train_info = "Sofia-Pernik"
        actual = self.st_with_arrival_trains.train_has_arrived(train_info)
        self.assertEqual(f"{train_info} is on the platform and will leave in 5 minutes.", actual)
        self.assertIn(train_info, self.st_with_arrival_trains.departure_trains)

    def test_train_has_left_with_incorrect_train_info_should_return_false(self):
        train_info = "Pernik-Radomir"
        self.assertFalse(self.st_with_departure_trains.train_has_left(train_info))

    def test_train_has_left_with_correct_train_info_should_return_true(self):
        train_info = "Sofia-Pernik"
        self.assertTrue(self.st_with_departure_trains.train_has_left(train_info))


if __name__ == '__main__':
    unittest.main()
