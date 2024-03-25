import unittest
from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Mark")
        self.student_with_courses = Student("Jimi", {"math": ["x + y = z"]})

    def test_correct_init(self):
        self.assertEqual("Mark", self.student.name)
        self.assertEqual("Jimi", self.student_with_courses.name)

        self.assertEqual({}, self.student.courses)
        self.assertEqual({"math": ["x + y = z"]}, self.student_with_courses.courses)

    def test_enroll_in_the_same_course_appends_new_notes(self):
        result = self.student_with_courses.enroll(
            "math", ["1 + 2", "2 + 4"]
        )

        self.assertEqual("Course already added. Notes have been updated.", result)

        self.assertEqual(
            ["x + y = z", "1 + 2", "2 + 4"],
            self.student_with_courses.courses["math"]
        )

    def test_enroll_in_new_course_without_third_param_adds_notes_to_course(self):
        result = self.student.enroll("math", ["x + y"])

        self.assertEqual("Course and course notes have been added.", result)

        self.assertEqual({"math": ["x + y"]}, self.student.courses)

    def test_enroll_with_third_param_Y_adds_notes_to_course(self):
        result = self.student.enroll("math", ["x + y"], "Y")

        self.assertEqual("Course and course notes have been added.", result)

        self.assertEqual({"math": ["x + y"]}, self.student.courses)

    def test_enroll_with_third_param_NO_returns_empty_list_to_course(self):
        result = self.student.enroll("math", ["x + y"], "NO")

        self.assertEqual("Course has been added.", result)

        self.assertEqual({"math": []}, self.student.courses)

    def test_add_notes_to_existing_course_expect_success(self):
        result = self.student_with_courses.add_notes("math", "abc")

        self.assertEqual("Notes have been updated", result)

        self.assertEqual(["x + y = z", "abc"], self.student_with_courses.courses["math"])

    def test_add_notes_to_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("math", "some note")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course_expect_success(self):
        result = self.student_with_courses.leave_course("math")

        self.assertEqual("Course has been removed", result)

        self.assertEqual({}, self.student_with_courses.courses)

    def test_leave_course_with_non_existent_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("math")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))



if __name__ == '__main__':
    unittest.main()
