import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 100)

    def test_correct_init(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.250, self.vehicle.fuel_consumption)

    def test_drive_raises_exception_when_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_reduces_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_valid_amount_of_fuel_adds_fuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(50)

        self.assertEqual(50, self.vehicle.fuel)

    def test_str_should_return_correct_format(self):
        expected = f"The vehicle has 100 " \
                   f"horse power with 50 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected, self.vehicle.__str__())


if __name__ == "__main__":
    unittest.main()
