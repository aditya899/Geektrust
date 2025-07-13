import unittest
from src.lms import LMS
from src.courses.course import Course
from src.courses.course_enum import CourseStatus
from src.employees.employee import Employee


class TestRegisterCourse(unittest.TestCase):
    def setUp(self):
        self.lms = LMS()

    def test_input_data_error(self):
        result = self.lms.register_course(["REGISTER", "john@example.com"])
        self.assertEqual(result, "INPUT_DATA_ERROR")

    def test_course_not_found(self):
        result = self.lms.register_course(["REGISTER", "john@example.com", "OFFERING-PYTHON-JOHN"])
        self.assertIsNone(result)

    def test_successful_registration(self):
        course = Course("PYTHON", "JOHN", "2025-08-01", "5", "50")
        self.lms.lms["OFFERING-PYTHON-JOHN"] = course

        result = self.lms.register_course(["REGISTER", "john@example.com", "OFFERING-PYTHON-JOHN"])
        self.assertTrue(result.startswith("REG-COURSE-john-PYTHON"))
        self.assertEqual(len(course.employees), 1)
        self.assertEqual(course.employees[0].email, "john@example.com")
        self.assertEqual(course.employees[0].employee_status, "ACCEPTED")

    def test_registration_when_course_full(self):
        course = Course("PYTHON", "JOHN", "2025-08-01", "1", "1")
        employee = Employee("REG-1", "alice", "alice@example.com", "ACCEPTED")
        course.employees.append(employee)
        self.lms.lms["OFFERING-PYTHON-JOHN"] = course

        result = self.lms.register_course(["REGISTER", "john@example.com", "OFFERING-PYTHON-JOHN"])
        self.assertEqual(result, "COURSE_FULL_ERROR")

    def test_decline_registration_if_status_confirmed(self):
        course = Course("PYTHON", "JOHN", "2025-08-01", "5", "50")
        course.set_course_status(CourseStatus.CONFIRMED.value)
        self.lms.lms["OFFERING-PYTHON-JOHN"] = course

        result = self.lms.register_course(["REGISTER", "john@example.com", "OFFERING-PYTHON-JOHN"])
        self.assertEqual(result, "DECLINED")
        self.assertEqual(len(course.employees), 0)


if __name__ == "__main__":
    unittest.main()
