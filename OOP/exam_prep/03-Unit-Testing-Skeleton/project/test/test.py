import unittest
from project.climbing_robot import ClimbingRobot


class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = ClimbingRobot("Alpine",
                                   "metal", 20, 10)

    def test_correct_init(self):
        self.assertEqual("Alpine", self.robot.category)
        self.assertEqual("metal", self.robot.part_type)
        self.assertEqual(20, self.robot.capacity)
        self.assertEqual(10, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_non_allowed_category_should_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "incorrect"

        self.assertEqual(f"Category should be one of {ClimbingRobot.ALLOWED_CATEGORIES}", str(ve.exception))

    def test_get_used_capacity_with_capacity_consumption_equal_to_10_should_return_10(self):
        self.robot.installed_software = [{"capacity_consumption": 5}, {"capacity_consumption": 5}]
        actual = self.robot.get_used_capacity()
        self.assertEqual(10, actual)

    def test_get_available_capacity_with_taken_capacity_equal_to_15_should_return_5(self):
        self.robot.installed_software = [{"capacity_consumption": 10}, {"capacity_consumption": 5}]
        actual = self.robot.get_available_capacity()
        self.assertEqual(5, actual)

    def test_get_used_memory_with_taken_memory_equals_3_should_return_3(self):
        self.robot.installed_software = [{"memory_consumption": 1}, {"memory_consumption": 2}]
        actual = self.robot.get_used_memory()
        self.assertEqual(3, actual)

    def test_get_available_memory_with_taken_memory_equals_3_should_return_7(self):
        self.robot.installed_software = [{"memory_consumption": 1}, {"memory_consumption": 2}]
        actual = self.robot.get_available_memory()
        self.assertEqual(7, actual)

    def test_install_software_with_0_capacity_should_return_proper_message(self):
        self.robot.capacity = 0
        actual = self.robot.install_software(
            {'capacity_consumption': 1, 'memory_consumption': 1, 'name': 'VisualStudio'})
        self.assertEqual("Software 'VisualStudio' cannot be installed on Alpine part.", actual)

    def test_install_software_with_0_memory_should_return_appropriate_memory(self):
        self.robot.memory = 0
        actual = self.robot.install_software(
            {'capacity_consumption': 1, 'memory_consumption': 1, 'name': 'VisualStudio'})
        self.assertEqual("Software 'VisualStudio' cannot be installed on Alpine part.", actual)

    def test_install_software_with_0_memory_and_capacity_should_return_error_message(self):
        self.robot.memory, self.robot.capacity = 0, 0
        actual = self.robot.install_software(
            {'capacity_consumption': 1, 'memory_consumption': 1, 'name': 'VisualStudio'})
        self.assertEqual("Software 'VisualStudio' cannot be installed on Alpine part.", actual)

    def test_install_software_with_available_memory_and_capacity_should_return_proper_message_and_append_software(self):
        actual = self.robot.install_software(
            {'capacity_consumption': 1, 'memory_consumption': 1, 'name': 'VisualStudio'})
        self.assertEqual("Software 'VisualStudio' successfully installed on Alpine part.", actual)
        self.assertEqual([{'capacity_consumption': 1, 'memory_consumption': 1, 'name': 'VisualStudio'}],
                         self.robot.installed_software)

    def test_install_software_with_max_available_memory_and_capacity_should_return_proper_message_and_append_software(
            self):
        actual = self.robot.install_software(
            {'capacity_consumption': 20, 'memory_consumption': 10, 'name': 'VisualStudio'})
        self.assertEqual("Software 'VisualStudio' successfully installed on Alpine part.", actual)
        self.assertEqual([{'capacity_consumption': 20, 'memory_consumption': 10, 'name': 'VisualStudio'}],
                         self.robot.installed_software)


if __name__ == '__main__':
    unittest.main()
